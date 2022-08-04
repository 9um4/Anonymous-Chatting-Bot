from random import shuffle
from discord import Intents
import disnake
import apikeys

charList = ["a", "b", "c", "d", "e", "f",
			"g", "h", "i", "j", "k", "l",
			"m", "n", "o", "p", "q", "r",
			"s", "t", "u", "v", "w", "x",
			"y", "z", "A", "B", "C", "D",
			"E", "F", "G", "H", "I", "J",
			"K", "L", "M", "N", "O", "P",
			"Q", "R", "S", "T", "U", "V",
			"W", "X", "Y", "Z", "0", "1",
			"2", "3", "4", "5", "6", "7",
			"8", "9"
]
shuffle(charList)

def base62(n):
	result = []
	while n > 0:
		n, mod = divmod(n, 62)
		result.append(mod)
	return result[::-1]

def random_nickname(id):
	base = base62(id)
	result = ""
	for i in base:
		result += charList[i]
	return result[::-1]

client = disnake.Client(intents=disnake.Intents.all())

@client.event
async def on_ready():
	print(f"We have logged in as {client.user}")

@client.event
async def on_message(message:disnake.Message):
	if message.author.id != apikeys.BOTID:
		await message.channel.send(random_nickname(message.author.id) + " : " + message.content)
		await message.delete()

client.run(apikeys.BOTTOKEN)
