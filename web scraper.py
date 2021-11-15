import pandas as pd
import requests
from bs4 import BeautifullSoup

page = requests.get('https://www.weather.com/wx/today/?lat=41.10&lon=-80.65&locale=en_US&par=google&temp=f')
soup = BeautifullSoup(page.content, 'html.parser')
week = soup.find(id='WeatherTable')
# print(week)

items = week.find_all(class_= 'Column--innerWrapper--1vUk1')


#print(items[0].find(class_='Ellipsis--ellipsis--1sNTm').get_text())
#print(items[0].find(class_='TemperatureValue').get_text())
#print(items[0].find(class_='SegmentPrecipPercentage').get_text())

period_name = [item.find(class_='Ellipsis--ellipsis--1sNTm').get_text() for item in items]
short_desciptions = [item.find(class_='TemperatureValue').get_text() for item in items]
temperatures = [item.find(class_='SegmentPrecipPercentage').get_text() for item in items]

#print(period_name)
#print(short_desciptions)
#print(temperatures)

weather_stuff = pd.DataFrame(
    {
        'period': period_name,
        'short_desciptions': short_desciptions,
        'temperatures': temperatures,
        })


print(weather_stuff)

weather_stuff.to_csv('weather.csv')