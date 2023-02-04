import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Data = pd.read_csv("t20-world-cup-22.csv")
Data["Match Won By 1st Batting or 2nd"]=''

d1=pd.DataFrame()
d1['Whether Team Won by winning Toss']=np.where((Data['toss_winner'] == Data['winner']),'Yes','No')
# print(d1)

col='Whether Team Won by winning Toss'
count=d1.groupby(col).size()
#print(type(count))
d2=pd.DataFrame(count)



plot=d2.plot.pie(y=0, figsize=(5,5),autopct='%1.1f%%')
plt.title("Pie Chart to show whether team won by winning toss or not")
# plt.show()
# plt.savefig("D:\Winter training\T20_WorldCup_2022")