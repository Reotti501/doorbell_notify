# Raspberry Piでインターホンの音を検知してLINEに通知する

## はじめに
[このページ](https://qiita.com/nkgwwwww/items/cd0e7433cfc4b2ea0a59)を参考に一部改変しました。 とても分かりやすかったです　先人に最大限の敬意を(｀･ω･´)ゞ

## 開発/実行環境
### 開発環境
* windows 11
* Docker Desktop
* Python 3.12.7

### 実行環境
* Raspberry Pi 4B 8GB   (Raspberry Pi OS 64bit)
* Python 3.11.2

## 必要なもの
* LINE Messaging API Key
* LinuxOSコンピュータ

> [!IMPORTANT]  
>[ENV_README.md](./ENV_README.md)にもあるようにdockerでは仮想環境のため基本的に音を取得することができないため、実行しても下記のエラーが表示されます。
>
>        Cannot connect to server socket err = No such file or directory
>        Cannot connect to server request channel
>        jack server is not running or cannot be started
>        JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
>        JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
>        Segmentation fault

## ファイル説明
|ファイル名                                          |ファイル内容  |
|---                                                |---    |
|[.env](./src/.env)                                 |各種APIキーやユーザーIDなどをここを参照しています |
|[CheckID.py](./src/CheckID.py)                     |PyAudioで使用するデバイス番号を確認するために使用します    |
|[Doorbell_notify.py](./src/Doorbell_notify.py)     |メインプログラムです    |
|[error_hider.py](./src/error_hider.py)             |ALSAエラーを非表示にするのに使用しています    |
|[print_amp.py](./src/print_amp.py)                 |[print_indices.py](./src/print_indices.py)の結果からピーク位置で強度が足し合わせた値が出力されます <br> 出力される値を使います   詳しいことはURLへ    |
|[print_indices.py](./src/print_indices.py)         |検出に使うデータ点を決めるために使用します <br> 出力される値を使います	詳しいことは[URL](https://qiita.com/nkgwwwww/items/cd0e7433cfc4b2ea0a59)へ    |
|[record.py](./src/record.py)                       |インターホンの音を録音するために使用します    |
|[send_messagingAPI.py](./src/send_messagingAPI.py) |LINE Messaging API の送信テスト用です |
|[send_notify.py](./src/send_notify.py)             |LINE Notify の送信用テストです 2025/3/31にサービス終了するためもう使用しないと思いますが念のため    |
