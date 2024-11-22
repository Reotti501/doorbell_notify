# https://forums.raspberrypi.com/viewtopic.php?t=71062

import pyaudio

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    print((i, dev['name'], dev['maxInputChannels']))

"""
result
(0, 'bcm2835 Headphones: - (hw:0,0)', 0)
(1, 'USB 2.0 Camera: Audio (hw:3,0)', 1)
(2, 'sysdefault', 0)
(3, 'lavrate', 0)
(4, 'samplerate', 0)
(5, 'speexrate', 0)
(6, 'pulse', 32)
(7, 'upmix', 0)
(8, 'vdownmix', 0)
(9, 'dmix', 0)
(10, 'default', 32)
"""
