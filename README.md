# env_raspberrypi

気温・湿度・気圧データを取得して値をJSONとして返すAPIサーバ。

以下のリポジトリと組み合わせて運用する。

https://github.com/ABC10946/

# インストール

```
$ git clone https://github.com/ABC10946/env_raspberrypi
$ cd env_raspberrypi
$ sh install.sh
```

# 常時運用のための設定

Webサーバである`main.py`をデーモンとして動作するように設定する。

systemdを用いた設定は以下のようになる。

```
[Unit]
Description=sensing data web api server with bme280
After=network.target

[Service]
Type=simple
WorkingDirectory=/path/to/env_webserver/
ExecStart=/usr/bin/python3 main.py
Restart=yes

[Install]
WantedBy=multi-user.target
```
