def palindrome(x):
    n=-1
    i=0  
    while(i<(len(x)//2)):
        if(x[i]!=x[n]) : return False
        else :
           n=n-1
           i=i+1
    return True
        
def prime(x):
    if(x<=1): return False
    else:
        for i in range(2,x):
            if(x%i==0): return False
        return True
        
def range1(x,start,end):
    if(x>start and x<end):return True
    else : return False

def factorial (x):
    f=x
    if(x<0): return 1
    else:
     for i in range(2,x):
        f=f*i
     return f

def reverse(x):
    c=''
    n=-1
    for i in range(len(x)):
        c=c+x[n]
        n=n-1
    return c
     
def sum(L):
    s=0
    for i in L:
       s=s+i
    return s

def max1(x,y,z):
    return max(x,y,z)

