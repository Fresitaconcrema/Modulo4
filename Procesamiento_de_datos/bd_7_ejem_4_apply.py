import pandas as pd
import numpy as np
#usar apply para aplicar funciones a Series y DataFrames

df = pd.read_csv('drive-download/new_york_times_bestsellers-dirty.csv', sep=',', index_col=0)

def years_since_bestseller(value):
    as_datetime = pd.to_datetime(value, unit='ms')
    today = pd.to_datetime('today')
    difference_in_days = (today - as_datetime).days
    in_years = difference_in_days / 365

    return in_years

output_1 = df['published_date.numberLong'].apply(years_since_bestseller)

print(output_1)

def weeks_on_list_percentage_of_maximum(value, max_weeks_on_list):
    percentage = value * 100 / max_weeks_on_list
    as_string = f'{percentage:.2f}%'

    return as_string

output_2 = df['weeks_on_list.numberInt'].apply(weeks_on_list_percentage_of_maximum, args=(df['weeks_on_list.numberInt'].max(),))

print(output_2)


