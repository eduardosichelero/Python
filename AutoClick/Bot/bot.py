import pyautogui as bot

bot.press("win")



games = bot.write("league of legends")
bot.press("enter")
games()

bot.PAUSE = 2
tools = bot.write("discord") 
bot.press("enter")
tools()