import json
from youtube_search import YoutubeSearch as search
import yt_dlp
import customtkinter
import os
from PIL import Image
import pygame
import threading
from typing import Optional
import random
import time
import os
import sys
from tkinter import filedialog
import string
import requests
from tkinter import messagebox
import webbrowser
import argparse

def rgb(r, g, b):
    return "#%02x%02x%02x" % (r, g, b) ## % 1 = r, % 2 = g, % 3 = b. 02x = hex per

filetypes = [
    ".flac",
    ".mp3",
    ".ogg",
    ".wav",
    ".wma",
    ".aac",
    ".m4a",
    ".m4b",
    ".m4p",
    ".m4r",
    ".m4v",
    ".mid",
    ".midi",
    ".midiin",
    ".midiout",
    ".mp4",
    ".mpg",
    ".mpeg",
    ".mpg4",
]

os.system("")

#####################################################################
args = argparse.ArgumentParser(
    prog=None,
    description=None
)

options = [
    "looped",
    "paused",
    "dir", "directory"
]

post = [
    "y",
    "yes",
    "1",
    "true"
]

posf = [
    "n",
    "no",
    "0",
    "false"
]

loop = True
paused = False
for option in options:
    args.add_argument(f"-{option}")

zz = args.parse_args()


try:
    f = open("config.json", "r")
    filetype = json.loads(f.read())["filetype"]
    f.close()
except:
    filetype = filetypes[0]

version = "2.3.3"
try:
    url = "https://raw.githubusercontent.com/GogleSiteBank/sPYracyLatestVersion/main/latest"
    d = requests.get(url).content.decode("utf-8").replace("\n", "")
    print(f"[Spyracy] {d} is latest version.")
    print(f"[Spyracy] {version} is currently installed.")
    if version < d: ## latest greater than version
        update = messagebox.askokcancel("New Update Available", "New version of sPYracy is available. Please update to the latest version")
        if update:
            u = "https://github.com/gogleSiteBank/spyracy/releases/latest/download/sPYracy.zip"
            webbrowser.open(u)
            sys.exit()
    else: ## latest less than version or equal
        if version > d:
            msg = messagebox.showwarning("Unstable version of sPYracy", "This version of sPYracy is higher than the latest version.")
except:
    print(f"[Spyracy] Aborting update check, no internet connection...")

config = {""}

toDownload = []


def updateconfig():
    global config
    config = {
        "outtmpl": "%(title)s",
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": filetype.replace(".", ""),
            }
        ],
    }


updateconfig()
files = []
playing = ""
pygame.mixer.init()
lastplayed = ""
forlength = ""
for file in os.listdir():
    if file.endswith(tuple(filetypes)):
        files.append(file)

x = 0


def shuffle():
    random.shuffle(files)
    play()


def play():
    global playing, lastplayed, x, forlength
    if loop != True:
        try:
            for file in files:
                playing = files[x] + "       "
                forlength = files[x]
                pygame.mixer.music.unload()
                pygame.mixer.music.load(files[x])
                pygame.mixer.music.play()
                x += 1
                break
        except IndexError:
            print("[Spyracy] Songs have ended.")
        except Exception as e:
            print(f"[Spyracy] unexpected error! \n{e}")
    else:
        try:
            for file in files:
                playing = files[x] + "       "
                forlength = files[x]
                pygame.mixer.music.unload()
                pygame.mixer.music.load(files[x])
                pygame.mixer.music.play()
                x += 1
                break
        except IndexError:
            x = 0
            play()
        except Exception as e:
            print(f"[Spyracy] unexpected error! \n{e}")


def previous():
    global playing, lastplayed, x, forlength
    for file in files:
        x -= 1
        playing = files[x]
        forlength = files[x]
        pygame.mixer.music.unload()
        time.sleep(0.1)
        pygame.mixer.music.load(files[x])
        pygame.mixer.music.play()
        break




def skip():
    play()

class CustomTkinter(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x450")
        self.resizable(False, False)
        self.title(f"sPYracy v{version}")
        path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "images/online-16.ico"
        )
        self.iconbitmap("online-16.ico")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self._set_appearance_mode("Dark")
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        self.Title = customtkinter.CTkLabel(
            self.navigation_frame, text="sPYracy", font=("Arial", 20, "bold")
        )
        self.Title.grid(row=0, column=0, padx=20, pady=15)
        ################ Start of Page Frames ################
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))

        self.streamingicon = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "online-64.png")),
        )
        self.downloadicon = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "download-64.png")),
        )
        self.settingicon = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "cog-64.png")),
        )
        self.play = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "Play.png"))
        )
        self.pause = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "Pause.png"))
        )
        self.skip = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "Skip.png"))
        )
        self.previous = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "Previous.png"))
        )
        self.sPYracy = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "Image.png")), size=(520, 225)
        )
        self.shuffleicon = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "shuffle-64.png")),
        )
        self.opendiricon = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "folder-3-64.png")),
        )
        self.loopicon = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "loop-64.png")),
        )
        self.Streaming = customtkinter.CTkButton(
            self.navigation_frame,
            image=self.streamingicon,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Streaming",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=self.streaming,
        )
        self.Streaming.grid(row=1, column=0, sticky="ew")
        self.Downloading = customtkinter.CTkButton(
            self.navigation_frame,
            image=self.downloadicon,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Download FLACs",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=self.downloading,
        )
        self.Downloading.grid(row=2, column=0, sticky="ew")
        self.Settings = customtkinter.CTkButton(
            self.navigation_frame,
            image=self.settingicon,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Settings",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=self.misc,
        )
        self.Settings.grid(row=3, column=0, sticky="ew")
        self.frame1 = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent", width=100, height=100
        )
        self.frame1.grid(row=0, column=1, sticky="nsew")
        self.frame2 = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent", width=100, height=100
        )
        self.frame3 = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent", width=100, height=100
        )
        self.streaming()
        ################ End of Page Frames ################
        self.Loop = customtkinter.CTkButton(
            self.frame1,
            image=self.loopicon,
            corner_radius=10,
            height=40,
            border_spacing=10,
            text="",
            fg_color="transparent",
            width=16,
            hover_color=rgb(50, 50, 50),
            command=self.loop
        )
        self.Loop.place(x=350, y=14)
        self.Previous = customtkinter.CTkButton(
            self.frame1,
            image=self.previous,
            corner_radius=10,
            height=40,
            border_spacing=10,
            text="",
            fg_color="transparent",
            width=16,
            hover_color=rgb(50, 50, 50),
            command=self.previousSong,
        )
        self.Previous.place(x=200, y=14)
        self.Shuffle = customtkinter.CTkButton(
            self.frame1,
            image=self.shuffleicon,
            corner_radius=10,
            height=40,
            border_spacing=10,
            text="",
            fg_color="transparent",
            width=16,
            hover_color=rgb(50, 50, 50),
            command=self.shuffleExec,
        )
        self.Shuffle.place(x=150, y=14)
        self.Play = customtkinter.CTkButton(
            self.frame1,
            image=self.pause,
            corner_radius=10,
            height=40,
            border_spacing=10,
            text="",
            fg_color="transparent",
            width=16,
            hover_color=rgb(50, 50, 50),
            command=self.playSong,
        )
        self.Play.place(x=250, y=14)
        self.Skip = customtkinter.CTkButton(
            self.frame1,
            image=self.skip,
            corner_radius=10,
            height=40,
            border_spacing=10,
            text="",
            fg_color="transparent",
            width=16,
            hover_color=rgb(50, 50, 50),
            command=self.skipSong,
        )
        self.Skip.place(x=300, y=14)
        self.Open = customtkinter.CTkButton(
            self.frame1,
            image=self.opendiricon,
            corner_radius=10,
            height=40,
            border_spacing=10,
            text="",
            fg_color="transparent",
            width=16,
            hover_color=rgb(50, 50, 50),
            command=self.open,
        )
        self.Open.place(x=500, y=14)
        self.thread()
        self.scrollingText()
        self.frame = customtkinter.CTkFrame(master=self.frame1, height=55, width=500)
        self.frame.pack(pady=80)
        self.Playing = customtkinter.CTkLabel(
            self.frame, font=("Arial", 15, "bold"), width=300
        )
        self.Playing.place(anchor=customtkinter.CENTER, relx=0.5, rely=0.5)
        self.Playing.configure(text=f"Currently Playing:\n {playing}")
        self.spyracyl1 = customtkinter.CTkLabel(
            text="", master=self.frame1, image=self.sPYracy, corner_radius=10
        )
        self.spyracyl2 = customtkinter.CTkLabel(
            text="", master=self.frame2, image=self.sPYracy, corner_radius=10
        )
        self.spyracyl3 = customtkinter.CTkLabel(
            text="", master=self.frame3, image=self.sPYracy, corner_radius=10
        )
        self.spyracyl1.place(x=5, y=210)
        self.spyracyl2.place(x=5, y=210)
        self.spyracyl3.place(x=5, y=210)
        self.flacdownloader = customtkinter.CTkEntry(
            self.frame2,
            placeholder_text=f"Enter name of the {filetype}(s) to download (seperate with ':').",
            width=500,
            height=30,
        )
        self.flacdownloader.place(x=25, y=30)
        self.filetype = customtkinter.CTkOptionMenu(
            self.frame3,
            values=filetypes,
            width=500,
            height=30,
            fg_color=rgb(50, 50, 50),
            button_color=rgb(31, 31, 31),
            command=self.fileType,
        )
        self.filetype.place(x=25, y=30)
        self.filetype.set(f"Select a File Type. (current: {filetype})")
        self.Ver = customtkinter.CTkLabel(
            self.frame3,
            text=f"Version: {version}",
            font=customtkinter.CTkFont("Gotham", 24, "bold")
        )
        self.Ver.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
        self.workingdir = customtkinter.CTkLabel(
            self.frame3,
            text=f"Working Directory: {os.getcwd()}",
            font=customtkinter.CTkFont("Gotham", 15, "bold")
        )
        self.Upd = customtkinter.CTkButton(
            self.frame3,
            text="Reload songs. (Unloads current song.)",
            font=customtkinter.CTkFont("Gotham", 15, "bold"),
            fg_color=rgb(50,50,50),
            hover_color=rgb(31,31,31),
            command=self.load
        ); self.Upd.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
        self.workingdir.pack()
        self.download = customtkinter.CTkButton(
            self.frame2,
            image=self.downloadicon,
            corner_radius=10,
            height=40,
            border_spacing=1,
            width=500,
            hover_color=rgb(50, 50, 50),
            fg_color=rgb(31, 31, 31),
            text="Download",
            command=self.downloada,
        )
        self.download.place(x=25, y=90)
        self.update()
        self.isclipause()
    def load(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        files.clear()
        for file in os.listdir():
            if file.endswith(tuple(filetypes)):
                files.append(file)
        play()
    def loop(self):
        global loop
        loop = not loop
        if loop == False: print("[Spyracy] Looping OFF")
        if loop == True: print("[Spyracy] Looping ON")
    def open(self):
        global files
        files.clear()
        dir = filedialog.askdirectory(title="Select Music Directory")
        os.chdir(dir)
        for file in os.listdir(dir):
            if file.endswith(tuple(filetypes)):
                files.append(f"{dir}/" + file)
        play()

    def shuffleExec(self):
        shuffle()

    def update(self):
        try:
            threading.Timer(0.1, self.update).start()
            self.Playing.configure(text=f"Currently Playing:\n {playing}")
        except RuntimeError:
            sys.exit(0)

    def thread(self):
        threading.Timer(1.0, self.thread).start()
        self.getBusy()

    def playSong(self):
        global paused
        if paused == True:
            paused = False
            self.Play.configure(image=self.pause)
            pygame.mixer.music.unpause()
        else:
            paused = True
            self.Play.configure(image=self.play)
            pygame.mixer.music.pause()

    def isclipause(self):
        global loop, files
        if zz.looped in post: loop = True; print("[Spyracy] Loop Enabled via CLI.")
        elif zz.looped in posf: loop = False; print("[Spyracy] Loop disabled via CLI.")
        if zz.paused in post: self.playSong(); print("[Spyracy] Paused via CLI.")
        elif zz.paused in posf: print("[Spyracy] Unpaused via CLI.")
        if zz.dir or zz.directory:
            files.clear()
            os.chdir(zz.dir)
            for file in os.listdir(dir):
                if file.endswith(tuple(filetypes)):
                    files.append(f"{dir}/" + file)
    def previousSong(self):
        try:
            for i in range(2):
                previous()
        except:
            previous()

    def skipSong(self):
        skip()

    def showFrame(self, name):
        if name == "1":
            self.frame2.grid_forget()
            self.frame3.grid_forget()
            self.frame1.grid(row=0, column=1, sticky="nsew")
        elif name == "2":
            self.frame1.grid_forget()
            self.frame3.grid_forget()
            self.frame2.grid(row=0, column=1, sticky="nsew")
        elif name == "3":
            self.frame2.grid_forget()
            self.frame1.grid_forget()
            self.frame3.grid(row=0, column=1, sticky="nsew")

    def scrollingText(self):
        global playing
        if len(playing) > 20:
            threading.Timer(0.3, self.scrollingText).start()
            for i in range(3):
                playing = playing[1:] + playing[0]
        else:
            threading.Timer(0.05, self.scrollingText).start()

    def streaming(self):
        self.showFrame("1")
        self.Downloading.configure(fg_color="transparent")
        self.Streaming.configure(fg_color=rgb(31, 31, 31))
        self.Settings.configure(fg_color="transparent")

    def downloading(self):
        self.showFrame("2")
        self.Streaming.configure(fg_color="transparent")
        self.Downloading.configure(fg_color=rgb(31, 31, 31))
        self.Settings.configure(fg_color="transparent")
        self.frame2.grid(row=0, column=1, sticky="nsew")

    def misc(self):
        self.showFrame("3")
        self.Streaming.configure(fg_color="transparent")
        self.Settings.configure(fg_color=rgb(31, 31, 31))
        self.Downloading.configure(fg_color="transparent")

    def getBusy(self):
        if paused == False:
            if pygame.mixer.music.get_busy():
                pass
            else:
                play()

    def fileType(self, s: str):
        global filetype
        filetype = s
        self.filetype.set(f"Select a File Type. (current: {filetype})")
        f = open("config.json", "w")
        f.write(json.dumps({"filetype": s}))
        updateconfig()

    def downloadFLACs(self):
        global toDownload
        for FLAC in toDownload:
            song = (
                f"https://youtube.com/watch?v="
                + str(search(FLAC, max_results=10).to_dict())
                .replace("[{'id': '", "")
                .split("', 't", 1)[0]
            )
            try:
                with yt_dlp.YoutubeDL(config) as down:
                    down.download([song])
            except yt_dlp.utils.DownloadError as e:
                print(
                    f"\x1b[31m[Spyracy] FFmpeg is not installed, please install here: https://ffmpeg.org/"
                )
            except Exception as e:
                s = "".join(random.choices(string.ascii_letters + string.digits, k=10))
                name = f"{s}.log"
                f = open(f"{s}.log", "a")
                f.write(
                    f"[Spyracy] When downloading {song}, this ERROR occured:\n{e}\nThis is likely due to invalid file type formats that your converter or os does not support."
                )
                print(f"[Spyracy] Error occured, saved to {name}")
                break
        print("[Spyracy] Song(s) downloaded successfully, head over to settings to load them.")

    def downloada(self):
        global toDownload
        pos = 0
        toDownload.clear()
        text = self.flacdownloader.get()
        if ":" in text:
            toDownload.clear()
            for s in text.split(":"):
                toDownload.append(s)
            self.downloadFLACs()
        else:
            toDownload.clear()
            toDownload.append(text)
            self.downloadFLACs()



CustomTkinter().mainloop()
