import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_count = data[data['Primary Fur Color'] == 'Gray']
red_count = data[data['Primary Fur Color'] == 'Cinnamon']
black_count = data[data['Primary Fur Color'] == 'Black']

data_dict = {
    "Full color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count]
}

df = pandas.DataFrame(data_dict)

df.to_csv("squirrels_count")