import discord
import os
import requests
import json
import random
import keep_alive
from discord.ext import commands



ping = [
  "<@!896707795703971851>",
  "<@896707795703971851>",
]

nigger_triggers = [
  "kfc",
  "melon",
  "chicken bone",
  "chickenbone",
  "fried chicken",
]
nigger_react = [
  "melon muncher",
  "chicken bone fucker",
  "NIGGERS?!",
  "COON",
  "NiggaTwerk Corporation™",
  "NiggaTwerk Academy™",
  "NIGGERS?!",
  "NIGGERS?!",
  "NIGGERS?!",
  "NIGGERS?!",
  "NIGGERS?!",
  "NIGGERS?!",
  "NIGGERS?!",
  "NIGGERS?!",
]

nya_triggers = [
  "meow",
  "nya",
  "kitty",
  "kit kat",
  "kit cat",
  "miau",
]
nya_react = [
  "Nya!",
  "nya~",
  "Meow!",
  "meow~",
  "meow :3",
  "Nya?",
  "Nya? ~",
  "Nya!（=´∇｀=）",
  "(=｀ω´=)",
  "Nya（ꏿ ω ꏿ）",
  "（Φ ω Φ）",
  "ก₍⸍⸌̣ʷ̣̫⸍̣⸌₎ค",
]

pet_triggers = [
  "pets <@!896707795703971851>",
  "strokes <@!896707795703971851",
  "fondles <@!896707795703971851",
  "pets <@896707795703971851>",
  "strokes <@896707795703971851",
  "fondles <@896707795703971851",
]
pet_react = [
  "murr~",
  "nngh~",
  "mmmmmh :3",
  "mmmmmmmmmm~ (ꈍωꈍ)",
  "ah- ( “･ω･ﾞ)",
  "*hikup* (´･ω･`)",
  "murr~",
  "nngh~",
  "mmmmmh :3",
  "mmmmmmmmmm~ (ꈍωꈍ)",
  "ah- ( “･ω･ﾞ)",
  "*hikup* (´･ω･`)",
  "(=^ω^=)",
  " (=^ ◡ ^=) ",
  "（=´∇｀=）",
  "(=^-ω-^=)",
  "(^≗ω≗^)",
  "（＾・ω・＾✿）",
  "（＾・ω・＾❁）",
  "♡ॢ₍⸍⸌̣ʷ̣̫⸍̣⸌₎",
  "(=♡ ᆺ ♡=)",
  "*cums* (◯ω◯)",
  "aahhnnnnng~",
  "aahhnnnnng~ *heavy breathing*  (˵•ヘ•˵)",
  "purrr~ purrr~ purrr~",
  "purrr~ purrr~ purrr~ purrr~ purrr~ ...... huh? Hey! Don't stop now!  ʕ>⌓<｡ʔ",
  "Hey! Wha- a- ahhnnng~  ( ˊωˋ )",
  "Pet me more! ヽ(=^･ω･^=)丿",
  "mmmmmmmh~ my belly feels good~ (≈≧ܫ≦≈)",
  "I want to fuck my 7 year old cousin ( ͡o ͜ʖ ͡o)",
]

dont_be_racist_triggers = [
  "dont be racist",
  "don't be racist",
  "no being racist",
  "do not be racist",
  "racism bad",
  "racist bad",
  "racism is bad",
  "racists bad",
  "dumb racist",
  "stupid racist",
  "racists are dumb",
  "racists are idiot",
  "racists are stupid",
]
racist_triggers = [
  "nig",
  "coon",
  "ape",
  "neger",
  "porch monkey",
  "tar baby",
  "powder burn",
  "nlg",
  "n1g",
  "racism",
  "racist",
  "fag",
  "n3ger",
  "neg3r",
]

fuck_triggers = [
  "fucks <@!896707795703971851>",
  "fucks <@896707795703971851>",
]
fuck_react = [
  "n- no... wait! Help! <@!659714371928326144> please     help me! (˃̣̣̥∧˂̣̣̥`)",
  "w- what are you-? <@!659714371928326144> he's       touching me :'{",
  "what are you-? Hey! Get off! <@!659714371928326144> do something! ( ˃̣̣̥⌓˂̣̣̥)",
  "h- hey, don't- <@!659714371928326144>, he's trying to hurt me! (T﹏T`)",
  "I- I have a boyfriend! Get off! <@!659714371928326144> help me! (┰ω┰。)",
  "hey! stop it!... n- no! <@!659714371928326144> please help me! (✿´•̥̥̥ ‸ •̥̥̥` )",
  "no- I don't- wanna- Help! Please, someone help! <@!659714371928326144> I'm being molested  (T⌓T)",
]
fuck_me_react = [
  "Huh? H- hey~ what are you... doing~? Huh? Y- You want to do it... now? Wai- wha- h- mm- mmmmmuh~ don't... kiss me so... suddenly... m- mmmmhhhh huuh- no... not my... clothes... ah- mmh~ h- hey~ don't- mmmMMMMM HEY! STOP IT! huh? o- .................... I- I'm  sorry! (● ´ ^｀●) I didn't mean to snap! Ohw ( ︶︹︺ ) just leave me alone for a bit okay? I've had a bad day (T~T)",
]

kiss_triggers = [
 "kisses <@!896707795703971851>",
 "kisses <@896707795703971851>",
]
kiss_react = [
  "n- no... wait! Help! <@!659714371928326144> please help me! (˃̣̣̥∧˂̣̣̥`)",
  "w- what are you-? <@!659714371928326144> he's touching me :'{",
  "what are you-? Hey! Get off! <@!659714371928326144> do something! ( ˃̣̣̥⌓˂̣̣̥)",
  "h- hey, don't- <@!659714371928326144>, he's trying to hurt me! (T﹏T`)",
  "I- I have a boyfriend! Get off! <@!659714371928326144> help me! (┰ω┰。)",
  "hey! stop it!... n- no! <@!659714371928326144> please help me! (✿´•̥̥̥ ‸ •̥̥̥` )",
  "no- I don't- wanna- Help! Please, someone help! <@!659714371928326144> I'm being molested (T⌓T)",
]
kiss_me_react = [
  "Huh? H- Hey! Not so... sudden~ (≈≧ܫ≦≈)",
  "Hu- wha- hhhmmmmmmmmmmm-  (ꈍ⌓ꈍ✿) ...... 𝙠𝙞𝙨𝙨 𝙢𝙚 𝙢𝙤𝙧𝙚~  ( づ￣ ³￣ )づ",
  "u- mmmmmmmnng~ you make my heart race ♡  (♡´･ᴗ･`♡)",
 ]

hug_triggers = [
  "hugs <@!896707795703971851>",
  "hugs <@896707795703971851>",
]
hug_react = [
  "Hey, what are you...?! H- huh? U- h- hmmmmmmmmmmm~ （˶′◡‵˶）",
  "I... I have a boyfriend, but I guess a hug is fine?  ( ⊃ ‿ ⊂)",
]
hug_me_react = [
  "Yaayy a huug ( つ´∀｀)つ",
  "Y- you want to hug... me...?  (♡´･ᴗ･`♡)  How could I say no?  (｡^ ‿ ^｡)",
  "ＧＩＶＥ  ＨＵＧＧＩＥ  ＷＵＧＧＩＥＳ ( • ө • )♡",
]

hey_triggers = [
  "hey",
  "hai",
  "hello",
  "bonjour",
  "hola",
  "helo",
  "hewo",
  "hewwo",
  "good day",
  "hi",
]
hey_react = [
  "Hey! (✿◠‿◠)",
  "Hello! ʕ·ᴥ·ʔ",
  "Heyy~ ٩( ^ᴗ^ )۶",
  "Haiiii~ ヾ( ＾∇ ＾ )",
  "Hewwo~ ( ﾟ▽ﾟ )/",
  "Hai! ( ^ _ ^)/",
  "Hello good sir~  ( -ω-ゞ",
  "Hello! ヽ(^ ◇ ^*)/",
]
hey_me_react = [
  "Hello sweety~ ٩( ^ᴗ^ )۶",
  "Hey~ (*￣∇￣*)",
  "I was wondering when you would come back to see me~ (♡´･ᴗ･`♡)",
  "Heyo! ٩( ^ᴗ^ )۶",
  "You finally came back to see me! (*￣∇￣*)",
  "Yay! You're back! （＾∀＾）",
  "You're back! I'm so happy see see you again~ (˵•ᗜ•˵✿)",
  "( ﾉ^ ω ^)ﾉﾟ Master! You're back!",
  "Hello master~  ヾ(・ω・*)ノ",
]

gn_triggers = [
  "gn",
  "good night",
  "to bed",
  "to sleep",
  "nighty",
]
gn_react = [
  "Byyee~ ／(^ ㅅ ^)＼",
  "Good night~ Have a good sleep! (๑╹ᆺ╹ )",
]
gn_me_react = [
  "Huh? You- ... you're leaving already? Ohw ( ︶︹︺ ) so I'm going to be alone again for now ( ◞‸◟`) Good night, and have a good sleep (● ´ ^｀●)",
  "*yaaaawn* Huh? You're sleepy already? Me too... let's sleep together in one bed  (♡´･ᴗ･`♡)",
  "You're going to sleep? Me too... See you tomorrow, darling~  (♡´･ᴗ･`♡)",
  "I'm tired too... Good night, and sleep well~  ฅ(ﾐ~ᆽ~ﾐ)∫",
]

mean_triggers = [
  "kys",
  "kill yourself",
  "whore",
  "bitch",
  "cunt",
  "stupid",
  "ugly",
  "piece of shit",
  "fuck you",
  "fuck off",
  "dum",
  "hang yourself",
  "commit suicide",
  "stfu",
  "shut up",
  "shut it",
  "shut the f",
  "hang urself",
  "kill urself",
  "dumb",
  "piece o shit",
  "piece o' shit",
  "commit die",
  ]
mean_react = [
  "● ﹏ ●",
  "( ˃̣̣̥⌓˂̣̣̥)",
  "(T⌓T)",
  "(✿´•̥̥̥ ‸ •̥̥̥` )",
  "( ╥﹏╥) ノシ",
  "(つ ﹏< 。)",
  "ʕ>⌓<｡ʔ",
  "(T﹏T`)",
  "( つ﹏⊂ )",
  "(┰ω┰。)",
  "ヽ(T-T )ノ",
  "˚‧ º·(˚ ˃̣̣̥᷄⌓˂̣̣̥᷅ )‧º·˚",
  "( ಥ ﹏ ಥ )",
  "(ￗ﹏ￗ)",
  "(✖﹏✖)",
  "‧º·(˃̣̣̥︿˂̣̣̥)‧º·",
  "(´͈ ⌓ `͈ )",
  "( ☍﹏⁰ ) ｡",
  "˚‧º·(˃̣̣̥∩˂̣̣̥`)‧º·",
  "( T⌓T )",
  "(´°̥̥̥̥̥̥̥̥ω°̥̥̥̥̥̥̥̥｀)",
  "(┳ ◇ ┳)",
  "（´ ヘ｀；）",
  "( / ω＼)",
  "(✿´•̥̥̥︿•̥̥̥` )",
  "(✿ɵ̥̥︵ɵ̥̥)",
  "(✿๑•́∧•̩̥̀๑)",
  "ʕ ಡ ﹏ ಡ ʔ",
  "(╥_╥)",
  "(.づ◡﹏◡)づ.",
  "( ´ ｰ `)",
  "( T⌓T)",
  "( ◞‸◟`)",
  "(● ´ ^｀●)",
]
mean_me_react = [
  "Wha-? But...(つ ﹏ <。) I'm sorry! I didn't mean to make master mad! I swear! Please forgive me( ˃̣̣̥⌓˂̣̣̥) I won't do it again\n(.づ◡﹏◡)づ."
]

feet_lick_triggers = [
  "licks <@896707795703971851> feet",
  "licks <@896707795703971851>s feet",
  "licks <@896707795703971851> s feet",
  "licks <@896707795703971851>'s feet",
  "licks <@896707795703971851> 's feet",
    "licks <@!896707795703971851> feet",
  "licks <@!896707795703971851>s feet",
  "licks <@!896707795703971851> s feet",
  "licks <@!896707795703971851>'s feet",
  "licks <@!896707795703971851> 's feet",
]
feet_lick_react = [
  "Huh-? Hey! AAAAAh- a- h- hnnnng~  (ꈍoꈍ)........ I mean- Hey! Stop it! Those feet belong to my master!  >~<",
]
feet_lick_me_react = [
  "ah- hnnnnng~ heyyy!~ Not so sudden  (*>ω<*)",
  "Hehe, you sure love playing with me feet, don't you, master?  ԅ(≖◡≖ԅ)",
]

dog_triggers = [
  "bark",
  "woof",
  "borf",
  "barf",
  "wuff",
]
dog_react = [
  "NYAAAAA (°Д°)",
  "AAAAAAAAAAAAAAAAAAAAAAAAA  ヾ(ﾟдﾟ)ﾉ゛",
  "NYA NYA NYA NYA NYA  (ノ ′Дヾ )",
  "AAAAAAAA  〣 ( ºΔº ) 〣",
  "NOOO JUST LEAVE ME ALONE ( ⊃ д ⊂ )",
]

nice_age = [
  "10",
  "11",
  "12",
  "13",
  "14",
  "15",
]

love_triggers = [
  "i love",
  "i <3",
  "ily",
]
love_react = [
  "**No! Stay away! ‧º·(˃̣̣̥︿˂̣̣̥)‧º·**",
]
love_me_react = [
  "I love you too! I love you so much it's breaking me ʕ>⌓<｡ʔ",
]


client = discord.Client()

@client.event
async def on_message(message): 
  if message.author == client.user:
    return

  if any(word in message.content.lower() for word in nigger_triggers): 
    await message.channel.send(random.choice(nigger_react))

  if 'uwu' in message.content.lower():
    await message.channel.send('OwO')

  if 'owo' in message.content.lower():
    await message.channel.send('UwU')

  if any(word in message.content.lower() for word in nya_triggers): 
    await message.channel.send(random.choice(nya_react))

  if any(word in message.content.lower() for word in pet_triggers): 
    await message.channel.send(random.choice(pet_react))

  if any(word in message.content.lower() for word in dont_be_racist_triggers): 
    await message.channel.send('<:consentMegaYes:885974128526512158>')

  if any(word in message.content.lower() for word in racist_triggers) and not any(word in message.content.lower() for word in dont_be_racist_triggers) and not any(word in message.content.lower() for word in gn_triggers) and(not "opinion" in message.content.lower() and not any(word in message.content.lower() for word in ping)):
    await message.channel.send('<:emojigrin:882625052309340240>')

  if any(word in message.content.lower() for word in fuck_triggers) and message.author.id == 659714371928326144: 
   await message.channel.send(random.choice(fuck_me_react))

  elif any(word in message.content.lower() for word in fuck_triggers):
    await message.channel.send(random.choice(fuck_react))

  if any(word in message.content.lower() for word in kiss_triggers) and message.author.id == 659714371928326144: 
   await message.channel.send(random.choice(kiss_me_react))

  elif any(word in message.content.lower() for word in kiss_triggers):
    await message.channel.send(random.choice(kiss_react))

  if any(word in message.content.lower() for word in hug_triggers) and message.author.id == 659714371928326144: 
   await message.channel.send(random.choice(hug_me_react))

  elif any(word in message.content.lower() for word in hug_triggers):
    await message.channel.send(random.choice(hug_react))

  if any(word in message.content.lower() for word in hey_triggers) and any(word in message.content.lower() for word in ping) and not "nigger" in message.content.lower() and not "black" in message.content.lower() and message.author.id == 659714371928326144: 
   await message.channel.send(random.choice(hey_me_react))

  elif any(word in message.content.lower() for word in hey_triggers) and any(word in message.content.lower() for word in ping) and not "nigger" in message.content.lower() and not "black" in message.content.lower():
    await message.channel.send(random.choice(hey_react))

  if any(word in message.content.lower() for word in mean_triggers) and any(word in message.content.lower() for word in ping) and message.author.id == 659714371928326144: 
   await message.channel.send(random.choice(mean_me_react))

  elif any(word in message.content.lower() for word in mean_triggers) and any(word in message.content.lower() for word in ping):
    await message.channel.send(random.choice(mean_react))

  if "just joined. what a loser!" in message.content.lower():
    await message.channel.send(random.choice(hey_react))

  if any(word in message.content.lower() for word in gn_triggers) and any(word in message.content.lower() for word in ping) and message.author.id == 659714371928326144: 
   await message.channel.send(random.choice(gn_me_react))

  elif any(word in message.content.lower() for word in gn_triggers) and any(word in message.content.lower() for word in ping):
    await message.channel.send(random.choice(gn_react))

  if any(word in message.content.lower() for word in feet_lick_triggers) and message.author.id == 659714371928326144: 
   await message.channel.send(random.choice(feet_lick_me_react))

  elif any(word in message.content.lower() for word in feet_lick_triggers):
    await message.channel.send(random.choice(feet_lick_react))

  if any(word in message.content.lower() for word in dog_triggers): 
    await message.channel.send(random.choice(dog_react))

  if any(word in message.content.lower() for word in ping) and "opinion" in message.content.lower() and "nigger" in message.content.lower():
      await message.channel.send("I fucking **HATE** niggers!")

  if any(word in message.content.lower() for word in ping) and("are you" in message.content.lower() or "is" in message.content.lower() or "r u" in message.content.lower() or "are u" in message.content.lower() or "r you" in message.content.lower()) and("nigger" in message.content.lower() or "black" in message.content.lower()):
      await message.channel.send("**No!** I fucking **HATE** niggers!")

  if "🧑🏿‍🦲" in message.content.lower():
    await message.channel.send(random.choice(nigger_react))

  if any(word in message.content() for word in nice_age):
    await message.reply(":hot_face:")

  if any(word in message.content.lower() for word in love_triggers) and any(word in message.content.lower() for word in ping) and message.author.id == 659714371928326144: 
   await message.channel.send(random.choice(love_me_react))

  elif any(word in message.content.lower() for word in gn_triggers) and any(word in message.content.lower() for word in ping):
    await message.channel.send(random.choice(love_react))

    







keep_alive.keep_alive()
client.run(os.environ['TOKEN'])


