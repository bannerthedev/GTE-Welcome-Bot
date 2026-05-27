import discord
from discord.ext import commands

# === CONFIGURE THESE ===
TOKEN = "MTUwOTIzOTU3MzEzNjI4MTg5MQ.Gtluja.PlvFUHObHH_4n-yx6PMnMBTrcL53uC_NIyHYMM"
WELCOME_CHANNEL_ID = 1509247667371507742  # replace with your welcome channel ID

# Put your emoji ID number here
GTE_EMOJI_ID = 1509254546092855538 # <- replace with your emoji ID

# =======================

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_member_join(member: discord.Member):
    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
    if channel is None:
        return

    msg = await channel.send(
        f"Welcome {member.mention} to **GTE**! *Please Read The Server Rules*"
    )

    # Get the emoji object from the guild by ID
    emoji = discord.utils.get(member.guild.emojis, id=GTE_EMOJI_ID)
    if emoji is None:
        print("Emoji not found in this guild.")
        return

    try:
        await msg.add_reaction(emoji)
    except discord.HTTPException as e:
        print(f"Failed to add reaction: {e}")

bot.run(TOKEN)
