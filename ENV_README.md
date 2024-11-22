# Microsoft Python

Microsoft Dev Container 公式の Python イメージにパッケージ追加のオプションを加えた環境

~~Ruff で Format と Lint を行う~~　このプロジェクトでは無効にしてます

> [!重要]
>
> dockerでは仮想環境のため基本的に音を取得することができないため実行しても下記のエラーが表示されます。
>
>        Cannot connect to server socket err = No such file or directory
>        Cannot connect to server request channel
>        jack server is not running or cannot be started
>        JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
>        JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
>        Segmentation fault

## Environment

2024/04/11 現在

| OS | Version |
|----|---------|
| Debian | LTS | 

| Language / runtime | Version | 
|--------------------|---------|
| Python | 3.12.2 | 

| Docker | SIZE |
|--------|------|
| Image Size | 1.49GB | 

## Extensions

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent)
- [autoDocstring - Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
- [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
- [IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)
