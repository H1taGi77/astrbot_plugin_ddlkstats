from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

import aiohttp
import json
import datetime

@register("astrbot_plugin_ddlkstats", "H1taGi77", "死锁战绩查询", "v0.3.1")
class DdlockstatsPlugin(Star):
    """死锁战绩查询"""

    def __init__(self, context: Context):
        super().__init__(context)

    # ===== Steam账号绑定 =====
    @filter.command("绑定")
    async def 绑定(self, event: AstrMessageEvent,steam_id:str):
        """将 Steam 账号与 QQ 号绑定"""
        if len(steam_id) != 17 and not steam_id.isdigit():
            yield event.plain_result("喵啊啊！你都输入了些什么喵！乱七八糟的！Steam ID 是 17 位的纯数字！")
            return
        if len(steam_id) != 17:
            yield event.plain_result("检查一下 Steam ID 是不是搞错了喵")
            yield event.plain_result("Steam ID 是 17 位哦")
            return
        if not steam_id.isdigit():
            yield event.plain_result("检查一下 Steam ID 是不是搞错了喵")
            yield event.plain_result("Steam ID 是纯数字哦，不要混进去那么多乱七八糟的东西啦——")
            return
        qq_id = event.get_sender_id()
        binds = await self.get_kv_data("binds", {})
        binds[qq_id] = steam_id
        await self.put_kv_data("binds",binds)
        yield event.plain_result("成功绑住（划掉(*/ω＼*）），成功绑定了喵！")

    # ===== 调查命令 =====
    # ----- 最近场次查询命令 -----
    @filter.command("调查")
    async def 调查(self, event: AstrMessageEvent,steam_id:str = ""):
        """查询玩家对局历史"""

        if steam_id == "":
            binds = await self.get_kv_data("binds",{})
            sender = event.get_sender_id()
            bound = binds.get(sender)
            steam_id = bound
            if bound is None:
                yield event.plain_result("这个账号下没找到 Steam ID喵~ 先使用 /绑定 <Steam ID> 绑定账号呗")
                return

        yield event.plain_result(f"正在努力调查 {steam_id} ，请稍等喵...")

        mh_url = f"https://api.deadlock-api.com/v1/players/{steam_id}/match-history"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(mh_url) as resp:
                    if resp.status !=200:
                        yield event.plain_result(f"查不到喵......只有几个奇怪的数字（HTTP {resp.status}）")
                        return

                    matches = await resp.json()

            if not matches:
                yield event.plain_result("这个账号空空的喵")
                return

            # ----- 角色名称映射 -----
            #角色映射api查询
            heros_url = "https://api.deadlock-api.com/v1/assets/heroes"
            async with aiohttp.ClientSession() as session:
                async with session.get(heros_url) as resp:
                    heros = await resp.json()
                    
                #角色映射对应
                heros_list = {} 
                for h in heros:
                    hid = h['id']
                    hname = h['name']
                    heros_list[hid] = hname

            # ----- 场次查询 -----
            matches_lines = []
            for m in matches[:5]:
                minutes = m["match_duration_s"] // 60
                seconds = m["match_duration_s"] % 60

                #场次胜负映射
                if m["player_team"] == m["match_result"]:
                    win = "得胜😍"
                else:
                    win = "败北😭"

                # 时间戳转换
                time_obj = datetime.datetime.fromtimestamp(m["start_time"])
                date = time_obj.strftime("%m-%d %H:%M")

                # 英雄名称转换
                player_hero = heros_list.get(m['hero_id'])

                # 最近场次数据格式
                match_line = (
                    f"»「 {date} {player_hero}\n"
                    f"　　{m['player_kills']} / {m['player_deaths']} / {m['player_assists']}　　{win}\n"
                    f"　　{minutes} 分 {seconds} 秒 经济 {m['net_worth']} 」"
                )
                matches_lines.append(match_line)

            yield event.plain_result("\n".join(matches_lines))

        except Exception as e:
            logger.error(f"查询出错：{e}")
            yield event.plain_result("网络好像出问题了喵，过会再试试~")