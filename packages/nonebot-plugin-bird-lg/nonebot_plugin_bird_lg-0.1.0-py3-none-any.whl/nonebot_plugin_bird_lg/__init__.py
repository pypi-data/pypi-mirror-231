from nonebot.plugin import PluginMetadata
from . import __main__ as __main__
from .config import ConfigModel

__version__ = "0.1.0"
__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-bird-lg",
    description="使用指令在 QQ 内查询 bird 状态。",
    usage="指令: bird / bgp",
    type="application",
    homepage="https://github.com/lgc-NB2Dev/nonebot-plugin-bird-lg",
    config=ConfigModel,
    supported_adapters={"~onebot.v11"},
    extra={"License": "MIT", "Author": "XieXiLin & student_2333"},
)
