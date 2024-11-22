import matplotlib.pyplot as plt
import numpy as np
import os
import pyaudio
import requests
import time
from dotenv import load_dotenv
from error_hider import noalsaerr  # 第2回参照。ALSA Errorが出ない場合は不要。

load_dotenv(verbose=True)

Check_every_time = False  # 検知したときにFFTプロット。実際に運用するときはFalse。
LINE_token = os.getenv('Notify_API_TOKEN')
RECORD_SECONDS = 1  # 第3回で使用した値に合わせる
threshold = 1.5e7  # 要調整
threshold2 = 5
freq_indices = [797, 798, 799, 800, 801]  # 第3回で決めた値を入れる
freq_indices2 = [f * 2 for f in freq_indices]
input_device_index = 1  # 第1回で調べた値
CHUNK = 1024 * 4  # 第1~3回で使用した値に合わせる
FORMAT = pyaudio.paInt16
CHANNELS = 1  # モノラル入力
RATE = 44100  # 第1~3回で使用した値に合わせる
rng = int(RATE / CHUNK * RECORD_SECONDS)

def setup():
    with noalsaerr():  # 第2回参照。ALSA Errorが出ない場合はwith文は不要。
        p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        input_device_index=input_device_index,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
    )
    return p, stream

def collect_data(stream, rng, CHUNK):
    frames = []
    for i in range(rng):
        data = stream.read(CHUNK, exception_on_overflow=False)  # 第2回参照
        frames.append(data)
    d = np.frombuffer(b"".join(frames), dtype="int16")
    return d

def calc_FFTamp(frames, freq_indices, freq_indices2):
    fft_data = np.abs(np.fft.fft(frames))
    amp, amp2 = 0, 0
    for i in freq_indices:
        amp += fft_data[i]
    for i in freq_indices2:
        amp2 += fft_data[i]
    return amp, amp2

def check_plot(d):
    fft_data = np.abs(np.fft.fft(d))  # FFTした信号の強度
    freqList = np.fft.fftfreq(d.shape[0], d=1.0 / RATE)  # 周波数（グラフの横軸）の取得
    plt.plot(freqList, fft_data)
    plt.xlim(0, 5000)  # 0～5000Hzまでとりあえず表示する
    plt.show()

def send(token, amp, amp2, threshold, threshold2):
    url = "https://notify-api.line.me/api/notify"
    token = token
    headers = {"Authorization": "Bearer " + token}
    message = (
        "が鳴ってるよ\n強度 {:.2e} --- 基準 {:.1e}\n比率 {:.2e} --- 基準 {:.1e}".format(
            amp, threshold, amp / amp2, threshold2
        )
    )
    payload = {"message": message}
    r = requests.post(url, headers=headers, params=payload)

# Send LINE message
def line_message():
    url = "https://api.line.me/v2/bot/message/push"
    access_token = os.getenv('Messaging_API_TOKEN')
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json",
    }
    # Loop through user_ids
    user_ids = os.getenv('USER_IDS').split(',')
    for user_id in user_ids:
        payload = {
            "to": user_id,
            "messages": [
                {
                    "type": "text",
                    "text": os.getenv('MESSAGE'),
                }
            ]
        }

if __name__ == "__main__":
    p, stream = setup()
    print("Watching...")
    try:
        while True:
            d = collect_data(stream, rng, CHUNK)
            amp, amp2 = calc_FFTamp(d, freq_indices, freq_indices2)
            if (amp > threshold) & (amp / amp2 > threshold2):
                print("Someone is at the door.")
                send(LINE_token, amp, amp2, threshold, threshold2)
                if Check_every_time:
                    check_plot(d)
                time.sleep(5)
                print("Keep watching...")
    except KeyboardInterrupt:
        print("You terminated the program.\nThe program ends.")
        stream.stop_stream()
        stream.close()
        p.terminate()
