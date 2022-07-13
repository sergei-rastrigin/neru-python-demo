from dataclasses import dataclass, field
from typing import Dict, List, Generic, TypeVar
from abc import ABC, abstractmethod

from src.providers.voice.contracts.IInviteMemberPayload import IInviteMemberPayload
from src.providers.voice.contracts.IUser import IUser
from src.providers.voice.memberActions import MemberActions
from src.providers.voice.memberStates import MemberStates
from src.providers.voice.contracts.IChannel import IChannel
from src.providers.voice.contracts.user import User

@dataclass
class InviteMemberPayload(IInviteMemberPayload):
    channel: IChannel
    state: str
    action: str
    user: IUser
    def __init__(self,userName,channel):
        user = User()
        user.name = userName
        self.user = user
        self.action = MemberActions.Join
        self.state = MemberStates.Invited
        self.channel = channel
    
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