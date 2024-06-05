import discord
import os
from dotenv import load_dotenv
import requests

load_dotenv()
bot = discord.Bot()
api_base_url = f"https://api.cloudflare.com/client/v4/accounts/{os.getenv("CF_ACCOUNT_ID")}/ai/run/"
headers = {"Authorization": f"Bearer {os.getenv("CF_TOKEN")}"}


@bot.event
async def on_ready():
	print(f"Logged in as {bot.user}")
	
	
def run_model(prompt) -> str:
	"""
	Runs the model with the given prompt.
	:param prompt: Should be a string of the user prompt to run the model with.
	:return: A string of the model's response, filtered from all the json.
	"""
	
	inputs = [
		{"role": "system", "content": os.getenv('SYSTEM_ROLE')},
		{"role": "user", "content": f"{prompt}"}
	]
	
	print("Fired request!")
	prompts: dict = {"messages": inputs}
	response = requests.post(f"{api_base_url}{os.getenv("MODEL")}", headers=headers, json=prompts)
	if response.status_code != 200 or not response.json()["success"]:
		print(response.json())
		return f"An error occurred: {response.json()['errors'][0]['message']}\n Status code: {response.status_code}\n Sorry, please try again."
	reply: str = response.json()["result"]["response"]
	if len(reply) > 2000:
		reply = reply[:1997] + "..."
	print(reply)
	return reply


@bot.command()
async def chat(ctx, prompt: discord.Option(discord.SlashCommandOptionType.string)):
	return await ctx.send(run_model(prompt))


bot.run(os.getenv('BOT_TOKEN'))
