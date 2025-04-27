def mergestring(word1,word2):
    a,b=0,0
    A,B =len(word1),len(word2)
    s=[]
    while a<A and b<B:
        s.append(word1[a])
        a+=1
        s.append(word2[b])
        b+=1
    while a<A:
        s.append(word1[a])
        a+=1
    while b<B:
        s.append(word2[b])
        b+=1
    return "".join(s)
word1 ="abc"
word2 = 'pqrstus'
print(mergestring(word1,word2))


                
