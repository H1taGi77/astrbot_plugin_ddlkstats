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

                    matches = await resp.json()

            if not matches:
                yield event.plain_result("这个账号空空的喵")
                return

            lines = []
            for m in matches[:5]:
                minutes = m["match_duration_s"] // 60
                seconds = m["match_duration_s"] % 60

                if m["player_match_outcome"] == 1:
                    win = "得胜😍"
                else:
                    win = "败北😭"

                time_obj = datetime.datetime.fromtimestamp(m["start_time"])
                date = time_obj.strftime("%m-%d %H:%M")

                line = (
                    f"{date} | 英雄{m['hero_id']} | "
                    f"{m['player_kills']}/{m['player_deaths']}/{m['player_assists']}"
                    f" | {win} | {minutes}分{seconds}秒 | 经济{m['net_worth']}"
                )
                lines.append(line)

            yield event.plain_result("\n".join(lines))

        except Exception as e:
            logger.error(f"查询出错：{e}")
            yield event.plain_result("网络好像出问题了喵，过会再试试~")