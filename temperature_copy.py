import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

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
    fig = ff.create_distplot([df], ["Temperature"], show_hist = False)
    fig.show()

def set_up():
    mean_list = []

    for i in range(1, 1000):
        set_off_mean = random_mean(100)
        mean_list.append(set_off_mean)

    show_figure(mean_list)
    mean = statistics.mean(mean_list)
    print("Mean of meanlist is " + str(mean))

def find_std_deviation():
    mean_list = []

    for i in range(0, 1000):
        set_off_mean = random_mean(100)
        mean_list.append(set_off_mean)
    
    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of mean list is " + str(std_deviation))

set_up()
find_std_deviation()

##Mean = statistics.mean(data)
##print("Mean of data is " + str(Mean))