import openpyxl
import pandas as pd
import os
import xlwt
df=pd.read_excel('/Users/wacai/Desktop/d2/output(1).xlsx',index_col=False,)
# print(df.head())
data_path=os.path.join('data','write.xlsx')
# data_path1=os.path.join('data','out0.xlsx')
f=open(data_path,'w',encoding='utf-8')
# f1=open(data_path1,'w',encoding='utf-8')
fi_1=df[df['result']==1]
for i ,row in fi_1.iterrows():
    
    input='历史对话：'+row[0]+'上下文:'+row[1]+row[2]+'\n'
    print(row[3])
    f.write('{},{}\n'.format(input, str(row[3])))