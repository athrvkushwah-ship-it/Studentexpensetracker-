# #expense tracker 
# from Expenseediting import edit
def category1():
  Add_expense = int(input("Enter your expense :", ))
  Add_catagrory = input('Catageory :')
  Reasone = input('Reasone :')
  print('Expense diary')
  print('Amount', Add_expense,  'Category:', Add_catagrory, 'Reason:', Reasone, sep = '\n')
category1()

def category2():
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
    print('Amount :', New_expense , 'Reasone' ,New_Reasone , 'Category', New_catageory ,sep= '\n')
    break
category2()

def edit():
    print('Select which catagory you want to edit')
    while True:
        print('1. cataogry1')
        print('2  .catrgory2')
        break
    Option = input("choose the option :")
    if Option == '1':category1()
    elif Option =='2':category2()

while True:
 print('1. yes')
 print('2. NO')
 break
Option = input('If you want to edit the entry :')
if Option =='1':edit()
elif Option =='2':print('proceed')


