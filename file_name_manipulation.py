import os

def get_song_name(link, typ="link"):
    """Return the formatted song name from the 'link'\
    passed, made with considerations of how song names\
    were structured."""
    if typ == "link":
        song_name = link.getText().lower()
    else:
        song_name = link.lower()
    digits = [s for s in song_name.split() if s.isdigit()]
    for digit in digits:
        song_name = song_name.replace(digit, "")
    song_name = song_name.strip()
    song_name = song_name.replace("(", "").replace(")", ""\
    ).replace("feat.", "ft").replace("feat", "ft").replace("–", "-"\
    ).replace(",", " &").replace("ft.", "ft").replace("ft", "ft."\
    ).replace("'", "").replace("[", "").replace("]", "")
    if 'netnaija' in song_name and typ != 'link':
        song_name = song_name.replace("netnaija.com.mp3", "").strip()
    #else:
    song_name = song_name + ".mp3"
    return song_name
    
def rename_netnaija_songs(folder):
    """Renames an already saved netnaija song to conform to song naming standard"""
    music_path = os.path.expanduser(os.path.join("~", folder))
    items_list = os.listdir(music_path)
    for item in items_list:
        if "NetNaija" in item:
            song_name = get_song_name(item, typ='rename')
            src =f"{music_path}/{item}"
            dst =f"{music_path}/{song_name}"
            os.rename(src, dst)

def artists_found(song_name):
    """Return a list of artist names found in the song_name."""
    artist_list = []
    song_name = song_name.replace(".mp3", "")
    if song_name.count("-") == 2:
        song_name_split = song_name.rsplit("-", maxsplit=1)
    else:
        song_name_split = song_name.split("-")
    if len(song_name_split) == 1:
        return []
    if "album" in song_name:
        return []
    if "&" not in song_name_split[0]:
        artist_list.append(song_name_split[0].strip())
    else:
        split_name2 = song_name_split[0].split("&")
        for name in split_name2:
            artist_list.append(name.strip())
    song_name_split_rem = song_name_split[1].split("ft.")
    if len(song_name_split_rem) > 1:
        song_name_split = song_name_split_rem[-1].split("&")
        for name in song_name_split:
            artist_list.append(name.strip())
    return artist_list

def found_artists(artist_list, artists_of_interest):
    """Return True if any artist in artist_list is found
    in artists_of_interest, else it returns False."""
    for name in artist_list:
        if name in artists_of_interest:
            return True
    return False
