import random
import string
import customtkinter
import os
import time
from pygame import mixer
from typing import Optional
import yt_dlp
from youtube_search import YoutubeSearch as search
from tkinter import filedialog
import webbrowser
import json
from PIL import Image

root = customtkinter.CTk()
root.geometry("325x370")
root.resizable(False, False)
root.title("sPYracy")

filetypes = ['.mp3', '.wav', '.ogg', '.m4a', '.aac', '.flac']
playlist = []
dropdownplaylist = ["None (press this to shuffle)"]
songamount = 0
queue = os.listdir()
mixer.init()
for file in queue:
    if file.endswith(tuple(filetypes)):
        playlist.append(file)
        dropdownplaylist.append(file)

config = {
    'outtmpl': '%(title)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'flac',
    }]
}

os.system("")

class Variables:
    paused = True
    toDownload = []
    themes = ["Dark", "Light", "SystemDefault"]

class Commands:
    def setTheme(self, theme: str):
        if theme != "SystemDefault":
            customtkinter.set_appearance_mode(theme)
            f = open("config.json", "w")
            f.write(json.dumps({"theme": theme}))
        else:
            customtkinter.set_appearance_mode("system")
            f = open("config.json", "w")
            f.write(json.dumps({"theme": theme}))
    def resetconfig(self):
        os.remove("config.json")
    def discord(self):
        webbrowser.open_new("https://discord.gg/MQxKdcN3VB")
    def downloadFLACs(self):
        downloaded = 0
        playlist.clear()
        dropdownplaylist = ["None (press this to shuffle)"]
        for FLAC in Variables.toDownload:
            downloaded += 1
            Objects.currentDownload.configure(text=f"Lasted downloaded FLAC:\n {FLAC} ({downloaded})")
            time.sleep(0.3)
            song = (f"https://youtube.com/watch?v=" +
                    str(search(FLAC,
                               max_results=10).to_dict()).replace("[{'id': '", "").split("', 't", 1)[0])
            try:
                with yt_dlp.YoutubeDL(config) as down:
                    down.download([song])
            except yt_dlp.utils.DownloadError as e:
                print(f"\x1b[31mffmpeg is not installed, please install here: https://ffmpeg.org/")
            except Exception as e:
                if input("Unkown error, would you like to print it?(y/n): ").lower() == "y":
                    print(f"\x1b[31mERROR BELOW: \n{e}")
            for file in os.listdir():
                if file.endswith(tuple(filetypes)):
                    playlist.append(file)
                    dropdownplaylist.append(file)
                    Objects.combobox_1.configure(values=dropdownplaylist)
    def download(self):
        pos = 0
        Variables.toDownload.clear()
        text = Objects.downloadQueries.get()
        for l in text:
            pos += 1
            if ":" in text:
                if l == ":":
                    Variables.toDownload.clear()
                    Variables.toDownload.append(text.split(":", pos))
                    Commands().downloadFLACs()
            else:
                Variables.toDownload.append(text)
                Commands().downloadFLACs()
                break
    def play(self, val: Optional[str] = None):
        if val == "Placeholder" or "None (press this to shuffle)" or None:
            if Variables.paused != False:
                Objects.playButton.configure(text="⏯ (UNPAUSED)")
                Variables.paused = False
                mixer.music.unpause()
                global songamount
                for song in playlist:
                    mixer.music.queue(song)
                    songamount += 1
                mixer.music.load(random.choice(playlist))
                mixer.music.play()
            else:
                Objects.playButton.configure(text="⏯ (PAUSED)")
                Variables.paused = True
                mixer.music.pause()
        else:
            mixer.music.stop()
            mixer.music.unload()
            mixer.music.load(val)
            mixer.music.play()
    def skip(self):
        mixer.music.stop()
        mixer.music.load(random.choice(playlist))
        if Variables.paused == False:
            mixer.music.play()

class Objects:
    tabview = customtkinter.CTkTabview(master=root, width=200, height=50)
    tabview.pack(expand=False)

    player = tabview.add("Player")
    downloader = tabview.add("Downloader")
    info = tabview.add("Misc")

    options = customtkinter.CTkComboBox(master=info, values=Variables.themes, command=Commands().setTheme)
    options.pack(pady=3)
    options.set("Select a theme")

    discord = customtkinter.CTkButton(master=info, text="Click to join discord!", font=customtkinter.CTkFont("comic sans ms"), command=Commands().discord)
    discord.pack()

    version = customtkinter.CTkLabel(master=info, text="Version 1.0.0",  font=customtkinter.CTkFont("comic sans ms", 20))
    version.pack(pady=3)

    downloadQueries = customtkinter.CTkEntry(master=downloader, width=280, border_width=0, corner_radius=10, placeholder_text="Seperate songs with ':' (no1:no2:no3)", font=customtkinter.CTkFont("Comic Sans MS"))
    downloadQueries.pack()

    downloadSongs = customtkinter.CTkButton(master=downloader, text="Download", font=customtkinter.CTkFont("comic sans ms", 20), command=Commands().download)
    downloadSongs.pack(pady=3)

    currentDownload = customtkinter.CTkLabel(master=downloader, text="Last downloaded FLAC\nNone (0)", font=customtkinter.CTkFont("comic sans ms", 20))
    currentDownload.pack(pady=3)

    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Image.png")), size=(250, 125))

    label = customtkinter.CTkLabel(text="",master=root, image=image, corner_radius=10)
    label.pack(pady=25)


    playButton = customtkinter.CTkButton(master=player, text="⏯ (PAUSED)", command=Commands().play,  font=customtkinter.CTkFont("comic sans ms", 20))
    playButton.pack()

    combobox_1 = customtkinter.CTkComboBox(tabview.tab("Player"), values=dropdownplaylist, command=Commands().play)
    combobox_1.pack(pady=3)
    combobox_1.set("Select a song (Optional)")

    skipButton = customtkinter.CTkButton(master=player, text="Skip", command=Commands().skip)
    skipButton.pack(pady=3)

try:
    f = open("config.json", "r")
    customtkinter.set_appearance_mode(json.loads(f.read())["theme"])
except:
    pass

root.mainloop()