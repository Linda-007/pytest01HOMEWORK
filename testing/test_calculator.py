import yaml

import pytest

from pythoncode.Calculator import Calculator


def get_datas():
    with open("./datas/calc.yaml") as f:
        datas = yaml.safe_load(f)
    return datas
    return (datas['add']['datas'],datas['add']['ids'])

#测试类
class TestCalc:
    datas:list = get_datas()

    #前置条件
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator

    #后置条件
    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,result",datas[0],ids=datas[1])
    def test_add(self,a,b,result):
        assert result == self.calc.add(a,b)

    def test_add1(self):
        datas = [[1,1,2],[-1,1,0],[-0,1,1]]
        for data in datas:
            print(data)
            assert data[2] == self.calc.add(data[0],data[1])

    @pytest.mark.parametrize("a,b,result",datas[0],ids=[datas[1]])
    def test_div(self,a,b,result):
        assert result == self.calc.div(a,b)

    def test_div1(self):
        datas = [[2,1,2],['3','0','无效除数'],[-8,2,-4],[0,3,0]]
        for data in datas:
            if data[1] == 0:
                try:
                    self.calc.div(data[0],[data[1]])
                except ZeroDivisionError as e:
                    print("除数不能为0")
            else:
                assert  data[2] == self.calc.div(data[0],data[1])

if __name__ == '__main__':
    pytest.main()

