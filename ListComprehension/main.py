# file1 = []
# file2 = []
# result = []
# result22 = []
# with open("text1.txt", "r") as data:
#     file1 = data.readlines()
#
# with open("text2.txt", "r") as data2:
#     file2 = data2.readlines()
#
# must_return = [int(d) for d in file1 if(file2.__contains__(d))]
# print(must_return)
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# result = {word: len(word) for word in sentence.split()}
# print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {key: (value * 9 / 5) + 32 for (key, value) in weather_c.items()}
print(weather_f)
