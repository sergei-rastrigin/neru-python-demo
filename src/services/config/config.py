from dataclasses import dataclass, field
from typing import Dict, List, Generic, TypeVar
from abc import ABC, abstractmethod

from src.services.config.IConfig import IConfig
from src.IBridge import IBridge

@dataclass
class Config(IConfig):
    assetUrl: str
    appUrl: str
    privateKey: str
    apiAccountId: str
    apiApplicationId: str
    applicationId: str
    instanceServiceName: str
    bridge: IBridge
    instanceId: str = field(default = "debug")
    debug: bool = field(default = False)
    namespace: str = field(default = "neru")
    def __init__(self,bridge):
        self.bridge = bridge
        if self.bridge.getEnv("NAMESPACE") is not None:
            self.namespace = self.bridge.getEnv("NAMESPACE")
        
        self.instanceServiceName = self.bridge.getEnv("INSTANCE_SERVICE_NAME")
        self.applicationId = self.bridge.getEnv("APPLICATION_ID")
        if self.bridge.getEnv("INSTANCE_ID") is not None:
            self.instanceId = self.bridge.getEnv("INSTANCE_ID")
        
        self.apiApplicationId = self.bridge.getEnv("API_APPLICATION_ID")
        self.apiAccountId = self.bridge.getEnv("API_ACCOUNT_ID")
        self.privateKey = self.bridge.getEnv("PRIVATE_KEY")
        self.appUrl = f'{self.bridge.getEnv("ENDPOINT_URL_SCHEME")}/{self.bridge.getEnv("INSTANCE_SERVICE_NAME")}'
        debug = self.bridge.getEnv("DEBUG")
        if debug is "true":
            self.debug = True
        
        self.assetUrl = "http://openfaas.euw1.dev.nexmo.cloud/function/vonage-assets?get="
    
    def getExecutionUrl(self,func):
        value = f'{func}.{self.namespace}'
        if self.debug:
            return f'http://localhost:3001?func={value}&async=false'
        
        else: 
            return f'http://{value}'
        
    
    def reprJSON(self):
        dict = {}
        keywordsMap = {"from_":"from","del_":"del","import_":"import","type_":"type"}
        for key in self.__dict__:
            val = self.__dict__[key]

            if type(val) is list:
                parsedList = []
                for i in val:
                    if hasattr(i,'reprJSON'):
                        parsedList.append(i.reprJSON())
                    else:
                        parsedList.append(i)
                val = parsedList

            if hasattr(val,'reprJSON'):
                val = val.reprJSON()
            if key in keywordsMap:
                key = keywordsMap[key]
            dict.__setitem__(key.replace('_hyphen_', '-'), val)
        return dict