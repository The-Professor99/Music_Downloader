def get_song_name(link):
    """Return the formatted song name from the 'link'\
    passed, made with considerations of how song names\
    were structured."""
    song_name = link.getText().lower()
    song_name = song_name.replace("(", "").replace(")", ""\
    ).replace("feat.", "ft").replace("feat", "ft").replace("–", "-"\
    ).replace(",", " &").replace("ft.", "ft").replace("ft", "ft."\
    ).replace("'", "")
    song_name = song_name + ".mp3"
    return song_name

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
