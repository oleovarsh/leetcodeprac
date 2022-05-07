def romanToInt (s):
        """
        :type s: str
        :rtype: int
        """
        
        arrdict={'V':5,'X':10, 'L':50,'C':100,'D':500, 'M':1000, 'I':1}
        val=0
        i=0
        
        while(i!=len(s)-1):
          fval=arrdict[s[i]]
          sval=arrdict[s[i+1]]

          if(fval<=sval):
            val-=fval
            i=i+1
          else:
            val+=fval
            i+=1


            
        return val+arrdict[s[i]]
        

s="DCXXI"
print(romanToInt(s))

# the key was to observe the pattern of the number, if the current letter has s
# lower value than the next letter, then we need to minus the current value
# if not then add the value