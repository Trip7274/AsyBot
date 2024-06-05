# Asybot
Very simple Discord bot written in Python using Py-Cord, with the goal of trying to make a belivable person who chats at random
intervals, and remembers others' actions and general sentiment towards them.

Currently, it uses a model of your choosing using [Cloudflare AI](https://ai.cloudflare.com/), and uses a .env that follows this format:
```
BOT_TOKEN='# Discord Bot Token'
CF_TOKEN='# Cloudflare AI API Token'
CF_ACCOUNT_ID='# Found in the Cloudflare dashboard'

# AI Configs:
SYSTEM_ROLE='# This is the role the bot will play and follow'
MODEL='# Model ID, found in Cloudflare's docs'
```

This README (and project!) are in a very early stage and are a work in progress, and will be updated and grown further as the bot is developed.