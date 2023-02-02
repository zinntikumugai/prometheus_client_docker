## prometheus_client_docker

**とても雑に** dockerコンテアで動かすExporter類

| | | Port | github | docker |
|:--|:--|:--|:--|:--|
| node-exporter | マシン自体のExporter | 9100 | [github](https://github.com/prometheus/node_exporter) | [docker image](https://quay.io/repository/prometheus/node-exporter?tab=tags&tag=latest) |
| container-exporter | DockerコンテナのExporter | 9101 | [github](https://github.com/google/cadvisor) | [docker image](https://console.cloud.google.com/gcr/images/cadvisor/GLOBAL/cadvisor) |
| promtail-docker | Dockerコンテナログ | 9080 |  | [docker image](https://hub.docker.com/r/grafana/promtail) |

## node-exporter

よくあるやつ  
これを動かすマシン自体の状態を吐き出す

## container-exporter

各Dockerコンテナの状態を吐き出す

## promtail-docker

ログをlokiに吐き出すやつ  
Dockerコンテナの標準出力をlokiに出力する  
サービスのログファイルは別にした方が良いかも?  
ttyがtrueになっていると動かない


# build

```bash
cp builds/build_config.yaml .
vim build_config.yaml
# fix
cd builds
docker compose build
docker compose run --rm buildtool python builds/build_scripts.py
```

## 必要な物

- Docker Compose

## 使い方

1. `builds/build_config.yaml`を直下にコピーし、ホスト名とかを修正
1. `builds`ディレクトリに入り、ビルド実行

## 設定とか

`build_config.yaml`の内容次第

### `static_config`

いわゆる静的データ  
ホスト名、IPアドレスとか

### `use_container`

使用するDockerコンテナを指定
