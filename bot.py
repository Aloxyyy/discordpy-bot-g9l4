import disnake
from disnake.ext import commands
import os


bot = commands.Bot(command_prefix='-', help_command= None, intents=disnake.Intents.all(), activity= disnake.Game(name = 'creator > roxyyy#9999'))


@bot.event
async def on_command_error(ctx, error):
    print(error)

    if isinstance(error, commands.BotMissingPermissions):
        embed = disnake.Embed(title='У вас недостаточно прав для выполнения этой команды')
        await ctx.send(embed = embed)
    
    elif isinstance(error, commands.UserInputError):
        embed = disnake.Embed(
            title='❗Вы ввели команду неправильно❗',
            description=f'Правильное использование команды\n{ctx.prefix}{ctx.command.name} {ctx.command.brief}\nПример:{ctx.prefix}{ctx.command.usage}', 
            color=0x470085
        )
        await ctx.send(embed = embed)
    

@bot.event
async def on_message(message: disnake.Message):
    await bot.process_commands(message)
    if message.author.bot:
        return
    
    content = message.content
    if content == 'Привет':
        await message.channel.send('И тебе привет!')


@bot.event
async def on_ready():
    print(f'Бот {bot.user} готов работать!')




for fn in os.listdir('./cogs'):
	if fn.endswith('.py'):
		bot.load_extension(f"cogs.{fn[:-3]}")


bot.run(os.environ["DISCORD_TOKEN"])
