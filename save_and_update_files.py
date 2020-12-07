import os
import sys


def song_exists(song_name, music_folder_path):
    """Return True if song_name in music folder and False if otherwise."""
    music_path = os.path.expanduser(os.path.join("~", music_folder_path))
    return song_name in os.listdir(music_path)


def set_song_path(music_folder_path, song_name=""):
    """set music download path"""
    if not os.path.isdir(music_folder_path):
        music_folder_path = os.path.expanduser(os.path.join(
            "~", music_folder_path))
        if not os.path.isdir(music_folder_path):
            print(f"Folder Not Found: modify folder variable from '{music_folder_path}'\
            \nto an existing path with no tilde expansion symbol,\
            \ntry entering the music folder's absolute path!!!", file=sys.stderr)
            sys.exit(-1)
    return os.path.join(music_folder_path, song_name)


def save_music(res, song_name, music_folder_path):
    """Save downloaded song to music folder."""
    save_path = set_song_path(music_folder_path, song_name=song_name)
    with open(save_path, "wb") as file_obj:
        for chunk in res.iter_content(100000):
            file_obj.write(chunk)

def update_list_downloaded(song_name, update_file_path):
    """Update a file set aside to
    show the songs downloaded using this program."""
    if not os.path.isfile(update_file_path):
        print(f"Warning: {update_file_path} path not found\
        \n{song_name} won't be written to any file that keeps a list of songs you've downloaded. check the update_file_path variable", file=sys.stderr)
        return
    with open(update_file_path, "a") as file_obj:
        file_obj.write(song_name + "\n")
