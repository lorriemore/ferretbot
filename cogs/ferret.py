from discord import File
from discord.ext import commands

class Ferret(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        author = ctx.author
        await ctx.reply(f'Hello, {author.mention}!')
    
    @commands.command()
    async def ferret(self, ctx):
        f = open("./src/Ferret_in_a_hat.jpg", "rb")
        img = File(f)
        await ctx.reply(file=img)

async def setup(bot):
    await bot.add_cog(Ferret(bot))
