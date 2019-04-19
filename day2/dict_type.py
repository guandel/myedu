import json

adict = {"username": "gdsaj", "password": "123456"}
bdict = {5: "yansl", "password": [2, 5]}
cdict_str='{"username": "gdsaj", "password": "123456"}'

def dict_set():
    print(adict['username'])


def dict_sel():
    bdict.pop(5)
    print(bdict)
def update_sel():
    adict['password']='hah'
    print(adict)
    adict.update(bdict)
    print(adict)
def dict_add():
    adict['爱好']='学习'
    print(adict)
def dict2str():#字典转换成字符串形式
    adict_str=json.dumps(adict)
    print(adict_str)
    print(type(adict_str))
def str2dict():#字符串转换成字典形式
    cdict=json.loads(cdict_str)
    print(cdict)
    print(type(cdict))


if __name__ == '__main__':
    # dict_set()
    #dict_sel()
    #update_sel()
    #dict_add()
    #dict2str()
    str2dict()
