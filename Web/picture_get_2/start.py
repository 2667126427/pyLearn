import os
import web
import conf

if __name__ == '__main__':
    start = input("input the start page(1~124): ")
    start = int(start)
    end = input("input the end page(>=start): ")
    end = int(end)
    count = 1
    if os.path.exists("./pic"):
        print("the pic folder has existed")
    else:
        os.mkdir("./pic")
        print("Create the pic folder")

    for page in range(start, end + 1):
        links = web.get_links(conf.url + str(page))
        for link in links:
            if web.save(link, conf.path, count):
                count = count + 1
    print("Finished")
