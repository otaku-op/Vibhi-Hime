import discord
from discord.ext import commands
import os
import random
from disputils import BotEmbedPaginator
import pyrebase
import json
from decouple import config

links_str="""
[Youtube](https://www.youtube.com/channel/UCq4FMXXgsbsZmw5A-Mr7zSA) , [GitHub](https://GitHub.com/ATCtech) , [Twitter](https://twitter.com/ATC_YT_2014) , [Instagram](https://instagram.com/weebletkun) , [Reddit](https://www.reddit.com/u/TECHIE6023) , [Fiverr](https://fiverr.com/atctech)
[Support Server](https://discord.gg/7cnnXB)
[Vibhi Chan Invite Link](https://discord.com/api/oauth2/authorize?client_id=746984468199374908&permissions=8&scope=bot)
"""


firebase = pyrebase.initialize_app(json.loads(config("FIREBASE")))
db=firebase.database()

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
  
    
    @commands.command()
    async def help(self,ctx):
        global help_str
        rolepl=""
        try:
            d = db.child("RP").child("GIF").get().val()
            for c in d:
                rolepl+=c+" , "
            
            h = discord.Embed(title='Vibhi Chan help',description='need help?',color=0xFF0055)
            h.add_field(name='__ABOUT__',value="Hi I'm Vibhi Chan\nPrefix : ``v!``\nFor custom prefix do `v!prefix`\nDeveloped by : ``weeblet~kun#1193``")
            h.add_field(name='__SUPPORT__',value="If you find any bugs or would like to reccomend a feature [join this server](https://discord.gg/7cnnXB)")
            h.add_field(name='__INVITE__',value="[Invite me to your server (click here)](https://discord.com/api/oauth2/authorize?client_id=746984468199374908&permissions=8&scope=bot)")
            h.add_field(name='__ROLEPLAY__',value=rolepl[:-3])
            h.add_field(name='__FUN__',value='gif , meme , ask , pun , joke')
            h.add_field(name='__ANIME MANGA__',value='anime , manga')
            h.add_field(name='__GAMES__',value='rps')
            h.add_field(name='__UTILITY__',value='wiki , img')
            h.add_field(name='__MUSIC__',value='play , pause , resume , stop , skip , queue , join , shuffle , disconnect , remove')
            h.add_field(name='__MISC__',value='afk , pfp , say , invite , stats , servers , about , prefix')
            h.add_field(name='__MODERATION__',value='announce , dm , clear , ban , unban , kick')
            h.add_field(name='__DEVELOPER LINKS__',value=links_str)
            #await ctx.author.send(embed=h)
            await ctx.send(embed=h)
        except Exception as e:
            print(e)
    

def setup(bot):
    bot.add_cog(Help(bot))
    print('---> HELP LOADED')

