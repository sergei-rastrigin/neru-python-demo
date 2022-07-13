from dataclasses import dataclass, field
from typing import Dict, List, Generic, TypeVar
from abc import ABC, abstractmethod



#interface
class ISayTextBody(ABC):
    text:str
    level:int
    loop:int
    voice_name:str
    queue:bool
    ssml:bool
    language:str
    style:int