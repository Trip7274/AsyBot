import threading

import discord
import os
from dotenv import load_dotenv
import requests

load_dotenv()
bot = discord.Bot()

system_role = os.getenv('SYSTEM_ROLE')
model = os.getenv('MODEL')
api_base_url = f"https://api.cloudflare.com/client/v4/accounts/{os.getenv("CF_ACCOUNT_ID")}/ai/run/"
headers = {"Authorization": f"Bearer {os.getenv("CF_TOKEN")}"}


@bot.event
async def on_ready():
	print(f"Logged in as {bot.user}")
	
	
def run_model(prompt: str) -> str:
	"""
	Runs the model with the given prompt.
	:return: A string of the model's response, filtered from all the json.
	"""
	
	print("Firing request!")
	
	inputs = [
		{"role": "system", "content": system_role},
		{"role": "user", "content": f"{prompt}"}
	]
	
	prompts: dict = {"messages": inputs}
	response = requests.post(f"{api_base_url}{model}", headers=headers, json=prompts)
	
	if response.status_code != 200:  # Error handling!!!
		print(response.json())
		return f"An error occurred: {response.json()['errors'][0]['message']}\n Status code: {response.status_code}\n Sorry, please try again."
	
	reply: str = response.json()["result"]["response"]
	
	if len(reply) > 2000:  # Discord doesn't allow bots to send more than 2000 characters, apparently?
		reply = reply[:1997] + "..."

	return reply


@bot.command()
async def chat(ctx, prompt: discord.Option(discord.SlashCommandOptionType.string)):
	return await ctx.send(run_model(prompt))


bot.run(os.getenv('BOT_TOKEN'))
