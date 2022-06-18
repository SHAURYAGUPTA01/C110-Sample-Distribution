import pandas as pd 
import plotly.figure_factory as ff 
import statistics as st 
import random

df = pd.read_csv("newdata.csv")
data = df["average"].tolist()

population_mean = st.mean(data)
population_std = st.stdev(data)

print(f"mean and standard deviation of population is : {population_mean,population_std}\n")

fig= ff.create_distplot( [data], ["average"], show_hist= False)
# fig.show()

def sample( counter ):
    data_set = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        data_set.append(value)
    mean = st.mean(data_set)
    return mean

def setup():
    mean_list=[]
    for i in range(0,1000):
        s = sample(100)
        mean_list.append(s)
    mean = st.mean(data)
    std = st.stdev(data)
    print(f"mean and standard deviation of sample is : {mean,std}")
    show_fig(mean_list)

def show_fig( mean):
    fig = ff.create_distplot([mean],["sample mean"],show_hist=False)
    fig.show()
    
setup()