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

# 運用方法

Webサーバである`main.py`をデーモンとして動作するように設定する。

