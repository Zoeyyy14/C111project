import csv
import pandas as pd
import statistics
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go

df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()
# fig=ff.create_distplot([data],["Math Scores"],show_hist=False)
# fig.show()

# mean=statistics.mean(data)
# std=statistics.stdev(data)
# print("Mean of Math Scores Is:",mean)
# print("Standared Deviation Is:",std)

def random_set_mean(c):
    dataset=[]
    for i in range(0,c):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
    set_off_mean=random_set_mean(100)
    mean_list.append(set_off_mean)
mean=statistics.mean(mean_list)
std=statistics.stdev(mean_list)
print("Mean of Sampling Distribution is",mean)
print("Standared Deviation of Sampling Distribution is:",std)

# fig=ff.create_distplot([mean_list],["Student Math"],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.20],mode="lines", name="MEAN"))
# fig.show()

first_sd_start,first_sd_end=mean-std,mean+std
second_sd_start,second_sd_end=mean-(2*std),mean+(2*std)
third_sd_start,third_sd_end=mean-(3*std),mean+(3*std)

# fig=ff.create_distplot([mean_list],["Student Math"],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17],mode="lines", name="MEAN"))
# fig.add_trace(go.Scatter(x=[first_sd_start,first_sd_start], y=[0,0.17],mode="lines", name="STANDARED DEVIATION ONE START"))
# fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end], y=[0,0.17],mode="lines", name="STANDARED DEVIATION ONE END"))
# fig.add_trace(go.Scatter(x=[second_sd_start,second_sd_start], y=[0,0.17],mode="lines", name="STANDARED DEVIATION TWO START"))
# fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end], y=[0,0.17],mode="lines", name="STANDARED DEVIATION TWO END"))
# fig.add_trace(go.Scatter(x=[third_sd_start,third_sd_start], y=[0,0.17],mode="lines", name="STANDARED DEVIATION THREE START"))
# fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end], y=[0,0.17],mode="lines", name="STANDARED DEVIATION THREE END"))
# fig.show()

# df=pd.read_csv("data1.csv")
# data=df["Math_score"].tolist()
# mean_sample1=statistics.mean(data)
# print("Mean of Sample1 is:",mean_sample1)
# fig=ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17],mode="lines", name="MEAN"))
# fig.add_trace(go.Scatter(x=[mean_sample1,mean_sample1], y=[0,0.17],mode="lines", name="Mean of Sample1"))
# fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end], y=[0,0.17],mode="lines", name="STANDARED DEVIATION ONE END"))
# fig.show()

# df=pd.read_csv("data2.csv")
# data=df["Math_score"].tolist()
# mean_sample2=statistics.mean(data)
# print("Mean of Sample2 is:",mean_sample2)
# fig=ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17],mode="lines", name="MEAN"))
# fig.add_trace(go.Scatter(x=[mean_sample2,mean_sample2], y=[0,0.17],mode="lines", name="Mean of Sample2"))
# fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end], y=[0,0.17],mode="lines", name="STANDARED DEVIATION ONE END"))
# fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end], y=[0,0.17],mode="lines", name="STANDARED DEVIATION TWO END"))
# fig.show()

# df=pd.read_csv("data3.csv")
# data=df["Math_score"].tolist()
# mean_sample3=statistics.mean(data)
# print("Mean of Sample3 is:",mean_sample3)
# fig=ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17],mode="lines", name="MEAN"))
# fig.add_trace(go.Scatter(x=[mean_sample3,mean_sample3], y=[0,0.17],mode="lines", name="Mean of Sample3"))
# fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end], y=[0,0.17],mode="lines", name="STANDARED DEVIATION ONE END"))
# fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end], y=[0,0.17],mode="lines", name="STANDARED DEVIATION TWO END"))
# fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end], y=[0,0.17],mode="lines", name="STANDARED DEVIATION THIRD END"))
# fig.show()

# df=pd.read_csv("School1.csv")
# data=df["Math_score"].tolist()
# mean_sample1=statistics.mean(data)
# print("Mean of Sample1 is:",mean_sample1)
# fig=ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17],mode="lines", name="MEAN"))
# fig.add_trace(go.Scatter(x=[mean_sample1,mean_sample1], y=[0,0.17],mode="lines", name="Mean of Sample1"))
# fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end], y=[0,0.17],mode="lines", name="STANDARED DEVIATION ONE END"))
# fig.show()
# z_score=(mean-mean_sample1)/std
# print("The Z Score is:",z_score)

# df=pd.read_csv("School2.csv")
# data=df["Math_score"].tolist()
# mean_sample2=statistics.mean(data)
# print("Mean of Sample2 is:",mean_sample2)
# fig=ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17],mode="lines", name="MEAN"))
# fig.add_trace(go.Scatter(x=[mean_sample2,mean_sample2], y=[0,0.17],mode="lines", name="Mean of Sample2"))
# fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end], y=[0,0.17],mode="lines", name="STANDARED DEVIATION ONE END"))
# fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end], y=[0,0.17],mode="lines", name="STANDARED DEVIATION TWO END"))
# fig.show()
# z_score=(mean-mean_sample2)/std
# print("The Z Score is:",z_score)

f=pd.read_csv("School3.csv")
data=df["Math_score"].tolist()
mean_sample3=statistics.mean(data)
print("Mean of Sample3 is:",mean_sample3)
fig=ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17],mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_sample3,mean_sample3], y=[0,0.17],mode="lines", name="Mean of Sample3"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end], y=[0,0.17],mode="lines", name="STANDARED DEVIATION ONE END"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end], y=[0,0.17],mode="lines", name="STANDARED DEVIATION TWO END"))
fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end], y=[0,0.17],mode="lines", name="STANDARED DEVIATION THIRD END"))
fig.show()
z_score=(mean-mean_sample3)/std
print("The Z Score is:",z_score)