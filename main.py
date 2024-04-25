from sortedcontainers import SortedList
import requests
import main
import os
from controller.url_controller import UrlController
def main():
    arg = "./tests/test1" # input("Input file path\n")
    cache_size = 0
    num_urls = 0
    urls = []
    with open(arg, "r") as rf:
        try:
            cache_size = int(rf.readline())
            num_urls = int(rf.readline())
            url = rf.readline()
            while url != "":
                urls.append(url[:-1])
                url = rf.readline()
            print(cache_size, num_urls, urls)
        except Exception as e:
            print(e)
            exit(1)
    print("Data parsed successfully")

    urlController = UrlController(cache_size)

    response = []

    for url in urls:
        response.append(urlController.DownloadOrInCacheURL(url))
    cleanup(urls)
    return "\n".join(response)

def cleanup(urls):
    for url in urls:
        try:
            os.remove("./local_cache/"+ url.split("/")[-1])
        except Exception as e:
            print(e)
if __name__ == '__main__':
    response = main()
    print(response)