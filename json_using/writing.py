import json


class Object:
    def __init__(self, _id, _name, _age):
        super().__init__()
        self._id = _id
        self._name = _name
        self._age = _age

    def __dict__(self):
        return {'id': self._id, 'name': self._name, 'age': self._age}

    @classmethod
    def dict2obj(cls, obj):
        return obj.__dict__()


def dict2obj(dic):
    pass


def obj2dict(obj):
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__())
    return d


if __name__ == '__main__':
    obj = Object(12, 'Jack', 17)
    print(Object.dict2obj(obj))


    # s = json.dumps(obj, indent=4, default=obj2dict)
    # print(s)
