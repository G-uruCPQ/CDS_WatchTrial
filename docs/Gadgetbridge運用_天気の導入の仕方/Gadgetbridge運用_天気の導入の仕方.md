# Gadgetbridge運用   ── 天気の導入の仕方 ──
※本資料はSmart BandおよびGadgetbridgeの本質的な運用に関係しません。<br>しかし、UIのディテールがどうしても気になる方は参考にしていただければよいかと。

GadgetbridgeでXiaomi Smart Bandを利用するときに、天気の部分が`??`の表示になる。

<img src="./img/PXL_20260917_100402094.jpg" height="500">

Gadgetbridgeはスマートフォンに標準搭載されている天気アプリを参照できない（っぽい）ため、表示させるためには個別で天気アプリをインストールする必要がある。

## Gadgetbridgeに対応している天気アプリ
[Gadgetbridge](https://gadgetbridge.org/)の[Weather providers](https://gadgetbridge.org/basics/integrations/weather/)にある、4つのプロバイダアプリが利用可能。
- [Tiny Weather Forecast Germany](https://f-droid.org/packages/de.kaffeemitkoffein.tinyweatherforecastgermany/)
- [QuickWeather](https://f-droid.org/packages/com.ominous.quickweather/)
- [Breezy Weather](https://apt.izzysoft.de/fdroid/index/apk/org.breezyweather/)
- [OpenWeatherProvider (LineageOS)](https://mirrorbits.lineageos.org/WeatherProviders/OpenWeatherMapWeatherProvider.apk)

本資料では、[Breezy Weather](https://apt.izzysoft.de/fdroid/index/apk/org.breezyweather/)を例として手順を示す。

## Breezy Weatherのインストール
F-DroidからAPKファイルをダウンロードし、インストールする。

<img src="./img/Screenshot_2026-08-06-16-15-17-437_com.android.chrome.jpg" height="500">

## 天気を取得する地域の設定
アプリを開いたら、`現在地を追加`を押す。

<img src="./img/Screenshot_2026-08-06-16-17-26-042_org.breezyweather.jpg" height="500">

<br>`気象情報源`の確認画面が出るので、`保存`を押す。

<img src="./img/Screenshot_2026-08-06-16-17-33-735_org.breezyweather.jpg" height="500">

<br>位置情報へのアクセスを許可する。

<img src="./img/Screenshot_2026-08-06-16-17-37-589_org.breezyweather.jpg" height="500"> <img src="./img/Screenshot_2026-08-06-16-17-40-863_com.google.android.permissioncontroller.jpg" height="500">

<br>バックグラウンドでの位置情報アクセスを許可する。

<img src="./img/Screenshot_2026-08-06-16-17-44-337_org.breezyweather.jpg" height="500"> <img src="./img/Screenshot_2026-08-06-16-17-49-118_com.google.android.permissioncontroller.jpg" height="500">

## 天気データをGadgetbridgeで運用する
Breexy Weatherアプリ画面右上の三点マークから、`別のアプリケーションで開く`を選択する。

<img src="./img/Screenshot_2026-08-06-16-18-42-500_org.breezyweather.jpg" height="500"> <img src="./img/Screenshot_2026-08-06-16-18-48-940_org.breezyweather.jpg" height="500">

<br>`アプリで開く`タブに出てくるGadgetbridgeのアイコンを選択し、`常時`に設定する。

<img src="./img/Screenshot_2026-08-06-16-18-53-408_com.android.intentresolver.jpg" height="500">

<br>Gadgetbridgeアプリで、画面左上の三本線のアイコンを押してメニューを開き、`デバッグ`を押す。

<img src="./img/Screenshot_20260917-175137.png" height=500>

<br>`天気`を開き、`天気情報をキャッシュする`を有効化する。<br>`Cache`に地域が表示されたら`Send wheather to devices`を押して、デバイスに情報を反映する。

<img src="./img/Screenshot_20260917-175147.png" height=500> <img src="./img/Screenshot_20260917-175214.png" height=500> <img src="./img/PXL_20260917_100633453.jpg" height="500">

---
**Author: [Chi-robot](https://github.com/G-uruCPQ)** | Date: 2026-09-17
