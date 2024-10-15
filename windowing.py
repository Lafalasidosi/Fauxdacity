import pyglet
from pyglet.gl import Config 


# several ways to control the context that is created




window = pyglet.window.Window(1280, 500, resizable=True)
window.set_caption("YYYY")
wizard_hat = pyglet.image.load('resources/normal/png/16x16/Wizard.png')
window.set_icon(wizard_hat)


window.set_visible()
pyglet.app.run()