global jan
def hii():
        new=list(b)
        new[0]="1"
        ''.join(new)
        print('-a')
        print(new) 
        indexes = [index for index in range(len(new)) if new[index] == '1']
        #print(indexes)
        q=max(indexes)
        #print(q)
        i=1
        for i in range(i,q):
    
                if new[i]=='0':
                        new[i]='1'


                else:
                        new[i]='0'
        #print(new)
        
        list1=new
        str1=''.join(list1)
        print("2's compliment of second number is:")
        print(str1)

        print('subtraction of 2 numbers is:')
        c = bin(int(y,2) + int(str1,2))
        #print(c)
        yes=list(c)
        #print(yes)


        if  c[2]=='1'and len(c)==19:
            print('answer is POSITIVE number')
           # print(yes)
            ans=print(yes[3:])
        else:
                    print('answer is NEGATIVE number')
                    indexes = [index for index in range(len(yes)) if yes[index] == '1']
                    #print(indexes)
                    me=max(indexes)# greatest number
                    #print(me)
            
                    j=2
                    for j in range(j,me):
    
                            if yes[j]=='0':
                                      yes[j]='1'


                            else:
                                      yes[j]='0'
                    ans=print(yes[2:]) 

        print(ans)
        print('answer in interger is:')
        print(jan)




    

print('postive numbers are valid upto 32768')
x=int(input('enter the 1st number'))
a=int(input('enter the 2st number'))
jan=int(x)-int(a)

if (x>0) and (a>0):
    print('number are positive')
    y=bin(x)[2:].zfill(16) 
    print('x in binary is')
    print(y)
    
    b=bin(a)[2:].zfill(16)
    print('a in binary is')
    print(b)
    hii()
    

elif (x>0) and (a<0):
    print('2nd number is is negative')
    print('plz enter postive number')
elif (x<0) and (a>0):
    print('1st number is is negative')
    print('plz enter postive number') 
elif (x<0) and (a>0):
    print('1st number is is negative')
    print('plz enter postive number') 
elif (x<0) and (a<0):
    print('both  number are negative')
    print('plz enter postive number') 
