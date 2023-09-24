from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment, Message, GroupMessageEvent
import httpx
from typing import List
from .config import config
from .utils import *

bgp = on_command("bgp", aliases={"bgp"})

@bgp.handle()
async def _(bot: Bot, event: MessageEvent, message: Message = CommandArg()):
    messages: List[MessageSegment] = []
    if message.extract_plain_text() != "":
        query = message.extract_plain_text().replace(" ", "+")
    else:
        query = "show+protocols"
    for sid in config.BIRDLG_SERVERS:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/237.84.2.178 Safari/537.36 nonebot-plugin-bird-lg(https://github.com/lgc-NB2Dev/nonebot-plugin-bird-lg, 0.1.0)"}
        data = httpx.get(
            f"http://{sid}.{config.BIRDLG_DOMAIN}:8000/bird?q={query}", headers=headers)
        if data.status_code == 200:
            messages.append(MessageSegment.node_custom(event.user_id, f"{sid}: {query}", MessageSegment.image(generate_image(convert_data(data.text)))))
        else:
            messages.append(MessageSegment.node_custom(event.user_id, f"{sid}: {query}", MessageSegment.text("查询失败: 返回状态码 {data.status_code}")))
    if isinstance(event, GroupMessageEvent):
        await bot.call_api("send_group_forward_msg", group_id=event.group_id, messages=messages)
    else:
        await bot.call_api("send_private_forward_msg", user_id=event.user_id, messages=messages)