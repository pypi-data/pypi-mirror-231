#    ____       _        _____  _                  
#   / __ \     | |      |  __ \(_)                 
#  | |  | | ___| |_ ___ | |  | |_  __ _ _ __ _   _ 
#  | |  | |/ __| __/ _ \| |  | | |/ _` | '__| | | |
#  | |__| | (__| || (_) | |__| | | (_| | |  | |_| |
#   \____/ \___|\__\___/|_____/|_|\__,_|_|   \__, |
#                                             __/ |
#                                            |___/ 
# 
#                 © Copyright 2023
#        🔒 Licensed under the MIT License
#        https://opensource.org/licenses/MIT
#           https://github.com/OctoDiary

import json
import typing
from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class Type(BaseModel):
    @staticmethod
    def __default__(type: "Type"):
        if isinstance(type, (bytes, typing.Match)):
            return repr(type)
        elif isinstance(type, (Enum, datetime)):
            return str(type)

        return {
            "_": type.__class__.__name__,
            **{
                attr: getattr(type, attr)
                for attr in filter(lambda x: not x.startswith("_"), type.__dict__)
                if getattr(type, attr) is not None
            }
        }

    def __str__(self) -> str:
        return json.dumps(
            self,
            indent=4,
            default=Type.__default__,
            ensure_ascii=False
        )


class EveryType(Type):
    id: int
    name: str
    actual_from: str
    actual_to: str
