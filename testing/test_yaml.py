import yaml


def test_yaml():
     with open("./datas/calc.yaml") as f:
         datas = yaml.safe_load(f)
         print(datas)
         print(datas['add']['datas'])