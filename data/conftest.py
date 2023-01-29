import pytest
import yaml

with open('com.yaml') as f:
    com = yaml.safe_load(f)
    comdom = com['dom']
    comdome = comdom['dome']
    print(comdome)
    idss=comdom['ids']

@pytest.fixture(params=comdome,ids=idss)
def com_add(request):
    dome_1=request.param
    return dome_1