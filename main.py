from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

import aiohttp
import json
import datetime

@register("astrbot_plugin_ddlkstats", "H1taGi77", "死锁战绩查询", "0.2.0")
class DdlockstatsPlugin(Star):
    """死锁战绩查询"""

    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("调查")
    async def 调查(self, event: AstrMessageEvent,account_id:str):
        """查询玩家对局历史"""
        yield event.plain_result(f"正在努力调查 {account_id} ，请稍等喵...")

        url = f"https://api.deadlock-api.com/v1/players/{account_id}/match-history"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status !=200:
                        yield event.plain_result(f"查询失败（HTTP {resp.status}）！检查一下账号ID对不对喵~")
                        return

                    data = await resp.json()

            if not matches:
                

        except Exception as e:
            logger.error(f"查询出错：{e}")
            yield event.plain_result("网络好像出问题了喵，过会再试试~")