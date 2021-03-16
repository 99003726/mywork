# import numpy as np
# import pandas as pd
# dict1 = {
#        "ID":[1234567,2345678,1234567,4567890],
#        "Name":['Barrera Jr. Woody','Lambert Malaika', 'Joyce, Traci','Flower John Gregg'],
#        "Network_Id":['WXB12345','MXL12345','TXJ12345','JGF12345'],
#        "Email_Address":['WOODY.BARRERA_JR@UNIV.EDU','a','a','c'],
#        "section":['1','2','3','4']
# }
#
# dict2 = {
#        "dummyID":["N1234567","A2345678","B1234567","B4567890"],
#        "dummyName":['Barrera Jr. Woody','Lambert Malaika', 'Joyce, Traci','Flower John Gregg'],
#        "dummyNetwork_Id":['WXB12345','MXL12345','TXJ12345','JGF12345'],
#        "dummyEmail_Address":['WOODY.BARRERA_JR@UNIV.EDU','a','a','c'],
#        "dummysection":['1','2','3','4']
# }
# df1=pd.DataFrame(dict1)
# df2=pd.DataFrame(dict2)
# df1.set_index('ID')
# nf1=df1.set_index('ID')
# # print(df1)
# # print(nf1)
#
#
#
#
#
#
# # print(type(df1.ID))
# df1.ID=df1.ID.astype(str)
# # print(type(df1.ID))
# # #
# # #
# # # with pd.ExcelWriter('data12.xlsx') as writer:
# # #     df1.to_excel(writer, sheet_name='Sheet_name_1')
# # #     df2.to_excel(writer, sheet_name='Sheet_name_2')
# #
#
# #
#
#
#
#
#
# a=str(input("enter Name number"))
#
# b=str(input("enter EMAIL"))
# op1 = df1[df1['Email_Address'].str.contains(str(a))]
#
# op2 = df1[df1['Name'].str.contains(str(b))]
#
#
#
#
#
#
#
#
#
#
# # op2 = df2[df2['dummyEmail_Address'].str.contains(str(a))]
# # # print(op1)
#
#
#
#
#
# print(nf1.index)
# # # df1.index=["ID"]
# print(nf1.loc[index].at['section'])
# #        print("correct")
# #
# # else:
# #        print("False")
#
#
#
#
#
# #
# # op.to_csv('output.csv')
# # horizontal_concat = pd.concat([op1, op2], axis=1)
# # outputcc=horizontal_concat
# # outputcc.to_excel("outputcc.xlsx",sheet_name='output',)
#
#
# a=str(input("enter Name "))
# op1 = df1[df1['Name'].str.contains(str(b))]
# op2 = df2[df2['Name'].str.contains(str(b))]
# op3 = df3[df3['Name'].str.contains(str(b))]
# op4 = df4[df4['Name'].str.contains(str(b))]
# op5 = df5[df5['Name'].str.contains(str(b))]
#
#
# horizontal_concat = pd.concat([op1, op2, op3, op4, op5], axis=1)
# fp=horizontal_concat
#
#
# with pd.ExcelWriter('dataof_5sheets.xlsx') as writer:
#    fp.to_excel(writer, sheet_name='Master_sheet')
#
# with pd.ExcelFile("path_to_file.xls") as xls:
#     df1 = pd.read_excel(xls, "Sheet1")
#     df2 = pd.read_excel(xls, "Sheet2")




import numpy as np
import pandas as pd

dff1 = pd.read_csv("quiz_1_grades.csv")
dff2 = pd.read_csv("quiz_2_grades.csv")
dff3 = pd.read_csv("quiz_3_grades.csv")
dff4 = pd.read_csv("quiz_4_grades.csv")
dff5 = pd.read_csv("quiz_5_grades.csv")


with pd.ExcelWriter('dataof_5sheets.xlsx') as writer:
    dff1.to_excel(writer, sheet_name='Sheet_Quiz_1')
    dff2.to_excel(writer, sheet_name='Sheet_Quiz_2')
    dff3.to_excel(writer, sheet_name='Sheet_Quiz_3')
    dff4.to_excel(writer, sheet_name='Sheet_Quiz_4')
    dff5.to_excel(writer, sheet_name='Sheet_Quiz_5')

with pd.ExcelFile('dataof_5sheets.xlsx') as xls:
    df1 = pd.read_excel(xls, "Sheet_Quiz_1")
    df2 = pd.read_excel(xls, "Sheet_Quiz_2")
    df3 = pd.read_excel(xls, "Sheet_Quiz_3")
    df4 = pd.read_excel(xls, "Sheet_Quiz_4")
    df5 = pd.read_excel(xls, "Sheet_Quiz_5")


b=str(input("enter Email"))
op1 = df1[df1['Email'].str.contains(str(b))]
op2 = df2[df2['Email'].str.contains(str(b))]
op3 = df3[df3['Email'].str.contains(str(b))]
op4 = df4[df4['Email'].str.contains(str(b))]
op5 = df5[df5['Email'].str.contains(str(b))]

horizontal_concat = pd.concat([op1, op2, op3, op4, op5], axis=1)
fp=horizontal_concat

with pd.ExcelWriter('dataof_5sheets.xlsx', mode='a') as writer:
   fp.to_excel(writer, sheet_name='Master_sheet')
print("data succesfully added in MAster Sheeet ")
