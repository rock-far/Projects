import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('bd-dec22-births-deaths-natural-increase.csv')

#df['countp'] = df['Count']+df['Period']
#df['countf'] = round(df['Count']/df['Period'])

#df.drop(['Births_Deaths_or_Natural_Increase'], axis = 1, inplace= True)

#data = pd.DataFrame({'Period': [2023], 'Count': [16700], 'countp': [19200], 'countf': [9]})

#pd.concat([df,data], axis = 0, ignore_index= True)

#first_30 = df.iloc[1:10]
#Count = df[df['Count']>61000]
#Period = df[df['Period']>2010]
#print(first_30)
#print(Count)
#print(Period)

Period = df['Period']
Count = df['Count']
plt.plot(Period, Count, color = 'blue', linewidth = 3, marker = 'o', markerfacecolor = 'green')
plt.xlabel('Period')
plt.ylabel('Count')
plt.legend()
plt.title("Idfk what this is but f it")

plt.show()

