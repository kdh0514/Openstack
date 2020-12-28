import http.client
import requests


def conController(sendCode):
    url = "http://127.0.0.1:8080/recorder"
    numplate = {'num': sendCode}
    r = requests.get(url, params=numplate)

    print(r.text)


# if __name__ == "__main__":
#     conController("ssibal")