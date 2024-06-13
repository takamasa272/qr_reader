# qr_reader
クリップボードにある画像内のQRコードを読み取るpythonコード

生粋のPCユーザにとって，QRコードのみでURL等を案内されてしまったとき，非常にふしあわせです．

そんなときに一助になるかもしれません．

## USAGE
画面上のQRコードを読む場合は，さきに`printscreen`キーや，`Win`+`Shift`+`S`等を使用し，クリップボードにQRコードを収めておく．

そして，ターミナルで
```
qread
```
と打つだけ．

### example
例として，以下の画像がクリップボードにあるとする．

![example image](img/example.png)

このとき，`qread`を叩くと，
```
$ qread
1: https://www.example.co.jp
2: https://maps.google.com/local?q=35.68518697509635,139.75261688232422
3: https://www.example.com
4: mailto:takamasa272@example.com?subject=Hello!&body=World!
```
のように，QRコードをデコードするので，よしなにコピペする．

## installation
### requirements
以下のパッケージを要します
- `python`
    - `opencv-python`
    - `pillow`
    - `numpy`

また，Linuxでは`wl-paste`コマンドが必要かもしれません．

### install
`pip`を使うことで，以下のコマンドで導入できます．(要`git`のインストール)

```
pip install git+https://github.com/takamasa272/qr_reader
```

## おことわり
QRコードは株式会社デンソーウェーブの登録商標です．

例示用QRコードは，[qrcodemonkey](https://www.qrcode-monkey.com/) なるサイトで作成しました．