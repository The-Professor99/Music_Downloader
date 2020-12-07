import os

def song_exists(song_name, music_folder_path):
    """Return True if song_name in music folder and False if otherwise."""
    music_path = os.path.expanduser(os.path.join("~", music_folder_path))
    return song_name in os.listdir(music_path)

def save_music(res, song_name, music_folder_path):
    """Save downloaded song to music folder."""
    save_path = music_folder_path + song_name
    if not os.path.isdir(save_path):
        save_path = os.path.expanduser(os.path.join(\
        "~", os.path.join(music_folder_path, song_name)))
    with open(save_path, "wb") as file_obj:
        for chunk in res.iter_content(100000):
            file_obj.write(chunk)

def update_list_downloaded(song_name, update_file_path):
    """Update a file set aside to
    show the songs downloaded using this program."""
    file_path = os.path.expanduser(os.path.join("~", update_file_path))
    if not os.path.isdir(os.path.dirname(file_path)):
        print("Error Occurred: path not found, song_list file not updated.")
        return
    with open(file_path, "a") as file_obj:
        file_obj.write(song_name + "\n")
