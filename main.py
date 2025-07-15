import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.message_content = True  # Needed if you add commands later

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is ready. Logged in as {bot.user} ({bot.user.id})")

@bot.event
async def on_member_join(member):
    try:
        # Set nickname to JA <display name>
        new_nick = f"JA {member.display_name}"
        await member.edit(nick=new_nick)
        print(f"✅ Nickname set for {member.name} → {new_nick}")

        # Add "JA ARMY" role if it exists
        role_name = "JA ARMY"
        role = discord.utils.get(member.guild.roles, name=role_name)
        if role:
            await member.add_roles(role)
            print(f"✅ Role '{role_name}' added to {member.name}")
        else:
            print(f"❌ Role '{role_name}' not found in server.")

    except Exception as e:
        print(f"⚠️ Error setting nickname or role: {e}")

# Start Flask web server to keep Replit alive
keep_alive()

# Run bot using token stored in Replit secret
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
