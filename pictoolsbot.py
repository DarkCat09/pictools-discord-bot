import os
import discord
from discord.ext import commands
from PIL import Image
from PIL import ImageFilter

# Add the bot:
# https://discord.com/api/oauth2/authorize?client_id=867021940174094397&permissions=2147585024&scope=bot

# Setting Up
token = '*** YOUR TOKEN ***'
bot = commands.Bot(command_prefix='/')

@bot.command()
async def picresize(ctx, *args):
	if ctx.message.attachments and len(args) > 0:
		attachedimg = ctx.message.attachments[0]
		await attachedimg.save(attachedimg.filename)

		img = Image.open(attachedimg.filename)
		w, h = img.size
		if (len(args) == 2) and (args[0] == 'w'):
			neww = int(args[1])
			newh = neww * h // w
		elif (len(args) == 2) and (args[0] == 'h'):
			newh = int(args[1])
			neww = newh * w // h
		elif (len(args) == 2):
			neww = int(args[0])
			newh = int(args[1])

		img = img.resize((neww, newh), Image.ANTIALIAS)
		img.save(attachedimg.filename)
		await ctx.send(file=discord.File(attachedimg.filename))
		os.remove(attachedimg.filename)

@bot.command()
async def pic8bit(ctx):
	if ctx.message.attachments:
		attachedimg = ctx.message.attachments[0]
		await attachedimg.save(attachedimg.filename)

		img = Image.open(attachedimg.filename)
		w, h = img.size
		img = img.resize((w // 8, h // 8), Image.NEAREST)
		img = img.resize((w *  8, h *  8), Image.NEAREST)

		img.save(attachedimg.filename)
		await ctx.send(file=discord.File(attachedimg.filename))
		os.remove(attachedimg.filename)

@bot.command()
async def piccrop(ctx, *args):
	if ctx.message.attachments and len(args) > 3:
		attachedimg = ctx.message.attachments[0]
		await attachedimg.save(attachedimg.filename)

		img = Image.open(attachedimg.filename)
		img = img.crop((int(args[0]),int(args[1]),int(args[2]),int(args[3])))
		img.save(attachedimg.filename)
		await ctx.send(file=discord.File(attachedimg.filename))
		os.remove(attachedimg.filename)

@bot.command()
async def picrotate(ctx, *args):
	if ctx.message.attachments and len(args) > 0:
		attachedimg = ctx.message.attachments[0]
		await attachedimg.save(attachedimg.filename)

		img = Image.open(attachedimg.filename)
		img = img.rotate(int(args[0]))
		img.save(attachedimg.filename)
		await ctx.send(file=discord.File(attachedimg.filename))
		os.remove(attachedimg.filename)

@bot.command()
async def picblur(ctx, *args):
	if ctx.message.attachments:
		attachedimg = ctx.message.attachments[0]
		await attachedimg.save(attachedimg.filename)

		img = Image.open(attachedimg.filename)
		radius = int(args[0]) if len(args) > 0 else 40
		img = img.filter(ImageFilter.GaussianBlur(radius))
		img.save(attachedimg.filename)
		await ctx.send(file=discord.File(attachedimg.filename))
		os.remove(attachedimg.filename)

@bot.command()
async def picconv(ctx, *args):
	if ctx.message.attachments and len(args) > 0:
		attachedimg = ctx.message.attachments[0]
		await attachedimg.save(attachedimg.filename)

		img = Image.open(attachedimg.filename)
		ext = str(args[0])
		newname = attachedimg.filename[:attachedimg.filename.rfind('.')] + '.' + ext
		img.save(newname, ext)
		await ctx.send(file=discord.File(newname))
		os.remove(attachedimg.filename)
		os.remove(newname)

# Starting
bot.run(token)
