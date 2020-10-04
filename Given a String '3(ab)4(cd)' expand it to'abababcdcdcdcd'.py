
#Given a String '3(ab)4(cd)' expand it to'abababcdcdcdcd'.


def printer(arr):
    i=0 #keep track of the letter in the string
    k=''#variarible to store the string to be printed
    ite=0 #variable to store the number of times to print each set of string
    while(i!=len(arr)): #looping through string
        try: 
            int(arr[i]) #if the value is a number and will not cause any error  
            ite=int(arr[i]) #assign value ite
            i+=1 #move to next letter
        except: #if error occurs then int(arr[i]) is not valid ie, arr[i] is a letter or symbol
            if arr[i]=='(': #sub string to be printed multiple times is given in brackets
                while(arr[i]!=')'): #while not ) append the arr[i] to the variable k
                    i+=1
                    if arr[i]!=')':
                        k+=arr[i] #append
                for j in range(ite): #print the string in k ite number of times
                    print(k,end='')
                k=''
            i+=1 #next string literal
            
printer('3(ab)4(cd)') #function call
