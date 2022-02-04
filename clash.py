import os
import discord
import requests
import json


# Clash of Clans Api Header
headers = {
    'Accept' : 'application/json',
    'authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjQwMDkzOGNiLWZjZDItNDRkMC05MThkLWJhZjFjNjFjN2Q1MSIsImlhdCI6MTY0Mjg3OTQxNSwic3ViIjoiZGV2ZWxvcGVyL2E4ZTcyYmU2LTA4ZDktNmQ1NS02NjgwLTY0MTEwZDZiNDJlOSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE1My4zMy4zNC4xNTgiXSwidHlwZSI6ImNsaWVudCJ9XX0.fIxbunpWssXCjXjZAGoOP_WM_RhY_YSdEAVO-UC49m8vQSXB0M33G-mhLRi5YhhJxW0gEvWezvw3nE6ielHOXw'
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


def get_memberNames(tags):
  
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
clanNames = get_memberNames(clantags)





client = discord.Client() 

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  
@client.event
async def on_message(message):
  if message.author == client.user:
   return
  
  msg = message.content 
  if message.content.startswith('$trophies'):
    trophies = get_userTrophies()
    await message.channel.send(trophies)

  if message.content.startswith('$MyClanNames'):
    await message.channel.send(clanNames)

  if any(word in msg for word in clanNames):
    LOL = message.content + " is in clan" 
    await message.channel.send(LOL)



client.run('OTM1MjMyMTQwODY0NTM2NTk5.Ye7ozg.QUtnt7vclQClIJ92mmUEpLWuYxM')