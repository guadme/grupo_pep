# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 15:39:38 2020

@author: Guillermo Adam Merino
"""

import os #acceder al sistema operativo
import pandas as pd #libreria que permite tener dataframes, python puede gestionar matrices de datos, y se importa como "pd", que es un nickname, así lo llamaremos pd
import numpy as np #para hacer operaciones númericas con python
import matplotlib.pyplot as plt #para hacer gráficos
from datetime import date #para tratar fechas
from datetime import datetime #para tratar horas



os.getcwd()
os.chdir('C:/Users/guill/OneDrive/Escritorio/master/grupo_data/booking') 
#directorio del csv

booking = pd.read_csv('hotel_bookings.csv', sep=',', decimal='.') #cargo el csv

booking.info() #veo las columnas y que tipod e dato son
booking.shape #dimensiones del dataset
booking.head #primeros registros
booking.tail #ultimos registros


# Si nos fijamos en el dataset, hay una columna para el año, una columna para el mes,
#una columna para el dia del mes, y otra columna (que no utilizo ahora) de la semana del año

#Entonces nos conviene tener una columna con la fecha completa (año-mes-dia) para poder así
#a la hora de filtrar por fechas hcaerlo más comodo.

#Como la columna mes es un nombre, hago una columna con el numero de mes que le corresponde.
# ejemplo: enero -> 1, diciembre -> 12 
#la columna se llama "arrival_date_month"

booking.loc[ (booking["arrival_date_month"] == "January"), "arrival_date_month_num" ] = 1
booking.loc[ (booking["arrival_date_month"] == "February"), "arrival_date_month_num" ] = 2
booking.loc[ (booking["arrival_date_month"] == "March"), "arrival_date_month_num" ] = 3
booking.loc[ (booking["arrival_date_month"] == "April"), "arrival_date_month_num" ] = 4
booking.loc[ (booking["arrival_date_month"] == "May"), "arrival_date_month_num" ] = 5
booking.loc[ (booking["arrival_date_month"] == "June"), "arrival_date_month_num" ] = 6
booking.loc[ (booking["arrival_date_month"] == "July"), "arrival_date_month_num" ] = 7
booking.loc[ (booking["arrival_date_month"] == "August"), "arrival_date_month_num" ] = 8
booking.loc[ (booking["arrival_date_month"] == "September"), "arrival_date_month_num" ] = 9
booking.loc[ (booking["arrival_date_month"] == "October"), "arrival_date_month_num" ] = 10
booking.loc[ (booking["arrival_date_month"] == "November"), "arrival_date_month_num" ] = 11
booking.loc[ (booking["arrival_date_month"] == "December"), "arrival_date_month_num" ] = 12

#Compruebo que se han asignado correctamente los meses
#veo cuantos registros hay para cada numero de mes
mytable=booking.groupby (['arrival_date_month_num']). size()
print (mytable)


#si cruzamos los valores de meses con los numeros de mes tiene que coincidir el mes 
#que tiene registros con su numero correspondiente

pd.crosstab(booking.arrival_date_month,booking.arrival_date_month_num)

# se ha formado OK la columna

#Ahora que ya tenemos el mes con el numero, creamos una columna con la fecha
#al método datetime le pasamos la columna del año, la columna del mes y la columna del dia
#y de ahi crea la fecha.


booking["Arrival_date"] = pd.to_datetime(dict(year=booking["arrival_date_year"], 
                                         month=booking["arrival_date_month_num"], 
                                         day=booking["arrival_date_day_of_month"]))

# si nos fijamos ahora tenemos una nueva columna llamada "Arrival_date" con la fecha de llegada
#pero nos ha creado junto a la fecha la hora, por lo que tenemos que quitar la hora de la fecha ya
#que no tenemos información sobre ella

#Google me ha dicho que se hace de la siguiente manera y tiene razón xD

booking['Arrival_date'] = pd.to_datetime(booking['Arrival_date']).dt.date

# Con esto hemos creado una columna por la fecha y le hemos quitado la hora
# Ya tenemos la fecha de llegada en una columna

#Ahora voy a ver cuantos registros hay para cada mes
mytable=booking.groupby(["arrival_date_month_num"]). size()
print (mytable)

#Veo lo siguiente:

#   1.0      5929
#   2.0      8068
#   3.0      9794
#   4.0     11089
#   5.0     11791
#   6.0     10939
#   7.0     12661
#   8.0     13877
#   9.0     10508
#   10.0    11160
#   11.0     6794
#   12.0     6780

#Ahora quiero representar graficamente cuantas reservas hay cada mes.
#que en el eje x tenga los numeros del mes del año y en el eje y el numero de registros que
#tiene cada mes. Creo que no sale porque hay que hacer que la variable sea categorica.


plt.hist(booking.arrival_date_month_num)

booking.to_csv("booking_modified.csv")
