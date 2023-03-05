from discord import Interaction, SelectOption, app_commands, Object
import discord
from discord.ext import commands
from discord.ui import View, Select
from discord import app_commands, Interaction, Object
from discord.ext import commands
from discord.ui import Button, View
from discord import ButtonStyle
from discord_webhook import DiscordWebhook
from dotenv import load_dotenv
import json
import os
message_log = "./message_log_data.json"

class user_chat_list(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    @app_commands.command(name="유저챗_불러오기", description="준?섭(봇 계발자)만 사용할수 있는 특별한기능 특정 유저에 모든 쳇 기록을 가져온다")
    async def select(self, interaction: discord.Interaction, member: discord.Member) -> None:
        if not interaction.user.id == 709390388728954960:
            await interaction.response.send_message("해당 명령어는 준?섭(봇 계발자)만 사용할수 있습니다", ephemeral=True)
            return
        with open(message_log, 'r') as file:
            data = json.load(file)

        # embed.add_field(name="", value="", inline=False)
        # embed.add_field(name="유저 이름", value="", inline=False)
        dtss = []
        dtsss = []
        # async for msg in interaction.client.logs_from(channel):
        #     await interaction.client.delete_message(msg)
        # await interaction.response.send_message("채널로 전송중..........", ephemeral=True)
        async def yess(interaction: Interaction):
            embed = discord.Embed(title="유저 챗 리스트", description="")
            embed.add_field(name="----------------------", value="", inline=False)
            await interaction.response.send_message("알겠습니다. 전송채널 전채삭제밎 기록전송을 시작합니다 좀 시간이 소요될수 있습니다", ephemeral=True)
            await interaction.client.get_guild(1081575616610045982).get_channel(1081913176322490398).purge(limit=100000)
            await interaction.client.get_guild(1081575616610045982).get_channel(1081913176322490398).send(embed=embed)
            for datas in data:
                # print(datas)
                # print(data)
                if not data[str(datas)].get(str(member.id)) == None:
                    for i in data[str(datas)][str(member.id)]:
                        # print(i)
                        # print(data[str(datas)][str(member.id)][i])
                        # print("무야호")
                        user_name = data[str(datas)][str(member.id)][i]["message_author"]
                        user_id = data[str(datas)][str(member.id)][i]["message_author_id"]
                        dtss.append(i)
                        dtsss.append(data[str(datas)][str(member.id)][i])
                        embed = discord.Embed(title="유저 챗 리스트", description="")
                        embed.add_field(name="유저 이름", value=user_name, inline=False)
                        embed.add_field(name="유저 ID", value=user_id, inline=False)
                        embed.add_field(name="서버", value=data[str(datas)][str(member.id)][i]["message_guild"], inline=False)
                        embed.add_field(name="서버 ID", value=data[str(datas)][str(member.id)][i]["message_guild_id"], inline=False)
                        embed.add_field(name="채팅 올라온 시간(UTC기준)", value=data[str(datas)][str(member.id)][i]["message_created_at"], inline=False)
                        embed.add_field(name="채팅 내용", value=data[str(datas)][str(member.id)][i]["message_content"], inline=False)
                        embed.add_field(name="채팅 올라온 체널", value=data[str(datas)][str(member.id)][i]["message_channel"], inline=False)
                        embed.add_field(name="채팅 올라온 체널 ID", value=data[str(datas)][str(member.id)][i]["message_channel_id"], inline=False)
                        embed.add_field(name="채팅 url", value=data[str(datas)][str(member.id)][i]["message_content_url"], inline=False)
                        embed.add_field(name="--------------------------------------------", value="",
                                               inline=False)

                        await interaction.client.get_guild(1081575616610045982).get_channel(1081913176322490398).send(
                            embed=embed)

        async def noo(interaction: Interaction):
            embed = discord.Embed(title="유저 챗 리스트", description="")
            embed.add_field(name="----------------------", value="", inline=False)
            await interaction.response.send_message("알겠습니다. 전송채널 기록전송을 시작합니다 좀 시간이 소요될수 있습니다", ephemeral=True)
            await interaction.client.get_guild(1081575616610045982).get_channel(1081913176322490398).send(
                embed=embed)
            for datas in data:
                # print(datas)
                # print(data)
                if not data[str(datas)].get(str(member.id)) == None:
                    for i in data[str(datas)][str(member.id)]:
                        # print(i)
                        # print(data[str(datas)][str(member.id)][i])
                        # print("무야호")
                        user_name = data[str(datas)][str(member.id)][i]["message_author"]
                        user_id = data[str(datas)][str(member.id)][i]["message_author_id"]
                        dtss.append(i)
                        dtsss.append(data[str(datas)][str(member.id)][i])
                        embed = discord.Embed(title="유저 챗 리스트", description="")
                        embed.add_field(name="유저 이름", value=user_name, inline=False)
                        embed.add_field(name="유저 ID", value=user_id, inline=False)
                        embed.add_field(name="서버", value=data[str(datas)][str(member.id)][i]["message_guild"],
                                        inline=False)
                        embed.add_field(name="서버 ID",
                                        value=data[str(datas)][str(member.id)][i]["message_guild_id"],
                                        inline=False)
                        embed.add_field(name="채팅 올라온 시간(UTC기준)",
                                        value=data[str(datas)][str(member.id)][i]["message_created_at"],
                                        inline=False)
                        embed.add_field(name="채팅 내용",
                                        value=data[str(datas)][str(member.id)][i]["message_content"],
                                        inline=False)
                        embed.add_field(name="채팅 올라온 체널",
                                        value=data[str(datas)][str(member.id)][i]["message_channel"],
                                        inline=False)
                        embed.add_field(name="채팅 올라온 체널 ID",
                                        value=data[str(datas)][str(member.id)][i]["message_channel_id"],
                                        inline=False)
                        embed.add_field(name="채팅 url",
                                        value=data[str(datas)][str(member.id)][i]["message_content_url"],
                                        inline=False)
                        embed.add_field(name="--------------------------------------------", value="",
                                        inline=False)

                        await interaction.client.get_guild(1081575616610045982).get_channel(
                            1081913176322490398).send(
                            embed=embed)
        yes = Button(label="에", style=ButtonStyle.primary)
        no = Button(label="아니요", style=ButtonStyle.danger)
        yes.callback = yess
        no.callback = noo
        view = View()
        view.add_item(yes)
        view.add_item(no)
        await interaction.response.send_message("기록 전용 채팅창의 매새지를 모두 지운후 전송을 시작하기겠습니까?", view=view, ephemeral=True)
                # embed.add_field(name="유저 이름", value=user_name, inline=False)
                # embed.add_field(name="유저 ID", value=user_id, inline=False)
                # embed.add_field(name="----------------------", value="", inline=False)
                # for i in dtsss:
                #     datassss = i
                #     embed.add_field(name="서버", value=datassss["message_guild"], inline=False)
                #     embed.add_field(name="서버 ID", value=datassss["message_guild_id"], inline=False)
                #     embed.add_field(name="채팅 올라온 시간(UTC기준)", value=datassss["message_created_at"], inline=False)
                #     embed.add_field(name="채팅 내용", value=datassss["message_content"], inline=False)
                #     embed.add_field(name="채팅 올라온 체널", value=datassss["message_channel"], inline=False)
                #     embed.add_field(name="채팅 올라온 체널 ID", value=datassss["message_channel_id"], inline=False)
                #     embed.add_field(name="채팅 url", value=datassss["message_content_url"], inline=False)
                #     embed.add_field(name="--------------------------------------------", value="",
                #                            inline=False)
        # await interaction.response.send_message("불러오기 성공!",
        #                                         embed=embed, ephemeral=True)
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(user_chat_list(bot))