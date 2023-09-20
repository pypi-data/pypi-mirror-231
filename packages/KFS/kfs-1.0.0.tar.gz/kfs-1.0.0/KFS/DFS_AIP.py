# Copyright (c) 2023 구FS, all rights reserved. Subject to the MIT licence in `licence.md`.
import concurrent.futures
import datetime as dt
import enum
import inspect
import json
import lxml.html            # HTML parsing
import os
import playwright.sync_api  # pretend to be a real user and click print button
import re                   # regular expressions
import requests
from . import log, media


class AIP(enum.Enum):   # AIP root URL
    VFR="https://aip.dfs.de/BasicVFR/"
    IFR="https://aip.dfs.de/BasicIFR/"


def download_aerodrome_charts_old(aerodrome_ICAO_code: str, DFS_AIP_URL: AIP=AIP.VFR):
    aerodromes_URL: str # AIP/AD Aerodromes
    names_URL: list     # AIP/AD Aerodromes/ABCDEFG
    aerodrome_URL: str  # AIP/AD Aerodromes/ABCDEFG/Name ICAO-Code
    charts_PDF=[]       # charts PDF


    aerodrome_ICAO_code=str(aerodrome_ICAO_code)
    aerodrome_ICAO_code=aerodrome_ICAO_code.upper()         # convert all letters to uppercase
    if re.search("[0-9A-Z]{4}", aerodrome_ICAO_code)==None: # ICAO code must be 4 letters numbers
        raise ValueError("Error in KFS::DFS_AIP::download_aerodrome(...): Aerodrome ICAO code is invalid.")
    
    DFS_AIP_URL=DFS_AIP_URL.value                       # convert AIP.VFR or AIP.IFR to value string
    AIP_page=requests.get(DFS_AIP_URL)
    DFS_AIP_URL=f"{AIP_page.url.rsplit('/', 1)[0]}/"    # add latest AIRAC date to AIP root URL to get latest AIP
    AIP_page=lxml.html.fromstring(AIP_page.content)


    log.write("Navigating through DFS AIP to requested aerodrome...")
    # navigate to aerodromes page
    aerodromes_URL=f"""{DFS_AIP_URL}{AIP_page.xpath("//a[@class='folder-link'][span='AD Aerodromes']")[0].get('href')}"""   # folder-link, span AD Aerodromes URL
    aerodromes_page=requests.get(aerodromes_URL)
    aerodromes_page=lxml.html.fromstring(aerodromes_page.content)

    # navigate to names pages
    names_URL=[f"{DFS_AIP_URL}{sub_URL.get('href')}" for sub_URL in aerodromes_page.xpath("//a[@class='folder-link']")][3:]  # all folder-link, only use [3:] (no general information, only aerodromes list)
    names_pages=[]
    for name_URL in names_URL:
        names_pages.append(requests.get(name_URL))
        names_pages[-1]=lxml.html.fromstring(names_pages[-1].content)

    # navigate to specific aerodrome page
    try:
        aerodrome_URL=f"""{DFS_AIP_URL}{[name_page.xpath(f"//a[@class='folder-link'][contains(span, '{aerodrome_ICAO_code}')]") for name_page in names_pages if name_page.xpath(f"//a[@class='folder-link'][contains(span, '{aerodrome_ICAO_code}')]")[0:1]!=[]][0][0].get("href")}""" # go through all aerdromes names pages, folder-link, ICAO-Code, concatenate all lists and extract URL out
    except IndexError:  # if index error: aerdrome does not exist in AIP
        raise FileNotFoundError("Error in KFS::DFS_AIP::download_aerodrome(...): Aerodrome ICAO code does not exist in AIP.")
    aerodrome_page=requests.get(aerodrome_URL).content
    aerodrome_page=lxml.html.fromstring(aerodrome_page)

    # navigate to chart page
    charts_URL=[f"{DFS_AIP_URL}{chart_URL.get('href')}" for chart_URL in aerodrome_page.xpath("//a[@class='document-link']")]
    log.write("\rNavigated through DFS AIP to requested aerodrome.")
    # charts_names=[f"./{aerodrome_ICAO_code}/{chart_URL.text}.png" for chart_URL in aerodrome_page.xpath("//a[@class='document-link']/span[@lang='en']")]
    charts_filepaths=[f"./{aerodrome_ICAO_code}/{chart_URL.text}.png" for chart_URL in aerodrome_page.xpath("//a[@class='document-link']/span[@lang='en']")]

    # download charts
    with playwright.sync_api.sync_playwright() as pw:
        browser=pw.chromium.launch(headless=False)
        media.download_images(charts_URL, charts_filepaths, worker_function=_download_chart, browser=browser)

    charts_PDF=media.convert_images_to_PDF(charts_filepaths, f"{aerodrome_ICAO_code}.pdf")


    return charts_PDF


def download_aerodrome_charts(aerodrome_ICAO_code: str, DFS_AIP_URL: AIP=AIP.VFR):
    aerodrome_page: lxml.html.HtmlElement   # aerodome page
    aerodromes_page_ID: dict                # all aerodome page ID
    AERODROMES_PAGE_ID_FILENAME=f"{dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d')} DFS {DFS_AIP_URL.name} Aerodome Page ID.json" # aerodome page ID filename
    AIRAC_URL: str                          # DFS AIP URL including AIRAC
    charts_PDF=[]                           # charts PDF


    aerodrome_ICAO_code=str(aerodrome_ICAO_code)
    aerodrome_ICAO_code=aerodrome_ICAO_code.upper()                 # convert all letters to uppercase
    if re.search("^E[DT][A-Z][A-Z]$", aerodrome_ICAO_code)==None:   # ICAO code must be 4 letters and start with ED or ET
        raise ValueError(f"Error in {download_aerodrome_charts.__name__}{inspect.signature(download_aerodrome_charts)}: Aerodrome ICAO code must consist of 4 letters and start with ED or ET.")
    

    if os.path.isfile(AERODROMES_PAGE_ID_FILENAME)==False:                                  # if page ID file for today does not exist yet:
        aerodromes_page_ID=_create_page_ID_json(DFS_AIP_URL, AERODROMES_PAGE_ID_FILENAME)   # create file for next time and return data as dit
    else:                                                                       # if page ID file for today does exist already:
        with open(AERODROMES_PAGE_ID_FILENAME, "rt") as aerodrome_page_ID_file: # load file
            aerodromes_page_ID=json.loads(aerodrome_page_ID_file.read()) 
    # TODO delete old files, load old files if new file can't be generated
    
    # navigate to aerodrome page
    redirect_page=requests.get(f"{DFS_AIP_URL.value}pages/{aerodromes_page_ID[aerodrome_ICAO_code]}.html")  # download initial redirect page
    aerodrome_page_URL=f"""{DFS_AIP_URL.value}{lxml.html.fromstring(redirect_page.text).xpath('//meta[@http-equiv="Refresh"]')[0].get("content").split("url=../")[1]}"""
    aerodrome_page=requests.get(aerodrome_page_URL)         # download aerodrome page
    AIRAC_URL=f"{aerodrome_page.url.rsplit('/', 1)[0]}/"    # DFS AIP URL including AIRAC
    aerodrome_page=lxml.html.fromstring(aerodrome_page.text)

    # navigate to chart page
    images_URL=[f"{AIRAC_URL}{image_URL.get('href')}" for image_URL in aerodrome_page.xpath("//a[@class='document-link']")]
    images_filepaths=[f"./{aerodrome_ICAO_code}/{chart_name.text}.png" for chart_name in aerodrome_page.xpath("//a[@class='document-link']/span[@lang='en']")]

    # download charts
    with playwright.sync_api.sync_playwright() as pw:
        browser=pw.firefox.launch(headless=False)
        media.download_images(images_URL, images_filepaths, False, worker_function=_download_chart, browser=browser)

    charts_PDF=media.convert_images_to_PDF(images_filepaths, f"{dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d')} {aerodrome_ICAO_code}.pdf")

    return charts_PDF


def _create_page_ID_json(DFS_AIP_URL: AIP, AERODROMES_PAGE_ID_FILENAME: str) -> dict:
    aerodromes_page_ID={}
    threads=[]

    AERODROMES_PAGE_ID_FILENAME=str(AERODROMES_PAGE_ID_FILENAME)

    if DFS_AIP_URL==AIP.IFR:
        page_ID_min=0xC000C1
        page_ID_max=0xC0060A
    elif DFS_AIP_URL==AIP.VFR:
        page_ID_min=0xC0194C
        page_ID_max=0xC01B06
    else:
        raise RuntimeError(f"Error in {_create_page_ID_json.__name__}{inspect.signature(_create_page_ID_json)}: DFS_AIP_URL is an invalid value ({DFS_AIP_URL.name}: {DFS_AIP_URL.value}).")


    with concurrent.futures.ThreadPoolExecutor() as thread_manager:
        for page_ID in range(page_ID_min, page_ID_max+1):   # iterate through all page ID, get aerodrome code
            threads.append((thread_manager.submit(_get_aerodrome_ICAO_code, page_ID, DFS_AIP_URL), page_ID))

        for thread in threads:
            aerodrome_ICAO_code=thread[0].result()              # get aerodrome ICAO code
            if aerodrome_ICAO_code==None:                       # if invalid page ID: skip
                continue
            aerodromes_page_ID[aerodrome_ICAO_code]=f"{thread[1]:06X}"  # enter aerodrome ICAO code and page ID


    with open(AERODROMES_PAGE_ID_FILENAME, "wt") as aerodrome_page_ID_file: # save as json
        aerodrome_page_ID_file.write(json.dumps(aerodromes_page_ID, indent=4))

    return aerodromes_page_ID   # return results


def _download_chart(image_URL: str, image_filepath: str, browser: playwright.sync_api.Browser):
    image_URL=str(image_URL)
    image_filepath=str(image_filepath)


    browser_context=browser.new_context()
    tab=browser_context.new_page()              # open new tab
    tab.goto(image_URL)                         # go to page url
    tab.click("xpath=//a[@class='btn btn-sm']") # click print icon to go to print tab
    browser_context.wait_for_event("page")      # wait for new print tab to open, this is mandatory or it won't be added to context
    tab=browser_context.pages[-1]               # switch tabs to print tab
    
    with tab.expect_download() as download_info:
        tab.click("xpath=//button[@class='btn btn-outline-dark']")  # click print button to open print context menu
    # browser_context.wait_for_event("page")      # wait for new print context menu to open
    # tab=browser_context.pages[-1]               # switch tabs to print context menu
    # tab.click("xpath=//select[@class='md-select']/option[@value='Save as PDF/local/']") # click save as PDF option
    # tab.locator("xpath=//div[@class='pageAIP d-print-block']/img").screenshot(path=image_filepath) # download image by taking screenshot
    download=download_info.value
    path=download.path()
    download.save_as(image_filepath)
    
    
    browser_context.close()

    return
    # TODO CONTINUE HERE CLICK THROUGH PRINT SAVE CONTEXT MENU AND SAVE PDF 

def _get_aerodrome_ICAO_code(page_ID: int, DFS_AIP_URL: AIP):
    page_ID=int(page_ID)


    redirect_page=requests.get(f"{DFS_AIP_URL.value}pages/{page_ID:06X}.html")  # download initial redirect page
    if redirect_page.ok==False:                                                 # if page ID does not lead to aerodrome, because some are placeholders: skip
        return None
    aerodrome_page_URL=f"""{DFS_AIP_URL.value}{lxml.html.fromstring(redirect_page.text).xpath('//meta[@http-equiv="Refresh"]')[0].get("content").split("url=../")[1]}"""
    
    aerodrome_page=requests.get(aerodrome_page_URL)                             # download aerodrome page
    aerodrome_ICAO_code=lxml.html.fromstring(aerodrome_page.text).xpath('//div[@class="headlineText left"]/span')[1].text.split(" ")[-1]    # parse ICAO code
    if re.search("[0-9A-Z]{4}", aerodrome_ICAO_code)==None: # if aerodrome could not be parsed, saml aerodrome without ICAO code: skip
        return None
    
    return aerodrome_ICAO_code