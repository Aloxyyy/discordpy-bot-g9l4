import disnake
from disnake.ext import commands
import random
import datetime
import asyncio


thumbnail_gif_suc = 'https://media.tenor.com/GNNL9kej3JMAAAAi/check-symbols.gif'
thumbnail_gif_err = 'https://media.tenor.com/8ojdgLE6lsUAAAAi/cross-red-cross.gif'
gif_reason = 'https://i.imgur.com/WF1sYjJ.gif'
gif_kick = 'https://i.imgur.com/Rcdvl7q.gif'
gif_ban = 'https://i.imgur.com/oOqrZNK.gif'
gif_mention = 'https://i.imgur.com/OGFC8OG.gif'

class Moder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    
    @commands.command(name = 'clear', description = 'написать нужное количество сообщений', aliases = ['очистить', 'удалить', 'смести'], usage = 'clear <количество> <причина>', brief = 'удаляет нужное количество сообщений в чате')
    @commands.has_permissions(manage_messages = True, administrator = True)
    async def clear(self, ctx, amount = 20, *, reason = 'Нарушение правил'):
        await ctx.channel.purge(limit = amount)
        gif = [
            'https://media.tenor.com/kRCx3IrdtoEAAAAC/garbal.gif',
            'https://media.tenor.com/lsPkD8wDSQUAAAAC/clear-delete.gif',
            'https://media.tenor.com/tAk3fLRFf84AAAAC/akb48-clear.gif',
            'https://media.tenor.com/z4dDQufTOusAAAAC/purge-button-press.gif',
            'https://media.tenor.com/J4A_2BiQj5MAAAAC/overlord-wenpurge.gif',
            'https://media.tenor.com/IPq-Ep9u10AAAAAd/tom-jerry-cleaning-house-tomjerry.gif',
            'https://media.tenor.com/2T_mpBdB1kgAAAAC/discord-delete-message.gif',
            'https://media.tenor.com/ruOISJmEgEEAAAAC/erase-delete-it.gif'
        ]
        
        embed = disnake.Embed(
            title = f'Успешно удалено {amount} сообщений',
            description = f'Модератор: {ctx.author.mention}\nСообщений удалено: {amount}\nПричина: {reason}',
            color = 0x00FF00
        )
        embed.set_thumbnail(thumbnail_gif_suc)
        embed.set_image(random.choice(gif))

        await ctx.send(embed = embed)


    @commands.command(name="avatar", description = 'упомянуть участника', usage = 'avatar <@участник>', aliases = ['аватар', 'аватарка', 'ава'], brief = 'Показывает аватар участника') 
    async def avatar(self, inter: disnake.UserCommandInteraction, user: disnake.User):
        embed = disnake.Embed(title=f"Аватар пользователя {user}:", color = 0xda70d6)
        embed.set_image(url=user.display_avatar.url)
        await inter.channel.send(embed=embed)

    @commands.command(name = 'kick', description = 'упоминание пользователя и причины', aliases = ['кик'], usage= 'kick <@пользователь> <причина>', brief= 'кикает участника')
    @commands.has_permissions(kick_members = True, administrator = True)
    async def kick(self, ctx, member: disnake.Member, *, reason='Нарушение правил' ):
        
        gif = [
            'https://media.tenor.com/8YtBJxaqbFYAAAAd/success-successful.gif',
            'https://media.tenor.com/nTWaxH_L3bEAAAAC/loki-success.gif',
            'https://media.tenor.com/paKmomDgKIkAAAAC/happened-success.gif',
            'https://media.tenor.com/KDxpEh5dSEEAAAAC/sponge-bob-square-pants-animation.gif',
            'https://media.tenor.com/uzPAjkVpFfAAAAAC/done-finished.gif',
            'https://media.tenor.com/pLgewiX-gb8AAAAC/ted-lasso-tedlassogifs.gif'
        ]
        
        
        embed = disnake.Embed(
            title="Успешно!",
            description=f"Администратор {ctx.author.mention} кикнул пользователя {member.name}#{member.discriminator}", 
            colour= 0x00FF00)

        embed.add_field(name="Причина: ", value=reason, inline=False)
        embed.set_thumbnail(thumbnail_gif_suc)
        embed.set_image(random.choice(gif))
        await ctx.send(embed=embed)
        await member.kick(reason = reason)


    @commands.command(name='ban', description = 'упоминание пользователя и причины', aliases = ['бан'], usage='ban <@пользователь> <причина>', brief='банит участника')
    @commands.has_permissions(ban_members = True, administrator = True)
    async def ban(self, ctx, member: disnake.Member, *, reason='Нарушение правил' ):
        
        gif = [
            'https://media.tenor.com/8YtBJxaqbFYAAAAd/success-successful.gif',
            'https://media.tenor.com/nTWaxH_L3bEAAAAC/loki-success.gif',
            'https://media.tenor.com/paKmomDgKIkAAAAC/happened-success.gif',
            'https://media.tenor.com/KDxpEh5dSEEAAAAC/sponge-bob-square-pants-animation.gif',
            'https://media.tenor.com/uzPAjkVpFfAAAAAC/done-finished.gif',
            'https://media.tenor.com/pLgewiX-gb8AAAAC/ted-lasso-tedlassogifs.gif'
        ]
        
        
        embed = disnake.Embed(
            title="Успешно!",
            description=f"Администратор {ctx.author.mention} забанил пользователя {member.name}#{member.discriminator}", 
            colour= 0x00FF00)

        embed.add_field(name="Причина: ", value=reason, inline=False)
        embed.set_thumbnail(thumbnail_gif_suc)
        embed.set_image(random.choice(gif))
        await ctx.send(embed=embed)
        await member.ban(reason = reason)

    @commands.command(name = 'mute', description = 'упоминание пользователя, времени и причины', aliases = ['мут', 'мьют', 'заткнись'], usage = '-mute <@пользователь> <время> <причина>\n\nm - дни, h - часы, m - минуты, s - секунды', brief = 'мутит участника')
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: disnake.Member, time, d, *, reason = 'Нарушение правил'):
        guild = ctx.guild
        role = disnake.utils.get(guild.roles, name="Muted")
        

        for channel in guild.channels:
            await channel.set_permissions(role, speak=False, send_messages=False, read_message_history=True, read_messages= True)
        await member.add_roles(role)
        embed = disnake.Embed(title="Успешно", description=f"{member.mention} замьючен\n", colour=disnake.Colour.green(), timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Модератор: ", value=ctx.author.mention, inline=False)
        embed.add_field(name="Причина: ", value=reason, inline=False)
        embed.add_field(name="Время мьюта: ", value=f"{time}{d}", inline=False)
        await ctx.reply(embed=embed)
        if d == "s" or d == 'с':
            await asyncio.sleep(int(time))
        if d == "m" or d == 'м':								
            await asyncio.sleep(int(time*60))
        if d == "h" or d == 'ч':
            await asyncio.sleep(int(time*60*60))
        if d == "d" or d == 'д':
            await asyncio.sleep(int(time*60*60*24))
        
        await member.remove_roles(role)

        embed = disnake.Embed(title="Размьючен", 
        description=f"Пользователь {member.mention} провел все время наказание и был размьючен",
        colour=0xda70d6, 
        timestamp = datetime.datetime.utcnow())
        await ctx.reply(embed=embed)

def setup(bot):
	bot.add_cog(Moder(bot))