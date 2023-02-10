def check(s):
    l=[]
    if len(s)==0 or len(s)==1:
        return False
    if s[-1]=='{' or s[-1]=='[' or s[-1]=='(':
        return False
    for i in range(len(s)):
        if s[i]=='{' or s[i]=='[' or s[i]=='(':
            l.append(s[i])
        else:
            try:
                if l[-1]=='{' and s[i]!='}':
                    return False
                elif l[-1]=='[' and s[i]!=']':
                    return False
                elif l[-1]=='(' and s[i]!=')':
                    return False
                else:
                    l.pop()
            except IndexError:
                return False
    if len(l)==0:
        return True
    else:
        return False
s=input()
print(check(s))
