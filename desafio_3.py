#!/bin/python3

import json, math

# Benoit - Desafio 3
#
# Crie um objeto com os dias e suas respectivas temperaturas e escreva um algoritmo que receba um vetor do objeto, onde o algortimo deverá escrever as seguintes informações:
#
# 1. Dia com a menor temperatura entre os dias informados
# 2. Dia com a maior temperatura entre os dias informados
# 3. Temperatura média do período
# 4. O número de dias em que a temperatura foi inferior a média anual
#

class Weather:
  min_temp, avg_temp, max_temp, min_days = 0, 0, 0, 0
  weather_list = []

  def __init__(self, data) -> None:
    self.weather_list = data
    
  def minimum_temp(self):
    tmp_min = list(weather_list.items())[0][1]
    for day in self.weather_list:
      if weather_list[day] <= tmp_min:
        tmp_min = weather_list[day]
    self.min_temp = tmp_min
    print("The minimum recorded temperature was {} celsius degrees".format(float(self.min_temp)))

  def maximum_temp(self):
    tmp_max= list(weather_list.items())[0][1]
    for day in self.weather_list:
      if weather_list[day] >= tmp_max:
        tmp_max = weather_list[day]
    self.max_temp = tmp_max
    print("The highest recorded temperature was {} celsius degrees".format(float(self.max_temp)))

  def average_temp(self):
    tmp_sum = 0
    for day in self.weather_list:
        tmp_sum += weather_list[day]
    self.avg_temp = tmp_sum / float(len(weather_list))
    print("The average recorded temperature was {:.1f} celsius degrees".format(float(self.avg_temp)))

  def average_days(self):
    days_sum = 0

    # Just in case you call this function without calling the average first ;)
    if self.avg_temp == 0:
        self.average_temp()

    for day in self.weather_list:
      if weather_list[day] < self.avg_temp:
        days_sum += 1
    self.min_days = days_sum
    print("The temperature was below than the annual average for {} days".format(int(self.min_days)))

# weather_list = {"2022-01-01": -15.0, "2022-01-02": -6.0,"2022-01-13": 0, "2022-01-14": 0}
weather_list = {"2022-01-01": 27.5, "2022-01-02": 27, "2022-01-03": 24, "2022-01-04": 24.2, "2022-01-05": 23.8, "2022-01-06": 23, "2022-01-07": 12.1, "2022-01-08": -12.5, "2022-01-09": 20.9, "2022-01-10": 18, "2022-01-11": 14.2, "2022-01-12": 14.5, "2022-01-13": 14.4}

weather = Weather(weather_list)
weather.minimum_temp()
weather.maximum_temp()
weather.average_temp()
weather.average_days()
