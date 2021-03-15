import discord
from discord.ext import commands
import os

token = 'ODIwOTgwMzczMDg1MzU2MDM0.YE9Djg.ID6MwTEWJFpm4mf_ej6YLQlYvDo'
bot = commands.Bot(command_prefix='!')

@bot.command()
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason: str = 'No blocking reason specified.'):
    await member.ban(reason=reason, delete_message_days=0)
    await ctx.send(embed = discord.
 Embed(description = (f"**{member} has been banned**"),color=0xc582ff))
 
@bot.command()
@commands.has_permissions(kick_members=True)
@commands.bot_has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason: str = 'No kick reason specified.'):
    await member.kick(reason=reason)
    await ctx.send(embed = discord.
 Embed(description = (f"**{member} has been kicked**"),color=0xc582ff))

@bot.command()
async def user(ctx, Member: discord.Member = None ):
    if not Member:
        Member = ctx.author
    emb = discord.Embed(title='User info'.format(Member.name), description=f"Joined: {Member.joined_at.strftime('%b %#d, %Y')}\n\n "
    f"Nickname: {Member.name}\n\n"
    
   f"Nickname on server: {Member.nick}\n\n
                                                                                      f"ID: {Member.id}\n\n"
                                                                                      f"Highest role: {Member.top_role}\n\n"
                                                                                      f"Account created: {Member.created_at.strftime('%b %#d, %Y')}", 
                                                                                      color=0xc582ff, timestamp=ctx.message.created_at)
 
    emb.set_thumbnail(url= Member.avatar_url)
    emb.set_footer(icon_url= Member.avatar_url)
    await ctx.send(embed=emb)
 
@bot.command()
async def delete(ctx, amount= None):
         await ctx.channel.purge(limit = int(amount) + 1)
         await ctx.send(embed= discord.Embed(description = (f'**Deleted {amount} messages.**'), color=0xc582ff))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, command does not exist**', color=0xc582ff))
   

@bot.command()
@commands.has_permissions( administrator = True )
async def unban( ctx, *, member = None ):
    if member is None:
         await ctx.send(embed = discord.Embed(description = f'{ ctx.author.name }, specify user', color = 0x4f4db3 ))
    else:
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            await ctx.guild.unban( user )
            await ctx.send(embed = discord.Embed(description = (f"**{member} has been unbanned**"),color=0xc582ff))
 
@bot.event
async def on_ready():
    game = discord.Game(r"!help")
    await bot.change_presence(status=discord.Status.online, activity=game)

token = os.environ.get('Bot_token')
bot.run(str(token))