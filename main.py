from discord import Intents
from discord.ext import commands
from discord import Game
from discord import Status
from discord import Object
from dotenv import load_dotenv
import os
import json
import time
import discord as dt
load_dotenv()
token = os.getenv("BOT_TOKEN")
message_log = "./message_log_data.json"
def message_log_data(message_content, message_author, message_channel, message_guild, message_guild_id, message_channel_id, message_author_id, message_content_url, message_created_at):
    with open(message_log, 'r') as file:
        data = json.load(file)
    # data[str(message_guild_id)] = {}
    times = time.time()
    if data.get(str(message_guild_id)) == None:
        data[str(message_guild_id)] = {}
    if data[str(message_guild_id)].get(str(message_author_id)) == None:
        data[str(message_guild_id)][str(message_author_id)] = {}
    data[str(message_guild_id)][str(message_author_id)][str(times)] = {}
    data[str(message_guild_id)][str(message_author_id)][str(times)]['message_content'] = str(message_content)
    data[str(message_guild_id)][str(message_author_id)][str(times)]['message_author'] = str(message_author)
    data[str(message_guild_id)][str(message_author_id)][str(times)]['message_channel'] = str(message_channel)
    data[str(message_guild_id)][str(message_author_id)][str(times)]['message_guild'] = str(message_guild)
    data[str(message_guild_id)][str(message_author_id)][str(times)]['message_guild_id'] = str(message_guild_id)
    data[str(message_guild_id)][str(message_author_id)][str(times)]['message_channel_id'] = str(message_channel_id)
    data[str(message_guild_id)][str(message_author_id)][str(times)]['message_author_id'] = str(message_author_id)
    data[str(message_guild_id)][str(message_author_id)][str(times)]['message_content_url'] = str(message_content_url)
    data[str(message_guild_id)][str(message_author_id)][str(times)]['message_created_at'] = str(message_created_at)
    with open(message_log, 'w') as file:
        json.dump(data, file, indent="\t", ensure_ascii=False)



class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='준섭아 ',
            intents=Intents.all(),
            sync_command=True,
            application_id=1080786159581532160
        )
        self.initial_extension = ["Cogs.button","Cogs.help","Cogs.music_test", "Cogs.user_block", "Cogs.user_chat_list"]

    async def setup_hook(self):
        for ext in self.initial_extension:
            await self.load_extension(ext)
        await bot.tree.sync()

    async def on_message(self, msg):
        message_content = msg.content
        message_author = msg.author.display_name
        try:
            message_channel = msg.channel.name
            message_guild_id = msg.guild.id
        except:
            message_channel = "DM MESSAGE CHANNEL"
            message_guild_id = "UNknown"
        message_guild = msg.guild
        message_channel_id = msg.channel.id
        message_author_id = msg.author.id
        message_content_url = msg.jump_url
        message_created_at = msg.created_at


        message_log_data(message_content, message_author, message_channel, message_guild, message_guild_id, message_channel_id, message_author_id, message_content_url, message_created_at)
        await bot.process_commands(msg)
    async def on_ready(self):
        print("login")
        print(self.user.name)
        print(self.user.id)
        print("===============")
        game = Game("....")
        await self.change_presence(status=Status.online, activity=game)


bot = MyBot()
bot.run(token)
