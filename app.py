from tkinter import filedialog as fd
from tkinter import messagebox as msg
from tkinter import ttk
from tkinter import *
import pygame as pg
import about
import webbrowser
import homepage
import os

pg.init()
isPause = False

def aboutme():
    msg.showinfo("About Me",f"author: {about.author}\nversion: {about.version}\ncreated in: {about.created}")

def homePage():
    webbrowser.open(homepage.url)

def manage(event):
    global isPause
    if isPause == False:
        pg.mixer.music.unpause()
        isPause = True
    elif isPause == True:
        pg.mixer.music.pause()
        isPause = False

def main():
    global songs,name,musicPath
    musicPath = fd.askdirectory(initialdir = os.path.normpath("Desktop"),title = "Open")
    songs = []
    files = os.listdir(musicPath)
    try:
        for i in range(0,len(files)):
            x = files[i].split(".")[1]
            if (x == "mp3")|(x == "ogg")|(x == "wav"):
                songs.append(files[i])
        songsBox["values"] = tuple(songs)
    except:
        msg.showerror("Error","There is no files")

def end(event):
    global top
    if top == "None":
        pass
    else:
        app.title(f"Music-GUI-[{top}]")
        pg.mixer.music.stop()
        headingLabel.config(text = f"{top} has been stopped!")

def play():
    global name,top
    try:
        if songsBox.get() != "None":
            name = songsBox.get()
            top = name
            app.title(f"Music-GUI-[{top}]")
            fullPath = musicPath+"/"+name
            headingLabel.config(text = f"now you are listening {name}")
            pg.mixer.music.load(fullPath)
            pg.mixer.music.play()
        else:
            msg.showerror("Error",f"{name} song not found in the given directory")
    except:
        msg.showerror("Error","Select the file to play the songs!")

def use():
    msg.showinfo("How to Use?","1. Select the song from directory from top left corner\n2. Press spacebar to pause/unpause the current song!")

top = "None"
app = Tk()
app.geometry("700x150")
app.title(f"Music-GUI-[{top}]")
app.resizable(False,False)

menuBar = Menu(app)
app.config(menu = menuBar)
menuBar.add_command(label = "Directory",command = main)
menuBar.add_command(label = "About",command = aboutme)
menuBar.add_command(label = "HomePage",command = homePage)
menuBar.add_command(label = "Help",command = use)

headingFrame = Frame(app,relief = GROOVE,bd = 0)
headingFrame.pack(fill = BOTH,padx = 5,pady = 5)
headingLabel = Label(headingFrame,text = "Choose the songs!",font = ("ubuntu",16),bg = "gray")
headingLabel.pack(fill = BOTH,padx = 5,pady = 5)
mainFrame = Frame(app)
mainFrame.pack(fill = BOTH,padx = 5,pady = 5)
mainLabel = Label(mainFrame,text = "Songs: ",font = ("ubuntu",13))
mainLabel.grid(row = 0,column = 0,padx = 5,pady = 5)

title = StringVar()
songsBox = ttk.Combobox(mainFrame,font = ("ubuntu",13),textvariable = title,width = 40,state = "readonly")
songsBox.grid(row = 0,column = 1,padx = 5,pady = 5)
songsBox["values"] = "None"
songsBox.current(0)
playBtn = Button(mainFrame,text = "play",font = ("ubuntu",9),width = 20,fg = "#ffffff",bg = "#000000",command = play)
playBtn.grid(row = 0,column = 2,padx = 5,pady = 5)

helpFrame = Frame(app)
helpFrame.pack(fill = BOTH,padx = 5,pady = 5)
helpLabel = Label(helpFrame,font = ("ubuntu",9),text = "press spacebar to pause/unpause the current playing song!\npress escape button to stop the current song!")
helpLabel.pack(fill = BOTH,padx = 5)

app.bind("<space>",manage)
app.bind("<Escape>",end)

app.mainloop()
