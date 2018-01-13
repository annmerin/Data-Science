import pandas as pd

#cust_dataset = open("/Users/annmerinpeter/Documents/python/marketing_campaign.csv")
#for x in cust_dataset:
#    print(x)
#cust_dataset.close()

df = pd.read_csv("/Users/annmerinpeter/Documents/python/marketing_campaign.csv",delimiter='\t',nrows=20)
print(df.columns)
print(df)
