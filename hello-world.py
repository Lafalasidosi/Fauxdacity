# https://docs.pyglet.org/en/latest/programming_guide/quickstart.html

import pyglet
from pyglet.window import key
from pyglet.window import mouse


window = pyglet.window.Window()
#image = pyglet.resource.image("play.jpg") # looks wrt hello-world, not working directory


#label = pyglet.text.Label('Hello, world', 
  #                        font_name='Times New Roman', 
 #                        font_size=36,
  #                        x=window.width//2, y=window.height//2, 
   #                       anchor_x='center', anchor_y='center')


# Keyboard events have two params: virtual key 'symbol" that was pressed,
# and a bitwise combination of any modifiers which are present
# e.g. CTRL, SHIFT, ALT
# key symbols are defined in pyglet.window.key
@window.event
def on_key_press(symbol, modifiers):
    #print('A key was pressed')
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The Enter key was pressed.')
    else:
        print('Some other key was pressed.')


@window.event
def on_mouse_press(x,y,button,modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed at:', x, y) # python adds spaces? Nice!
    
# music = pyglet.resource.media('start.wav') # use pyglet.media.load() when using absolute/relative path
# music.play() # plays at app startup


# decodes in memory before used
# allaws sound to play more immediately and incur less CPU performance penalty
# probably mostly for games; streaming works well for "longer music tracks"
# MP3/other compressed audio formats require FFmpeg. WAVs do not.
sound = pyglet.resource.media('start.wav', streaming=False) 
sound.play()


@window.event
def on_draw():
    window.clear()
    #image.blit(0,0) # starting from lower-left corner
   # label.draw()


pyglet.app.run()







#There are more than 20 event types that you can handle on a window. 
# An easy way to find the event names and parameters you need 
# is to add the following lines to your program:

### event_logger = pyglet.window.event.WindowEventLogger()
###window.push_handlers(event_logger)

# This will cause all events received on the window to be printed to the console.