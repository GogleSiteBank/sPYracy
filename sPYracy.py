import json
from youtube_search import YoutubeSearch as search
import yt_dlp
import customtkinter
import os
from PIL import Image
import pygame
import threading
from typing import Optional
def rgb(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)
import sys

filetypes = [".flac", ".mp3", ".ogg", ".wav", ".wma", ".aac", ".m4a", ".m4b", ".m4p", ".m4r", ".m4v", ".mid", ".midi", ".midiin", ".midiout", ".mp4", ".mpg", ".mpeg", ".mpg4"]

filetype = "flac"

config = {""}

def updateconfig():
    config = {
        'outtmpl': '%(title)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': filetype,
        }]
    }

updateconfig()
files = []
playing = "Example"
pygame.mixer.init()
lastplayed = ""

for file in os.listdir():
    if file.endswith(tuple(filetypes)):
        files.append(file)

x = 0


def play():
    global playing, lastplayed, x
    for file in files:
        playing = files[x] + "       "
        pygame.mixer.music.unload()
        pygame.mixer.music.load(files[x])
        pygame.mixer.music.play()
        x += 1
        break


def previous():
    global playing, lastplayed, x
    for file in files:
        x -= 1
        playing = files[x]
        pygame.mixer.music.unload()
        pygame.mixer.music.load(files[x])
        pygame.mixer.music.play()
        break

paused = False

def skip():
    play()


play()

class CustomTkinter(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x450")
        self.resizable(False, False)
        self.title("sPYracy")
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images/online-16.ico")
        self.iconbitmap("online-16.ico")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self._set_appearance_mode("Dark")
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        self.Title = customtkinter.CTkLabel(self.navigation_frame, text="sPYracy", font=("Arial", 20, "bold"))
        self.Title.grid(row=0, column=0, padx=20, pady=15)
       ################ Start of Page Frames ################

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))

        self.streamingicon = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "online-64.png")),)
        self.downloadicon = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "download-64.png")),)
        self.settingicon = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "cog-64.png")),)
        self.play = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Play.png")))
        self.pause = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Pause.png")))
        self.skip = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Skip.png")))
        self.previous = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Previous.png")))
        self.sPYracy = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Image.png")), size=(520, 225))

        self.Streaming = customtkinter.CTkButton(self.navigation_frame, image=self.streamingicon, corner_radius=0, height=40, border_spacing=10, text="Streaming", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.streaming)
        self.Streaming.grid(row=1, column=0, sticky="ew")
        self.Downloading = customtkinter.CTkButton(self.navigation_frame, image=self.downloadicon, corner_radius=0, height=40, border_spacing=10, text="Download FLACs", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.downloading)
        self.Downloading.grid(row=2, column=0, sticky="ew")
        self.Settings = customtkinter.CTkButton(self.navigation_frame, image=self.settingicon, corner_radius=0, height=40, border_spacing=10, text="Settings", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.misc)
        self.Settings.grid(row=3, column=0, sticky="ew")
        self.frame1 = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", width=100, height=100)
        self.frame1.grid(row=0, column=1, sticky="nsew")
        self.frame2 = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", width=100, height=100)
        self.frame3 = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", width=100, height=100)
        self.streaming()

        ################ End of Page Frames ################
        self.Previous = customtkinter.CTkButton(self.frame1, image=self.previous, corner_radius=10, height=40, border_spacing=10, text="", fg_color="transparent", width=16, hover_color=rgb(50, 50,50), command=self.previousSong)
        self.Previous.place(x=200, y=30)
        self.Play = customtkinter.CTkButton(self.frame1, image=self.pause, corner_radius=10, height=40, border_spacing=10, text="", fg_color="transparent", width=16, hover_color=rgb(50, 50,50), command=self.playSong)
        self.Play.place(x=250, y=30)
        self.Skip = customtkinter.CTkButton(self.frame1, image=self.skip, corner_radius=10, height=40, border_spacing=10, text="", fg_color="transparent", width=16, hover_color=rgb(50, 50, 50), command=self.skipSong)
        self.Skip.place(x=300, y=30)
        self.thread()
        self.scrollingText()
        self.frame = customtkinter.CTkFrame(master=self.frame1, height=55, width=500)
        self.frame.pack(pady=80)
        self.Playing = customtkinter.CTkLabel(self.frame, font=("Arial", 15, "bold") ,width=300)
        self.Playing.place(anchor=customtkinter.CENTER, relx=0.5, rely=0.5)
        self.Playing.configure(text = f"Currently Playing:\n {playing}")
        self.spyracyl1 = customtkinter.CTkLabel(text="",master=self.frame1, image=self.sPYracy, corner_radius=10)
        self.spyracyl2 = customtkinter.CTkLabel(text="",master=self.frame2, image=self.sPYracy, corner_radius=10)
        self.spyracyl3 = customtkinter.CTkLabel(text="",master=self.frame3, image=self.sPYracy, corner_radius=10)
        self.spyracyl1.place(x=5, y=210)
        self.spyracyl2.place(x=5, y=210)
        self.spyracyl3.place(x=5, y=210)
        self.flacdownloader = customtkinter.CTkEntry(self.frame2, placeholder_text=f"Enter name of the {filetype}(s) to download (seperate with ':').", width=500, height=30)
        self.flacdownloader.place(x=25, y=30)
        self.filetype = customtkinter.CTkOptionMenu(self.frame3, values=filetypes, width=500, height=30, fg_color=rgb(50,50,50), button_color=rgb(31,31,31), command=self.fileType)
        self.filetype.place(x=25, y=30)
        self.filetype.set(f"Select a File Type. (current: {filetype})")
        self.download = customtkinter.CTkButton(self.frame2, image=self.downloadicon, corner_radius=10, height=40, border_spacing=1, width=500, hover_color=rgb(50, 50,50), fg_color=rgb(31,31,31), text="Download", command=self.download)
        self.download.place(x=25, y=90)
        self.update()

    def update(self):
        try:
            threading.Timer(0.1, self.update).start()
            self.Playing.configure(text = f"Currently Playing:\n {playing}")
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
    def fileType(self, s : str):
        global filetype
        filetype = s
        self.filetype.set(f"Select a File Type. (current: {filetype})")
        f = open("config.json", "w")
        f.write(json.dumps({"filetype": s}))
        updateconfig()

    toDownload = []
    def downloadFLACs(self):
        global toDownload
        for FLAC in toDownload:
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
                    files.append(file)

    def download(self):
        global toDownload
        pos = 0
        toDownload.clear()
        text = self.flacdownloader.get()
        for l in text:
            pos += 1
            if ":" in text:
                if l == ":":
                    toDownload.clear()
                    toDownload.append(text.split(":", pos))
                    self.downloadFLACs()
            else:
                toDownload.append(text)
                self.downloadFLACs()
                break
try:
    f = open("config.json", "r")
    filetype = json.loads(f.read())["filetype"]
    f.close()
except:
    pass
CustomTkinter().mainloop()
