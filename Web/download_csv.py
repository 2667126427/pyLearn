from urllib import request

goog_url = 'http://chart.finance.yahoo.com/table.csv?s=GOOG&a=2&b=1&c=2017&d=3&e=1&f=2017&g=d&ignore=.csv'


def download_csv(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    goog_csv = r'goog.csv'
    fx = open(goog_csv, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_csv(goog_url)