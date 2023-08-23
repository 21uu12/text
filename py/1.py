import re
import json
with open('/Users/wacai/Desktop/d2/llama_0817.json') as f:
    llama=json.load(f)
all_=[]
pattern = r"\$\{[^}]+\}" 
for i in range(len(llama)):
   find1=re.finditer(pattern=pattern,string=llama[i]['output'])
   find2=re.finditer(pattern=pattern,string=llama[i]['input'])
   for i in find1:
    #    print(group_)
       all_.append(i.group())
   for i in find2:
        print(i.group())
        all_.append(i.group())
# print(all_)
# print(len(set(all_)))
# all_=list(set(all_))
# print(all_)
# print(len(all_))
# print(all_)
#   print(find1)

with open ('/Users/wacai/Desktop/d2/data/占位符.json') as f2:
    ll=json.load(f2)
    print(len(ll))