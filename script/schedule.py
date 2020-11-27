import asyncio

import nonebot

from script import config


async def getlist():
    nonebot.init(config)
    bot = nonebot.get_bot()
    info =''
    try:
        info = await bot.get_group_list()
    except Exception as e:
        pass
    print(info)
    return info


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getlist())
    loop.close()
