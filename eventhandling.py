import pyglet
import pyglet.gui
from pyglet.gl import *



class HelloWorldWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = pyglet.text.Label('Hello, world!')

    def on_draw(self):
        self.clear()
        self.label.draw()

if __name__ == '__main__':
    window = HelloWorldWindow(resizable=True)
    
    print(window._resizable)
    pyglet.app.run()