# Raspberry Piでインターホンの音を検知してLINEに通知する

## はじめに
[このページ](https://qiita.com/nkgwwwww/items/cd0e7433cfc4b2ea0a59)をベースに（ほとんどそのまま）しました  
とても分かりやすかったです　先人に最大限の敬意を(｀･ω･´)ゞ

## 開発/実行環境
### 開発環境
* windows 11
* Docker Desktop
* Python 3.12.7

### 実行環境
* Raspberry Pi 4B 8GB   (Raspberry Pi OS 64bit)
* Python 3.11.2

> [!IMPORTANT]  
>ENV_README.mdにもあるようにdockerでは仮想環境のため基本的に音を取得することができないため、実行しても下記のエラーが表示されます。
>
>        Cannot connect to server socket err = No such file or directory
>        Cannot connect to server request channel
>        jack server is not running or cannot be started
>        JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
>        JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
>        Segmentation fault

## ファイル説明
|ファイル名                          |ファイル内容  |
|---                                |---    |
|CheckDevID.py                      |PyAudioで使用するデバイス番号を確認するために使用します    |
|error_hider.py                     |<b> !! 削除するとDoorbell_notifier_20220310.pyが動かなくなります!! </b><br> ALSAエラーを非表示にするのに使用しています |
|wo_ALSAerror.py                    |インターホンの音を録音するのに使用します   |
|print_indices.py                   |検出に使うデータ点を決めるために使用します <br> 出力される値を使います	詳しいことはURLへ   |
|print_amp.py                       |print_indices.pyの結果からピーク位置で強度が足し合わせた値が出力されます <br> 出力される値を使います   詳しいことはURLへ   |
|send_notify.py                     |LINE Notifyの送信テスト用です|
|send_messagingAPI.py               |LINE Messaging APIの送信テスト用です|
|Doorbell_notifier_20220310.py      |これを常駐化(デーモン化)すればLINEに通知が来ます <br> LINE Notifyの発行を忘れずに  |
