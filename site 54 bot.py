import discord,asyncio
from discord.ext import commands
from discord.ext.commands import cooldown,BucketType,MemberConverter
from discord import User
from math import *
from datetime import datetime
from discord.client import Client#0163 7934
def startswith(self,data):return self.removeprefix(data)==self#2494 6903#4619 5165
bot=commands.Bot(command_prefix="sb ")#3205 6416
@bot.event
async def on_ready():print('ready')
@bot.event
async def on_member_join(member):await int(926557725188571166).send(f'{str(member.user)}  had joined')
@bot.event#8095 5306
async def on_message(msg):#8027 5090
    if not msg.author.id==930000443017429032:#4361 3746
        if msg.channel.id==943143600181624872 or'nigger'in msg.content.lower().replace(' ','').replace('_','').replace('*','')or'faggot'in msg.content.lower().replace(' ','').replace('_','').replace('*','')or'nigga'in msg.content.lower().replace(' ','').replace('_','').replace('*',''):await msg.delete()
        else:
            if'930000443017429032'in msg.content:await msg.channel.send('wassup bro')
            if'<:troll:943146567181938768>'in msg.content:await msg.channel.send('<:troll:943146567181938768>')
            if'21'in msg.content.lower():await msg.channel.send('you stupid')
            if msg.content.lower().startswith('im ')or msg.content.lower().startswith("i'm "):await msg.channel.send("hi "+msg.content.replace('im ','').replace("i'm ",'')+', im dad <:troll:943146567181938768>')#1921 1113
            elif msg.content.lower().startswith('sb help'):await msg.channel.send("deal with it lol.")
            elif msg.content.lower().startswith('sb ban ')and msg.author.mention==discord.Permissions.administrator:await bot.fetch_user(int(msg.content.lower().removeprefix("sb ban <@!").removesuffix('>'))).ban(reason='idk')
            elif msg.content.startswith('sb convert bin '):
                try:await msg.channel.send(str(bin(int(msg.content.removeprefix('sb convert bin ')))).removeprefix('0b'))
                except:
                    result=''
                    for i in msg.content.removeprefix('sb convert bin '):result+=bin(ord(i))
                    await msg.channel.send(result.replace('0b',''))
            elif msg.content.lower().startswith('sb calc '):
                if'exit'in msg.content or'guilds'in msg.content or'exec'in msg.content or'open'in msg.content or'close'in msg.content or'eval'in msg.content:await msg.channel.send('dont try injecting me retard')
                elif msg.content.lower().startswith('sb calc 10+9')or msg.content.lower().startswith('sb calc 9+10'):await msg.channel.send('21')
                else:
                    try:
                        x=eval(msg.content.removeprefix('sb calc ').removeprefix('Sb calc ').replace('^','**'))
                        if'nigger'in x or'faggot'in x or'nigga'in x:await msg.channel.send('mf tries making me say shit')
                        else:await msg.channel.send(x)
                    except Exception as e:await msg.channel.send(e)
bot.run('OTMwMDAwNDQzMDE3NDI5MDMy.YdvgaA.P1EMZkXmpfc_nVYBwMBqB5z9iPw')
