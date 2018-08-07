import json

import CityAir

if __name__ == '__main__':
    asker = CityAir.AirCond('鹤壁')
    print(json.dumps(asker.get_station(), indent=4, ensure_ascii=False))
    # asker = CityAir.AirCond('北京')
    # print(json.dumps(asker.get_station(), indent=4, ensure_ascii=False))
