# Music_Downloader

This Program downloads songs with minimal human interaction from sites such as:
 - Netnaija
 - Justnaija
 - Songslover

---

## What this does

Are you tired of downloading new songs of your favorite artistes the moment it drops, this helps you download new songs off the websites above depending on if the song is by an artiste you like.

You can choose to run this at intervals of days or set up a cron job to run it as at when required.

This Ensures your playlist is always updated with new music from your Favorite Artistes. All with no stress.

More Functionalities/Websites will be added Later on.

## Installation
This project can be installed by running the following commands in your preferred directory.

    $ git clone https://github.com/The-Professor99/Music_Downloader.git
    $ pip install -r requirements.txt
    
## Requirements
Run the command below in the project's root folder to install the requirements.

    $ pip install -r requirements.txt

## How To Use
Modify the `artistes_of_interests` in the `download_songs` module to your artistes of interest

Still in the `download_songs` module, Change the `folder` variable to your Music folder path and if you want a text file updated whenever a download is made, add the text file path to the `update_file_path` 

The `webdriver` is cached for 5 days, change the `num_days` variable to suit your preferences

After these modifications are made, simply run the below command to start up the project
    $ python download_songs.py

## Note
Only songs available on the sites above can be downloaded. 
