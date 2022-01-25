import os
import discord
import requests

# Clash of Clans Api Header
headers = {
    'Accept' : 'application/json',
    'authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjUwZjEyMTllLWZiNGEtNGMwYy04MDMxLTA1ZjJjNGQzMjMyYiIsImlhdCI6MTY0MzA1MTc2Miwic3ViIjoiZGV2ZWxvcGVyL2E4ZTcyYmU2LTA4ZDktNmQ1NS02NjgwLTY0MTEwZDZiNDJlOSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjM1LjIzMy4yNDYuNzEiXSwidHlwZSI6ImNsaWVudCJ9XX0.vJe20nhG5btlDpHhs_OoQHOloq-zQjezcHy8T3i7opJZdqpRUroK3DGU63tjbIKYeWTcXjq1zvMcFnMVEDl_Cg'
}

def get_userTrophies():
    response = requests.get('https://api.clashofclans.com/v1/players/%239YQR2LPV', headers=headers)
    user_json = response.json()
    trophies = str(user_json['trophies'])
    return(trophies)

def get_userName():
    response = requests.get('https://api.clashofclans.com/v1/players/%239YQR2LPV', headers=headers)
    user_json = response.json()
    print(user_json)


my_secret = os.environ['TOKEN']

client = discord.Client() 

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  
@client.event
async def on_message(message):
  if message.author == client.user:
   return
  
  if message.content.startswith('$trophies'):
    trophies = get_userTrophies()
    await message.channel.send(trophies)



client.run(os.getenv('TOKEN'))