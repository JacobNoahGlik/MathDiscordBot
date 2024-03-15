import discord
from config import __BOTTOKEN__ as __TOKEN__
from knowledge import __COMPARE__, __GREEK__, __INTEGRALS__, __KNOWN__
from knowledge import __POWERS__, __REPLACE__, __SUPERSCRIPT__, __SUPERSCRIPT_GREEK_LETTERS__

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f'got message "{message.content}"')
    if message.author == client.user:
        return

    if message.content.startswith('$math '):
        print(f'replying to {message.content} with an equation')
        msg = message.content.split('$math ')
        if len(msg) < 2:
            await message.reply('Hi I am your math bot. I can help you build an equation. Try `$math <theta>(n^2)` to get `Θ(n²)`', mention_author=True)
        elif msg[1].lower() == 'help':
            await message.reply(known_keywords(), mention_author=True)
        elif message.content.startswith('$math help'):
            await message.reply(help(message.content), mention_author=True)
        else:
            response = message.content.split('$math ')[1]
            await message.reply(mathify(response), mention_author=True)
    elif message.content.startswith('$math-replace'):
            embedVar = discord.Embed(title=message.author, color=0x00ff00)
            embedVar.add_field(name="Org Msg", value=message.content.split('$math-replace ')[1], inline=False)
            embedVar.add_field(name="Fixed", value=mathify(message.content.split('$math-replace ')[1]), inline=False)
            await message.delete()
            await message.channel.send(embed=embedVar)

def mathify(response):
    response = power_replace(response)
    response = power_parenth(response)
    global __REPLACE__
    for key, value in __REPLACE__.items():
        while (key.lower() in response.lower()):
            index_found_at = response.lower().index(key.lower())
            response = response[:index_found_at] + value + response[index_found_at + len(key):]
    return response

def known_keywords():
    global __KNOWN__
    pairs = ''
    for key, value in __KNOWN__.items():
        pairs += f'\n`{key}` -> "{value}"'
        if value == 'integral-symbol':
            pairs += ' (run `$math help integrals` for a list of all known integral names and symbols)'
        elif value == 'greekLetter':
            pairs += ' (run `$math help greekLetters` for a list of all known greek letters'
        elif key == '^int':
            pairs += ' (run `$math help powers` for a list of all known powers)'
        elif key == '<set-theory-symbol-name>':
            pairs += ' (run `$math help compare` for a list of all known set theory symbols)'
    return f"""Hi I am a math bot. I can help you building an equation. Try using `$math <<your math here>>`
    known keywords:{pairs}
    Note: if your power is non-numeric use `^[<power>]`. ex: `x^[n + (5-3)]`
    Note: I'm not case sensitive :nerd:
    """

# callable
def power_replace(message: str) -> str:
    while '^' in message and message.find('^') + 1 < len(message) and message[message.find('^') + 1].isdigit():
        index = message.find('^')
        message = _power_replace(message, index)
    return message
def _power_replace(message: str, index: int) -> str:
    i = index + 1
    while i < len(message) and message[i].isdigit():
        i += 1
    global __POWERS__
    power = ''.join([__POWERS__[f'^{ch}'] for ch in message[index+1:i]])
    return message[:index] + power + message[i:]
# callable
def power_parenth(message:str) -> str:
    while '^[' in message:
        index = message.find('^[')
        i = index + 2
        while i < len(message) and message[i] != ']':
            i += 1
        power = _make_upper(message[index + 2 : i])
        message = message[: index] + power + message[i + 1:]
    return message

def _make_upper(message: str) -> str:
    global __SUPERSCRIPT_GREEK_LETTERS__
    global __SUPERSCRIPT__
    for key, value in __SUPERSCRIPT_GREEK_LETTERS__.items():
        message = message.replace(key, value)
    for key, value in __SUPERSCRIPT__.items():
        message = message.replace(key, value)
    return message
    

def help(response: str) -> str:
    arg = response[response.index('help') + 5:]
    
    if arg.lower().endswith('greekletters'):
        global __GREEK__
        dict_type = __GREEK__
        path = 'greek-letters'
    elif arg.lower().endswith('integrals'):
        global __INTEGRALS__
        dict_type = __INTEGRALS__
        path = 'integrals'
    elif arg.lower().endswith('powers'):
        global __POWERS__
        dict_type = __POWERS__
        path = 'powers'
    elif arg.lower().endswith('compare'):
        global __COMPARE__
        dict_type = __COMPARE__
        path = 'set-theory'
    else:
        return f"Sorry I don't know what you mean by `{arg}`. Did you mean `powers`, `greekLetters`, `compare`, or `integrals`?"
    pairs = ''
    for key, value in dict_type.items():
        pairs += f'\n`{key}` -> "{value}"'
    return f"Here are all the keywords I know in the mathamatics-{path} area: {pairs} \nNote: I'm not case sensitive :nerd:"
    
def run():
    client.run(__TOKEN__)

if __name__ == '__main__' :
    print('running mathbot ...')
    run()
    print('ERROR: runtime complete')