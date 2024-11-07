import pyglet
import pyglet.gui
from pyglet.gl import *
from tkinter import *
from tkinter import filedialog
import array, itertools, wave
from pyglet.shapes import Line

# global variable for audio
global audio 







    

class AppWindow(pyglet.window.Window):
    def __init__(self, width, height, *args, **kwargs):
        super().__init__(width, height, *args, **kwargs)
        self.width = width
        self.height = height
        self.lines = []
        self.loaded_audio = None
        global audio
        #audio = wave.open("start.wav", "rb")
        load_pressed = pyglet.image.load('resources/folder_small.png')  # attr. to Freepik      
        load_depressed = pyglet.image.load('resources/folder_small.png')
        play_pressed = pyglet.image.load('resources/play_button_small.png')
        play_depressed = pyglet.image.load('resources/play_button_small.png')
        self.buttonsBatch = pyglet.graphics.Batch()
        self.waveformBatch = pyglet.graphics.Batch()
        self.loadButton = pyglet.gui.PushButton(x=0, y=height-32, pressed=load_pressed, depressed=load_depressed, batch=self.buttonsBatch)
        self.playButton = pyglet.gui.PushButton(x=33, y=height-32, pressed=play_pressed, depressed=play_depressed, batch=self.buttonsBatch)
        self.loadButton.on_press = self.browseFiles
        self.playButton.on_press = self.playSound
        self.push_handlers(self.loadButton)
        self.push_handlers(self.playButton) 

    def process_audio(self):
        # waveform 
        samples = self.loaded_audio.readframes(self.loaded_audio.getnframes()) 
        array_of_ints = array.array("h", samples)
        normalized = [x / 65536 for x in array_of_ints]
        batched_samples = list(itertools.batched(normalized, 2))
        
        moreSamples = batched_samples[0::40]
        sample_width = self.width / len(moreSamples)

        # starting point
        x = 0
        left_y1 = 405
        right_y1  = 135

        
        for left, right in moreSamples:
            left_y2 = left * 250 + 405
            right_y2 = right * 250 + 135
            self.lines.append(Line(x, left_y1, x + sample_width, left_y2, color=(255, 192, 105), batch=self.waveformBatch))
            self.lines.append(Line(x, right_y1, x + sample_width, right_y2, color=(0,192,255), batch=self.waveformBatch))
            x += sample_width
            left_y1 = left_y2
            right_y1 = right_y2
        
    def browseFiles(self):
        global audio
        filename = filedialog.askopenfilename(initialdir = "/home/lafalasidosi/Fauxdacity", title = "Select a File", filetypes = (("Text files","*.txt*"),("all files", "*.*")))
        print(filename)
        self.loaded_audio = wave.open(filename, 'rb')
        self.process_audio()
        self.draw(0.1)

    def playSound(self): 
        global audio
        audio.play() 

    def on_draw(self):
        self.clear()
        self.buttonsBatch.draw()
        self.waveformBatch.draw()
        

if __name__ == '__main__':
    window = AppWindow(1000, 1000)
    window.set_visible(True)
    
    pyglet.app.run()

    