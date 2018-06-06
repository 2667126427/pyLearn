from pymongo import MongoClient


class DBWriter:
    def __init__(self, host='localhost', port=27017, dbname='test',
                 coll='test'):
        self._client = MongoClient(host=host, port=port)
        self._db = self._client[dbname]
        self._coll = self._db[coll]

    def write_one(self, data):
        if self._coll.count(data) == 0:
            self._coll.insert_one(data)

    def write_all(self, datas):
        for data in datas:
            if self._coll.count(data) == 0:
                self._coll.insert_one(data)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._client.close()
