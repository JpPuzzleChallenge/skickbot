import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
	print('Ready!')
    
@client.event
async def on_member_join(member):
    try:    
        await client.send_message(member,"
        asyncio.sleep(0.5)
        await client.kick(member)
    except:
        print("ERROR.")
        await client.send_message(client.get_channel("357091959388504065"),"ERROR!")
        await client.kick(member)
client.run("MzU3MTA1MTEzNjY5NTY2NDY0.DJlDlg.tZn_CLvBjjHBws3Yz5aIdXBEvhc")