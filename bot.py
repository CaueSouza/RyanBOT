import discord
import resposes
import getters


async def send_message(message, user_message, is_private):
    try:
        response = resposes.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTAzNzUzNTgzMzk0MDU2NjA4Nw.GHynZr.benVmYqk6K5MrOwD8EqflTOETp6u8mPTCvcdZU'  # INSERT BOT TOKEN HERE

    intents = discord.Intents.all()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_member_join(member):
        await member.send('Bem vindo ao Ryanverso seu merda')

        print(f'{member} entered the server')

        message = getters.get_welcome_message(member.id)

        try:
            channel = member.guild.system_channel
            await channel.send(message)

        except Exception as e:
            print(e)


    @client.event
    async def on_member_remove(member):
        print(f'{member} left the server')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message} ({channel})"')

        if user_message[0] == '?':
            if user_message[1] == '?':
                user_message = user_message[2:]
                await send_message(message, user_message, is_private=True)
            else:
                user_message = user_message[1:]
                await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
