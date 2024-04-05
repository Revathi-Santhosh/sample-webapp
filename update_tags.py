import yaml
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mq_version")
parser.add_argument("-p", "--python_app_version")
parser.add_argument("-j", "--java_app_verison")

args = parser.parse_args()
with open("docker-compose.yaml", "r") as file:
    data = yaml.safe_load(file)

data["services"]["rabbitmq"]["image"] = f"mq_stomp_server:{args.mq_version}"
data["services"]["pythonapp"]["image"] = f"python_app:{args.python_app_version}"
data["services"]["javaapp"]["image"] = f"java_app:{args.java_app_verison}"
with open("docker-compose.yaml", "w") as file:
    yaml.dump(data, file)
