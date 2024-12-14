import time
from aiogram.fsm.context import FSMContext
import asyncio
import requests
from aiogram.types import Message, BotCommand, BotCommandScopeDefault
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, F, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import datetime

# 747, "DozDmmNEQpqDqCGfGnLDDDswOUeKnCwUVFuZedsY"

statusNotification = False


def GetEmission(region, AppToken):
    url = f"https://eapi.stalcraft.net/{region}/emission"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AppToken}"
    }
    response = requests.request("GET", url, headers=headers)
    return response.json()


def getTime():
    date = datetime.datetime.now()
    return f"{date.year}-{date.month}-{date.day}T{int(date.hour) - 3}:{date.minute}:{date.second}Z"


async def StopHandler(msg: Message, bot: Bot):
    global statusNotification
    if statusNotification:
        await msg.answer(text="Stop notification")
        statusNotification = False
    else:
        await msg.answer(text="Notification is stop")


async def StartHandler(msg: Message, bot: Bot):
    global statusNotification
    if statusNotification:
        await msg.answer(text="Notification is started")
    else:
        await msg.answer(text="Start notification")
        statusNotification = True
    while statusNotification:
        if GetEmission("ru",
                       "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI3NDciLCJqdGkiOiJhZDZjMGI2MDQwYzc3NTA4MzZkZTg5NjE1NGI1MTQ2MDNjMjQ1NmE0OTdhMWUwYTdkYTIwMmRjOGRkZWRlMGJlODY5NGRmMmQ5NmVkNjVjYiIsImlhdCI6MTczNDA5MDMzNS44MTY5NTQsIm5iZiI6MTczNDA5MDMzNS44MTY5NTcsImV4cCI6MTc2NTYyNjMzNS42MTQ4MDcsInN1YiI6IiIsInNjb3BlcyI6W119.WmTDtKrBkWlo7AwN0Wegb3H5Qit0TFxfhPQcpPHBVZJ764RhhKwbPR6FsU9i1_dxXD6OXdP4WeRHRAEPLMcdvq8AE4s7zJTVPhwLHAt2_69P2r4UYiO6fieItWMiuN2UHsLw24XM1y5FH-7jtUzan-uFDL-2a9CvwGiv_FNYm1_MWg4pDCvMD5BF7xhoVpd86bjb8nD99mJf6_dqpELTA5RKFD0EPWdgd0-z_2ARhporba55jGttNLgK7_Fd_n_HUuNYQ0ao4YkYivYNf5kiLp9fT5T8cLSDhJ-0jHQI43oELM9wv257cYWlySE67-7Addj0KvWeja1hhFe-0vb8tXXqGuHkN2Zci1E0b3iZezNrdwQkzPiPoFTiVPK8EoZBCz9HrmKmAI2sg3wvBWbSP4jzrR5YZh7N-eKx2gItCkJYpRv939cy1Q1JCEpdvp983sqjqpdGYoH0VY8tuWyA1ColPc-FtuzOmW-f9jwJJtyO2tUAnwxQeylNhQzrD9tbOtN6s9edUVciGDtNXJlygVO1I5kZb-51FICjmX3YFAvYEtiLH2OSDB4ksNvC1dkKvuZsIAONz_bP7xS6O9Hr6mXOahpqsM4I_vI0knwAJb9Oc9SN9io7blXeKe89Q7vk9FPNW1uxHaPFDHfRnC0g4bhoTbV2FaJECIPNKXUNjmU")[
            "previousStart"] == getTime():
            await msg.answer(text="Выброс начинается")
        elif GetEmission("ru",
                         "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI3NDciLCJqdGkiOiJhZDZjMGI2MDQwYzc3NTA4MzZkZTg5NjE1NGI1MTQ2MDNjMjQ1NmE0OTdhMWUwYTdkYTIwMmRjOGRkZWRlMGJlODY5NGRmMmQ5NmVkNjVjYiIsImlhdCI6MTczNDA5MDMzNS44MTY5NTQsIm5iZiI6MTczNDA5MDMzNS44MTY5NTcsImV4cCI6MTc2NTYyNjMzNS42MTQ4MDcsInN1YiI6IiIsInNjb3BlcyI6W119.WmTDtKrBkWlo7AwN0Wegb3H5Qit0TFxfhPQcpPHBVZJ764RhhKwbPR6FsU9i1_dxXD6OXdP4WeRHRAEPLMcdvq8AE4s7zJTVPhwLHAt2_69P2r4UYiO6fieItWMiuN2UHsLw24XM1y5FH-7jtUzan-uFDL-2a9CvwGiv_FNYm1_MWg4pDCvMD5BF7xhoVpd86bjb8nD99mJf6_dqpELTA5RKFD0EPWdgd0-z_2ARhporba55jGttNLgK7_Fd_n_HUuNYQ0ao4YkYivYNf5kiLp9fT5T8cLSDhJ-0jHQI43oELM9wv257cYWlySE67-7Addj0KvWeja1hhFe-0vb8tXXqGuHkN2Zci1E0b3iZezNrdwQkzPiPoFTiVPK8EoZBCz9HrmKmAI2sg3wvBWbSP4jzrR5YZh7N-eKx2gItCkJYpRv939cy1Q1JCEpdvp983sqjqpdGYoH0VY8tuWyA1ColPc-FtuzOmW-f9jwJJtyO2tUAnwxQeylNhQzrD9tbOtN6s9edUVciGDtNXJlygVO1I5kZb-51FICjmX3YFAvYEtiLH2OSDB4ksNvC1dkKvuZsIAONz_bP7xS6O9Hr6mXOahpqsM4I_vI0knwAJb9Oc9SN9io7blXeKe89Q7vk9FPNW1uxHaPFDHfRnC0g4bhoTbV2FaJECIPNKXUNjmU")[
            "previousEnd"] == getTime():
            await msg.answer(text="Выброс закончился")
        await asyncio.sleep(10)


async def start():
    bot = Bot(token="7852420519:AAHGVGHDpZgGgDJRHO_HYnd1_mFYHZot3YI")
    dp = Dispatcher()
    dp.message.register(StartHandler, Command(commands=["StartNotification"]))
    dp.message.register(StopHandler, Command(commands=["StopNotification"]))
    try:
        await dp.start_polling(bot)
    finally:
        await  bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
