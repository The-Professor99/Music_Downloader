import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from make_requests_and_parse import request_and_parse
from make_requests_and_parse import request_download

def start_web_driver(cache_range=5):
    """Start up the web driver with preset preferences."""
    global driver
    options = Options()
    prefs = {
        "download_restrictions": 3,
        "download.default_directory": r"/home/ihechi/Music/auto_music"
    }
    options.add_experimental_option(
        "prefs", prefs
    )
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(ChromeDriverManager(\
        cache_valid_range=cache_range).install(), options=options)
        
def download_justnaija(url):
    """Download a song from justnaija."""
    soup = request_and_parse(url)
    class_to_scrap = soup.select(".download")
    if len(class_to_scrap) == 1:
        tag_to_scrap = class_to_scrap[0]
    elif len(class_to_scrap) > 1:
        tag_to_scrap = class_to_scrap[1]
    else:
        return None
    download_link = tag_to_scrap.get("href")
    res = request_download(download_link)
    return res

def download_netnaija(url):
    """Download a song from netnaija."""
    soup = request_and_parse(url)
    class_to_scrap = soup.select("div.db-one > a.btn")
    tag_to_scrap = class_to_scrap[0]
    link_to_scrap_ = tag_to_scrap.get("href")
    link_to_scrap = "https://www.thenetnaija.com" + link_to_scrap_
    download_link = sabishare_download(link_to_scrap)
    res = 200 # request_download(download_link)
    return res

def sabishare_download(url):
    """Download a song from netnaija's sabishare host using selenium to simulate clicks."""
    driver.get(url)
    element = driver.find_element_by_class_name("btn.shadow-sm.download.mt-3.mt-sm-0")
    driver.execute_script("arguments[0].click();", element);
    

def download_songslover(url):
    """Download a song from songslover."""
    soup = request_and_parse(url)
    class_to_scrap = soup.select("div.entry a")
    download_link = class_to_scrap[0].get("href")
    if download_link.endswith(".htm"):
        download_link = class_to_scrap[1].get("href")
    res = request_download(download_link)
    return res
