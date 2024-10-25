import pyglet
import pyglet.gui
from pyglet.gl import *
from tkinter import *
from tkinter import filedialog

# global variable for audio
global audio 


def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/home/lafalasidosi/Fauxdacity", title = "Select a File", filetypes = (("Text files","*.txt*"),("all files", "*.*")))
    print(filename)
    global audio 
    audio = pyglet.media.load(filename)


def playSound(): 
    global audio
    audio.play() 
    

class AppWindow(pyglet.window.Window):
    def __init__(self, width, height, *args, **kwargs):
        super().__init__(width, height, *args, **kwargs)
        self.width = width
        self.height = height

        load_pressed = pyglet.image.load('resources/folder_small.png')  # attr. to Freepik      
        load_depressed = pyglet.image.load('resources/folder_small.png')
        play_pressed = pyglet.image.load('resources/play_button_small.png')
        play_depressed = pyglet.image.load('resources/play_button_small.png')
        self.buttonsBatch = pyglet.graphics.Batch()
        self.loadButton = pyglet.gui.PushButton(x=0, y=height-32, pressed=load_pressed, depressed=load_depressed, batch=self.buttonsBatch)
        self.playButton = pyglet.gui.PushButton(x=33, y=height-32, pressed=play_pressed, depressed=play_depressed, batch=self.buttonsBatch)
        self.loadButton.on_press = browseFiles
        self.playButton.on_press = playSound
        self.push_handlers(self.loadButton)
        self.push_handlers(self.playButton) 
        
        

    def on_draw(self):
        self.clear()
        self.buttonsBatch.draw()

if __name__ == '__main__':
    window = AppWindow(500, 500)
    window.set_visible(True)
    
    pyglet.app.run()

    