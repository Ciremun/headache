import discord

import src.commands as cmd
import src.config as cfg
from .log import logger

client = discord.Client()

@client.event
async def on_ready(*args, **kwargs) -> None:
    logger.info('discord ready')

@client.event
async def on_message(message: discord.Message) -> None:
    if message.author.id == client.user.id and message.content.startswith(cfg.prefix):
        parts = message.content.split(' ')
        command = cmd.commands[parts[0][len(cfg.prefix):]]
        await command(message)
