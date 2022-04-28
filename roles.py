from discord_slash import SlashCommand
from discord.ext import commands  
import discord
import csv
import time

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = "!",case_insensitive=True, intents=intents)
slash = SlashCommand(bot,sync_commands=True)



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@slash.slash(name='getcsvlist',description='Get CSV list of users for mentioned role without BOTS')
async def getcsvlist(ctx,role): 

    if role!="@everyone":

        toBeRemoved=['!','@','<','>','&']
        roleIDTemp=''
        
        for letter in role:
            if letter not in toBeRemoved:
                roleIDTemp+=letter
        
        roleID=int(roleIDTemp)
        
        f = open('{}.csv'.format(roleIDTemp), 'w')
        writer = csv.writer(f)

        for guild in bot.guilds:
            if guild.id==ctx.guild.id:
                for member in guild.members:
                    if member.bot==False: 
                        for role in member.roles:
                            if role.id==roleID:
                                writer.writerow(str(member).splitlines())

        f.close()
        
        time.sleep(0.1)

        await ctx.reply(file=discord.File('{}.csv'.format(roleIDTemp)))

    else:
        f = open('everyone.csv', 'w')
        writer = csv.writer(f)
        for guild in bot.guilds:
            if guild.id==ctx.guild.id:
                for member in guild.members:
                    if member.bot==False: 
                        writer.writerow(str(member).splitlines())

        f.close()
        
        time.sleep(0.1)

        await ctx.reply(file=discord.File('everyone.csv'))



@slash.slash(name='getcsvlistwithbot',description='Get CSV list of users for mentioned role with BOTS')
async def getcsvlistwithbot(ctx,role): 

    if role!="@everyone":

        toBeRemoved=['!','@','<','>','&']
        roleIDTemp=''
        
        for letter in role:
            if letter not in toBeRemoved:
                roleIDTemp+=letter
        
        roleID=int(roleIDTemp)
        
        f = open('{}.csv'.format(roleIDTemp), 'w')
        writer = csv.writer(f)

        for guild in bot.guilds:
            if guild.id==ctx.guild.id:
                for member in guild.members:
                    for role in member.roles:
                        if role.id==roleID:
                            writer.writerow(str(member).splitlines())

        f.close()
        
        time.sleep(0.1)

        await ctx.reply(file=discord.File('{}.csv'.format(roleIDTemp)))

    else:
        f = open('everyone.csv', 'w')
        writer = csv.writer(f)
        for guild in bot.guilds:
            if guild.id==ctx.guild.id:
                for member in guild.members:
                    writer.writerow(str(member).splitlines())

        f.close()
        
        time.sleep(0.1)

        await ctx.reply(file=discord.File('everyone.csv'))


bot.run("YOUR_BOT_TOKEN")
