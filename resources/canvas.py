from pyglet.window import Window
from pyglet.gl import glClearColor
from pyglet.graphics import Batch
from pyglet.shapes import Line

class Canvas(Window):
    def __init__(self, batched_samples):
        super().__init__()
        glClearColor(75/255, 68/255, 83/255, 1)
        self.width = 896
        self.height = 540
        self.batch = Batch()
        samples = batched_samples[0::40]
        sample_width = self.width / len(samples)

        # starting point
        x = 0
        left_y1 = 405
        right_y1  = 135

        self.lines = []
        for left, right in samples:
            left_y2 = left * 250 + 405
            right_y2 = right * 250 + 135
            self.lines.append(Line(x, left_y1, x + sample_width, left_y2, color=(255, 192, 105), batch=self.batch))
            self.lines.append(Line(x, right_y1, x + sample_width, right_y2, color=(0,192,255), batch=self.batch))
            x += sample_width
            left_y1 = left_y2
            right_y1 = right_y2

    def on_draw(self):
        self.clear()
        self.batch.draw()