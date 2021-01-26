from typing import Union, List

import discord
from discord import Guild, Member, User, Attachment, Embed
from discord.ext import commands
from discord.ext.commands import Context
from datetime import datetime
from io import BytesIO
from serverContext import betaTest, titsConfig, ServerContext
import os

####################
# Obtain bot token from Discord Developer Site
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Token ID MUST
# be a string (in quotes)!

####################

channelConfiguration: ServerContext = titsConfig

# Creates the instances, uses "!" to activate commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

PURE_TEXT = 0
IMAGE_EMBED = 1
VIDEO_EMBED = 2

# "!conf" command
@bot.command(aliases=['vent', 'vc', 'horny', 'tiktok', 'meme', 'rec', 'gay'])
async def conf(ctx, *, message=""):
    await generic_conf(ctx, channelConfiguration.channelToID(ctx.invoked_with), message)


# abstracted out the generic confesion, supply a target channel destination and you're all set.
async def generic_conf(ctx: Context, channel_dest_id: int, message: str):
    # Error check: skips if message has no content or image
    if (len(message) != 0) or (ctx.message.attachments != []):

        # Obtains User ID and nickname to verify user is in guild/server
        userID = ctx.message.author.id
        server: Guild = bot.get_guild(channelConfiguration.GUILD_ID)
        member = server.get_member(userID)

        # If member is a member of the server, they will have a name (instead of None)
        if member is not None:
            # Assigns Discord channel (given channel ID)
            channel = bot.get_channel(channel_dest_id)

            # datetime object containing current date and time
            now = datetime.now()
            currentTime = now.strftime("%d/%m %H:%M")

            # Create embed message (looks better)
            embed: Embed = discord.Embed(description=message)
            author: Union[User, Member] = ctx.message.author

            # Set date/time as footer of embed
            embed.set_footer(text=currentTime)

            # Video/Image attachments
            files = []
            videos = []
            global PURE_TEXT, VIDEO_EMBED, IMAGE_EMBED

            post_type = PURE_TEXT

            for file in ctx.message.attachments:
                # print("got attachement: %s" % file)
                fp = BytesIO()
                await file.save(fp)
                if file.filename[-3:] == "mp4":
                    post_type = VIDEO_EMBED
                    videos.append([file, fp])
                else:
                    files.append(discord.File(fp, filename=file.filename, spoiler=file.is_spoiler()))
                    imageURL = ctx.message.attachments[0].url
                    embed.set_image(url=imageURL)

            # Send embed message to channel
            if post_type in [PURE_TEXT, IMAGE_EMBED]:
                await channel.send(embed=embed)
            else:
                vfile, vfilepointer = videos.pop(0)
                await channel.send(embed=embed, files=[discord.File(vfilepointer, vfile.filename)])
            # Inform user their message has been sent
            await ctx.send("Thanks for sending to Ritz's Domain")

        # If member is not a member is the server, they will be tagged None
        else:
            await ctx.send("You are not a member of the server! The message was not sent.")

            # If the message contains no image or text
    else:
        await ctx.send("Your message does not contain any content. Message failed.")


# Runs the bot given bot token ID
bot.run(BOT_TOKEN)
