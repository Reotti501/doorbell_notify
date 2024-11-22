import pyaudio
import wave

input_device_index = 1 # 前回確認したデバイス番号
CHUNK = 1024*4
FORMAT = pyaudio.paInt16
CHANNELS = 1 # モノラル入力 # 前回確認したmaxInputChannelsが上限
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                input_device_index = input_device_index,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
print("Recording...")
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    # ↓↓↓ここを変更
    data = stream.read(CHUNK, exception_on_overflow=False)
    # ↑↑↑
    frames.append(data)
print("Done!")
stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()