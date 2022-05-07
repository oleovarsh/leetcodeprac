def isPalindrome( x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0):
            return False
        else:
            length=0
            for i in range(1,32):
                qtcheck=x//(10**i)
                
                if(qtcheck<1):
                    length=i-1

                    
                    break
            
            valarray=[]
            num=x
            
            for i in range(length,0,-1):
                y=num//(10**i)
                print(y)
                valarray.append(y)
                num=num-y*(10**i)
                
            valarray.append(num)
            val=0
            print(valarray)
            for i in range(len(valarray)-1,-1,-1):
                val+=valarray[i]*(10**i)
                print(val)
            if val==x:
                return True
            else:
                return False
                
print(isPalindrome(121))