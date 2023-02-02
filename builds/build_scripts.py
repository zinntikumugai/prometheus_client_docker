import os
import sys
import shutil
import yaml

# /build
SAVE_DIR = os.getcwd()

TEMPLATE_DIR = os.path.join(SAVE_DIR, "builds", "templates")
DOCKER_COMPOSE_TEMPLATE = os.path.join(TEMPLATE_DIR, 'docker-compose.yml')
CONFIG_FILE = "build_config.yaml"
EXPORT_COMPOSE_FILE = os.path.join(SAVE_DIR, "docker-compose.yml")

if __name__ == "__main__":
    print("SAVE_DIR", SAVE_DIR)
    # configがあるかチェック
    config = None
    with open(CONFIG_FILE, "r") as config_yaml:
        config = yaml.safe_load(config_yaml)
    # 無ければ終了

    if config is None:
        print("config not found.")
        print("exit.")

    docker_compose_template = None
    with open(DOCKER_COMPOSE_TEMPLATE, "r") as docker_template_yaml:
        docker_compose_template = yaml.safe_load(docker_template_yaml)
    # print("docker_compose_template", docker_compose_template)

    # 使用するコンポーネントをビルド

    docker_compose_file = {
        "version": "3",
        "services": {}
    }
    for container_name in config["use_container"]:
        print("service: {}".format(container_name))
        if container_name not in docker_compose_template["services"]:
            print("service not found.")
            continue

        service = docker_compose_template["services"][container_name]
        docker_compose_file["services"][container_name] = service

        dir_path = os.path.join(TEMPLATE_DIR, container_name)
        if os.path.isdir(dir_path):
            # 設定ファイルとかある(かもしれない)
            files = os.listdir(dir_path)

            for file in files:
                file_path = os.path.join(dir_path, file)
                new_file_path = os.path.join(SAVE_DIR, file)
                # ファイルを処理してコピー
                file_data = None
                with open(file_path, "r") as f:
                    file_data = f.read()

                for item in config["static_config"]:
                    file_data = file_data.replace(item["replace_name"], item["data"])
                # print("file_data", repr(file_data))

                with open(new_file_path, "w") as f:
                    f.write(file_data)
    # print("docker_compose_file", docker_compose_file)
    with open(EXPORT_COMPOSE_FILE, "w") as f:

        file = yaml.safe_dump(docker_compose_file, sort_keys=False, default_flow_style=False)
        f.write(file)
    # おしまい
