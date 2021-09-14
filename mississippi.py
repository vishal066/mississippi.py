word=input("enter the string:")

def most_frequent(string):
    d= dict()
    i=0
    while i<len(string):
        a=0
        j=0
        while j<len(string):
            if string[i]==string[j]:
                a=a+1
            j+=1
        d[string[i]]=a
        i+=1
    b=dict(sorted(d.items(), key=lambda kv:kv[1],reverse=True))
                
    return b

print(most_frequent(word))
