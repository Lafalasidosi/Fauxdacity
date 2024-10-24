import pyglet
import pyglet.gui
from pyglet.gl import *

# To create an event dispatcher, 
# 1. Subclass EventDispatcher
# 2. Call register_event_type() on subclass for each event subclass will recognize
# 3. Call dispatch_event() to create and dispatch an event as needed.

class HelloWorldWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = pyglet.text.Label('Hello, world!')
        self.buttonBatch = pyglet.graphics.Batch()
        pressed_img = pyglet.image.load('resources/normal/png/16x16/Wizard.png')
        depressed_img = pyglet.image.load('resources/normal/png/16x16/Home.png')
        self.pushbutton = pyglet.gui.PushButton(x=100, y=300, pressed=pressed_img, depressed=depressed_img, batch=self.buttonBatch)
        self.push_handlers(self.pushbutton)

    def on_draw(self):
        self.clear()
        self.label.draw()
        self.buttonBatch.draw()

if __name__ == '__main__':
    window = HelloWorldWindow(resizable=True)

    def on_resize(width, height):
        window.pushbutton.x += 3

    window.on_resize = on_resize
    
    print(window._resizable)
    pyglet.app.run()

