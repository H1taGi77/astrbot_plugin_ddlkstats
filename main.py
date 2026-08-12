from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("astrbot_plugin_ddlkstats", "H1taGi77", "死锁战绩查询", "0.2.0")
class DdlockstatsPlugin(Star):
    """死锁战绩查询"""

    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("调查")
    async def 调查(self, event: AstrMessageEvent):
        """查询玩家对局历史"""
        yield event.plain_result(f"正在努力调查 {account_id} ，请稍等喵...")