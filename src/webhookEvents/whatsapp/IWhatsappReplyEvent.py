from dataclasses import dataclass, field
from typing import Dict, List, Generic, TypeVar
from abc import ABC, abstractmethod

from src.webhookEvents.whatsapp.IReplyObject import IReplyObject
from src.webhookEvents.whatsapp.IWhatsappEvent import IWhatsappEvent


#interface
class IWhatsappReplyEvent(IWhatsappEvent):
    reply:IReplyObject