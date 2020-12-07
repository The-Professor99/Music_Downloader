# Music_Downloader

This Program downloads songs with minimal human interaction from sites such as:
 - Netnaija
 - Justnaija
 - Songslover

More Functionalities/Websites will be added Later on.

## Requirements

 - `webdriver-manager`
   - Can be installed using pip or check the documentation [here](https://pypi.org/project/webdriver-manager/)

 - You should also have `requests`, `bs4` and `selenium` Libraries Installed

Modify the `artistes_of_interests` in the `download_songs` module to your artistes of interest

Still in the `download_songs` module, Change the `folder` variable to your Music folder path and if you want a text file updated whenever a download is made, add the text file path to the `update_file_path` 

The `webdriver` is cached for 5 days, change the `num_days` variable to suit your preferences
