import discord
import os

client = discord.Client()

@client.event 
async def on_ready():
    print('Hello, guardian. {0.user} is ready for duty.'.format(client))

@client.event
  
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('z$hello'):    
        await message.channel.send('Hello, Guardian.')

    elif message.content.startswith('z$stasis'):    
        await message.channel.send('Guardian, the darkness is a dangerous force. Stasis is no exeption. I do not approve of its use, but if its for the greater good then I guess I have to.')

    elif message.content.startswith('z$valus'):    
        await message.channel.send('Whether we wanted it or not, weve stepped into a war with the Cabal on Mars. So lets get to taking out their command, one by one. Valus Taaurc. From what I can gather he commands the Siege Dancers from an Imperial Land Tank outside of Rubicon. Hes well protected, but with the right team, we can punch through those defenses, take this beast out, and break their grip on Freehold.')

    elif message.content.startswith('z$indeed'):    
        await message.channel.send('Indeed.')

    elif message.content.startswith('z$light'):    
        await message.channel.send('Guardian, if you got your light back then we have some hope against the Red Legion.')

    elif message.content.startswith('z$pnotes'):    
        await message.channel.send('https://sites.google.com/view/czavlist/patch-notes')

    elif message.content.startswith('z$cmds'):    
        await message.channel.send('https://sites.google.com/view/czavlist/home')

client.run(os.getenv('TOKEN'))
