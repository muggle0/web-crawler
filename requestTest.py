import requests

if __name__ == "__main__":
    r = requests.get('https://juejin.cn/pins/hot');
    print(r.text)