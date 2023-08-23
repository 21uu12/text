import openpyxl
import pandas as pd
import os
import xlwt
# 数据提取
df=pd.read_excel('/Users/wacai/Desktop/d2/output(1).xlsx',index_col=False,)
# print(df.head())
# data_path=os.path.join('data','out.xlsx')
# data_path1=os.path.join('data','out0.xlsx')
# f=open(data_path,'w',encoding='utf-8')
# f1=open(data_path1,'w',encoding='utf-8')
fi_1=df[df['result']==1]
data = pd.DataFrame(columns=["input", "column2"])
times=0
for i ,row in fi_1.iterrows():
    for i in range(4):
        if type(row[i])!=float:
            row[i]=row[i].strip()
        
    if type(row[1])==float:
        input='历史对话：'+row[0]+';'+'上下文: ;'+row[2]+';'+'\n'
        
    else:
        input='历史对话：'+row[0]+';'+'上下文:'+str(row[1])+';'+row[2]+';'+'\n'
    data.loc[times] = [input, row[3]]
    
    times+=1
print(times)
    # f.write('{},{}\n'.format(input, row[3]))
data.to_excel('/Users/wacai/Desktop/d2/data/result_1.xlsx', index=False)
fi_0=df[df['result']==0]   
times1=0

data1 = pd.DataFrame(columns=["input", "column2"])
for i ,row in fi_0.iterrows():
    for i in range(4):
        if type(row[i])!=float:
            row[i]=row[i].strip()
        
    if type(row[1])==float:
        input='历史对话：'+row[0]+';'+'上下文: ;'+row[2]+';'+'\n'
    else:
        input='历史对话：'+row[0]+';'+'上下文:'+str(row[1])+';'+row[2]+';'+'\n'
        # print(input)
    data1.loc[times1] = [input, row[3]]
    
    times1+=1

data1.to_excel('/Users/wacai/Desktop/d2/data/result_0.xlsx', index=False)
# for i ,row in fi_0.iterrows():
#     input1='历史对话：'+row[0]+'上下文:'+row[1]+row[2]+'\n'
#     print(input1)
#     f1.write(f'{input1},{row[3]}\n')
# for h in fi_1['history']:
#     print(h)
#     h_='历史对话：'+h
#     break
# for a in fi_1['assistant']:
#     print(a)
#     break
# for usr in fi_1['user']:
#     print(usr)
#     break
# fi_0 = df[df['result'] == 0]  
# work=openpyxl.load_workbook('/Users/wacai/Desktop/d2/output(1).xlsx')
# sheet=work['Sheet1']
# E=sheet['E']
# history=sheet['A']
# for e in E:
    
