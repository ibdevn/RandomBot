import discord
from discord.ext import commands
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Eingeloggt als {bot.user}")

# Coinflip
@bot.slash_command(name="coinflip", description="Wirf eine Münze")
async def coinflip(ctx: discord.ApplicationContext):
    result = random.choice(["Kopf 🪙", "Zahl 🪙"])
    await ctx.respond(f"{ctx.author.mention} hat **{result}**!")

# Dice
@bot.slash_command(name="dice", description="Würfle einen Würfel")
async def dice(ctx: discord.ApplicationContext, sides: int = 6, rolls: int = 1):
    results = [random.randint(1, sides) for _ in range(rolls)]
    await ctx.respond(f"{ctx.author.mention} würfelt: 🎲 {results}")

# Random Number
@bot.slash_command(name="random_number", description="Zufallszahl zwischen zwei Werten")
async def random_number(ctx: discord.ApplicationContext, start: int, end: int):
    number = random.randint(start, end)
    await ctx.respond(f"🔢 Zufallszahl zwischen {start} und {end}: **{number}**")

# Random Choice
@bot.slash_command(name="random_choice", description="Wähle zufällig aus Optionen")
async def random_choice(ctx: discord.ApplicationContext, *options: str):
    if not options:
        await ctx.respond("❌ Bitte gib mindestens 2 Optionen an!")
        return
    choice = random.choice(options)
    await ctx.respond(f"🤔 Ich wähle: **{choice}**")

# 8ball
@bot.slash_command(name="8ball", description="Frage den magischen 8-Ball")
async def eight_ball(ctx: discord.ApplicationContext, frage: str):
    antworten = ["Ja ✅", "Nein ❌", "Vielleicht 🤔", "Auf jeden Fall 🔥", "Eher nicht 😬"]
    await ctx.respond(f"🎱 Frage: *{frage}*\nAntwort: **{random.choice(antworten)}**")

# Random User
@bot.slash_command(name="random_user", description="Wähle ein zufälliges Mitglied")
async def random_user(ctx: discord.ApplicationContext):
    member = random.choice(ctx.guild.members)
    await ctx.respond(f"👤 Zufälliges Mitglied: {member.mention}")

# Random Color
@bot.slash_command(name="random_color", description="Erzeuge eine zufällige Farbe")
async def random_color(ctx: discord.ApplicationContext):
    color = discord.Color.random()
    embed = discord.Embed(title="🎨 Zufallsfarbe", description=f"Hex: {hex(color.value)}", color=color)
    await ctx.respond(embed=embed)

bot.run("TOKEN")
