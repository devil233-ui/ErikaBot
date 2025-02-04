import nonebot
import re
from nonebot import on_command,on_regex,on_notice
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Message,MessageSegment,GroupIncreaseNoticeEvent
from nonebot.permission import SUPERUSER
from nonebot.log import logger
from nonebot import require
import random
import datetime 

global time_task

time_task = []
time_task.append(('2022考研',datetime.date(2021,12,25)))
time_task.append(('2022上英语六级',datetime.date(2022,6,12)))
# time_task.append(('科A复兴祭CP29',datetime.date(2021,12,11)))
time_task.append(('大年夜/春假',datetime.date(2022,1,31)))
time_task.append(('亲戚催婚',datetime.date(2022,2,1)))
time_task.append(('老头环',datetime.date(2022,2,25)))
time_task.append(('FF14 6.0',datetime.date(2022,3,16)))
time_task.append(('2022高考',datetime.date(2022,6,7)))
time_task.append(('2023考研',datetime.date(2022,12,25)))

groups = ["904517835","729901771","757530435"]

async def CallDays()->str:
	msg = '小胶布提醒你，你剩下的时间不多了~\n-----------\n'
	today = datetime.date.today()
	for time in time_task:
		msg += '距离['+time[0]+']还有['+str((time[1]-today).days)+'天]\n'
	msg += '-----------'
	return msg

HowManyDays = on_command("倒计时",aliases=set(['考研倒计时','考研时间','考试']), priority=2)
@HowManyDays.handle()
async def handle(bot: Bot, event: Event, state: T_State):
	msg = await CallDays()
	await HowManyDays.finish(Message(msg))

# 请求定时任务对象scheduler   
scheduler = require('nonebot_plugin_apscheduler').scheduler
@scheduler.scheduled_job('cron', 
						hour=8, minute=00, second=0,
						timezone='Asia/Shanghai',
						id='call_days')
async def AutoCallDays():
	msg = await CallDays()
	if not msg:
		return
	msg += '\n本消息自动发送，当前时间为：8:00 AM'
	(schedBot,) = nonebot.get_bots().values()
	for group in groups:
		await schedBot.call_api('send_msg',**{
                    			'message':msg,
                        		'group_id':group
                				})

@scheduler.scheduled_job('cron',hour=19, minute=00, second=0,
						timezone='Asia/Shanghai',id='call_umiko')
async def CallUmiko():
	msg = "[CQ:at,qq=1366108600] 该海猫了"
	(schedBot,) = nonebot.get_bots().values()
	await schedBot.call_api('send_msg',**{
                			'message':msg,
                    		'group_id':"757530435"
            				})

AddDays = on_command("add 倒计时",priority=2)
@AddDays.handle()
async def handle(bot: Bot, event: Event, state: T_State):
	args = str(event.get_message()).strip()
	if args:
		state["args"] = args
@AddDays.got("args",prompt="？")
async def got(bot: Bot, event: Event, state: T_State):
	args = re.findall("([\u4E00-\u9FA5A-Za-z0-9_]+)，(\d{4}-\d{1,2}-\d{1,2})",state["args"])[0]
	name = args[0]
	date = args[1]
	# print(args)
	await AddDays.finish(Message("开发中……"))
