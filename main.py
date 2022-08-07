import discord
import requests
import discord.ext.commands
intents = discord.Intents().all()
bot = discord.Bot(intents=intents)

@bot.slash_command(guild_ids=[guild id here], description="Random meme")
async def meme(ctx):
    res = requests.get("https://meme-api.herokuapp.com/gimme/meme").json()
    meme_author = res["author"]
    meme_img = res["url"]
    x = discord.Embed(title=meme_author, url=meme_img)
    x.set_author(name=meme_author, url=meme_img)
    x.set_image(url=meme_img)
    await ctx.respond(embed=x)

bot.run("token here") # bot token here
