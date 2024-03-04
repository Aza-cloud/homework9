#Задача 1
# Дан файл california_housing_train.csv. Определить среднюю стоимость дома ,
# где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
# Используйте модуль pandas.

import pandas as pd
df = pd.read_csv('california_housing_train.csv')
filter = (df['population'] > 0) & (df['population'] < 500)
filter_df = df[filter]
avg = filter_df['median_house_value'].mean()