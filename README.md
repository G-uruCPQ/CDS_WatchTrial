# CDS_WatchTrial

スマートフォン、Smart Band、Raspberry Pi間の連携を確認するためのサンプルプログラムおよび手順書です。

## 利用について

本リポジトリは、講義受講生および講義関係者向けに公開しています。

受講生および講義関係者以外による、本リポジトリの内容の利用・転載・再配布等は認めていません。

## システム構成

本リポジトリでは、以下の構成で、Raspberry PiからSmart Bandへの通知等を送信します。

Raspberry Pi<br>
↓ HTTP通信<br>
Androidスマートフォン<br>
↓ Gadgetbridge<br>
Smart Band

## 使用する機器・ソフトウェア
本リポジトリでは、主に以下を使用します。
- Raspberry Pi
- Androidスマートフォン
- Xiaomi Smart Band 10
- Gadgetbridge
- Python 3

セットアップやサンプルプログラムの実行時には、
Mi Fitness、Xiaomi Cloud Tokens Extractor、Termux等も使用します。
詳細は各手順書を参照してください。

※ Androidのバージョンやスマートフォンの機種によって、画面表示や設定項目が異なる場合があります。

## はじめに

はじめて利用する場合は、以下の順番で確認してください。

1. GadgetbridgeとSmart Bandの接続

   [GadgetbridgeとSmart Bandデバイスの連携](./docs/GadgetbridgeとSmartBandデバイスの連携/GadgetbridgeとSmartBandデバイスの連携.md)

   SmartBandをAndroidスマートフォンへ接続し、Gadgetbridgeから利用できる状態にします。

2. Raspberry PiからSmart Bandへ通知を送る

   [遠隔バイブレーション手順書](./docs/遠隔バイブレーション手順書/遠隔バイブレーション手順書.md)

   Androidスマートフォン上でサーバを起動し、Raspberry PiからHTTPリクエストを送信します。

3. SmartBandの測定データをRaspberry Piから取得する

   [スマートバンド測定データ取得手順書](./docs/スマートバンド測定データ取得手順書/スマートバンド測定データ取得手順書.md)

   Gadgetbridgeに保存された測定データをSQLiteデータベースとしてエクスポートし、Raspberry PiからHTTP通信を介して取得します。

2、3については、各自の開発内容に応じて必要な機能を利用してください。

## サンプルプログラム

サンプルプログラムは[`samples/`](./samples/)にあります。

### [`vibration/`](./samples/vibration/)

Raspberry PiからSmart Bandへ通知・振動等を送信するためのサンプルプログラムです。

#### [`server_for_smartphone_sample_code.py`](./samples/vibration/server_for_smartphone_sample_code.py)
Androidスマートフォン上で実行するHTTPサーバの例です。

Raspberry Piから受信したリクエストに応じて、Gadgetbridgeを介してSmart Bandへ通知・振動等を送信します。

セキュリティを考えながら、工夫して活用してください。

#### [`samplecode_for_raspberrypi.py`](./samples/vibration/samplecode_for_raspberrypi.py)
Raspberry Pi上で実行するプログラムの例です。

本プログラムではPythonの`requests`パッケージを使用します。

### [`get_data/`](./samples/get_data/)

Smart Bandで取得した測定データをRaspberry Piから利用するためのサンプルプログラムです。

#### [`database_reader.py`](./samples/get_data/database_reader.py)

GadgetbridgeからエクスポートされたSQLiteデータベースを読み出すためのPythonライブラリです。

歩数、心拍数、ストレス、SpO₂、バッテリー残量等の最新値や、睡眠情報を含む日次集計データを取得できます。

#### [`smartphone_server.py`](./samples/get_data/smartphone_server.py)

Androidスマートフォン上で実行するHTTPサーバーの例です。

Raspberry Piから受信したリクエストに応じて、database_reader.pyを用いて取得した測定データをJSON形式で返します。

また、Gadgetbridgeのデータベースの定期エクスポート機能およびHTTPリクエストによるエクスポート要求機能を実装しています。

#### [`samplecode4raspberrypi.py`](./samples/get_data/samplecode4raspberrypi.py)

Raspberry Pi上で実行するプログラムの例です。

HTTP通信を介した測定データの取得、日付を指定した日次集計データの取得、データベースの更新要求等を行います。

本プログラムではPythonの`requests`パッケージを使用します。

## ディレクトリ構成
```
CDS_WatchTrial
├─ README.md
├─ docs/
│   ├─ GadgetbridgeとSmartBandデバイスの連携/
│   ├─ 遠隔バイブレーション手順書/
|   └─ スマートバンド測定データ取得手順書/
└─ samples/
    ├─ vibration/
    |   ├─ samplecode_for_raspberrypi.py
    |   └─ server_for_smartphone_sample_code.py
    └─ get_data/
        ├─ database_reader.py
        ├─ smartphone_server.py
        └─ samplecode4raspberrypi.py
```

## 注意事項
- 学生が利用する場合は、原則として`main`branchの内容を参照してください。
- Androidのバージョンや端末によって、手順書と画面表示が異なる場合があります。
- サンプルプログラム中のIPアドレス等は、使用する環境に合わせて変更してください。
- 正常に動作しない場合は、接続状態、IPアドレス、スマートフォンとRaspberry Piのネットワーク接続を確認してください。
- 測定データの取得には、Smart BandとGadgetbridge間の同期周期やデータベースのエクスポート周期による遅延が生じます。リアルタイム性が要求される用途では注意してください。
- 測定データには個人の生体情報が含まれます。ネットワークのアクセス制限や通信の保護等、セキュリティを考慮した上で利用してください。
- 実際の測定データを含むデータベースファイルをGitHub等へアップロードしないでください。

サンプルプログラムは基本的な機能を実装したものです。各自の開発内容に応じて、工夫して活用してください。

## 不具合・不明点について
手順書の誤りやサンプルプログラムの不具合を発見した場合は、TAへ連絡してください。

---
**Author: [Chi-robot](https://github.com/G-uruCPQ/), [sugiura](https://github.com/iruru0422)** | Date: 2026-11-27
