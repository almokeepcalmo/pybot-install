import discord

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_message(message):
  if message.author.id == 145102755134963712:
    # Create an embed message
    embed = discord.Embed(title='Hot person detected', color=0xFF0000)
    # Set the thumbnail of the embed message to the person's profile picture
    # Add a spicy footer to the embed message
    embed.set_footer(text='This message is spicy! 🔥')
    # Send the embed message
    await message.channel.send(embed=embed)
  elif message.author.id == 814857851406647309:
    # Create an embed message
    embed = discord.Embed(title='VtM Bot detected', color=0x00FF00)
    # Set the thumbnail of the embed message to the person's profile picture
    # Add a spicy footer to the embed message
    embed.set_footer(text='Bloody hell!')
    # Send the embed message
    await message.channel.send(embed=embed)


client.run('MTA5MTc1NjYyMDUxOTgzMzYyMA.GU2pT1.IhJb-gQjLxXiEXiJE-yj7dK3B5EgJuXuSjmDi0')