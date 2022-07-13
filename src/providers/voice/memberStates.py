from dataclasses import dataclass, field
from typing import Dict, List, Generic, TypeVar
from abc import ABC, abstractmethod


class MemberStates:
    Joined = "joined"
    Invited = "invited"
    Left = "left"
    Unknown = "unknown"