## Music_Downloader

This Program downloads songs with minimal human interaction from sites such as 
<ul>   
    <li>Netnaija<li>
    <li>Justnaija<li>
    <li>Songslover<li>
</ul>
More Functionalities/Websites will be added Later on.

## Requirements
<ul>
    <li>webdriver-manager 
        <p>Can be installed using pip or check the documentation <a href="https://pypi.org/project/webdriver-manager/">here</a></p>
    </li>
    <li>You should also have requests, bs4 and selenium Libraries Installed</li>
</ul>

<p>Modify the <span style="background-color:blue">artistes_of_interests</span> in the <span style="background-color:blue">download_songs</span> module to your artistes of interest</p>
<p>Still in the <span style="background-color:blue">download_songs</span> module, Change <span style="background-color:blue">folder</span> to your Music folder path and 
if you want a text file updated whenever a download is made, add the text file path to <span style="background-color:blue">update_file_path</span></p>
<p>The webdriver is cached for 5 days, change the <span style="background-color:blue">num_days</span> variable to suit your preferences</p>
