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
import os
import time
message_log = "./message_log_data.json"
user_blockss = "./user_block_data.json"
def user_block_data_gamto(server_id,author_id,sayu):
    with open(user_blockss, 'r') as file:
        data333 = json.load(file)
    # data[str(message_guild_id)] = {}
    times = time.time()
    if data333.get(str(server_id)) == None:
        data333[str(server_id)] = {}
    if data333[str(server_id)].get(str(author_id)) == None:
        data333[str(server_id)][str(author_id)] = {}
    data333[str(server_id)][str(author_id)]["sayu"] = sayu
    data333[str(server_id)][str(author_id)]["message"] = {}
    with open(message_log, 'r') as file:
        datass = json.load(file)
    dtss = []
    for datas in datass:
        if not datass[str(datas)].get(str(author_id)) == None:
            # for i in data[str(datass)][str(author_id)]:
            #     dtss.append(i)
            for i in datass[str(datas)][str(author_id)]:
                datassss = datass[str(datas)][str(author_id)][str(i)]
                data333[str(server_id)][str(author_id)]["message"][str(datas)] = {}
                data333[str(server_id)][str(author_id)]["message"][str(datas)][str(author_id)] = datass[str(datas)][str(author_id)]
                data333[str(server_id)][str(author_id)]["message"][str(datas)][str(author_id)][str(i)] = datass[str(datas)][str(author_id)][str(i)]
        with open(user_blockss, 'w') as file:
            json.dump(data333, file, indent="\t", ensure_ascii=False)
load_dotenv()
webhook_url = os.getenv("WEBHOOK_TOKEN_FOR_USER_BLOCK")
import json
data = {}
def reason_of_bans(data):
    global reason_of_ban
    reason_of_ban = data
class user_block(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="유저차단", description="유저를 차단합니다. 명령어를 사용하는 서버에 있는 사람만 가능하며 해당 서버에 관리자만 사용할수 있습니다")
    async def select(self, interaction: discord.Interaction, member: discord.Member) -> None:
        # await interaction.response.send_message(user_block_id)
        # await interaction.response.send_message(member.id)
        # await interaction.response.send_message(member.name)
        # await interaction.response.send_message(member.discriminator)
        if interaction.user.bot == True:
            await interaction.response.send_message("봇은 명령어를 호출할수 없습니다.", ephemeral=True)
            return
        if member.bot == True:
            await interaction.response.send_message("봇을 차단할수 없습니다.", ephemeral=True)
            return
        if interaction.permissions.administrator == True:
            select1to1 = Button(label="예", style=ButtonStyle.primary)
            select1to2 = Button(label="아니오", style=ButtonStyle.danger)
            sayu = Select(options=[
                SelectOption(
                    label="태러",
                    description="연속적인 도배, 욕설, 비속어, 불쾌감을 주는 행위"
                    # emoji="https://tenor.com/view/terror-gif-21007451"
                ),
                SelectOption(
                    label="사기",
                    description="말 그대로 사기를 예기한다 (예: 기프티콘 준다하고 돈만받고 튐)"
                    # emoji="https://tenor.com/view/itsascam-scam-meme-itsafraud-itsahoax-gif-23353011"
                ),
                SelectOption(
                    label="기타",
                    description="위 사유 외의 사유"
                    # emoji="https://tenor.com/view/etc-etc-etc-etcetera-other-option-diy-manual-do-mundo-gif-14323128"
                )
            ])

            async def sayu_callback(interaction: interaction) -> None:
                # await interaction.response.send_message(f"{sayu.values}를 선택하셨습니다.")
                # reason_of_ban = sayu.values[0]
                reason_of_bans(sayu.values[0])
                print(reason_of_ban)
                await interaction.response.send_message(
                    "현제 이서버를 준섭이의 유저 블랙시스트에 등록요청 하시겠습니까?(준섭이의 유저 블랙시스트란 준섭봇 0.3이 등록되어있는 서버에서 블랙리스트에 등록된 유저를 자동 밴시키는 기능입니다)",
                    view=view, ephemeral=True)
            async def select1to1_callback(interaction: Interaction):
                # global reason_of_ban
                # await interaction.response.send_message("감사합니다 해당유저는 밴되었으며 곧 관리자가 블랙리스트 신청을 검토한후 결과를 DM으로 드리겠습니다 감사합니다")
                user_block_data_gamto(interaction.guild.id, member.id, reason_of_ban)
                embed = discord.Embed(title="신고 접수 완료", description="신고 내용 확인")
                embed.add_field(name="신고자 이름", value=interaction.user.display_name, inline=False)
                embed.add_field(name="신고자 아이디", value=interaction.user.id, inline=False)
                embed.add_field(name="신고 대상 이름", value=member.name, inline=False)
                embed.add_field(name="신고 대상 아이디", value=member.id, inline=False)
                embed.add_field(name="서버 이름", value=interaction.guild.name, inline=False)
                embed.add_field(name="서버 아이디", value=interaction.guild.id, inline=False)
                embed.add_field(name="준섭이의 유저 블랙시스트 등록신청 여부", value="True", inline=False)
                embed.add_field(name="신고자 관리자 여부", value=interaction.permissions.administrator, inline=False)
                embed.add_field(name="밴사유", value=reason_of_ban, inline=False)
                embed_detail = discord.Embed(title="신고 접수됨!", description="신고 내용 확인")
                embed_detail.add_field(name="신고자 이름", value=interaction.user.display_name, inline=False)
                embed_detail.add_field(name="신고자 아이디", value=interaction.user.id, inline=False)
                embed_detail.add_field(name="신고 대상 이름", value=member.name, inline=False)
                embed_detail.add_field(name="신고 대상 아이디", value=member.id, inline=False)
                embed_detail.add_field(name="서버 이름", value=interaction.guild.name, inline=False)
                embed_detail.add_field(name="서버 아이디", value=interaction.guild.id, inline=False)
                embed_detail.add_field(name="준섭이의 유저 블랙시스트 등록신청 여부", value="True", inline=False)
                embed_detail.add_field(name="신고자 관리자 여부", value=interaction.permissions.administrator, inline=False)
                embed_detail.add_field(name="밴사유", value=reason_of_ban, inline=False)
                embed_detail.add_field(name="--------------------------------------------", value="", inline=False)
                await interaction.client.get_guild(1081575616610045982).get_channel(1081576115941933096).send(embed=embed)
                await member.send(f"당신은 {interaction.guild.name} 서버에서 밴되었습니다 밴사유 : {reason_of_ban}")
                with open(message_log, 'r') as file:
                    datass = json.load(file)
                dtss = []
                if not datass[str(interaction.guild.id)].get(str(member.id)) == None:
                    for i in datass[str(interaction.guild.id)][str(member.id)]:
                        dtss.append(i)
                    for i in dtss:
                        datassss = datass[str(interaction.guild.id)][str(member.id)][str(i)]
                        embed_detail.add_field(name="채팅 올라온 시간(UTC기준)", value=datassss["message_created_at"],inline=False)
                        embed_detail.add_field(name="채팅 내용", value=datassss["message_content"],inline=False)
                        embed_detail.add_field(name="채팅 올라온 체널", value=datassss["message_channel"], inline=False)
                        embed_detail.add_field(name="채팅 url", value=datassss["message_content_url"], inline=False)
                        embed_detail.add_field(name="--------------------------------------------", value="",
                                               inline=False)
                    await interaction.client.get_guild(1081575616610045982).get_channel(1081586368834183288).send(
                        embed=embed_detail)

                        # print(datass[str(interaction.guild.id)][str(member.id)][str(i)])
                # await interaction.user.send(f"""
                # 안녕하세요 {interaction.user.display_name}님!
                # 저늩 황준섭님의 봇인 준섭봇 0.3이라고 합니다
                # 다름이 아니라 {interaction.user.display_name}님이 밴하신 {member.name}에 대해 몆가지 여쭤볼게 있어
                # """)
                # await member.ban(self, reason_of_ban)
                await interaction.guild.ban(member)
                await interaction.response.send_message("감사합니다 해당유저는 밴되었으며 곧 관리자가 블랙리스트 신청을 검토한후 결과를 DM으로 드리겠습니다 감사합니다", embed=embed, ephemeral=True)
                # print(interaction.user.id)
                # print(interaction.user.display_name)
                # print(interaction.permissions.administrator)
                # print(interaction.user.bot)
                # print(interaction.user.discriminator)
                # print(interaction.guild.id)
                # print(interaction.guild.name)
                #
                # print(discord.Guild.name)
                # print(member.id)
                # print(member.name)
                # # print(ctx.guild_id)
                # # print(Interaction.user.bot)
                # print(discord.Permissions.administrator)
                # # print(Interaction.app_permissions.administrator)
                # print(discord.User.display_name)
                # print(discord.User.discriminator)
                # print(discord.User.id)
            async def select1to2_callback(interaction: Interaction):
                # global reason_of_ban
                embed = discord.Embed(title="신고 접수 완료", description="신고 내용 확인")
                embed.add_field(name="신고자 이름", value=interaction.user.display_name, inline=False)
                embed.add_field(name="신고자 아이디", value=interaction.user.id, inline=False)
                embed.add_field(name="신고 대상 이름", value=member.name, inline=False)
                embed.add_field(name="신고 대상 아이디", value=member.id, inline=False)
                embed.add_field(name="서버 이름", value=interaction.guild.name, inline=False)
                embed.add_field(name="서버 아이디", value=interaction.guild.id, inline=False)
                embed.add_field(name="준섭이의 유저 블랙시스트 등록신청 여부", value="False", inline=False)
                embed.add_field(name="신고자 관리자 여부", value=interaction.permissions.administrator, inline=False)
                embed.add_field(name="밴사유", value=reason_of_ban, inline=False)
                await interaction.client.get_guild(1081575616610045982).get_channel(1081576115941933096).send(
                    embed=embed)
                await member.send(f"당신은 {interaction.guild.name} 서버에서 밴되었습니다 밴사유 : {reason_of_ban}")
                await interaction.response.send_message("감사합니다 해단유저는 밴되었습니다 감사합니다", embed=embed, ephemeral=True)
                await interaction.guild.ban(member)
            sayu.callback = sayu_callback
            select1to1.callback = select1to1_callback
            select1to2.callback = select1to2_callback
            view = View()
            sayu_view = View()
            view.add_item(select1to1)
            view.add_item(select1to2)
            sayu_view.add_item(sayu)
            await interaction.response.send_message("밴 사유를 선택하주세요.", view=sayu_view, ephemeral=True)
            # await interaction.response.send_message("현제 이서버를 준섭이의 유저 블랙시스트에 등록요청 하시겠습니까?(준섭이의 유저 블랙시스트란 준섭봇 0.3이 등록되어있는 서버에서 블랙리스트에 등록된 유저를 자동 밴시키는 기능입니다)", view=view, ephemeral=True)
        else:
            await interaction.response.send_message("관리자가 아닙니다", ephemeral=True)
        # await ctx.send(user_block_id)
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(user_block(bot))