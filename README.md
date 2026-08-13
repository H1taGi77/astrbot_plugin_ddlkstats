# astrbot-plugin-ddlkstats

Deadlock 战绩查询插件

## 功能
- `/调查` — 查询玩家对局历史（基于 deadlock-api.com，无需配置）

## 安装
1. 将本插件放入 AstrBot 的 `data/plugins` 目录
2. 重启 AstrBot

## 配置
本插件暂无配置项

## 使用示例
指令：/调查 <account_id>
示例输出：
```
/调查 7656119xxxxxxxxxx

正在努力调查 7656119xxxxxxxxxx ，请稍等喵…

08-11 22:10 | Wraith | 7/0/13 | 得胜😍 | 36分44秒 | 经济49065
08-11 21:21 | Wraith | 9/3/17 | 得胜😍 | 43分10秒 | 经济54689
08-11 20:43 | Lady Geist | 11/5/15 | 得胜😍 | 35分25秒 | 经济41523
08-11 19:52 | Lady Geist | 1/7/10 | 败北😭 | 48分53秒 | 经济56869
08-11 16:53 | Paige | 3/2/19 | 得胜😍 | 32分44秒 | 经济34542
```

## 说明
- 数据来源：
- 数据来源：deadlock-api.com（免费，无需配置）
- 作者：H1taGi77
- 仓库：https://github.com/H1taGi77/astrbot_plugin_ddlkstats