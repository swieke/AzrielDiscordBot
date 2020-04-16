import discord, random
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = "!", status = discord.Status.idle, activity= discord.Game(name="#ajgg"))
jawab = ["Yes", "No"]
dice = ["1","2","3","4","5","6"]
coin = ["Head","Tail"]
kakek =  "Nguyễn Yohanes Nóng Tránh a.k.a yohanes77 was a General, Commander in Chief of the Vietnam People's Army (VPA). He played a major role as a commander in the First Indochina War (1946–1954) and the Vietnam War (1960–1975) in which he was involved directly in many important campaigns such as the Border Campaign in Fall–Winter (1950), which led to the fall of Saigon and South Vietnam. Giap, together with Ho Chi Minh, was the most prominent figure of North Vietnam during the wars in the country.He is also considered by both his partisans and opponents as one of the greatest military commanders in history. Infamously known for his pun related to twin tiles."
@bot.event
async def on_ready():
    print("Logged in successfully as")
    print(chalk.green(bot.user.name))
    print("---------------------------")
    await bot.change_presence(status=discord.Status.online, activity = discord.Game(name="escape room."))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    author = message.author
    msg = message.content

    if (msg=="oi" or msg=="Oi"):
        await message.channel.send("Oiiiiii")

    print(f"{author} : {msg}")

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    ping = bot.latency
    ping = ping * 1000
    await ctx.channel.send(f"My ping is {ping}ms")


@bot.command()
async def tanya(ctx):
    await ctx.channel.send(random.choice(jawab))

@bot.command()
async def rolladice(ctx):
    await ctx.channel.send(random.choice(dice))

@bot.command()
async def flipacoin(ctx):
    await ctx.channel.send(random.choice(coin))

@bot.command()
async def whoiskakek(ctx):
    await ctx.channel.send(f"""
    Nguyễn Yohanes Nóng Tránh a.k.a yohanes77 was a General, Commander in Chief of the Vietnam People's Army (VPA). He played a major role as a commander in the First Indochina War (1946–1954) and the Vietnam War (1960–1975) in which he was involved directly in many important campaigns such as the Border Campaign in Fall–Winter (1950), which led to the fall of Saigon and South Vietnam. Giap, together with Ho Chi Minh, was the most prominent figure of North Vietnam during the wars in the country.He is also considered by both his partisans and opponents as one of the greatest military commanders in history. Infamously known for his pun related to twin tiles.
    """)

bot.run('NTM1NzMyNTU0NTM2NTgzMTY4.XphXLg.7151QNsc10dP0ImIl3aia4HDjNk')
 


