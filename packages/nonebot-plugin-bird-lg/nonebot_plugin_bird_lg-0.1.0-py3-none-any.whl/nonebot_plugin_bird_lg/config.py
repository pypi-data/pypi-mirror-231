from nonebot import get_driver
from pydantic import BaseModel
from typing import List, Set

class ConfigModel(BaseModel):
    BIRDLG_SERVERS: List[str]
    BIRDLG_DOMAIN: str


config: ConfigModel = ConfigModel.parse_obj(get_driver().config.dict())
