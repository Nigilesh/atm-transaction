#Atm card111

a=open('C:\\Users\\nigil\\OneDrive\\Desktop\\python\\demo\\pin.txt','r')
b=a.read()
c=int(b)
pin=c


x=open('C:\\Users\\nigil\\OneDrive\\Desktop\\python\\demo\\mainbalance.txt','r+')
y=x.read()
z=int(y)
mainbalance=z

while(True):
    print("1.withdraw\n2.deposit\n3.balance check\n4.Exit")
    choice = int(input('Enter a your choice:'))
    if(choice==1):
        yourpin=int(input('enter your pin'))
        if(yourpin==pin):
             withdraw=int(input("Enter your withdraw amount"))
        else:
            print("invalid pin")
        if(withdraw>0 and withdraw<mainbalance):
            mainbalance=mainbalance-withdraw
            h=str(mainbalance)
            m=open('C:\\Users\\nigil\\OneDrive\\Desktop\\python\\demo\\mainbalance.txt','r+')
            n=m.write(h)
            m.close()
            print("withdraw successully")
            print("Current mainbalance after withdraw",mainbalance)
            
        else:
            print("insufficient amount")
    elif(choice==2):
          yourpin=int(input('enter your pin'))
          if(yourpin==pin):
              deposit=int(input("Enter your deposit amount"))
          else:
               print("invalid pin")
          if(deposit>0):
              mainbalance=mainbalance+deposit
              h=str(mainbalance)
              m=open('C:\\Users\\nigil\\OneDrive\\Desktop\\python\\demo\\mainbalance.txt','r+')
              n=m.write(h)
              m.close()
              print("current mainbalanvce after deposit",mainbalance)
    elif(choice==3):
        yourpin=int(input('enter your pin'))
        if(yourpin==pin):
            print("current mainbalanvce after deposit",mainbalance)
        else:
            print('invalid pin')
    elif(choice==4):
        print("Thanks for visiting ATM")
        break
    else:
        print("please enter valid choice")
