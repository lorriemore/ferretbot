import os
from discord import TextChannel
from discord.ext import commands
from dotenv import load_dotenv


class Lorrie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        load_dotenv()
        self.lorrie_id = int(os.getenv('LORRIE_DISCORD_ID'))

    async def cog_check(self, ctx):
        is_lorrie = ctx.author.id == self.lorrie_id
        if not is_lorrie:
            await ctx.send("Your circle isn't Lorrie. You aren't going anywhere.")
        return is_lorrie

    @commands.command()
    async def message(self, ctx, text: str, channel: TextChannel):
        if ctx.message.attachments:
            files = []
            for f in ctx.message.attachments:
                files.append(await f.to_file())
            
            await channel.send(text, files=files)
        else:
            await channel.send(text)
        
        await ctx.send(f"✅ Message sent to {channel.name} in {channel.guild.name}")

    @commands.command()
    async def update_avatar(self, ctx):
        if not ctx.message.attahments:
            return await ctx.send("I can't update my avatar without an image!")

        bytes = await ctx.message.attachments[0].read()
        await self.bot.user.edit(avatar=bytes)
        await ctx.send("I've updated my avatar!")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(f"!!! DEBUG ERROR: {error}")
        await ctx.send(f"An error occurred: {error}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot: return
        print(f"Cog saw message: {message.content}")

async def setup(bot):
    await bot.add_cog(Lorrie(bot))