# #expense tracker 
from Expenseediting import edit
Add_expense = int(input("Enter your expense :", ))
Add_catagrory = input('Catageory :')
Reasone = input('Reasone :')
print('Expense diary')
print('Amount', Add_expense,  'Category:', Add_catagrory, 'Reason:', Reasone, sep = '\n')

Total_expense = Add_expense
while True:
    while True:
      New_catageory = input('New catageory:')
      if not New_catageory:
         print('Pls Enter the catagory')
         continue
      break
    while True:
       New_Reasone = input('New_Resone:')
       if not New_Reasone:
        print('Pls enter Reasone')
        continue
       break
    while True:
        New_expense = int(input('Enter the new expense :'))
        if not New_expense:
          print('pls enter new expense')
          break
        Total_expense += New_expense
        print("Total expense :",Total_expense)
        break
    break


while True:
 print('1. yes')
 print('2. NO')
 break
Option = input('If you want to edit the entry :')
if Option =='1':edit()
elif Option =='2':print('proceed')
