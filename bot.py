# I'm not the author of this bot! Source: https://github.com/kylianxdev/discord-coolpersondetected/
import discord
import os

os.environ["discord_token_var"]

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_message(message):
  if message.author.id == enter discord ID here:
    # Create an embed message
    embed = discord.Embed(title='Hot person detected', color=0xFF0000)
    # Set the thumbnail of the embed message to the person's profile picture
    # Add a spicy footer to the embed message
    embed.set_footer(text='This message is spicy! 🔥')
    # Send the embed message
    await message.channel.send(embed=embed)
  elif message.author.id == enter discord ID here:
    # Create an embed message
    embed = discord.Embed(title='VtM Bot detected', color=0x00FF00)
    # Set the thumbnail of the embed message to the person's profile picture
    # Add a spicy footer to the embed message
    embed.set_footer(text='Bloody hell!')
    # Send the embed message
    await message.channel.send(embed=embed)


client.run(os.environ["discord_token_var"])
