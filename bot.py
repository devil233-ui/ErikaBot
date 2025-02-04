#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入nonebot
import nonebot
# 导入cqhttp协议配置类
from nonebot.adapters.cqhttp import Bot as CQHTTPBot

# Custom your logger
# 
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# 初始化
# You can pass some keyword args config to init function
nonebot.init()
app = nonebot.get_asgi()
driver = nonebot.get_driver()

# 使用协议
driver.register_adapter("cqhttp", CQHTTPBot)

# 加载插件
# nonebot.load_plugin("nonebot_plugin_songpicker2")
nonebot.load_builtin_plugins()
nonebot.load_from_toml("pyproject.toml")

# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...


if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
