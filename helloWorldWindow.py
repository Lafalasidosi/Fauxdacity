import pyglet
import pyglet.gui
from pyglet.gl import *


## DO NOT SUBCLASS pyglet.window.Window
#  You CANNOT make your window resizable if you do so
class HelloWorldWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__()
        self.buttonBatch = pyglet.graphics.Batch()
        self.labelBatch = pyglet.graphics.Batch()
        self.label = pyglet.text.Label("Hello World!", batch=self.labelBatch)
        self.resizable = True
        #pressed_img = pyglet.image.load('resources/normal/png/16x16/Wizard.png')
        #depressed_img = pyglet.image.load('resources/normal/png/16x16/Home.png')
        #self.pushbutton = pyglet.gui.PushButton(x=100, y=300, pressed=pressed_img, depressed=depressed_img, batch=self.buttonBatch)
        #self.push_handlers(self.pushbutton)

    def on_draw(self):
        self.clear()
        self.labelBatch.draw()
        self.buttonBatch.draw()

if __name__ == '__main__':
    window = HelloWorldWindow()
    window2 = pyglet.window.Window(resizable=True)
    window2.set_visible(True)
    window.set_visible(True)
    

    
    print(window.resizeable)



    
    pyglet.app.run()


