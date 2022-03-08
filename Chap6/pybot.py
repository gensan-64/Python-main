command_file = open('pybot.txt', encoding='utf-8')
raw_data = command_file.read()
command_file.close()
lines = raw_data.splitlines()

bot_dict = {}
for line in lines:
    word_list = line.split(',')
    key = word_list[0]
    response = word_list[1]
    bot_dict[key] = response

while True:
    command = input('pybot> ')
    response = ''
    for message in bot_dict:
        if message in command:
            response = bot_dict[message]
            break
    if '和暦' in command:
        wareki, year_str = command.split()
        year = int(year_str)
        if year >= 2019:
            reiwa = year - 2018
            response = f'西暦{year}年ハ、令和{reiwa}年デス'
        elif year >= 1989:
            heisei = year - 1988
            response = f'西暦{year}年ハ、平成{heisei}年デス'
        else:
            response = f'西暦{year}年ハ、平成ヨリ前デス'

    if not response:
        response = '何ヲ言ッテルカ、ワカラナイ'
    print(response)

    if 'さようなら' in command:
        break
