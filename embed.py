import discord
from discord import embeds
import numpy as np
import asyncio


async def t_embed(channel, title, description, data, icon, image):
  embed = discord.Embed(title=title, description=description, color=0xfd4949)
  embed.set_thumbnail(url = icon)
  embed.set_image(url = image)
  for info_key in data:
    if info_key == '가드판정':
        embed.add_field(name=info_key, value="```" + str(data[info_key]) + "```", inline=False)
    else:
        embed.add_field(name=info_key, value="```\n" + str(data[info_key]) + "\n```", inline=True)
  message = await channel.send(embed=embed)
  return message

async def c_embed(channel, title, description, data):
  embed = discord.Embed(title=title, description=description, color=0xf3fd68)
  embed.set_footer(text="`236X`같은 커맨드는 'X'부분에 약/중/강 버전을 써주세요!")
  for info_key in data:
    value_str = ''
    for obj in data[info_key]:
      value_str += '\n' + obj
    embed.add_field(name=info_key, value="```" + value_str + "```", inline=True)
  message = await channel.send(embed=embed)
  return message

async def g_embed(channel, title):
  embed = discord.Embed(title = title, description = ':stars: 공략글', color=0x00bd26)
  if title == '그랑':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844847960884772874/58px-GBVS_Gran_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/1KUXnX6EP0RmoNWdRoHzJ3P5F28s4OzrlwFrYJ6aNf24/edit#gid=214206506')
  elif title == '나루메아':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844852387335634944/58px-GBVS_Narmaya_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/1bHuWRYGxkfgK0dcRKKaca3tVivRf8-JENPfunGIML5A/edit#gid=1138560127')
  elif title == '랜슬롯':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844850858738974750/58px-GBVS_Lancelot_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/1RPdLqP347qjsBZ1zGIoXGBJYxaUXa7NhE-mz-SfBfJA/edit#gid=1138560127')
  elif title == '로아인':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844850675162808330/58px-GBVS_Lowain_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/1IZwMa2a9u95MpDp0XTFOtJ0K2DYTj5EWsAi1-ZBh4e0/edit#gid=1458995862')
  elif title == '메테라':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844851475690684426/58px-GBVS_Metera_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/179OqwGaL6xR0DaUsx-wa68CBgNJCdG9vWjZoy32PVKk/edit#gid=706569324')
  elif title == '바자라가':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844851655890829352/58px-GBVS_Vaseraga_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/1q7A4BePDKWxzGejQgi3GdOQtdeyRE-ZGVmHMKTe9Yhk/edit#gid=1138560127')
  elif title == '벨리알':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844852286500765716/58px-GBVS_Belial_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/13riXpv2ZeASmmCRFzF2hUAwDqHb2uBqbEVx5I-_Jhxg/edit#gid=214206506')
  elif title == '벨제붑':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844851948255576064/58px-GBVS_Beelzebub_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/1fDkQ39cEHCjb2nCxgZp0mrijzAXU1sWetMTJw-XDRbg/edit#gid=1138560127')
  elif title == '샤를로테':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844849879405690920/58px-GBVS_Charlotta_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/1AM_bs5mD9dDzqTneN3xTlUXYCu5p8sQi5kYeUa3h-lI/edit#gid=550430936')
  elif title == '소리즈':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844852588021415976/58px-GBVS_Soriz_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/1nz_K6CwhZ020U2MWd8oApsoDFBxEJM1pOmDA61oXqf4/edit#gid=1670795521')
  elif title == '우노':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844852144577839154/58px-GBVS_Anre_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/1S3Nbb_wyoc8u-zHBNvLVpdXE8cbOJKqjkJpjVeVcgmM/edit#gid=1468237284')
  elif title == '유스테스':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844852858561101855/58px-GBVS_Eustace_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/1aBDKMP9aVKJq08yEGrFY5LYUU3ug8cU102AgRo-h-wE/edit#gid=703581033')
  elif title == '유엘':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844852779373559808/58px-GBVS_Yuel_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/1Z11wYziu2fn3tl5eHvu3KVZUrVn-4muEIuZuDmKlzyc/edit')
  elif title == '제타':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844851114171301898/58px-GBVS_Zeta_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/1oEgW3a-sfuYEsnynsNY4W1jaio0GeO0v3C7tESXRs0Q/edit#gid=854574556')
  elif title == '조이':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844852506118979604/58px-GBVS_Zooey_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/1rS7PXESMCnKQLTfMxcNtmaSKQYSHU2mnf5mLhA2ed1o/edit#gid=1138560127')
  elif title == '지타':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844852058136772628/58px-GBVS_Djeeta_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/1TANkejJus0FGSqrmAUFvo1gLBNFsVMaDyNwU86U_uKw/edit#gid=1558871192')
  elif title == '카타리나':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844850222559658005/58px-GBVS_Katalina_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/1n_NAR2sCh-MEg8hg5BVYcmw4Bl8jyxCrd9MUIPo-IUc/edit#gid=1085753018')
  elif title == '칼리오스트로':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844852687601270824/58px-GBVS_Cagliostro_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/13dBgGrmkBJVR3ukLoDNhZeopNgtmDBwRgOh5v2xLV58/edit#gid=1559228280')
  elif title == '파스티바':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844850041826312253/58px-GBVS_Ladiva_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/1UfgUJeo0XCH72Ns9Um0mMk7tQZomwfOP7MxEiRWjEfc/edit#gid=1364340536')
  elif title == '퍼시벌':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844849671313686548/58px-GBVS_Percival_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/1ncZM9ioBxpWsolZKZ5fLxZotmAAmCc2nBxUQ2RT0dLU/edit#gid=69722501')
  elif title == '페리':
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819424959101141014/844850378234658836/58px-GBVS_Ferry_Icon.png")
    embed.add_field(name='링크', value='https://docs.google.com/spreadsheets/d/1e8OrLo-n0hZYfztgr2b9IV6Mnz8k7qkgpBsqIvquLEw/edit#gid=2137001956')
  
  await channel.send(embed=embed)
