

import urllib.request
if __name__ == "__main__":
    response = urllib.request.urlopen('https://juejin.cn/pins/hot')
    print(response.read().decode('utf-8'))