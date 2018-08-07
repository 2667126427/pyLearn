from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('47.100.124.50')
    db = client['nonstate']
    for coll_name in db.collection_names(include_system_collections=False):
        deleted = db[coll_name].delete_many({'aqi': -1})
        print(deleted.deleted_count)
