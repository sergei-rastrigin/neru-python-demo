from dataclasses import dataclass, field
from typing import Dict, List, Generic, TypeVar
from abc import ABC, abstractmethod

from src.providers.logger.ILogContext import ILogContext


#interface
class ILogAction(ABC):
    id:str
    session_id:str
    instance_id:str
    api_application_id:str
    api_account_id:str
    timestamp:str
    log_level:str
    message:str
    source_type:str
    source_id:str
    context:ILogContext