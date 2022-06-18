import pandas as pd 
import plotly.figure_factory as ff 
import statistics as st 
import random

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

population_mean = st.mean(data)
population_std = st.stdev(data)

print(f"mean and standard deviation of population is : {population_mean,population_std}")

fig= ff.create_distplot( [data], ["temp"], show_hist= False)
# fig.show()

data_set = []
for i in range(0,100):
    random_index = random.randint(0,len(data)) # 22
    value = data[random_index] #data[22]
    data_set.append(value)
    
mean = st.mean(data_set)
std = st.stdev(data_set)
# print(f"\nmean and standard deviation of sample is : {mean,std}")

def random_set_of_mean(counter):
    data_set = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data) - 1 ) # 22
        value = data[random_index] #data[22]
        data_set.append(value)
    
    mean = st.mean(data_set)
    return mean
    
def setup():
    mean_list = []
    for i in range(0,1000):
        set = random_set_of_mean(100)
        mean_list.append(set)
    mean = st.mean(mean_list)
    std = st.stdev(mean_list)
    print(f"\nmean and standard deviation of sample is : {mean,std}")
    show_fig(mean_list)
    
def show_fig(m_list):
    fig = ff.create_distplot([m_list],["mean of list"], show_hist =False)
    fig.show()

setup()
# mean of sample = mean of population

#Standard deviation of the sampling mean = 1/10 of Population Standard deviation
# SD of sample = 1/10 * 5.69
# SD 0f sample - 0.5
