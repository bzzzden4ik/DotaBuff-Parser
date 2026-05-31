import requests
import fake_useragent
import pandas as pd
import time
from bs4 import BeautifulSoup

url = 'https://www.dotabuff.com/players/1486361884/matches?enhance=overview&page='
url_before = 'https://www.dotabuff.com/players/'
url_after = '/matches?enhance=overview&page='
url_match = 'https://www.dotabuff.com/matches/'

user = fake_useragent.FakeUserAgent().random

headers = {'User-Agent': user}

user_id = input('Enter UserId: ')

response = requests.get(f'{url_before}{user_id}{url_after}1', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
nickname = soup.find('h1').text.rstrip('Matches')
print(nickname)
last_page = soup.find('span', class_='last').find('a').get('href').split('page=')[1]
print(last_page)

table_data = {
    'Герой': [],
    'Средний ранг': [],
    'ID Матча': [],
    'Дата': [],
    'Результат': [],
    'Режим лобби': [],
    'Режим игры': [],
    'Продолжительность': [],
    'Убийста': [],
    'Смерти': [],
    'Помощи': [],
    'КДА': [],
    # 'Общая ценность': [],
    # 'Добито крипов': [],
    # 'Не отдано крипов': [],
    # 'XPM': [],
    # 'GPM': [],
    # 'Урон по врагам': [],
    # 'Урон по постройкам': []
}

for page in range(1, int(last_page) + 1):
    response = requests.get(f'{url_before}{user_id}{url_after}{page}', headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    print(f'{url_before}{user_id}{url_after}{page}')
    rows = soup.find('table').find('tbody').find_all('tr')
    for row in rows:
        row_data = row.find_all('td')
        hero = row_data[1].find('a').text
        average_rank = row_data[1].find('div', class_='subtext').text
        match_id = row_data[3].find('a').get('href').split('/')[-1]
        date = row_data[3].find('time').get('title')
        result = row_data[3].find('a').text
        lobby_mode = row_data[4].text.rstrip('All Pick').rstrip('Turbo')
        game_mode = row_data[4].text.lstrip('Ranked').lstrip('Normal')
        duration = row_data[5].text
        kda = row_data[6].find('span', class_='kda-record').find_all('span')
        kills = kda[0].text
        deaths = kda[1].text
        assists = kda[2].text
        table_data['Герой'].append(hero)
        table_data['Средний ранг'].append(average_rank)
        table_data['ID Матча'].append(int(match_id))
        table_data['Дата'].append(date)
        table_data['Результат'].append(result)
        table_data['Режим лобби'].append(lobby_mode)
        table_data['Режим игры'].append(game_mode)
        table_data['Продолжительность'].append(duration)
        table_data['Убийста'].append(int(kills))
        table_data['Смерти'].append(int(deaths))
        table_data['Помощи'].append(int(assists))
        table_data['КДА'].append(float((int(kills) + int(assists)) / max(int(deaths), 1)))
        
        # response = requests.get(f'{url_match}{match_id}', headers=headers)
        # soup = BeautifulSoup(response.text, 'lxml')
        # tables = soup.find_all('table', class_='match-team-table')
        # found = False
        # for team in tables:
        #     players = team.find('tbody').find_all('tr')
        #     for player in players:
        #         player_id = player.get('class')[-1].split('-')[-1]
        #         if player_id == user_id:
        #             all_columns = player.find_all('td')
        #             net_worth = float(all_columns[8].text.rstrip('k'))
        #             last_hits = all_columns[9].text
        #             denies = all_columns[11].text
        #             if last_hits != '-':
        #                 last_hits = int(last_hits)
        #             else:
        #                 last_hits = 0
        #             if denies != '-':
        #                 denies = int(denies)
        #             else:
        #                 denies = 0
        #             gpm = float(all_columns[12].text.rstrip('k'))
        #             xpm = float(all_columns[14].text.rstrip('k'))
        #             dmg = all_columns[15].text.rstrip('k')
        #             bld = all_columns[17].text.rstrip('k')
        #             if dmg != '-':
        #                 dmg = float(dmg)
        #             else:
        #                 dmg = 0
        #             if bld != '-':
        #                 bld = float(bld)
        #             else:
        #                 bld = 0
        #             table_data['Общая ценность'].append(net_worth)
        #             table_data['Добито крипов'].append(last_hits)
        #             table_data['Не отдано крипов'].append(denies)
        #             table_data['GPM'].append(gpm)
        #             table_data['XPM'].append(xpm)
        #             table_data['Урон по врагам'].append(dmg)
        #             table_data['Урон по постройкам'].append(bld)
        #             found = True
        #             break
        #     if found:
        #         break
                    
df = pd.DataFrame(table_data)
df.to_excel(f'{nickname}.xlsx', index=False)