# GadgetbridgeとSmart Bandデバイスの連携

Xiaomi Smart Band 10をAndroidスマートフォンに接続し、同デバイスをGadgetbridgeアプリで利用できるようにするまでの一連の流れを示す。<br>
本記事において、スマートフォンはXiaomi REDME 15を利用したが、他のAndroidスマートフォン（Google Pixcelなど）においても、同様の設定を進めることで連携が可能である。

## 1. Mi Fitnessのインストール・初期設定
### 1.1 Mi Fitnessアプリのインストール
GooglePlayストアからMi Fitnessアプリをインストールする。

<img src=".\img\Screenshot_2026-08-06-15-41-29-491_com.android.vending.jpg" alt="MiFitnessインストール" height="500">

### 1.2 Mi Fitness初期設定
Mi Fitnessアプリを開き、`開始`を押す。

<img src=".\img\Screenshot_2026-08-06-15-44-17-324_com.xiaomi.wearable.jpg" alt="MiFitness開始" height="500">

<br>使用条件に同意し、地域を日本に設定する。

<img src=".\img\Screenshot_2026-08-06-15-44-30-820_com.xiaomi.wearable.jpg" alt="使用条件同意" height="500">
<img src=".\img\Screenshot_2026-08-06-15-44-45-608_com.xiaomi.wearable.jpg" alt="地域設定" height="500">

<br>身体活動データへのアクセスを許可する。

<img src=".\img\Screenshot_2026-08-06-15-44-51-982_com.xiaomi.wearable.jpg" alt="アクセス許可" height="500">
<img src=".\img\Screenshot_2026-08-06-15-44-58-497_com.google.android.permissioncontroller.jpg" alt="身体活動データアクセス" height="500">

### 1.3 Xiaomiアカウントの作成
Mi Fitessアプリ下の`プロフィール`タブを選択し、`サインイン`からサインインに移る。

<img src=".\img\Screenshot_2026-08-06-15-45-33-128_com.xiaomi.wearable.jpg" alt="初期設定完了" height="500">
<img src=".\img\Screenshot_2026-08-06-15-45-41-232_com.xiaomi.wearable.jpg" alt="プロフィール画面" height="500">

<br>メインUIより下の`アカウントを作成`を押し、手順に従ってアカウントを作成する。

<img src=".\img\PXL_20260806_064617421.jpg" alt="Xiaomiアカウントにサインイン" height="500">
<img src=".\img\PXL_20260806_064644318.jpg" alt="Xiaomiアカウントを作成" height="500">

## 2. Smart Bandのスマートフォンへの接続
### 2.1 Smart Bandの起動
充電ケーブルでSmart Bandを電源に接続し、起動する。

<img alt="MiBand電源接続" height="500">

<br>言語選択で`日本語`を選択する。

<img src=".\img\PXL_20260806_065428113.jpg" alt="MiBand言語選択" height="500">

### 2.2 Smart Bandの接続
画面右上からスワイプし、BluetoothをONに設定する。

<img src=".\img\Screenshot_2026-08-06-15-45-17-474_com.xiaomi.wearable.jpg" alt="BluetoothOn" height="500">

<br>Mi Fitnessアプリ下の`デバイス`タブを選択し、`デバイスを追加`を押す。

<img src=".\img\Screenshot_2026-08-06-15-45-33-128_com.xiaomi.wearable.jpg" alt="初期設定完了" height="500">
<img src=".\img\Screenshot_2026-08-06-15-51-30-404_com.xiaomi.wearable.jpg" alt="デバイス画面" height="500">

<br>Bluetoothによるデータ転送を許可する。

<img src=".\img\Screenshot_2026-08-06-15-51-54-060_com.xiaomi.wearable.jpg" alt="Bluetoothアクセス許可" height="500">

<br>付近のBluetoothデバイスの検出を許可する。

<img src=".\img\Screenshot_2026-08-06-15-51-59-850_com.xiaomi.wearable.jpg" alt="Bluetoothデバイス検出許可" height="500">
<img src=".\img\Screenshot_2026-08-06-15-52-05-413_com.google.android.permissioncontroller.jpg" alt="付近のデバイス検出許可" height="500">

<br>Smart Bandを検出したら、`ペア設定をする`を押して接続する。
Smart Band側でも`v(チェックマーク)`を押して、ペア設定をする。

<img src=".\img\Screenshot_2026-08-06-15-53-24-329_com.android.settings.jpg" alt="MiFitnessペア設定" height="500">
<img src=".\img\PXL_20260806_065505932.jpg" alt="MiBandペア設定" height="500">

<br>Smart Bandとスマートフォンの接続完了。次へ進む。

<img src=".\img\Screenshot_2026-08-06-15-55-29-714_com.xiaomi.wearable.jpg" alt="MiBandペア設定" height="500">

<br>以降設定が続くが、Mi Fitnessアプリ自体は使わないので適当に設定してOK。

<img src=".\img\Screenshot_2026-08-06-15-55-38-270_com.xiaomi.wearable.jpg" alt="Mi Fitnessアプリ通知設定" height="500">
<img src=".\img\Screenshot_2026-08-06-15-55-46-225_com.xiaomi.wearable.jpg" alt="Mi Fitnessアプリ着信設定" height="500">
<img src=".\img\Screenshot_2026-08-06-15-55-50-918_com.xiaomi.wearable.jpg" alt="Mi Fitnessアプリシステム情報同期設定" height="500">

<br>装着ガイドを読み、次へ進む。

<img src=".\img\Screenshot_2026-08-06-15-55-55-072_com.xiaomi.wearable.jpg" alt="Mi Fitnessアプリ装着ガイド" height="500">

<br>以降Smart Bandの使い方を読みながら、`次へ`で進む。

<img src=".\img\Screenshot_2026-08-06-15-56-03-926_com.xiaomi.wearable.jpg" alt="Mi Fitnessガイド1" height="500">
<img src=".\img\Screenshot_2026-08-06-15-56-06-196_com.xiaomi.wearable.jpg" alt="Mi Fitnessガイド2" height="500">
<img src=".\img\Screenshot_2026-08-06-15-56-09-070_com.xiaomi.wearable.jpg" alt="Mi Fitnessガイド3" height="500">
<img src=".\img\Screenshot_2026-08-06-15-56-10-937_com.xiaomi.wearable.jpg" alt="Mi Fitnessガイド4" height="500">

<br>`開始`を押して次へ進む。

<img src=".\img\Screenshot_2026-08-06-15-56-14-371_com.xiaomi.wearable.jpg" alt="Mi Fitness開始" height="500">

<br>バンド接続保護の警告が出るが、設定しなくてよい。ウィンドウ外をタップしてエスケープ。

<img src=".\img\Screenshot_2026-08-06-15-56-22-730_com.xiaomi.wearable.jpg" alt="バンド接続保護警告" height="500">

<br>以上でスマートフォンとSmart Bandの接続は完了しました。

## 3. Smart BandのGadgetbridgeへの接続
Smart Bandとの通信を制御できるようにするために、Gadgetbridgeというオープンソースアプリを利用する。

### 3.1 Gadgetbridgeのインストール
GadgetbridgeはGoogleStoreにもあるが、バージョンが古く使えないので、F-Droidというアプリストアから最新版をインストールする。

[F-Droid](https://f-droid.org/ja/)の検索バーから`gadgetbridge`で検索。
<br>無印のGadgetbirdgeを選択。

<img src=".\img\Screenshot_2026-08-06-16-01-19-092_com.android.chrome.jpg" alt="FDroid_gadgetbridge検索" height="500">
<img src=".\img\Screenshot_2026-08-06-16-01-31-931_com.android.chrome.jpg" alt="FDroid_gadgetbirdge選択" height="500">

<br>Gadgetbridgeのページで、下にスクロールすると最新版がある（`提案`と書いてあるもの。本記事製作時点ではver.0.92.2）。<br>同ブロックの最下部にある`APKをダウンロード`を押し、APKファイルをダウンロードする。

<img src=".\img\Screenshot_2026-08-06-16-01-41-882_com.android.chrome.jpg" alt="FDroid_gadgetbirdge" height="500">
<img src=".\img\Screenshot_2026-08-06-16-02-05-314_com.android.chrome.jpg" alt="FDroid_gadgetbirdge_latest_top" height="500">
<img src=".\img\Screenshot_2026-08-06-16-02-16-160_com.android.chrome.jpg" alt="FDroid_gadgetbirdge_latest_bottom" height="500">

<br>スマートフォンのエクスプローラーアプリからダウンロードしたAPKファイルを探し、実行。

<img src=".\img\Screenshot_2026-08-06-16-04-01-600_com.mi.android.globalFileexplorer.jpg" alt="エクスプローラー" height="500">

<br>Gadgetbridgeアプリがインストールされる。

<img src=".\img\Screenshot_2026-08-06-16-05-15-225_com.miui.home.jpg" alt="フォルダー" height="500">

### 3.2 Gadgetbridgeの権限設定
Gadgetbridgeアプリを開くと、アプリ権限の許可の画面が出てくる。
- `Background location`
- `Bluetooth connect`
- `Bluetooth scan`
- `Display over other apps`
- `Fine location`
- `Ignore battery optimizations`
- `Post notifications`
- `Query all packages`
- `通知`

を最低限許可するとよい。

<img src=".\img\Screenshot_2026-08-06-16-05-53-504_nodomain.freeyourgadget.gadgetbridge.jpg" alt="gb_permissions" height="500">

<br>`通知の管理`などの権限は、「制限付き設定」を許可しなければ許可できない。<br>設定のアプリ情報から、`制限付き設定を許可`を許可する。

<img src=".\img\Screenshot_2026-08-06-16-07-51-281_com.miui.securitycenter.jpg" alt="gb_アプリ情報" height="500">
<img src=".\img\Screenshot_2026-08-06-16-08-13-412_com.miui.securitycenter.jpg" alt="gb_制限付き設定を許可_不許可" height="500">
<img src=".\img\Screenshot_2026-08-06-16-08-18-616_com.miui.securitycenter.jpg" alt="gb_制限付き設定を許可_許可" height="500">

<br>`Get started`の画面で、一旦`Go to app`に進む。

<img src=".\img\Screenshot_2026-08-06-16-09-14-700_nodomain.freeyourgadget.gadgetbridge.jpg" alt="gb_Get_started" height="500">

### 3.3 Smart BandデバイスのID取得
GadgetbridgeにSmart Bandを接続するには、Smart Bandのtokenを取得する必要がある。
<br>[Xiaomi Cloud Tokens Extractor](https://github.com/PiotrMachowski/Xiaomi-cloud-tokens-extractor)にある[token_extratcor.exe](https://github.com/PiotrMachowski/Xiaomi-cloud-tokens-extractor/releases/latest/download/token_extractor.exe)をインストール、実行する。

<img src=".\img\スクリーンショット 2026-09-14 014839.png" alt="Xiaomi Cloud Tokens Extractor" height="500">
<img src=".\img\スクリーンショット 2026-08-06 155807.png" alt="token_extractor.exe" height="500">

<br>QRコード経由が便利なので、`q`を入力。<br>表示されたurlにブラウザでアクセスし、スマートフォンで読み取る。

<img src=".\img\スクリーンショット 2026-08-06 155820.png" alt="te_q" height="500">
<img src=".\img\スクリーンショット 2026-08-06 155832.png" alt="te_qr_url" height="500">

<br>[1.3節](#13-xiaomiアカウントの作成)で作成したXiaomiアカウントにサインインする。

<img src=".\img\Screenshot_2026-08-06-15-59-09-092_com.xiaomi.account.jpg" alt="te_signin" height="500">
<img src=".\img\Screenshot_2026-08-06-15-59-13-948_com.xiaomi.account.jpg" alt="te_signedin" height="500">

<br>`Logged in.`となり、`Select server`と出るが、空欄のままEnter。

<img src=".\img\スクリーンショット 2026-08-06 155925.png" alt="te_Select_server" height="500">

<br>出力されたもののいずれかの`TOKEN`の文字列が、接続に必要なtokenである（すべて同じものになるはず）。

<img src=".\img\スクリーンショット 2026-08-06 155956.png" alt="te_ids" height="500">

### 3.4 Mi Fitnessアプリのアンインストール
Mi FitnessアプリとGadgetbridgeのbluetooth干渉回避のため、Mi Fitnessアプリをアンインストールする。

<img src=".\img\Screenshot_2026-08-06-16-10-18-897_com.miui.home.jpg" alt="mf_uninstall" height="500">

### 3.5 Smart Bandの接続
GadgetbridgeアプリのUI左上三本線からドロワーを開き、`新しいデバイスに接続`を選択。

<img src=".\img\Screenshot_2026-08-06-16-10-34-363_nodomain.freeyourgadget.gadgetbridge.jpg" alt="gb_drwermenu" height="500">

<br>自分の利用しているSmart Bandを選択する。<br>MACアドレスが一致するものを探すとよい。

<img src=".\img\Screenshot_2026-08-06-16-10-46-937_nodomain.freeyourgadget.gadgetbridge.jpg" alt="gb_choose_device" height="500">

<br>[3.3節](#33-smart-bandデバイスのid取得)で取得したtokenを認証キーとして入力する。

<img src=".\img\Screenshot_2026-08-06-16-10-52-513_nodomain.freeyourgadget.gadgetbridge.jpg" alt="gb_token" height="500">

<br>Companion deviceのメッセージが出るが`はい`で進む。

<img src=".\img\Screenshot_2026-08-06-16-12-08-641_nodomain.freeyourgadget.gadgetbridge.jpg" alt="gb_companion" height="500">

<br>デバイスタブにて`接続済み`の表示が出ていたら成功。

<img src=".\img\Screenshot_2026-08-06-16-14-02-402_nodomain.freeyourgadget.gadgetbridge.jpg" alt="connected" height="500">
