## prometheus_client_docker

dockerコンテアナで動かすExporter類

| | | Port |
|:--|:--|:--|
| node-exporter | マシン自体のExporter | 9100 |
| container-exporter | DockerコンテナのExporter | 9101 |
| promtail | Dockerコンテナログ | 9080 |

## node-exporter

よくあるやつ  
これを動かすマシン自体の状態を吐き出す

## container-exporter

各Dockerコンテナの状態を吐き出す

## promtail

ログをlokiに吐き出すやつ  
Dockerコンテナの標準出力をlokiに出力する
サービスのログファイルは別にした方が良いかも?
