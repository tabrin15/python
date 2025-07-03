def palindrome(r):

    e = len(r)  -1
    s = 0 
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True

mytuple= (1,2,3,4,4,3,2,1)

if(mytuple):
    print("The tuple is Flip-Flop")
else:
    print("The tuple is not Flip-Flop")