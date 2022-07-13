import json
import os
import aiohttp
import jwt
import time
import uuid
from datetime import datetime
from src.IBridge import IBridge

class Bridge(IBridge):
    def substring(self,str,start,end):
        return str[start:end]
    def jsonStringify(self,data):
        return json.dumps(data, default=lambda o: o.reprJSON(),
            sort_keys=True, indent=4)
    def jsonParse(self,str):
        return json.loads(str)
    def getEnv(self,name):
        return os.getenv(name)
    async def request(self,params):
        if not params.url:
            raise Exception('url is required')
        if not params.method:
            raise Exception('method is required')

        url = params.url
        method = params.method

        if params.data:
            data = params.data.reprJSON()
        else:
            data = {}

        if params.headers:
            headers = params.headers.reprJSON()
        else:
            headers = {}

        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, json=data, headers=headers) as resp:
                return await resp.text()

    async def requestWithoutResponse(self,params):
        await self.request(params)
    def uuid(self):
        return str(uuid.uuid4())
    def isoDate(self):
        my_date = datetime.now()
        return my_date.isoformat()
    def jwtSign(self,payload,privateKey,algorithm):
        return jwt.encode(payload, privateKey, algorithm)
    def jwtVerify(self,token,privateKey,algorithm):
        return jwt.decode(token, privateKey, algorithm)
    def getSystemTime(self):
        return int(time.time())
    def log(self,logAction):
        print(logAction)
    def getObjectKeys(self,obj):
        return obj.keys()
    def getRouter(self):
        pass