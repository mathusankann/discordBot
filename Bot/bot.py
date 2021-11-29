# bot.py
import os
import discord
import LeagueOfLegends

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = '!'
client = discord.Client()
# Map with every function
# adding function by example :
# 'find_summoner': LeagueOfLegends.find_summoner, 'new_function': function_to_be_called


functionDict = {'!findsummoner': LeagueOfLegends.find_summoner,
                '!findclashteam': LeagueOfLegends.find_clash_team_by_summoner

                }


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # incMessage should be like this Prefix Command Keyword
    inc_message = message.content.split()
    if inc_message[0][0] == '!' and len(inc_message) > 1:
        try:
            response_text = functionDict[inc_message[0]](inc_message[1])
        except KeyError:
            response_text = "unknown command"
        await message.channel.send(response_text)


client.run(TOKEN)


