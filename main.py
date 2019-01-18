from discord.ext import commands
import discord, random

bot = commands.Bot(command_prefix = "!", status = discord.Status.idle, activity= discord.Game(name="#SmackQueenYaQueen"))
jawab = ["Iyaaaaaa", "Nggakkkk"]
dice = ["1","2","3","4","5","6"]
coin = ["Head","Tail"]

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
async def whoami(ctx, member:discord.User = None):
    if member == None:
        member = ctx.message.author
        pronoun = "Your"
    else:
        pronoun = "Their"
    name = f"{member.name}#{member.discriminator}"
    status = member.status
    joined = member.joined_at
    role = member.top_role
    if name == "swieke#1017":
        await ctx.channel.send("Nama anda Theo Azriel.")
    elif name == "Rere#4238":
        await ctx.channel.send("Nama anda Ariel Kurniawan.")
    elif name == "Bre#3901":
        await ctx.chanel.send("Nama anda Bryan Nathaniel.")
    elif name == "momo#1732":
        await ctx.channel.send("Nama anda Michael Tjahjadi.")
    elif name == "danieljasont#2656":
        await ctx.channel.send("Nama anda Daniel Jason Tatang. Hati-hati orang ini ngecit Pogo")
    elif name == "Greg The Actuary Boy#1344":
        await ctx.channel.send("Nama anda Gregorius Arvianto.")
    elif name == "Jokevarane#5170":
        await ctx.channel.send("Nama anda Jonathan Kevan.")
    elif name == "Si Bego#6146":
        await ctx.channel.send("Nama anda Joel Sugiarto.")
    elif name == "jasonadiw#2426":
        await ctx.channel.send("Nama anda Jason Adiwardhana.")
    elif name == "Proxx#1576":
        await ctx.channel.send("Nama anda Virnanto Buntarja.")
    elif name == "victor#758":
        await ctx.channel.send("Nama anda Victor Nathanael.")
    elif name == "james289#3414":
        await ctx.channel.send("Nama anda Ricky Hanson.")

@bot.command()
async def siapanurhadi(ctx):
    await ctx.channel.send(f"Meskipun Nurhadi-Aldo adalah pasangan fiktif, Nurhadi benar-benar ada. Nurhadi adalah seorang tukang urut yang berasal dari Mejobo, Kabupaten Kudus.")

@bot.command()
async def tanya(ctx):
    await ctx.channel.send(random.choice(jawab))

@bot.command()
async def rolladice(ctx):
    await ctx.channel.send(random.choice(dice))

@bot.command()
async def flipacoin(ctx):
    await ctx.channel.send(random.choice(coin))



bot.run(os.getenv('TOKEN'))
 
