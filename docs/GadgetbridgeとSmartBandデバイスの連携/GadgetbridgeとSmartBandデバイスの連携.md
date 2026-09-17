# GadgetbridgeとSmart Bandデバイスの連携

Xiaomi Smart Band 10をAndroidスマートフォンに接続し、同デバイスをGadgetbridgeアプリで利用できるようにするまでの一連の流れを示す。<br>
本手順では、スマートフォンとしてXiaomi Redmi 15を使用する。その他のAndroidスマートフォン（Google Pixelなど）でも、おおむね同様の手順で設定できる。<br>
ただし、Androidのバージョンや端末によって、画面表示や設定項目が異なる場合がある

## 1. Mi Fitnessのインストール・初期設定
### 1.1 Mi Fitnessアプリのインストール
Google Play ストアからMi Fitnessアプリをインストールする。

<img src=".\img\Screenshot_2026-08-06-15-41-29-491_com.android.vending.jpg" alt="MiFitnessインストール" height="500">

### 1.2 Mi Fitness初期設定
Mi Fitnessアプリを開き、`開始`を押す。

<img src=".\img\Screenshot_2026-08-06-15-44-17-324_com.xiaomi.wearable.jpg" alt="MiFitness開始" height="500">

<br>使用条件に同意し、地域を日本に設定する。

<img src=".\img\Screenshot_2026-08-06-15-44-30-820_com.xiaomi.wearable.jpg" alt="使用条件同意" height="500"> <img src=".\img\Screenshot_2026-08-06-15-44-45-608_com.xiaomi.wearable.jpg" alt="地域設定" height="500">

<br>身体活動データへのアクセスを許可する。

<img src=".\img\Screenshot_2026-08-06-15-44-51-982_com.xiaomi.wearable.jpg" alt="アクセス許可" height="500"> <img src=".\img\Screenshot_2026-08-06-15-44-58-497_com.google.android.permissioncontroller.jpg" alt="身体活動データアクセス" height="500">

### 1.3 Xiaomiアカウントの作成
Mi Fitnessアプリ下の`プロフィール`タブを選択し、`サインイン`をお明日。

<img src=".\img\Screenshot_2026-08-06-15-45-33-128_com.xiaomi.wearable.jpg" alt="初期設定完了" height="500"> <img src=".\img\Screenshot_2026-08-06-15-45-41-232_com.xiaomi.wearable.jpg" alt="プロフィール画面" height="500">

<br>サインイン画面下部の`アカウントを作成`を押し、画面の指示に従ってXiaomiアカウントを作成する。

<img src=".\img\PXL_20260806_064617421.jpg" alt="Xiaomiアカウントにサインイン" height="500"> <img src=".\img\PXL_20260806_064644318.jpg" alt="Xiaomiアカウントを作成" height="500">

## 2. Smart Bandのスマートフォンへの接続
### 2.1 Smart Bandの起動
充電ケーブルでSmart Bandを電源に接続し、起動する。

<img src=".\img\PXL_20260826_012811254.jpg" alt="MiBand電源接続" height="500">

<br>言語選択で`日本語`を選択する。

<img src=".\img\PXL_20260806_065428113.jpg" alt="MiBand言語選択" height="500">

### 2.2 Smart Bandの接続
スマートフォンの画面右上から下方向にスワイプしてクイック設定を開き、BluetoothをONにする。

<img src=".\img\Screenshot_2026-08-06-15-45-17-474_com.xiaomi.wearable.jpg" alt="BluetoothOn" height="500">

<br>Mi Fitnessアプリ下の`デバイス`タブを選択し、`デバイスを追加`を押す。

<img src=".\img\Screenshot_2026-08-06-15-45-33-128_com.xiaomi.wearable.jpg" alt="初期設定完了" height="500"> <img src=".\img\Screenshot_2026-08-06-15-51-30-404_com.xiaomi.wearable.jpg" alt="デバイス画面" height="500">

<br>Bluetoothによるデータ転送を許可する。

<img src=".\img\Screenshot_2026-08-06-15-51-54-060_com.xiaomi.wearable.jpg" alt="Bluetoothアクセス許可" height="500">

<br>付近のBluetoothデバイスの検出を許可する。

<img src=".\img\Screenshot_2026-08-06-15-51-59-850_com.xiaomi.wearable.jpg" alt="Bluetoothデバイス検出許可" height="500"> <img src=".\img\Screenshot_2026-08-06-15-52-05-413_com.google.android.permissioncontroller.jpg" alt="付近のデバイス検出許可" height="500">

<br>Smart Bandが検出されたら、スマートフォン側で`ペア設定をする`を押す。続いて、Smart Band側に表示されるチェックマークを押し、ペア設定を承認する。

<img src=".\img\Screenshot_2026-08-06-15-53-24-329_com.android.settings.jpg" alt="MiFitnessペア設定" height="500"> <img src=".\img\PXL_20260806_065505932.jpg" alt="MiBandペア設定" height="500">

<br>Smart Bandとスマートフォンの接続完了。次へ進む。

<img src=".\img\Screenshot_2026-08-06-15-55-29-714_com.xiaomi.wearable.jpg" alt="MiBandペア設定" height="500">

<br>以降もいくつか設定項目が表示されるが、本手順では最終的にMi Fitnessを使用しないため、任意の設定で進めてよい。

<img src=".\img\Screenshot_2026-08-06-15-55-38-270_com.xiaomi.wearable.jpg" alt="Mi Fitnessアプリ通知設定" height="500"> <img src=".\img\Screenshot_2026-08-06-15-55-46-225_com.xiaomi.wearable.jpg" alt="Mi Fitnessアプリ着信設定" height="500"> <img src=".\img\Screenshot_2026-08-06-15-55-50-918_com.xiaomi.wearable.jpg" alt="Mi Fitnessアプリシステム情報同期設定" height="500">

<br>装着ガイドを読み、次へ進む。

<img src=".\img\Screenshot_2026-08-06-15-55-55-072_com.xiaomi.wearable.jpg" alt="Mi Fitnessアプリ装着ガイド" height="500">

<br>以降Smart Bandの使い方を読みながら、`次へ`で進む。

<img src=".\img\Screenshot_2026-08-06-15-56-03-926_com.xiaomi.wearable.jpg" alt="Mi Fitnessガイド1" height="500"> <img src=".\img\Screenshot_2026-08-06-15-56-06-196_com.xiaomi.wearable.jpg" alt="Mi Fitnessガイド2" height="500"> <img src=".\img\Screenshot_2026-08-06-15-56-09-070_com.xiaomi.wearable.jpg" alt="Mi Fitnessガイド3" height="500"> <img src=".\img\Screenshot_2026-08-06-15-56-10-937_com.xiaomi.wearable.jpg" alt="Mi Fitnessガイド4" height="500">

<br>`開始`を押して次へ進む。

<img src=".\img\Screenshot_2026-08-06-15-56-14-371_com.xiaomi.wearable.jpg" alt="Mi Fitness開始" height="500">

<br>バンド接続保護に関する案内が表示されるが、本手順では設定する必要はない。メッセージボックス外をタップして閉じる。

<img src=".\img\Screenshot_2026-08-06-15-56-22-730_com.xiaomi.wearable.jpg" alt="バンド接続保護警告" height="500">

<br>以上でスマートフォンとSmart Bandの接続は完了です。

## 3. Smart BandのGadgetbridgeへの接続
Smart BandをMi FitnessではなくGadgetbridgeから利用できるようにするため、オープンソースアプリのGadgetbridgeを導入する。

### 3.1 Gadgetbridgeのインストール
本手順作成時点では、Google Play ストアで配布されているGadgetbridgeは古いバージョンで使えないので、F-Droidで配布されている最新版を使用する。

[F-Droid公式サイト](https://f-droid.org/ja/)を開き、検索バーから`gadgetbridge`で検索する。
<br>検索結果から、無印のGadgetbridgeを選択。

<img src=".\img\Screenshot_2026-08-06-16-01-19-092_com.android.chrome.jpg" alt="FDroid_gadgetbridge検索" height="500"> <img src=".\img\Screenshot_2026-08-06-16-01-31-931_com.android.chrome.jpg" alt="FDroid_gadgetbirdge選択" height="500">

<br>Gadgetbridgeのページで下にスクロールし、`提案`と表示されているバージョンを確認する（本記事製作時点ではver.0.92.2）。<br>同ブロックの最下部にある`APKをダウンロード`を押し、APKファイルをダウンロードする。

<img src=".\img\Screenshot_2026-08-06-16-01-41-882_com.android.chrome.jpg" alt="FDroid_gadgetbirdge" height="500"> <img src=".\img\Screenshot_2026-08-06-16-02-05-314_com.android.chrome.jpg" alt="FDroid_gadgetbirdge_latest_top" height="500"> <img src=".\img\Screenshot_2026-08-06-16-02-16-160_com.android.chrome.jpg" alt="FDroid_gadgetbirdge_latest_bottom" height="500">

<br>スマートフォンのエクスプローラーアプリからダウンロードしたAPKファイルを探し、実行。

<img src=".\img\Screenshot_2026-08-06-16-04-01-600_com.mi.android.globalFileexplorer.jpg" alt="エクスプローラー" height="500">

<br>Gadgetbridgeアプリがインストールされる。

<img src=".\img\Screenshot_2026-08-06-16-05-15-225_com.miui.home.jpg" alt="フォルダー" height="500">

### 3.2 Gadgetbridgeの権限設定
Gadgetbridgeアプリを開くと、アプリ権限の許可の画面が出てくる。<br>
本手順では以下の権限を許可する。
- `Background location`
- `Bluetooth connect`
- `Bluetooth scan`
- `Display over other apps`
- `Fine location`
- `Ignore battery optimizations`
- `Post notifications`
- `Query all packages`
- `通知`

<img src=".\img\Screenshot_2026-08-06-16-05-53-504_nodomain.freeyourgadget.gadgetbridge.jpg" alt="gb_permissions" height="500">

<br>`通知の管理`など一部の権限を有効にするには、Android側で`制限付き設定`を許可する必要がある。<br>Androidの設定からGadgetbridgeの`アプリ情報`を開き、`制限付き設定を許可`を許可する。

<img src=".\img\Screenshot_2026-08-06-16-07-51-281_com.miui.securitycenter.jpg" alt="gb_アプリ情報" height="500"> <img src=".\img\Screenshot_2026-08-06-16-08-13-412_com.miui.securitycenter.jpg" alt="gb_制限付き設定を許可_不許可" height="500"> <img src=".\img\Screenshot_2026-08-06-16-08-18-616_com.miui.securitycenter.jpg" alt="gb_制限付き設定を許可_許可" height="500">

<br>`Get started`の画面で、一旦`Go to the app`に進む。

<img src=".\img\Screenshot_2026-08-06-16-09-14-700_nodomain.freeyourgadget.gadgetbridge.jpg" alt="gb_Get_started" height="500">

### 3.3 Smart Bandの認証tokenの取得
GadgetbridgeからSmart Bandへ接続するために必要な認証tokenを取得する。
<br>[Xiaomi Cloud Tokens Extractor](https://github.com/PiotrMachowski/Xiaomi-cloud-tokens-extractor)のリリースページから[`token_extractor.exe`](https://github.com/PiotrMachowski/Xiaomi-cloud-tokens-extractor/releases/latest/download/token_extractor.exe)をPCにダウンロードし、実行する。

<img src=".\img\スクリーンショット 2026-09-14 014839.png" alt="Xiaomi Cloud Tokens Extractor" height="500"> <img src=".\img\スクリーンショット 2026-08-06 155807.png" alt="token_extractor.exe" height="500">

<br>QRコードを利用してログインするため、`q`を入力する。<br>表示されたURLをPCのブラウザで開き、表示されたQRコードをスマートフォンで読み取る。

<img src=".\img\スクリーンショット 2026-08-06 155820.png" alt="te_q" height="500"> <img src=".\img\スクリーンショット 2026-08-06 155832.png" alt="te_qr_url" height="500">

<br>[1.3節](#13-xiaomiアカウントの作成)で作成したXiaomiアカウントにサインインする。

<img src=".\img\Screenshot_2026-08-06-15-59-09-092_com.xiaomi.account.jpg" alt="te_signin" height="500"> <img src=".\img\Screenshot_2026-08-06-15-59-13-948_com.xiaomi.account.jpg" alt="te_signedin" height="500">

<br>`Logged in.`となり、`Select server`と出るが、空欄のままEnter。

<img src=".\img\スクリーンショット 2026-08-06 155925.png" alt="te_Select_server" height="500">

<br>出力結果を確認し、`TOKEN`の文字列を控える（いくつか出力されるが、すべて同じものになるはず）。この文字列を、後ほどGadgetbridgeの認証キーとして使用する。

<img src=".\img\スクリーンショット 2026-08-06 155956.png" alt="te_ids" height="500">

### 3.4 Mi Fitnessアプリのアンインストール
Mi FitnessとGadgetbridgeが同時にSmart Bandへ接続することを避けるため、Mi Fitnessをアンインストールする。

<img src=".\img\Screenshot_2026-08-06-16-10-18-897_com.miui.home.jpg" alt="mf_uninstall" height="500">

### 3.5 Smart Bandの接続
Gadgetbridgeアプリ画面左上の三本線のアイコンを押してメニューを開き、`新しいデバイスに接続`を選択。

<img src=".\img\Screenshot_2026-08-06-16-10-34-363_nodomain.freeyourgadget.gadgetbridge.jpg" alt="gb_drwermenu" height="500">

<br>検出されたデバイス一覧から、使用するSmart Bandを選択する。複数のデバイスが表示される場合は、MACアドレスを確認して判別する。

<img src=".\img\Screenshot_2026-08-06-16-10-46-937_nodomain.freeyourgadget.gadgetbridge.jpg" alt="gb_choose_device" height="500">

<br>[3.3節](#33-smart-bandデバイスのid取得)で取得したtokenを認証キーとして入力する。

<img src=".\img\Screenshot_2026-08-06-16-10-52-513_nodomain.freeyourgadget.gadgetbridge.jpg" alt="gb_token" height="500">

<br>`Companion device`に関する確認画面が表示された場合は、`はい`を選択して進む。

<img src=".\img\Screenshot_2026-08-06-16-12-08-641_nodomain.freeyourgadget.gadgetbridge.jpg" alt="gb_companion" height="500">

<br>`デバイス`タブを開き、Smart Bandに`接続済み`と表示されていれば設定完了。

<img src=".\img\Screenshot_2026-08-06-16-14-02-402_nodomain.freeyourgadget.gadgetbridge.jpg" alt="connected" height="500">

---
**Author: [Chi-robot](https://github.com/G-uruCPQ)** | Date: 2026-09-15
