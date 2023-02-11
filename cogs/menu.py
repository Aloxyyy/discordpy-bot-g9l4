import disnake
from disnake.ext import commands
import random
import datetime
import asyncio
from typing import Optional

thumbnail_gif_suc = 'https://media.tenor.com/GNNL9kej3JMAAAAi/check-symbols.gif'
thumbnail_gif_err = 'https://media.tenor.com/8ojdgLE6lsUAAAAi/cross-red-cross.gif'
gif_reason = 'https://i.imgur.com/WF1sYjJ.gif'
gif_kick = 'https://i.imgur.com/Rcdvl7q.gif'
gif_ban = 'https://i.imgur.com/oOqrZNK.gif'
gif_mention = 'https://i.imgur.com/OGFC8OG.gif'



class moder_menu(disnake.ui.View):

    def __init__(self, *, timeout: Optional[float] = 10):
        super().__init__(timeout=timeout)

    @disnake.ui.button(label = 'бан', emoji = '⚡', style = disnake.ButtonStyle.primary)
    async def ban(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):

        gif = [
        'https://media.tenor.com/8YtBJxaqbFYAAAAd/success-successful.gif',
        'https://media.tenor.com/nTWaxH_L3bEAAAAC/loki-success.gif',
        'https://media.tenor.com/paKmomDgKIkAAAAC/happened-success.gif',    
        'https://media.tenor.com/KDxpEh5dSEEAAAAC/sponge-bob-square-pants-animation.gif',
        'https://media.tenor.com/uzPAjkVpFfAAAAAC/done-finished.gif',
        'https://media.tenor.com/pLgewiX-gb8AAAAC/ted-lasso-tedlassogifs.gif'
        ]

        first_embed = disnake.Embed(
            title = 'Выбрано действие "бан"',
            description = 'Введите под этим сообщением упоминание пользователя',
            color = 0xda70d6
        )
        first_embed.set_image(gif_mention)
        first_embed.set_thumbnail(gif_ban)

        await inter.channel.purge(limit = 1)
        await inter.send(embed = first_embed, ephemeral= True)       
        user = await inter.bot.wait_for('message', check = lambda message: message.author == inter.author)
        member = user.mentions[0]


        second_embed = disnake.Embed(
            title = 'Отлично,',
            description = 'осталось ввести причину, по которой пользователь получит бан',
            color = 0xda70d6
        )
        second_embed.set_thumbnail(gif_ban)
        second_embed.set_image(gif_reason)

        await inter.channel.purge(limit = 2)
        await inter.send(embed = second_embed, ephemeral = True)       
        content = await inter.bot.wait_for('message', check = lambda message: message.author == inter.author)
        reason = content.content


        third_embed = disnake.Embed(
            title = 'Успешно забанен',
            description= f'Администратор: {inter.author.name}({inter.author.mention})\nНарушитель: {member}\nПричина: {reason}',
            color = 0xda70d6
        )
        third_embed.set_image(random.choice(gif))
        third_embed.set_thumbnail(thumbnail_gif_suc)
        await inter.channel.purge(limit=1)
    
        
        try:
            await member.ban(reason = reason)
        except:
            embed = disnake.Embed(
                title = 'Ошибка',
                description= 'У бота недостаточно прав, нужно переместить бота выше',
                color = 0xff0000
            )
            embed.set_thumbnail(thumbnail_gif_err)
            embed.set_image('https://media.tenor.com/pQ7kmYSBiZIAAAAC/bkrafty-bkraftyerror.gif')
            await inter.followup.send(embed = embed, ephemeral = True)
            pass
        else:
            await inter.send(embed = third_embed)
        self.stop()
    
    
    
    @disnake.ui.button(label = 'кик', emoji = '🌌', style = disnake.ButtonStyle.primary)
    async def kick(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        
        gif = [
        'https://media.tenor.com/8YtBJxaqbFYAAAAd/success-successful.gif',
        'https://media.tenor.com/nTWaxH_L3bEAAAAC/loki-success.gif',
        'https://media.tenor.com/paKmomDgKIkAAAAC/happened-success.gif',
        'https://media.tenor.com/KDxpEh5dSEEAAAAC/sponge-bob-square-pants-animation.gif',
        'https://media.tenor.com/uzPAjkVpFfAAAAAC/done-finished.gif',
        'https://media.tenor.com/pLgewiX-gb8AAAAC/ted-lasso-tedlassogifs.gif'
        ]
        
        first_embed = disnake.Embed(
           title = 'Выбрано действие "кик"',
           description = 'Введи под этим сообщением упоминание пользователя',
           color = 0xda70d6
        )
        first_embed.set_image(gif_mention)
        first_embed.set_thumbnail(gif_kick)
        

        await inter.channel.purge(limit = 1)
        await inter.send(embed = first_embed, ephemeral= True)
        user = await inter.bot.wait_for('message', check = lambda message: message.author == inter.author)
        member = user.mentions[0]

        second_embed = disnake.Embed(
            title = 'Отлично,',
            description= 'Осталось только ввести причину, по которой пользователь будет кикнут',
            color = 0xda70d6
        )
        second_embed.set_image(gif_reason)
        second_embed.set_thumbnail(gif_kick)

        await inter.channel.purge(limit = 2)
        await inter.send(embed = second_embed, ephemeral = True)       
        content = await inter.bot.wait_for('message', check = lambda message: message.author == inter.author)
        reason = content.content

        third_embed = disnake.Embed(
            title = 'Успешно кикнут',
            description= f'Администратор: {inter.author.name}({inter.author.mention})\nНарушитель: {member}\nПричина: {reason}',
            color = 0xda70d6
        )
        third_embed.set_image(random.choice(gif))
        third_embed.set_thumbnail(thumbnail_gif_suc)
        await inter.channel.purge(limit=1)
        
        
        try:
            await member.kick(reason = reason)
        except:
            embed = disnake.Embed(
                title = 'Ошибка',
                description= 'У бота недостаточно прав, нужно переместить бота выше',
                color = 0xff0000
            )
            embed.set_thumbnail(thumbnail_gif_err)
            embed.set_image('https://media.tenor.com/pQ7kmYSBiZIAAAAC/bkrafty-bkraftyerror.gif')
            await inter.followup.send(embed = embed, ephemeral = True)
            pass
        else:
            await inter.send(embed = third_embed)
        self.stop()



class menu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='moder', description = 'вызывает панель модератора', aliases = ['модер', 'панель', 'управление', 'админ', 'admin'])
    @commands.has_permissions(ban_members = True, kick_members = True, administrator = True)
    async def moder(self, ctx):
        embed = disnake.Embed(
            title = 'Меню модератора🛠',
            description='Меню модератора - удобная утилита для модераторской деятельности\nНажимай на кнопку ниже, чтобы выбрать нужное действие',
            color = 0xda70d6
        )
        
        embed.set_thumbnail('https://i.imgur.com/SQWq3bX.png')

        view = moder_menu()


        await ctx.send(embed = embed, view=view)



def setup(bot):
	bot.add_cog(menu(bot))