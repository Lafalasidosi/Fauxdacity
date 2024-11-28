import pyglet
import pyglet.gui
from pyglet.gl import *
from tkinter import *
from tkinter import filedialog
import array, itertools, wave
from pyglet.shapes import Line
import sys
from pyglet.media import Player
import os

class AppWindow(pyglet.window.Window):
    def __init__(self, width, height, *args, **kwargs):
        super().__init__(width, height, *args, **kwargs)
        self.width = width
        self.height = height
        self.resizable = True
        self.lines = []
        self.loaded_audio = None
        self.audio_file_name = ''
        self.source = None
        self.buttons_batch = pyglet.graphics.Batch()
        self.waveform_batch = pyglet.graphics.Batch()
        self.progress_batch = pyglet.graphics.Batch()
        self.set_up_buttons()
        self.player = Player() # Player can queue() a Source
        self.progress_bar_pos = (0,0)
        self.progress_bar = Line(0, 0, 0, 430, color=(255, 255, 255), batch=self.progress_batch)

    def set_up_buttons(self):
        # button images
        # depressed versions ought to be changed at some point
        load_pressed = pyglet.image.load('resources/folder_small.png')  # attr. to Freepik      
        load_depressed = pyglet.image.load('resources/folder_small.png')
        play_pressed = pyglet.image.load('resources/play_button_small.png')
        play_depressed = pyglet.image.load('resources/play_button_small.png')
        pause_pressed = pyglet.image.load('resources/pause_button.png')
        pause_depressed = pause_pressed
        boost_pressed = pyglet.image.load('resources/buck_icon_small.png')
        boost_depressed = boost_pressed
        
        # button constructors
        self.load_button = pyglet.gui.PushButton(x=0, y=self.height-32, pressed=load_pressed, depressed=load_depressed, batch=self.buttons_batch)
        self.play_button = pyglet.gui.PushButton(x=33, y=self.height-32, pressed=play_pressed, depressed=play_depressed, batch=self.buttons_batch)
        self.pause_button = pyglet.gui.PushButton(x=65, y=self.height-32, pressed=pause_pressed, depressed=pause_depressed, batch=self.buttons_batch) 
        self.boost_button = pyglet.gui.PushButton(x=97, y=self.height-32, pressed=boost_pressed, depressed=boost_depressed, batch=self.buttons_batch) 

        # set button event handlers
        self.load_button.on_press = self.browse_files
        self.play_button.on_press = self.play_sound
        self.pause_button.on_press = self.pause_sound
        self.boost_button.on_press = self.boost_sound

        # push handlers to... wherever pyglet does it idk
        self.push_handlers(self.load_button)
        self.push_handlers(self.play_button) 
        self.push_handlers(self.pause_button)
        self.push_handlers(self.boost_button)

    def process_audio(self):
        # for producing waveform 
        samples = self.loaded_audio.readframes(self.loaded_audio.getnframes())
        array_of_ints = array.array("h", samples)
        normalized = [x / 65536 for x in array_of_ints]
        batched_samples = list(itertools.batched(normalized, 2))
        more_samples = batched_samples[0::40]
        sample_width = self.width / len(more_samples)

        return more_samples, sample_width

    def draw_waveform(self, samples, sample_width):
        # starting point
        x = 0
        left_y1 = 405
        right_y1  = 135

        del self.lines[:]
        for left, right in samples:
            left_y2 = left * 250 + 405
            right_y2 = right * 250 + 135
            self.lines.append(Line(x, left_y1, x + sample_width, left_y2, color=(255, 192, 105), batch=self.waveform_batch))
            self.lines.append(Line(x, right_y1, x + sample_width, right_y2, color=(0,192,255), batch=self.waveform_batch))
            x += sample_width
            left_y1 = left_y2
            right_y1 = right_y2
        self.draw(0.1)
        
    def browse_files(self):
        self.player.next_source()
        self.audio_file_name = filedialog.askopenfilename(filetypes=[("WAV files","*.wav*")],initialdir=os.getcwd(),title="Select a File")
        self.load_audio(self.audio_file_name)
        samples, width = self.process_audio()
        self.draw_waveform(samples, width)
        

    def load_audio(self, filename):
        # changed from assiging self.player to Source returned by pyglet.media.load()
        # since Source objects have no pause() function
        self.source = pyglet.media.load(filename, streaming=False)
        self.player.queue(self.source)
        self.loaded_audio = wave.open(filename, 'rb')

    def play_sound(self): 
        print("Play button pressed.")
        self.player.play()

    def pause_sound(self):
        print("Pause button pressed.")
        self.player.pause()

    def boost_sound(self):
        print('Boost button pressed.')
        BOOST_CONSTANT = 1.05
        for line in self.lines:
            distance = abs(line.y - line.y2)
            shift = 0.5*distance*(BOOST_CONSTANT - 1)
            line.y -= shift
            line.y2 += shift
        self.waveform_batch.draw()
        self.player.volume *= 1.25

    def on_draw(self):
        self.clear()
        self.buttons_batch.draw()
        self.waveform_batch.draw()
        if self.player.playing:
            pos = self.progress_bar.position
            x = pos[0]
            y = pos[1]
            self.progress_bar.position = (x+0.017*self.width/self.source.duration,y)
            self.progress_batch.draw()

    def on_resize(self, width, height):
        super().on_resize(width, height)

        # reposition buttons vertically
        # updating the x-coordinates seems unnecessary? The buttons stick to the left edge
        self.load_button.y = height - 32
        self.play_button.y = height - 32
        self.pause_button.y = height - 32
        self.boost_button.y = height - 32

        # if audio is loaded, resize waveform
        if self.lines:
            sample_width = width / (len(self.lines))
            x = 0
            for i in range(0, len(self.lines)):
                line = self.lines[i]
                line.x = x
                line.x2 = x + sample_width
                x += sample_width

def main():
    
    window = AppWindow(1000, 1000, resizable=True)
    window.set_visible(True)

    pyglet.app.run()
    

if __name__ == '__main__':
    main()

    