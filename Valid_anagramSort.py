def ValidAnagram(s,t):
    return sorted(s)==sorted(t)
s="anagram"
t="gramana"
print(ValidAnagram(s,t)) #Ouput = True
