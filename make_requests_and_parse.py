import sys
import time
import requests
from bs4 import BeautifulSoup as bsoup


def request_and_parse(url):
    """Request and parse the passed url, Returns the parsed response."""
    res = request_download(url)
    print("Downloaded, Now Parsing")
    soup = bsoup(res.text, features="html5lib")
    return soup


def request_download(url):
    """Request to get the url passed and returns the response."""
    active = True
    count = 0
    wait_time = 10
    while active:
        try:
            res = requests.get(url)
            res.raise_for_status()
        except requests.exceptions.RequestException:
            print("Couldn't Get Request")
            count += 1
            if count == 6:
                print(
                    "Process Terminated, Check Internet \
                    Connectivity and Try Again!!!", file=sys.stderr)
                sys.exit(-1)
            for i in reversed(range(wait_time)):
                print(f"Retrying in {i}")
                time.sleep(1)
            wait_time += 3
        else:
            active = False

    return res
