# astrbot-plugin-ddlkstats

Deadlock 战绩查询插件

## 功能

- `/调查 &lt;玩家名&gt;` — 查询玩家对局历史（基于 deadlock-api.com，无需配置）
- 高级分析：PP Score、段位徽章、MVP 评分（基于 statlocker.gg，需配置 API key）

## 安装

1. 将本插件放入 AstrBot 的 `data/plugins` 目录
2. 重启 AstrBot

## 配置

在 AstrBot WebUI → 插件配置中填写：

- `statlocker_api_key`：你的 Statlocker API key（可选，留空则只使用基础查询）

申请地址：https://statlocker.gg/api

## 使用示例
