import itertools
import wave
import array
from canvas import Canvas
from pyglet.app import run

audio = wave.open("start.wav", "rb")
print("Channels:", audio.getnchannels())
print("Sample width:", audio.getsampwidth(), "Bytes")
print("Frequency:", audio.getframerate(), "kHz")

print("Number of frames:", audio.getnframes())
print("Audio length:", audio.getnframes() / audio.getframerate(), "seconds")


# readframes() needs number of samples as input
# sample made of 16 bits, 2 bytes, two channels -> 4 bytes per sample
samples = audio.readframes(audio.getnframes()) # 161280 frames * 4 bytes/frame = 645120 bytes
print("Number of bytes:", len(samples))

# sample first 4 bytes = first frame
# \x45\xa3\xd1\x00
# first two are for the first sample of left channel etc.
# look at first two bytes:
# range -32768, 32768
# one byte multiplied by 256
# one byte also stores sign
# arrays help

array_of_ints = array.array("h", samples)
print(len(array_of_ints))
print(type(array_of_ints[0])) # in large range

normalized = [x / 65536 for x in array_of_ints]

batched_samples = list(itertools.batched(normalized, 2))
#for s in batched_samples:
#    print(s)

# visualization
renderer = Canvas(batched_samples)
run()








