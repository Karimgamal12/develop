import asyncio
from pyrogram import Client,filters,enums,idle
from config import *
from asyncio import get_event_loop
from autoname import main as name

async def main():
  await app.start()
  await bot.start()
  try :
    await app.join_chat("Software_codes")
    await app.join_chat("P_PP_Pi")
  except :
    pass
  await name()
  await idle()
  


loop = get_event_loop()
loop.run_until_complete(main())
