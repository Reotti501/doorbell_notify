import wave
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
file_name = "src/sounds/doorbelldefault.wav" # 録音ファイル
RATE = 44100 # 録音時に設定したRATE
CHUNK = 1024 * 4 # 録音時に設定したCHUNK
RECORD_SECONDS = 1 # 検出に使いたい秒数
pnts = int(RATE / CHUNK * RECORD_SECONDS) * CHUNK # dataが何点になるかを計算

start = 3# ここをいろいろ変えてみる

wf = wave.open(file_name, "rb")
data = np.frombuffer(wf.readframes(wf.getnframes()), dtype='int16')
wf.close()

data = data[start:start+pnts]
fft_data = np.abs(np.fft.fft(data))
freqList = np.fft.fftfreq(data.shape[0], d=1.0/RATE)

df = pd.DataFrame(dict(freq = freqList, amp = fft_data))
df = df[df['freq']>500] # 500 Hz以下は無視する。
df = df[df['amp']>0.5e7] # 0.5e7以上の強度を持つ点を覚える。
print(list(df.index))
# [797, 798, 799, 800, 801]
print(list(df['freq']))
# [858.09814453125, 859.1748046875, 860.25146484375, 861.328125, 862.40478515625]
print(len(df))
# 5
