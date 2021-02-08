from datetime import datetime
from typing import Callable, Any
from io import BytesIO

import discord
from PIL import Image

import src.db as db
from .log import logger
from .plot import gen_plot
from .classes import Note

commands = {}


async def send_error(err: str, message: discord.Message) -> None:
    error_message = await message.channel.send(err)
    await error_message.delete(delay=3)


def command(name: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        async def wrapper(message: discord.Message) -> Any:
            try:
                return await func(message)
            except Exception as e:
                await send_error(e, message)
                logger.error(e)
            finally:
                await message.delete()
        wrapper.__name__ = func.__name__
        commands[name] = wrapper
        return wrapper
    return decorator


@command('add')
async def add_command(message: discord.Message) -> None:
    parts = message.content.split(' ')
    points = int(parts[1])
    med = parts[2]
    date = datetime.now()
    db.add_note(date, points, med)

@command('exec')
async def exec_command(message: discord.Message) -> None:
    code = '\n'.join(message.content.split('\n')[2:])[:-3]
    if code:
        exec(code)

@command('plot')
async def plot_command(message: discord.Message) -> None:
    notes = db.get_notes()
    if not notes:
        await send_error('you have no notes', message)
        return
    notes = [Note(*n) for n in notes]
    gen_plot(notes)
    plot_img = Image.open('flask/plot.png')
    with BytesIO() as image_binary:
        plot_img.save(image_binary, 'PNG')
        image_binary.seek(0)
        await message.channel.send(file=discord.File(fp=image_binary, filename='plot.png'))

# TODO(#3): color command
# add/remove/update color-med pairs
