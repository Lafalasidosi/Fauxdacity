import pyglet
import pyglet.gui

class HelloWorldWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__()
        self.buttonBatch = pyglet.graphics.Batch()
        self.label = pyglet.text.Label("Hello World!")
        

    def on_draw(self):
        self.clear()
        self.label.draw()
        self.buttonBatch.draw()

if __name__ == '__main__':
    window = HelloWorldWindow()
    pressed_img = pyglet.image.load('resources/play.png')
    depressed_img = pyglet.image.load('resources/play_copy.png')
    pushbutton = pyglet.gui.PushButton(x=0, y=0, pressed=pressed_img, depressed=depressed_img, batch=window.buttonBatch)
    
    window.push_handlers(pushbutton)
    pyglet.app.run()