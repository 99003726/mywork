mport numpy as np
import pandas as pd
dict1 = {
       "ID":["N1234567","A2345678","B1234567","B4567890"],
       "Name":['Barrera Jr. Woody','Lambert Malaika', 'Joyce, Traci','Flower John Gregg'],
       "Network_Id":['WXB12345','MXL12345','TXJ12345','JGF12345'],
       "Email_Address":['WOODY.BARRERA_JR@UNIV.EDU','a','a','c'],
       "section":['1','2','3','4']
}

dict2 = {
       "dummyID":["N1234567","A2345678","B1234567","B4567890"],
       "dummyName":['Barrera Jr. Woody','Lambert Malaika', 'Joyce, Traci','Flower John Gregg'],
       "dummyNetwork_Id":['WXB12345','MXL12345','TXJ12345','JGF12345'],
       "dummyEmail_Address":['WOODY.BARRERA_JR@UNIV.EDU','a','a','c'],
       "dummysection":['1','2','3','4']
}
df1=pd.DataFrame(dict1)
df2=pd.DataFrame(dict2)
#
with pd.ExcelWriter('data12.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet_name_1')
    df2.to_excel(writer, sheet_name='Sheet_name_2')



a=str(input("enter Email_Address number"))
op1 = df1[df1['Email_Address'].str.contains(str(a))]
op2 = df2[df2['dummyEmail_Address'].str.contains(str(a))]
# print(op)
#
#
# op.to_csv('output.csv')
horizontal_concat = pd.concat([op1, op2], axis=1)
outputcc=horizontal_concat
outputcc.to_excel("outputcc.xlsx",sheet_name='output',)

print(horizontal_concat)
