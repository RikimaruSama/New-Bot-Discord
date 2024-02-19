import datetime
import discord
from discord.ext import commands

from calendrier import UvsqCalendar

"""
    Cree notre bot, command_prefix est utilisé pour appeller le bot sur discord par exemple avec !help,
    l'intents concerne les droits, ici il aura toutes les permissions.
"""
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Le bot est en ligne.")

@bot.command()
async def ping(context : commands.Context) -> None:
    # Renvoie Pong suivi de la latence, environ 130ms
    await context.send(f"Pong! {bot.latency * 1000:.2f} ms")

@bot.command()
async def export_messages(ctx, channel_name: str):
    # Récupère le canal spécifié par le nom
    channel = discord.utils.get(ctx.guild.channels, name=channel_name)
    
    # Condition si le channel_name n'est pas un channel
    if not channel:
        await ctx.send("Le canal spécifié n'existe pas.")
        return
    
    # Ouvre un fichier texte pour écrire les messages
    with open(f'{channel_name}_messages.txt', 'w', encoding='utf-8') as f:
        async for message in channel.history(limit=None):
            f.write(f'{message.author.name} - {message.content}\n')

@bot.command()
async def beta_calendrier(ctx, args: str):
    uvsq = UvsqCalendar()
    print(args.split(" ")[3])
    for matiere in uvsq.request_dict(date_debut="15/02/2024", date_fin="15/02/2024", section="M1 SECRETS gr 1"):
        await ctx.send('/'.join(matiere.values()))

if __name__ == "__main__":
    with open(r'C:\\Users\\33685\\Desktop\\token.txt', "r") as file:
        token = file.read()
    bot.run(token)