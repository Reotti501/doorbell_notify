import wave
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
file_name = "src/output.wav" # 録音ファイル
RATE = 44100 # 録音時に設定したRATE
CHUNK = 1024 * 4 # 録音時に設定したCHUNK
RECORD_SECONDS = 1 # 検出に使いたい秒数
pnts = int(RATE / CHUNK * RECORD_SECONDS) * CHUNK # dataが何点になるかを計算

# ここに先ほどの結果を入れる
freq_indices = [797, 798, 799, 800, 801]

start = 0 # ここをいろいろ変えてみる

wf = wave.open(file_name, "rb")
data = np.frombuffer(wf.readframes(wf.getnframes()), dtype='int16')
wf.close()

data = data[start:start+pnts]
fft_data = np.abs(np.fft.fft(data))    #FFTした信号の強度

amp = 0
for i in freq_indices:
    amp += fft_data[i]

print('{:.2e}'.format(amp))
# 3.20e+07
