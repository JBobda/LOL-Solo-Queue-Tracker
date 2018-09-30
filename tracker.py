import requests
from bs4 import BeautifulSoup

#Url of the webpage with the data about North American rankings
url = "https://www.leagueofgraphs.com/rankings/summoners/na"

#Make the request to the webpage and store the HTML text
page = requests.get(url)

#Create a beautiful soup object to parse the html file
soup = BeautifulSoup(page.content, 'html.parser')

#Isolate the Div and table where the leaderboard is stored
div = soup.find('div', {'class': 'large-16 large-centered medium-21 medium-centered small-24 columns'})
table = div.find('table')

print("NORTH AMERICAN LEAGUE OF LEGENDS RANKINGS\n")

#Loop that moves through each tr element in the table
for tr in table.find_all('tr'):
    #If td element exists within tr element, create td object and scrape data from it
    if tr.find('td'):
        td = tr.find_all('td')
        if (len(td) >= 2):
            place = td[0].text.strip()
            info = td[1].text.strip()
            name = td[1].find('a').find('div').find('div', {'class' : 'txt'}).find('span').text.strip()
            points = td[2].find_all('i')[0].text.strip()
            wins = td[2].find_all('i')[1].text.strip()
            print(place.ljust(3), name.ljust(20), points.ljust(4), wins.rjust(3))
