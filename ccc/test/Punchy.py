from ast import Break


_dict_={}
while True:
    _in_=input().split()
    if _in_[0]=='0':...
    elif _in_[0]=='1':_dict_[_in_[1]]=int(_in_[2])
    elif _in_[0]=='2':print(_dict_[_in_[1]])
    elif _in_[0]=='3':_dict_[_in_[1]]=_dict_[_in_[1]]+_dict_[_in_[2]]
    elif _in_[0]=='4':_dict_[_in_[1]]=_dict_[_in_[1]]*_dict_[_in_[2]]
    elif _in_[0]=='5':_dict_[_in_[1]]=_dict_[_in_[1]]-_dict_[_in_[2]]
    elif _in_[0]=='6':_dict_[_in_[1]]=_dict_[_in_[1]]//_dict_[_in_[2]]
    elif _in_[0]=='7':print('',end='');break