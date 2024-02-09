import requests
from bs4 import BeautifulSoup
import argparse

#This code has been made usng argparse method rather than typer

#Provides task description

argparser=argparse.ArgumentParser(description = "displays weather of current city (Simrol in this case) from two reliable sources; Weather.com and TimeandDate.com")

#Verbose arguement provides full weather description if not then it shall display only temperature

argparser.add_argument("--verbose", help="gives full weather information", action="store_true")

#Obtains request from URL site

weather_com = requests.get("https://weather.com/en-IN/weather/today/l/2e5cd547a79cf6348db604bfc97b288876b84c0c0724347475ce724fdbf8c9c5")
tad_com=requests.get("https://www.timeanddate.com/weather/@10689521")

#The content is parsed from the site

weather_comSoup = BeautifulSoup(weather_com.content, "html.parser")
tad_comSoup=BeautifulSoup(tad_com.content, "html.parser")

#Valuable information from the site is scarpped from the site

weather_comTemp = weather_comSoup.find('span', {"data-testid":"TemperatureValue"}).text
weather_comVerboseInfo = weather_comSoup.find('div',{"class":"CurrentConditions--primary--2DOqs"})
tad_comTemp = tad_comSoup.find('div',{"class":"h2"}).text
tad_comVerboseInfo = tad_comSoup.find('div',{"id":"qlook"})
weather_comVerboseInfoT = ""
tad_comVerboseInfoT = ""

#The data is accessed and displayed

for tag in weather_comVerboseInfo.children:

    weather_comVerboseInfoT+=(tag.text+"\n")

for tag in tad_comVerboseInfo.children:

    if tag in tad_comSoup.find_all('p'):
        for tag1 in tag.children:
            tad_comVerboseInfoT+=(tag1.text+"\n")
    else:
        tad_comVerboseInfoT+=(tag.text+"\n")

args = argparser.parse_args()

if args.verbose:
    print("Weather data:\n\nWeather.com says:-\n\n", weather_comVerboseInfoT,"\n\nAlso, timeaanddate.com says:-\n\n", tad_comVerboseInfoT)
else:
    print("Temperature data:\n\nWeather.com says:-\n\n", weather_comTemp, "\nWhile timeanddate.com says:-\n\n", tad_comTemp)