# Asybot
### This is still very early, and functions as very simple a LLM-to-Discord bot so far, most of the intended functionality is yet to be implemented
Very simple Discord bot written in Python using Py-Cord, with the goal of trying to make a belivable creature who chats at random
intervals, and remembers others' recent actions and general sentiment towards them.

Currently, it uses a model of your choosing using [Cloudflare AI](https://ai.cloudflare.com/), and uses a .env that follows this format:
```
BOT_TOKEN='# Discord Bot Token'
CF_TOKEN='# Cloudflare AI API Token'
CF_ACCOUNT_ID='# Found in the Cloudflare dashboard'

# AI Configs:
SYSTEM_ROLE='# This is the role the bot will play and follow'
MODEL='# Model ID, found in Cloudflare's docs'
```

The character details, documents, and prompts will not be included here as they're Asymetrap's own characters, and he's yet to feel comfortable handing them out on a GPLv3 license, so, the code, and only the code, is included.

This README is currently in a very early stage and is a work in progress, and will be updated and grown further as the bot is developed.
