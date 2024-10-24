import pyglet

# To create an event dispatcher, 
# 1. Subclass EventDispatcher
# 2. Call register_event_type() on subclass for each event subclass will recognize
# 3. Call dispatch_event() to create and dispatch an event as needed.


class ClockTimer(pyglet.event.EventDispatcher):
    def tick(self):
        self.dispatch_event('on_update')

ClockTimer.register_event_type('on_update')

class Observer:
    def __init__(self, subject):
        subject.push_handlers(self)

class DigitalClock(Observer):
    def on_update(self):
        print('I, a digital clock, was notified of a tick.')
        pass

class AnalogClock(Observer):
    def on_update(self):
        print('I, an analog clock, was notified of a tick.')
        pass

timer = ClockTimer()
digital_clock = DigitalClock(timer)
analog_clock = AnalogClock(timer)


while True:
    text = input('awaiting input...')
    if text == 't':
        timer.tick()
    elif text == 'q':
        break
    else: continue
