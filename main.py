from discord import Intents
from discord.ext import commands
from discord import Game
from discord import Status
from discord import Object
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("BOT_TOKEN")

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='준섭아 ',
            intents=Intents.all(),
            sync_command=True,
            application_id=1080786159581532160
        )
        self.initial_extension = ["Cogs.button","Cogs.help"]

    async def setup_hook(self):
        for ext in self.initial_extension:
            await self.load_extension(ext)
        await bot.tree.sync(guild=Object(id=1080789358115823637))

    async def on_ready(self):
        print("login")
        print(self.user.name)
        print(self.user.id)
        print("===============")
        game = Game("....")
        await self.change_presence(status=Status.online, activity=game)


bot = MyBot()
bot.run(token)
