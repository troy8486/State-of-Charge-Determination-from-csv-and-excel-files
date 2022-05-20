
import pandas as pd
  

list1 = ['Assam', 'India',
         'Lahore', 'Pakistan', 
         'New York', 'USA',
         'Bejing', 'China']
  
df = pd.DataFrame()
  

df['State'] = list1[0::2]
df['Country'] = list1[1::2]
  

df.to_excel('result.xlsx', index = False)