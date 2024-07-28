 #using choice and printing the values
 # list=(1,2,3,4)
choice=int(intput())
if(choice==1):
  list.append(3)
  print(list)  
elif(choice==2):
  list.pop()
  print(list)
elif(choice==3):
  list=list+list
  print(list)
elif(choice==4):
  print(len(list))  