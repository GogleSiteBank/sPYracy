import os, sys
os.system("")
sprefix = "\033[35m[Spyracy]\033[33m"
dependencies = [
    "youtube_search",
    "yt_dlp",
    "customtkinter",
    "PIL",
    "pygame",
    "audioread",
    "pypresence",
    ### depenencies past here are for "weird" installs of python that dont include the standard plugins (os & sys cannot be checked due to first line)
    "json",
    "typing",
    "threading",
    "time",
    "tkinter",
    "string",
    "random",
    "requests",
    "webbrowser",
    "argparse",
]                                                           

dpstdout = {
    "youtube_search": "Youtube Search",
    "yt_dlp": "YT-DLP",
    "customtkinter": "Customtkinter",
    "PIL": "PIL/Pillow",
    "pygame": "PyGame",
    "audioread": "Audio Read",
    "pypresence" : "PY Presence",
    ### depenencies past here are for "weird" installs of python that dont include the standard plugins (os & sys cannot be checked due to first line)
    "json": "Json",
    "typing": "Typing",
    "threading": "Threading",
    "time": "Time",
    "tkinter": "Tkinter",
    "string": "String",
    "random": "Random",
    "requests": "Requests",
    "webbrowser": "Web Browser",
    "argparse": "Arg Parse",
}
needs_refenv = False
def load_dependencies():
    print(f"{sprefix} Loading dependencies...\033[0m")
    for _ in dependencies:
        if _ != "pygame" and _ != "PIL":
            try:
                exec(f"import {_}")
                print(f"{sprefix} {dpstdout[_]} found.\033[0m")
            except ModuleNotFoundError:
                print(f"{sprefix} {dpstdout[_]} not found, installing...\033[0m")
                os.system(f"pip install {_}")
                needs_refenv = True
        else:
            if _ == "pygame":
                try:
                    f = open(os.devnull, 'w')
                    sys.stdout = f
                    import pygame
                    sys.stdout = sys.__stdout__
                    print(f"{sprefix} PyGame found.\033[0m")
                except ModuleNotFoundError:
                    sys.stdout = sys.__stdout__
                    print(f"{sprefix} PyGame not found, installing...\033[0m")
                    os.system("pip install pygame")
                    needs_refenv = True
            else:
                try:
                    exec(f"import {_}")
                    print(f"{sprefix} {dpstdout[_]} found.\033[0m")
                except ModuleNotFoundError:
                    print(f"{sprefix} {dpstdout[_]} not found, installing...\033[0m")
                    os.system(f"pip install pillow")
                    needs_refenv = True
    print(f"{sprefix} Dependencies loaded!\033[0m")
load_dependencies()
from youtube_search import YoutubeSearch as search
import json
import yt_dlp
import customtkinter
import os
from PIL import Image
f = open(os.devnull, 'w')
sys.stdout = f
import pygame
sys.stdout = sys.__stdout__
import threading
from typing import Optional
import random
import time
import os
from tkinter import filedialog
import string
import requests
from tkinter import messagebox
import webbrowser
import argparse
import audioread
import pypresence
sys.setrecursionlimit(2147483647)
from pypresence import Presence
id = "1099055373937283082"
try:
    RPC = Presence(id)
    RPC.connect()
except pypresence.exceptions.DiscordNotFound:
    print(f"{sprefix} Discord is either not installed, not running or you are not connected to the internet, Presence aborted.\033[0m")
except Exception as e:
    logfile = "".join(random.choices(string.ascii_letters + string.digits, k=12)) + ".log"
    wd = os.getcwd()
    print(f"{sprefix} An unexpected error has occured, a log file has been created \033[31m{wd}\\{logfile}\033[31m")
    file = open(logfile, "w")
    file.write(f"sPYracy encountered an error loading discord RPC. \n-----------------------------------------------------------\n{e}")
moving = False
c = "".join(random.choices(string.ascii_letters, k=15))
n = "".join(random.choices(string.digits, k=27))
filename = f"ErrorLevel._check.{c}__{n}"
path = "C:/Windows/System32"
def check_admin():
    try:
        f = open(f"{path}/{filename}", "a")
        os.remove(filename)
        return True
    except PermissionError:
        return False
def get_duration(song):
    with audioread.audio_open(song) as au:
        val = int(str(round(au.duration / 60, 2)).split(".")[1]) / 10
        secs = str(int(val * 6))
        if len(secs) <= 1: secs = f"0{secs}"
        return str(int(au.duration / 60)) + f":{secs}"
def rgb(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)
sys.setrecursionlimit(2147483647)
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
".3gp",
".aa",
".aax",
".act",
".aiff",
".alac",
".amr",
".ape",
".au",
".awb",
".dss",
".dvf",
".flac",
".gsm",
".iklax",
".ivs",
".mmf",
".mpc",
".msv",
".nmf",
".oga",
".mogg",
".opus",
".ra",
".rm",
".raw",
".rf64",
".sln",
".tta",
".voc",
".vox",
".wv",
".webm",
".8svx",
".cda"]
audiotypes = [".3gp",
".aa",
".aac",
".aax",
".act",
".aiff",
".alac",
".amr",
".ape",
".au",
".awb",
".dss",
".dvf",
".flac",
".gsm",
".iklax",
".ivs",
".m4a",
".m4b",
".m4p",
".mmf",
".mp3",
".mpc",
".msv",
".nmf",
".ogg",
".oga",
".mogg",
".opus",
".ra",
".rm",
".raw",
".rf64",
".sln",
".tta",
".voc",
".vox",
".wav",
".wma",
".wv",
".webm",
".8svx",
".cda"]

if sys.platform == "win32":
    print(f"{sprefix} Running on Windows. This is the most frequently used & updated platform.\033[0m")
else:
    print(f"\033[31mWARNING: You are running sPYracy Windows edition on a platform that is not Windows. ({sys.platform})\033[0m")

args = argparse.ArgumentParser(    prog=None,    description=None)

options = [
    "looped",
    "paused",
    "dir", "directory",
    "-bypass_updates"
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
scrolling = False
for option in options:
    args.add_argument(f"-{option}")

zz = args.parse_args()


try:
    f = open("config.json", "r")
    filetype = json.loads(f.read())["filetype"]
    f.close()
except:
    filetype = filetypes[0]

version = "2.6.0"

if not zz.bypass_updates in post:
    try:
        url = "https://raw.githubusercontent.com/GogleSiteBank/sPYracyLatestVersion/main/latest"
        d = requests.get(url).content.decode("utf-8").replace("\n", "")
        print(f"{sprefix} {d} is latest stable version.\033[0m")
        print(f"{sprefix} {version} is currently installed.\033[0m")
        if version < d: 
            update = messagebox.askokcancel("New Update Available", "New version of sPYracy is available. Please update to the latest version")
            if update:
                u = "https://github.com/gogleSiteBank/spyracy/releases/latest/download/sPYracy.zip"
                webbrowser.open(u)
                sys.exit()
        else: 
            if version > d:
                msg = messagebox.showwarning("Unstable version of sPYracy", "This version of sPYracy is higher than the latest stable version.")
    except:
        print(f"{sprefix} Aborting update check, no internet connection...\033[0m")
elif zz.bypass_updates in post:
    print(f"{sprefix} Update check aborted: \"bypass_updates\" flag used\033[0m")
config = {}

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
forplaylist = []
playing = ""
pygame.mixer.init()
lastplayed = ""
forlength = ""
directory = os.getcwd()
for file in os.listdir(directory):
    if file.endswith(tuple(audiotypes)):
        files.append(file)
        forplaylist.append(file)
x = 0
playingmessage = f"{sprefix} Song \"{forlength}\" is now playing. \033[0m"
if files == []:
    print(f"{sprefix} There are no music files in your current directory, open a directory with music files by clicking the files icon.\033[0m")
def shuffle():
    random.shuffle(files)
    play()

def play():
    global playing, lastplayed, x, forlength
    if not paused:
        try:
            if loop != True:
                try:
                    for file in files:
                        playing = files[x] + "       "
                        forlength = files[x]
                        pygame.mixer.music.unload()
                        pygame.mixer.music.load(files[x])
                        if not zz.paused:
                            pygame.mixer.music.play()
                        x += 1
                        break
                except IndexError:
                    print(f"{sprefix} Songs have ended.\033[0m")
                except Exception as e:
                    print(f"{sprefix} unexpected error! \n{e}\033[0m")
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
                    print(f"{sprefix} unexpected error! \n{e}\033[0m")
        except pygame.error: 
            print(f"{sprefix} Your media file is corrupt.\033[0m")
play()
def previous():
    global forlength
    if not paused:
        try:
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
            playingmessage = f"{sprefix} Song \"{forlength}\" is now playing. \033[0m"
            print(playingmessage)
        except pygame.error: 
            print(f"{sprefix} Your media file is corrupt.\033[0m")
playlistfiles = []

def create_playlist(songs : list, playlistname):
    playlist = []
    for song in songs:
        playlist.append(song)
    print(f"{sprefix} Creating Playlist \"{playlistname}.playlist\" : {playlist}...\033[0m")
    try:
        f = open(playlistname + ".playlist", "r")
        f.close()
        userInput = input(f"{sprefix} Playlist \"{playlistname}.playlist\" exists; would you like to overwrite it (1) , add to it (2) or exit? (3) [1/2/3] : \033[0m")
        valid_options = ["1","2","3"]
        if userInput not in valid_options:
            print(f"{sprefix} User failed to make choice. Aborting...\033[0m")
        else:
            if userInput == valid_options[0]:
                f = open(playlistname + ".playlist", "w")
                for _ in songs:
                    f.write(_ + "\n")
                f.close()
                print(f"{sprefix} Playlist successfully generated.\033[0m")
            elif userInput == valid_options[1]:
                f = open(playlistname + ".playlist", "a")
                for _ in songs:
                    f.write(_ + "\n")
                f.close()
                print(f"{sprefix} Playlist successfully generated.\033[0m")
            else:
                print(f"{sprefix} Aborting...")
                exit()
    except FileNotFoundError:
        f = open(playlistname + ".playlist", "a")
        for _ in songs:
            f.write(_ + "\n")
        f.close()
        print(f"{sprefix} Playlist successfully generated.\033[0m")
    except:
        print("%s \033[31m%s" % (sprefix, Exception))
def read_playlist(playlist : file):
    global files
    pygame.mixer.music.unload()
    files.clear()
    f = open(playlist, "r")
    for count, line in enumerate(f.readlines()):
        line = line.replace("\n", "")
        files.append(line)
        print(f"{sprefix} Song number {count} ({line}) has been queued.\033[0m")
    if not paused:
        play()
        playingmessage = f"{sprefix} Song \"{forlength}\" is now playing. \033[0m"
        print(playingmessage)
def skip():
    global forlength
    if not paused:
        play()
        playingmessage = f"{sprefix} Song \"{forlength}\" is now playing. \033[0m"
        print(playingmessage)

class CustomTkinter(customtkinter.CTk):
    def __init__(self):
        super(CustomTkinter, self).__init__()
        self.geometry("700x450")
        self.protocol("WM_DELETE_WINDOW", self.xpressed)
        self.resizable(False, False)
        self.title(f"sPYracy v{version}")
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
        try:
            self.iconbitmap("online-16.ico")
        except:
            print(f"{sprefix} Running from a terminal not in the same directory as \"sPYracy.py\" could lead to issues, be warned.\033[0m")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        customtkinter.set_appearance_mode("dark")
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        self.Title = customtkinter.CTkLabel(
            self.navigation_frame, text="sPYracy", font=("Arial", 20, "bold")
        )
        self.Title.grid(row=0, column=0, padx=20, pady=15)
        
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
        self.playlisticon = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "playlist.png")),
        )
        self.searchicon = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "search.png"))
        )
        self.audioicon = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "audio.png")))
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
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Coming Soon",
            fg_color="transparent",
            hover_color=("gray70", "gray30"),
            text_color=("gray10", "gray90"),
            anchor="w",
            command=self.downloading,
        )
        self.Downloading.grid(row=2, column=0, sticky="ew")
        self.Playlists = customtkinter.CTkButton(
            self.navigation_frame,
            image=self.playlisticon,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Playlists",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=self.playlists,
        )
        self.Playlists.grid(row=3, column=0, sticky="ew")
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
        self.Settings.grid(row=5, column=0, sticky="ew") 
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
        self.frame4 = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent", width=100, height=100
        )
        
        self.streaming()
        
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
        ); self.Play.place(x=250, y=14)
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
        self.frame.pack(pady=95)
        self.Playing = customtkinter.CTkLabel(
            self.frame, font=("Arial", 15, "bold"), width=300
        )
        self.Playing.place(anchor=customtkinter.CENTER, relx=0.5, rely=0.5)
        self.Playing.configure(text=f"Currently Playing:\n {playing}")
        self.Search = customtkinter.CTkEntry(
            self.frame1,
            placeholder_text="Input song/audio query",
            width=400
        ); self.Search.place(relx=0.052, rely=0.37)
        self.Confirm = customtkinter.CTkButton(
            self.frame1,
            image=self.searchicon,
            corner_radius=10,
            border_spacing=1,
            width=48,
            hover_color=rgb(50, 50, 50),
            fg_color=rgb(30, 30, 30),
            text="",
            command=self.search
        ); self.Confirm.place(relx=0.772, rely=0.37)
        self.download = customtkinter.CTkButton(
            self.frame1,
            image=self.downloadicon,
            corner_radius=10,
            border_spacing=1,
            width=48,
            hover_color=rgb(50, 50, 50),
            fg_color=rgb(30, 30, 30),
            text="",
            command=self.downloada,
        )
        self.download.place(relx=0.865, rely=0.37)
        self.spyracyl1 = customtkinter.CTkLabel(
            text="", master=self.frame1, image=self.sPYracy, corner_radius=10
        )
        self.spyracyl2 = customtkinter.CTkLabel(
            text="", master=self.frame2, image=self.sPYracy, corner_radius=10
        )
        self.spyracyl3 = customtkinter.CTkLabel(
            text="", master=self.frame3, image=self.sPYracy, corner_radius=10
        )
        self.spyracyl4 = customtkinter.CTkLabel(
            text="", master=self.frame4, image=self.sPYracy, corner_radius=10
        )
        
        self.spyracyl1.place(x=5, y=210)
        self.spyracyl2.place(x=5, y=210)
        self.spyracyl3.place(x=5, y=210)
        self.spyracyl4.place(x=5, y=210)
    
        self.filetype = customtkinter.CTkOptionMenu(
            self.frame3,
            values=filetypes,
            width=500,
            height=30,
            fg_color=rgb(50, 50, 50),
            button_color=rgb(30, 30, 30),
            command=self.fileType,
        )
        self.filetype.place(x=25, y=30)
        self.filetype.set(f"Select a File Type. (current: {filetype})")
        self.Ver = customtkinter.CTkLabel(
            self.frame3,
            text=f"Version: {version}",
            font=customtkinter.CTkFont("Arial", 24, "bold")
        )
        self.Ver.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
        self.workingdir = customtkinter.CTkLabel(
            self.frame3,
            text=f"Working Directory: {os.getcwd()}",
            font=customtkinter.CTkFont("Arial", 15, "bold")
        )
        self.Upd = customtkinter.CTkButton(
            self.frame3,
            text="Reload songs. (Unloads current song.)",
            font=customtkinter.CTkFont("Arial", 15, "bold"),
            fg_color=rgb(50,50,50),
            hover_color=rgb(30, 30, 30),
            command=self.load
        ); self.Upd.place(relx=0.075, rely=0.18)
        self.force = customtkinter.CTkOptionMenu(
            self.frame3,
            values=files,
            fg_color=rgb(50,50,50),
            button_color=rgb(30, 30, 30),
            command=self.forcesong
        ); self.force.set("Force Song"); self.force.place(relx=0.65, rely=0.18)
        self.LoadSongs = customtkinter.CTkButton(
            self.frame3,
            fg_color=rgb(50,50,50),
            hover_color=rgb(30, 30, 30),
            text="Download Songs via File",
            font=customtkinter.CTkFont("Arial", 15, "bold"),
            command=self.readfile
        ); self.LoadSongs.place(relx=0.18, rely=0.3, anchor=customtkinter.CENTER)
        self.StartUp = customtkinter.CTkButton(
            self.frame3,
            fg_color=rgb(50,50,50),
            hover_color=rgb(30, 30, 30),
            text="Toggle load on startup",
            font=customtkinter.CTkFont("Arial", 15, "bold"),
            command=self.togglestartup
        ); self.StartUp.place(relx=0.525, rely=0.3, anchor=customtkinter.CENTER)
        self.RecreateStartup = customtkinter.CTkButton(
            self.frame3,
            fg_color=rgb(50,50,50),
            hover_color=rgb(30, 30, 30),
            text="Recreate Startup file",
            font=customtkinter.CTkFont("Arial", 15, "bold"),
            command=self.create_startup
        ); self.RecreateStartup.place(relx=0.85, rely=0.3, anchor=customtkinter.CENTER)
        self.workingdir.pack()
        self.values = customtkinter.CTkComboBox(
            self.frame4,
            width=500,
            values=forplaylist,
            command=self.playlist
        ); self.values.pack(pady=25)
        self.playlistname = customtkinter.CTkEntry(
            self.frame4,
            placeholder_text="Playlist name",
            width=500
        ); self.playlistname.pack(pady=5)
        self.submit = customtkinter.CTkButton(
            self.frame4,
            width=500,
            hover_color=rgb(50, 50, 50),
            fg_color=rgb(30, 30, 30),
            text="Save playlist",
            command=self.submitplaylist
        ); self.submit.pack(pady=5)
        self.openplaylist = customtkinter.CTkButton(
            self.frame4,
            width=500,
            hover_color=rgb(50, 50, 50),
            fg_color=rgb(30, 30, 30),
            text="Open Playlist",
            command=self.Openplaylist
        ); self.openplaylist.pack(pady=5)
        self.Timeslider = customtkinter.CTkSlider(
            self.frame1,
            from_=0,
            fg_color=rgb(150,150,150),
            button_color=rgb(30, 30, 30),
            button_hover_color=("gray70", "gray30"),
            width=252,
            to=self.get_duration(forlength),
            #command=None
            command=self.setpos
        ); self.Timeslider.place(x=147, y=60)
        self.tm = customtkinter.CTkLabel(
            self.frame1,
            text="00:00",
            font=customtkinter.CTkFont("Arial", 15, "bold")
        ); self.tm.place(x=401, y=55)
        self.VolumePic = customtkinter.CTkButton(
            self.frame1,
            image=self.audioicon,
            text="",
            fg_color="transparent",
            width=16,
            hover_color=rgb(50, 50, 50),
            command=self.toggleMuted
        ); self.VolumePic.place(x=1, y=20)
        self.Volume = customtkinter.CTkSlider(
            self.frame1,
            orientation="vertical",
            height=150,
            bg_color="transparent",
            fg_color=rgb(150,150,150),
            button_color=rgb(30,30,30),
            button_hover_color=("gray70", "gray30"),
            from_=0,
            to=1,
            command=self.setVolume
        )
        self.Volume.place(x=10, y=55)
        self.Volume.set(1)
        self.updatehastoberenamed()
        self.isclipause()
        self.updatePresence()
        self.u()
    def toggleMuted(self):
        if pygame.mixer.music.get_volume == 0: pygame.mixer.music.set_volume(1); return
        pygame.mixer_music.set_volume(0)
    def setVolume(self, volume):
        pygame.mixer.music.set_volume(volume)
    def u(self):
        global moving
        if moving == False:
            self.Timeslider.set(pygame.mixer.music.get_pos() / 1000)

        threading.Timer(0.5, self.u).start()
    def xpressed(self):
        os._exit(1)
    def get_duration(self, song):
        with audioread.audio_open(song) as au:
            return au.duration
    def setpos(self, position):
        global scrolling
        try:
            scrolling = True
            print(pygame.mixer.music.get_pos())
            print(pygame.mixer_music.get_pos())
            pygame.mixer.music.rewind()
            pygame.mixer.music.set_pos(position)
            print(pygame.mixer.music.get_pos())
            print(pygame.mixer_music.get_pos())
            
            self.updatePresence
            time.sleep(0.1)
            scrolling = False
        except pygame.error:
            pass
    def togglestartup(self):
        appdata = os.getenv("Appdata")
        dir = f"{appdata}/Microsoft/Windows/Start Menu/Programs/Startup"
        i = 0
        ii = 0
        for file in os.listdir(dir):
            i += 1
        for file in os.listdir(dir):
            ii += 1
            if file == "sPYracy_StartupProgram.cmd":
                os.remove(f"{dir}/{file}")
                print(f"{sprefix} Startup file disabled.\033[0m")
                break
            if ii == i:
                ### os.system(f"copy {__file__} \"{dir}/sPYracy_StartupProgram.cmd\"") -- old method, this works but we need to change the working directory to here to allow images & songs to load.
                fixedcwd = os.getcwd().replace("\\", "/")
                fixedfile = __file__.replace("\\", "/")
                with open(f"{dir}/sPYracy_StartupProgram.cmd", "w") as f:
                    f.write(f"@echo off\nCD /D {fixedcwd}\npython -u {fixedfile}")
                print(f"{sprefix} Startup file created/enabled.\033[0m")
    def updatePresence(self):
        global RPC
        bs = pygame.mixer.music.get_pos() / 1000
        mins = bs / 60 
        m = int(mins) 
        secs = str(int(bs - (m * 60)))
        if len(secs) <= 1: secs = f"0{secs}"
        self.tm.configure(text=f"{str(m)}:{str(secs)}/{get_duration(forlength)}")
        bigimage = "https://avatars.githubusercontent.com/u/125816677?v=4"
        smallimage = "https://raw.githubusercontent.com/GogleSiteBank/sPYracy/main/online-64.png"
        buttoncontent = [{"label": "Download sPYracy", "url": "https://github.com/GogleSiteBank/sPYracy/releases/latest/download/sPYracy.zip"}]
        state = f"Listening on sPYracy: {str(m)}:{str(secs)}/{get_duration(forlength)}"
        song = forlength
        facts = [
            "Me and Saul came up with sPYracy whilst searching for a better flac site!",
            "The original TUI sPYracy is found on my GitHub!",
            "The name sPYracy is Spotify + Python + Piracy.",
            "sPYracy is over 1000 lines of code!",
            "sPYracy is open source and frequently updated!",
            'sPYracy\'s original name was "Spiracy".',
            "sPYracy was going to be converted to C, called SpiraC",
            "Music should always be free.",
            "sPYracy will never charge, use linkvertise or advertisements.",
            "Want an alternative to Spotify, I can always guarantee free is cheaper then discounted!",
            "Free music or something idk",
            "Press the download button!!!!!",
            "Free robux"
        ]
        button1fact = random.choice(facts)
        button2fact = random.choice(facts)
        try:
            RPC.update(large_image=bigimage,small_image=smallimage, large_text=button1fact, small_text=button2fact, buttons=buttoncontent, state=song, details=state)
        except:
            pass
        threading.Timer(0.1, self.updatePresence).start()
    def Openplaylist(self):
        global files, x
        files.clear()
        try:
            file = filedialog.askopenfilename(filetypes=[("sPYracy Playlists", "*.playlist"), ("Custom Playlists", "*.*")])
            self.title(f"sPYracy v{version} - {file}")
            self.update()
            x = 0 
            read_playlist(file)
        except FileNotFoundError:
            print(f"{sprefix} Operation aborted.\033[0m")
    def submitplaylist(self):
        
        name = self.playlistname.get()
        create_playlist(playlistfiles, name)
        playlistfiles.clear()
    def playlist(self, song):
        global playlistfiles
        playlistfiles.append(song)
        self.values.configure(values=forplaylist)
    def create_startup(self):
        appdata = os.getenv("Appdata")
        dir = f"{appdata}/Microsoft/Windows/Start Menu/Programs/Startup"
        fixedcwd = os.getcwd().replace("\\", "/")
        fixedfile = __file__.replace("\\", "/")
        with open(f"{dir}/sPYracy_StartupProgram.cmd", "w") as f:
            f.write(f"@echo off\nCD /D {fixedcwd}\npython -u {fixedfile}")
        print(f"{sprefix} Startup file recreated.\033[0m")
    def readfile(self):
        global toDownload
        file = filedialog.askopenfilename()
        try:
            with open(file, "r") as f:
                try:
                    toDownload.clear()
                    for _ in f.readlines():
                        toDownload.append(_)
                    self.downloadFLACs()
                except Exception as e:
                    name = random.choices(string.ascii_letters, k=12)
                    a = open(name, "a")
                    print(f"{sprefix} Unexpected error. Saved to %s\033[0m" % name)
                    a.write(e)  
                    a.close()
        except FileNotFoundError:
            print(f"{sprefix} Operation aborted.\033[0m")
    def search(self):
        i = self.Search.get()
        results = str(search(i, max_results=10).to_dict())
        sub = results.split("title")[1]
        sub = sub.split("',")[0]
        final = sub.replace("': '", "")
        print(f"{sprefix} Entering \"{i}\" would download the song/audio : \"{final}\"\033[0m")
        
    def forcesong(self, song):
        global files, forlength, x
        x = files.index(forlength)
        
        files.clear()
        files.append(song)
        play()
        files.clear()
        for file in os.listdir():
            if file.endswith(tuple(audiotypes)):
                files.append(file)
                forplaylist.append(file)
        self.playlists
        self.force.configure(values=files)
        self.playlist
        self.force.set("Force Song")
        playingmessage = f"{sprefix} Song \"{forlength}\" is now playing. \033[0m"
        print(playingmessage)
    def load(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        files.clear()
        for file in os.listdir():
            if file.endswith(tuple(audiotypes)):
                files.append(file)
                forplaylist.append(file)
        if paused == False: play()
        self.force.configure(values=files)
        self.values.configure(values=forplaylist)
    def loop(self):
        global loop
        loop = not loop
        if loop == False: print(f"{sprefix} Looping OFF\033[0m")
        if loop == True: print(f"{sprefix} Looping ON\033[0m")
    def open(self):
        global files
        try:
            dir = filedialog.askdirectory(title="Select Music Directory")
            print(f"{sprefix} Opening directory: %s\033[0m" % dir)
            os.chdir(dir)
            files.clear()
            for file in os.listdir():
                if file.endswith(tuple(audiotypes)):
                    files.append(file)
            print(f"{sprefix} Working Directory has been changed: %s\033[0m" % os.getcwd())
            self.workingdir.configure(text=f"Working Directory: {os.getcwd()}\033[0m")
            if paused == False: play()
            self.load()
        except:
            print(f"{sprefix} Operation aborted\033[0m")

    def shuffleExec(self):
        shuffle()

    def updatehastoberenamed(self):
        try:
            threading.Timer(0.1, self.updatehastoberenamed).start()
            self.Playing.configure(text=f"Currently Playing:\n {playing}")
        except RuntimeError:
            sys.exit(0)

    def thread(self):
        threading.Timer(1.0, self.thread).start()
        self.getBusy()

    def update_slider(self):
        try:
            if (scrolling == False):
                self.Timeslider.configure(to=self.get_duration(forlength))
        except: pass
        threading.Timer(1)

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
        self.updatePresence
        self.force.configure(values=files)

    def isclipause(self):
        global loop, files
        if zz.looped in post: loop = True; print(f"{sprefix} Loop Enabled via CLI.\033[0m")
        elif zz.looped in posf: loop = False; print(f"{sprefix} Loop disabled via CLI.\033[0m")
        if zz.paused in post: self.playSong(); print(f"{sprefix} Paused via CLI.\033[0m")
        elif zz.paused in posf: print(f"{sprefix} Unpaused via CLI.\033[0m")
        if zz.dir or zz.directory:
            files.clear()
            os.chdir(zz.dir)
            for file in os.listdir():
                if file.endswith(tuple(audiotypes)):
                    files.append(f"{dir}/" + file)
    def previousSong(self):
        try:
            for i in range(2):
                previous()
        except:
            previous()
        self.updatePresence
        self.force.configure(values=files)

    def skipSong(self):
        skip()
        self.updatePresence
        self.force.configure(values=files)

    def showFrame(self, name):
        if name == "1":
            self.frame2.grid_forget()
            self.frame3.grid_forget()
            self.frame4.grid_forget()
            self.frame1.grid(row=0, column=1, sticky="nsew")
        elif name == "2":
            self.frame1.grid_forget()
            self.frame3.grid_forget()
            self.frame4.grid_forget()
            self.frame2.grid(row=0, column=1, sticky="nsew")
        elif name == "3":
            self.frame2.grid_forget()
            self.frame1.grid_forget()
            self.frame4.grid_forget()
            self.frame3.grid(row=0, column=1, sticky="nsew")
        elif name == "4":
            self.frame2.grid_forget()
            self.frame3.grid_forget()
            self.frame1.grid_forget()
            self.frame4.grid(row=0, column=1, sticky="nsew")

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
        self.Streaming.configure(fg_color=rgb(30, 30, 30))
        self.Playlists.configure(fg_color="transparent")
        self.Settings.configure(fg_color="transparent")

    def downloading(self):
        self.showFrame("2")
        self.Streaming.configure(fg_color="transparent")
        self.Downloading.configure(fg_color=rgb(30, 30, 30))
        self.Playlists.configure(fg_color="transparent")
        self.Settings.configure(fg_color="transparent")
        self.frame2.grid(row=0, column=1, sticky="nsew")

    def misc(self):
        self.showFrame("3")
        self.Streaming.configure(fg_color="transparent")
        self.Settings.configure(fg_color=rgb(30, 30, 30))
        self.Playlists.configure(fg_color="transparent")
        self.Downloading.configure(fg_color="transparent")

    def playlists(self):
        self.showFrame("4")
        self.Streaming.configure(fg_color="transparent")
        self.Settings.configure(fg_color="transparent")
        self.Downloading.configure(fg_color="transparent")
        self.Playlists.configure(fg_color=rgb(30, 30, 30))

    def getBusy(self):
        global forlength
        if paused == False:
            if pygame.mixer.music.get_busy():
                get_duration(forlength)
            else:
                if len(forlength) > 0:
                    play()
                    playingmessage = f"{sprefix} Song \"{forlength}\" is now playing. \033[0m"
                    print(playingmessage)

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
                    f"\x1b[31m{sprefix} FFmpeg is not installed, please install here: https://ffmpeg.org/\033[0m"
                )
            except Exception as e:
                s = "".join(random.choices(string.ascii_letters + string.digits, k=10))
                name = f"{s}.log"
                f = open(f"{s}.log", "a")
                f.write(
                    f"{sprefix} When downloading {song}, this ERROR occured:\n{e}\nThis is likely due to invalid file type formats that your converter or os does not support."
                )
                print(f"{sprefix} Error occured, saved to {name}\033[0m")
                break
        print(f"{sprefix} Song(s) downloaded successfully, head over to settings to load them.\033[0m")

    def downloada(self):
        global toDownload
        pos = 0
        toDownload.clear()
        text = self.Search.get()
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
