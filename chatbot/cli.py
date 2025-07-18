import click
from .chat import chat

@click.group()
def cli():
    pass

cli.add_command(chat.chatbot)
