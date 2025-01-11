# Author: reDragonCoder

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Sampling frequency
freq=44100

# Recording duration
duration=3

# Start recorder with the given values of
# duration and sample frequency
recording=sd.rec(int(duration*freq), samplerate=freq, channels=2)
print("Recording...")

# Record audio for the given number of seconds
sd.wait()
print("Audio saved")

# Convert the NumPy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)

