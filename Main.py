import pyglet
import pyglet.gui
from pyglet.gl import *
from tkinter import *
from tkinter import filedialog

def browseFiles():
        filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))

class AppWindow(pyglet.window.Window):
    def __init__(self, width, height, *args, **kwargs):
        super().__init__(width, height, *args, **kwargs)
        self.width = width
        self.height = height
        load_pressed = pyglet.image.load('resources/folder_small.png')        
        load_depressed = pyglet.image.load('resources/folder_small.png')

        self.buttonsBatch = pyglet.graphics.Batch()
        self.loadButton = pyglet.gui.PushButton(x=250, y=250, pressed=load_pressed, depressed=load_depressed, batch=self.buttonsBatch)
        self.loadButton.on_press = browseFiles   
        self.push_handlers(self.loadButton)  

    def on_draw(self):
        self.clear()
        self.buttonsBatch.draw()

if __name__ == '__main__':
    window = AppWindow(500, 500)
    window.set_visible(True)
    
    pyglet.app.run()

    