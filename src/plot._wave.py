import wave
import numpy as np
import matplotlib.pyplot as plt
 
file_name = "src/output.wav" # 録音ファイル
RATE = 44100 # 録音時に設定したRATE
CHUNK = 1024 * 4 # 録音時に設定したCHUNK
RECORD_SECONDS = 1 # 検出に使いたい秒数
pnts = int(RATE / CHUNK * RECORD_SECONDS) * CHUNK # dataが何点になるかを計算

start = 0 # ここをいろいろ変えてみる

wf = wave.open(file_name, "rb")
data = np.frombuffer(wf.readframes(wf.getnframes()), dtype='int16')
wf.close()

data = data[start:start+pnts]
fft_data = np.abs(np.fft.fft(data))    #FFTした信号の強度
freqList = np.fft.fftfreq(data.shape[0], d=1.0/RATE)    #周波数（グラフの横軸）の取得
plt.plot(freqList, fft_data)
plt.xlim(0, 5000)    #0～5000Hzまでとりあえず表示する
plt.show()
