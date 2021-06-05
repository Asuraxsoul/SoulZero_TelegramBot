# **Telegram Bot** - Boulder_SG
> ## Singapore bouldering gym finder
### Telegram bot username: _@SoulZero_bot_

## Bot Functions
### /places: 
> 1. Notify north, north-east, east, west and central options
> 2. Gives user a list of bouldering gyms

### /nearby:
> 1. Picks up user current location
> 2. Gives user a list of nearby gyms (5km radius)

### /all:
> 1. Gives user the full list of gyms in Singapore

### gym_name:
> 1. Gives detail about the gym based on user query
> 2. If user keys in full gym name, the bot will give detail about the gym
> 3. If user keys in incomplete gym name, the bot will give gym recommendations

### /feedback:
> 1. Sends me a query / improvement about the bot

### /help:
> 1. Displays all commands

## Idea Extensions
1. Opening and closing times (put the timing w picture)
2. Set alerts for upcoming climbing slot
3. Set gyms that user has been before and never been before

### Note
1. This bot is strictly free to use for people in Singapore.
2. Do not use my credentials, Telegram Bot API keys are easy to get via @BotFather.
3. Thank you for reading my repository and feel free to give me any feedback, enjoy!

### Python Libraries
1. json
2. math
3. flask
4. request
5. telegram-bot-api