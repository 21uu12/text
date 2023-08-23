import xlwt
import pandas as pd
df=pd.read_excel('/Users/wacai/Desktop/d2/output(1).xlsx',index_col=False,)
book=xlwt.Workbook()
headers=['input','out']
sheet=book.add_sheet('sheet1')
# print(df.head())
# data_path=os.path.join('data','out.xlsx')
# data_path1=os.path.join('data','out0.xlsx')
# f=open(data_path,'w',encoding='utf-8')
# f1=open(data_path1,'w',encoding='utf-8')
fi_1=df[df['result']==1]
fi_0=df[df['result']==0]
times=0
for i ,row in fi_1.iterrows():
    input='历史对话：'+row[0]+'上下文:'+row[1]+row[2]+'\n'
    sheet.write(times,0,input)
    sheet.write(times,1,row[3])
    times+=1
book.save('txe.xlsx')