def longestprefix(strs):
    minword=min(strs, key=len)
    while( len(minword)>0):
        if all([s.startswith(minword) for s in strs]):
            return minword
        else:
            minword=minword[0:len(minword)-1]
    return ""


strs = ["care","car","car"]
print(longestprefix(strs))
