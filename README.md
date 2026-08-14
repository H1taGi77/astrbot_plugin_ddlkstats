# astrbot-plugin-ddlkstats

Deadlock 战绩查询插件

## 功能
- `/调查 <Steam ID>` — 查询最近 5 场战绩（英雄 / KDA / 胜负 / 时长 / 经济）
- `/调查`（不带 ID）— 自动使用绑定的账号查询
- `/绑定 <Steam ID>` — 绑定 Steam 账号，之后可免 ID 查询（持久化存储）

## 安装
1. 将本插件放入 AstrBot 的 `data/plugins` 目录
2. 重启 AstrBot

## 配置
本插件暂无配置项

## 使用示例
指令：/调查 <Steam ID>
示例输出：
```
/调查 7656119xxxxxxxxxx

正在努力调查 7656119xxxxxxxxxx ，请稍等喵…

»「 08-13 17:05 Wraith
　　5 / 8 / 9 败北😭
　　44 分 4 秒 经济 46237 」
»「 08-13 16:11 Lady Geist
　　3 / 2 / 18 得胜😍
　　48 分 18 秒 经济 52240 」
»「 08-13 15:31 Paige
　　2 / 5 / 10 败北😭
　　30 分 7 秒 经济 25720 」
»「 08-13 14:45 Lady Geist
　　1 / 4 / 18 得胜😍
　　42 分 40 秒 经济 45284 」
»「 08-11 22:10 Wraith
　　7 / 0 / 13 得胜😍
　　36 分 44 秒 经济 49065 」
```

## 说明
- 数据来源：deadlock-api.com（免费，无需配置）
- 作者：H1taGi77
- 仓库：https://github.com/H1taGi77/astrbot_plugin_ddlkstats