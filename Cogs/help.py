from discord import Interaction, SelectOption, app_commands, Object
from discord.ext import commands
from discord.ui import View, Select


class select(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="help")
    async def select(self, interaction: Interaction) -> None:
        big_catagori = Select(options=[
            SelectOption(
                label="준비중",
                description="준비중이니 기다리슈",
                emoji="👌"
            )
            # SelectOption(
            #     label="태스트 2번",
            #     description="2번",
            #     emoji="😐"
            # )
        ])
        selects2 = Select(options=[
            SelectOption(
                label="태스트 22",
                description="1번 22 ",
                emoji="👌"
            ),
            SelectOption(
                label="태스트 2번 22 ",
                description="2번 22",
                emoji="😐"
            )
        ])

        async def select_callback(interaction: interaction) -> None:
            await interaction.response.send_message(f"{big_catagori.values}를 선택하셨습니다.")
            # if big_catagori.values[0] == "태스트":
            #     # await interaction.response.send_message("1번을 선택하셨습니다.")
            #     selects2.callback = select_callback
            #     view2 = View()
            #     view2.add_item(big_catagori)
            #     await interaction.response.send_message("무엇을 원하십니까? 2.", view=view2)

        big_catagori.callback = select_callback
        view = View()
        view.add_item(big_catagori)
        await interaction.response.send_message("무엇을 원하십니까?.", view=view)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        select(bot))