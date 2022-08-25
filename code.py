import random
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].to_list()
print("the mean of the data=",statistics.mean(data))
print("the standard deviation of the data =",statistics.stdev(data))


def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)

mean=statistics.mean(mean_list)
print("the mean of the sampling distrubution=",mean)
stddev=statistics.stdev(mean_list)
print("the standard deviation of the sampling distrubution =",stddev)

fig=ff.create_distplot([mean_list],["readingtime"],show_hist=False)


first_stddev_start,first_stddev_end=mean-stddev,mean+stddev
second_stddev_start,second_stddev_end=mean-(2*stddev),mean+(2*stddev)
third_stddev_start,third_stddev_end=mean-(3*stddev),mean+(3*stddev)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1.2],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_stddev_start,first_stddev_start],y=[0,1.2],mode="lines",name="std dev 1 start"))
fig.add_trace(go.Scatter(x=[first_stddev_end,first_stddev_end],y=[0,1.2],mode="lines",name="std dev 1 end"))

fig.add_trace(go.Scatter(x=[second_stddev_start,second_stddev_start],y=[0,1.2],mode="lines",name="std dev 2 start"))
fig.add_trace(go.Scatter(x=[second_stddev_end,second_stddev_end],y=[0,1.2],mode="lines",name="std dev 2 end"))

fig.add_trace(go.Scatter(x=[third_stddev_start,third_stddev_start],y=[0,1.2],mode="lines",name="std dev 3 start"))
fig.add_trace(go.Scatter(x=[third_stddev_end,third_stddev_end],y=[0,1.2],mode="lines",name="std dev 3 end"))

fig.show()



df=pd.read_csv("sample_2.csv")
data=df["reading_time"].to_list()
mean_sample1=statistics.mean(data)
print("mean of sample1=",mean_sample1)

fig=ff.create_distplot([mean_list],["readingtime"],show_hist=False)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1.2],mode="lines",name="mean"))

fig.add_trace(go.Scatter(x=[mean_sample1,mean_sample1],y=[0,1.2],mode="lines",name="mean"))

fig.add_trace(go.Scatter(x=[first_stddev_start,first_stddev_start],y=[0,1.2],mode="lines",name="std dev 1 start"))
fig.add_trace(go.Scatter(x=[first_stddev_end,first_stddev_end],y=[0,1.2],mode="lines",name="std dev 1 end"))

fig.add_trace(go.Scatter(x=[second_stddev_start,second_stddev_start],y=[0,1.2],mode="lines",name="std dev 2 start"))
fig.add_trace(go.Scatter(x=[second_stddev_end,second_stddev_end],y=[0,1.2],mode="lines",name="std dev 2 end"))

fig.add_trace(go.Scatter(x=[third_stddev_start,third_stddev_start],y=[0,1.2],mode="lines",name="std dev 3 start"))
fig.add_trace(go.Scatter(x=[third_stddev_end,third_stddev_end],y=[0,1.2],mode="lines",name="std dev 3 end"))

fig.show()

z_score=(mean-mean_sample1)/stddev
print("z score of sample1 is=",z_score)


