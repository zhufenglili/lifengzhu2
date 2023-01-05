import  pytest
import yaml


@pytest.fixture()
def test_5():
    print('你好')
@pytest.mark.parametrize('a,b',[(12,2),(3,4)])
def test_3(a,b,test_5):
    return a + b
@pytest.mark.parametrize('aa',yaml.safe_load(open('./dome.yaml')))
def test_4(aa):
    print('打印',aa['my'])

if __name__ == '_main_':
    pytest.main(['test_2'])
