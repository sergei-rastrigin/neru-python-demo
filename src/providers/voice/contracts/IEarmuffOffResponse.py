from dataclasses import dataclass, field
from typing import Dict, List, Generic, TypeVar
from abc import ABC, abstractmethod

from src.providers.voice.contracts.ICreateEventResponse import ICreateEventResponse


#interface
class IEarmuffOffResponse(ICreateEventResponse):
    pass