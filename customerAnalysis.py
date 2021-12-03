import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

#cust_dataset = open("/Users/annmerinpeter/Documents/python/marketing_campaign.csv")
#for x in cust_dataset:
#    print(x)
#cust_dataset.close()

df = pd.read_csv("/Users/annmerinpeter/Documents/python/marketing_campaign.csv",delimiter='\t')
print(df.head().truncate())

plt.scatter(df['Education'],df['Marital_Status'],df['Income'],df['Kidhome'])
plt.show()
