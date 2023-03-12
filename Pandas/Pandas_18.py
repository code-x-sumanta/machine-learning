# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 09:41:06 2022

@author: Asus
"""

"""
1)pd.concat()
2)pandas concat join
3)pandas concat join axis
4)pandas concat keys
5)pandas conca sort
"""
import pandas as pd
df=pd.read_csv('E:\ML SD\CSV files\Student_Details3.csv')
print(df)

sr1=pd.Series([0,1,2])
sr1
sr2=pd.Series([3,4,5,6,7])
sr2
pd.concat([sr1,sr2])
df1=pd.DataFrame({'ID':[1,2,3,4],'Name':['A','B','C','D'],'Class':[5,6,7,8]})
df1
df2=pd.DataFrame({'ID':[5,6,7,8],'Name':['E','F','G','H'],'Class':[9,10,11,12]})
df2

pd.concat([df1,df2])
pd.concat([df2,df1])
pd.concat([df1,df2],axis=1)
pd.concat([df1,df2],axis=0)
pd.concat([df1,df2],axis=0,ignore_index=True)

df1=pd.DataFrame({'ID':[1,2,3,4],'Name':['A','B','C','D'],'Class':[5,6,7,8]})
df1
df3=pd.DataFrame({'ID':[3,4],'Name':['C','D'],'Class':[7,8]})
df3

pd.concat([df1,df3])
pd.concat([df1,df3], axis=1)

pd.concat([df1,df3],axis=1,join='inner')
pd.concat([df1,df3],axis=1,join='outer')


pd.concat([df1,df3],axis=1,join_axes=[df1.index])

df1=pd.DataFrame({'ID':[1,2,3,4],'Name':['A','B','C','D'],'Class':[5,6,7,8]})
df1
df2=pd.DataFrame({'ID':[5,6,7,8],'Name':['E','F','G','H'],'Class':[9,10,11,12]})
df2
pd.concat([df1,df2],keys=['df1','df2'])
pd.concat([df1,df2],keys=['first df','second df'])

pd.concat([df1,df2],axis=1,keys=['first df','second df'])

df1=pd.DataFrame({'ID':[1,2,3,4],'Name':['A','B','C','D'],'Class':[5,6,7,8]})
df1
df3=pd.DataFrame({'Marks':[40,50,60,70]})
df3

pd.concat([df1,df3])
pd.concat([df1,df3],sort=False)