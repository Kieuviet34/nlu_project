import pandas as pd 

df = pd.read_excel('output.xlsx', index_col=0)

df_mon_hoc = df[df['TÊN HỌC PHẦN'] == 'Chiến lược kinh doanh quốc tế']
credits = df_mon_hoc.iloc[0].to_dict()
print(credits)