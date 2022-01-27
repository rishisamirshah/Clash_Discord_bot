import os
import discord
import requests
import json

# Clash of Clans Api Header
headers = {
    'Accept' : 'application/json',
    'authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjkzY2JkYTY2LWU1YTctNDVhOC05N2UyLThhMjAzYWY2MzAzMSIsImlhdCI6MTY0MzEzODYyMSwic3ViIjoiZGV2ZWxvcGVyL2E4ZTcyYmU2LTA4ZDktNmQ1NS02NjgwLTY0MTEwZDZiNDJlOSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjM1LjIyMi4xNjguNSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.eC61H5TKSlHMz-yunkx1-F7wWUFnOrJLScfNjUXmu969R_6N8Glreopy1lIf7dx9zi4uHVd5fpXS1-dgkqLiBA'
}

def get_userTrophies():
    response = requests.get('https://api.clashofclans.com/v1/players/%239YQR2LPV', headers=headers)
    user_json = response.json()
    trophies = str(user_json['trophies'])
    return(trophies)

def get_PlayerInfo():
    response = requests.get('https://api.clashofclans.com/v1/players/%239YQR2LPV', headers=headers)
    user_json = response.json()
    print(user_json)

#Prints clan members id
def get_clanMembers():
  response = requests.get('https://api.clashofclans.com/v1/clans/%23GC2G89L8/members', headers=headers)
  user_json = response.json()
  items = user_json['items']
  count = int(len(items))
  x = 0
  tags = [None] * count
  
  while(x < count):
    tags[x] = items[x].get('tag')
    x = x + 1
  return tags


def get_memberInfo(tags):
  
  count = int(len(tags))
  x = 0
  userdata = [None] * count
  while (x < count):
      tag = tags[x]
      tag = tag.replace("#","")
      
      #print('https://api.clashofclans.com/v1/players/%23' + tag)
      response = requests.get('https://api.clashofclans.com/v1/players/%23' + tag, headers=headers)
      user_json = response.json()
      userdata[x] = user_json.get('name')
      print(user_json.get('name'))
      x = x + 1
  return userdata






clantags = get_clanMembers()



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

  if message.content.startswith('$MyClanNames'):
    names = get_memberInfo(clantags)
    print(names)
    await message.channel.send(names)



client.run(os.getenv('TOKEN'))
