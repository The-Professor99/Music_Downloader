import website_scrap as ws
import file_name_manipulation as fnm
import make_requests_and_parse as mrp
import save_and_update_files as suf

# Add the names of artistes you're interested in here - in lower letters
# eg artistes_of_interest = ["jorja smith", "burna boy"]
artistes_of_interest: list = ['burna boy', 'bnxn']

# Currently Supported Website Pages - Please Do not Modify!!!
# Doing so is at your own risk!!!
url1: str = "https://www.thenetnaija.com/music/"
url2: str = "https://www.thenetnaija.com/music/page/2"
url3: str = "https://www.thenetnaija.com/music/afro"
url4: str = "https://www.thenetnaija.com/music/hip-hop"
url5: str = "https://www.thenetnaija.com/music/hip-hop/page/2"
url6: str = "https://justnaija.com/music/download-mp3/"
url7: str = "https://justnaija.com/music/download-mp3/page/2/"
url8: str = "https://justnaija.com/music/foreign/"

#url9: str = "https://songslover.cam/"
urls: list = [url1, url2, url3, url4, url5, url6, url7, url8] # url1, url2, url3, url4, url5

# Enter Your Music Folder's path here, it should have no tilde symbol!!!
folder: str = "Music/auto_music/"

# filepath of text file for Storing List of Songs downloaded, should have no tilde sign
# create the text file, copy the absolute path and paste in here
update_file_path: str = "/home/ihechi/Music/downloaded_songs.txt"

# specify the number of days to cache webdriver
num_days: int = 10

suf.set_song_path(folder)

def main():
    """downloads music files based on your \
    artistes of interest from sites such as Netnaija,\
    Justnaija and songslover. It does this through web\
    scrapping. More functionalities will be added later on."""

    print("Beginning Download Now!")

    def get_download_list(url):
        """Return a list of links through which available songs will be downloaded."""
        soup = mrp.request_and_parse(url)
        if "songslover" in url:
            tag_to_scrap = soup.select("li.other-news h3.post-box-title a")
        else:
            if "netnaija" in url:
                tag_to_scrap = soup.select("h2 > a")
                other_tag = soup.select("h2 > span")
            else:
                tag_to_scrap = soup.select(".file-name > a")

        # Stores song links to scrap
        download_list = []

        if "netnaija" not in url:
            for link in tag_to_scrap:
                song_name = fnm.get_song_name(link)
                print(song_name, "; songname")
                if not suf.song_exists(song_name, folder):
                    if fnm.found_artists(fnm.artists_found(song_name), artistes_of_interest):
                        download_list.append(link)
            print([x.getText() for x in download_list])
            return download_list
        else:
            netnaija_names = []
            for link, artiste_name in zip(tag_to_scrap, other_tag):
                song_name_ = fnm.get_song_name(link)
                artiste_name = fnm.get_song_name(artiste_name)
                artiste_name = artiste_name.replace(".mp3", "")
                song_name = artiste_name + " - " + song_name_
                song_name = song_name.strip()
                print("songname: ", song_name)
                if not suf.song_exists(song_name, folder):
                    if fnm.found_artists(fnm.artists_found(song_name), artistes_of_interest):
                        download_list.append(link)
                        netnaija_names.append(song_name)
            print([x.getText() for x in download_list])
            return download_list, netnaija_names

    for url in urls:
        fnm.rename_netnaija_songs(folder)
        if "netnaija" in url:
            download_list, names_netnaija = get_download_list(url)
        else:
            download_list = get_download_list(url)
        if len(download_list) == 0:
            continue

        links_from_download_list = [x.get("href") for x in download_list]

        for link in links_from_download_list:
            print(f"Downloading {link}")
            if "justnaija" in link:
                res = ws.download_justnaija(link)
            elif "netnaija" in link:
                res = ws.download_netnaija(link)
            else:
                res = ws.download_songslover(link)
            if not res:
                continue
            current_index = links_from_download_list.index(link)
            if "netnaija" in url:
                name = names_netnaija[current_index]
            else:
                name = fnm.get_song_name(download_list[current_index])
                suf.save_music(res, name, folder)
                suf.update_list_downloaded(name, update_file_path)
    print("Done!")


if __name__ == "__main__":
    ws.start_web_driver(cache_range=num_days)
    main()
    ws.driver.quit()
