import requests
from bs4 import BeautifulSoup


# 请求ip的函数
def get_ip():
    # 请求输入
    addr = input("请输入要查询的ip，输入q退出：")
    # 退出检测
    if addr == "q":
        print("退出查询")
        exit(0)
    # 切割
    ips = addr.split(".")
    # 长度必须为4
    if len(ips) != 4:
        print("输入ip不正确")
        return get_ip()
    # 必须是int
    for i in ips:
        try:
            i = int(i)
        except:
            print("输入ip不正确")
            return get_ip()
        # 范围是0～255,出去的全部不可能
        if i < 0 or i > 255:
            print("输入的ip不正确")
            return get_ip()
    # 返回结果
    return addr


def query():
    # 输入ip
    ip = get_ip()
    # 设置参数
    options = {"ip": ip}
    # 查询的api
    ipcn = "http://ip.cn/index.php"
    # 查询
    req = requests.get(ipcn, options)
    # 检测返回状态
    print("查询状态码", req.status_code)
    req.raise_for_status()
    # 设置编码
    req.encoding = req.apparent_encoding
    # 转为soup
    soup = BeautifulSoup(req.text, "html.parser")
    # 找到结果
    result = soup.select("#result")[0]
    # 结果转换为soup
    soup = BeautifulSoup(str(result), "html.parser")
    # 输出结果
    for i in soup.find_all("p"):
        print(i.text)
    print()


if __name__ == '__main__':
    while True:
        query()
