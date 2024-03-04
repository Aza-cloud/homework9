import pandas as pd
df = pd.read_csv('california_housing_train.csv')
filter = (df['population'] > 0) & (df['population'] < 500)
filter_df = df[filter]
avg = filter_df['median_house_value'].mean()