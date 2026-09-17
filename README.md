# CDS_WatchTrial

スマートフォン、Smart Band、Raspberry Pi間の連携を確認するためのサンプルプログラムおよび手順書です。

## 利用について

本リポジトリは、講義受講生および講義関係者向けに公開しています。

受講生および講義関係者以外による、本リポジトリの内容の利用・転載・再配布等は認めていません。

## システム構成

本リポジトリでは、以下の構成で、Raspberry PiからSmart Bandへの通知等を送信します。

Raspberry Pi<br>
↓ HTTP通信<br>
Andriodスマートフォン<br>
↓ Gadgetbridge<br>
Smart Band

## 使用する機器・ソフトウェア
本リポジトリでは、主に以下を使用します。
- Raspberry Pi
- Androidスマートフォン
- Xiaomi Smart Band 10
- Gadgetbridge
- Python 3

※ Androidのバージョンやスマートフォンの機種によって、画面表示や設定項目が異なる場合があります。

## はじめに

はじめて利用する場合は、以下の順番で確認してください。

1. GadgetbridgeとSmart Bandの接続

   [GadgetbridgeとSmart Bandデバイスの連携](./docs/GadgetbridgeとSmartBandデバイスの連携/GadgetbridgeとSmartBandデバイスの連携.md)

   SmartBandをAndroidスマートフォンへ接続し、Gadgetbridgeから利用できる状態にします。

2. Raspberry PiからSmart Bandへ通知を送る

   [遠隔バイブレーション手順書](./docs/遠隔バイブレーション手順書/遠隔バイブレーション手順書.md)

   Androidスマートフォン上でサーバを起動し、Raspberry PiからHTTPリクエストを送信します。

## サンプルプログラム

サンプルプログラムは[`samples/vibration/`](./samples/vibration/)にあります。

### [`server_for_smartphone_sample_code.py`](./samples/vibration/server_for_smartphone_sample_code.py)
Androidスマートフォン上で実行するHTTPサーバの例です。

Raspberry Piから受信したリクエストに応じて、Gadgetbridgeを介してSmart Bandへ通知・振動等を送信します。

セキュリティを考えながら、工夫して活用してください。

### [`samplecode_for_raspberrypi.py`](./samples/vibration/samplecode_for_raspberrypi.py)
Raspberry Pi上で実行するプログラムの例です。

本プログラムではPythonの`requests`パッケージを使用します。

## ディレクトリ構成
CDS_WatchTrial<br>
├─ README.md<br>
├─ docs/<br>
│  ├─ GadgetbridgeとSmartBandデバイスの連携/<br>
│  └─ 遠隔バイブレーション手順書/<br>
└─ samples/<br>
   └─ vibration/<br>
      ├─ samplecode_for_raspberrypi.py<br>
      └─ server_for_smartphone_sample_code.py

## 注意事項
- 学生が利用する場合は、原則として`main`branchの内容を参照してください。
- Androidのバージョンや端末によって、手順書と画面表示が異なる場合があります。
- サンプルプログラム中のIPアドレス等は、使用する環境に合わせて変更してください。
- 正常に動作しない場合は、接続状態、IPアドレス、スマートフォンとRaspberry Piのネットワーク接続を確認してください。

## 不具合・不明点について
手順書の誤りやサンプルプログラムの不具合を発見した場合は、TAへ連絡してください。

---
**Author: [Chi-robot](https://github.com/G-uruCPQ/)** | Date: 2026-09-18
