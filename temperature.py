import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("data.csv")
data = df["temp"].tolist()
'''new_data = []
for i in range(0, 1000):
    new_data.append(data[random.randint(0, len(data))])

mean = statistics.mean(data)
standard_deviation = statistics.stdev(data)
new_data_mean = statistics.mean(new_data)
new_data_std_deviation = statistics.stdev(new_data)
print("The mean of the data is " + str(mean))
print("The standard deviation is " + str(standard_deviation))
print("The sample data mean is " + str(new_data_mean))
print("The sample data standard deviation is " + str(new_data_std_deviation))'''

def random_mean(counter):
    dataset = []

    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_figure(mean_list):
    df = mean_list
    fig = ff.create_distplot([data], ["Temperature"], show_hist = False)
    fig.show()
'''fig.add_trace(go.Scatter(
    x = [mean, mean],
    y = [0, 1],
    mode = "lines",
    name = "Mean"
))'''

def set_up():
    mean_list = []

    for i in range(1, 1000):
        set_off_mean = random_mean(100)
        mean_list.append(set_off_mean)

    show_figure(mean_list)

set_up()