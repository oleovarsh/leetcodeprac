def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        counterdict={}
        
        for i in nums:
            if((target-i)not in counterdict):
                counterdict[target-i]=1
            else:
                counterdict[target-i]+=1
        
        check=False
        
        for i in counterdict.keys():
            x=target-i
            print(i)
            if(x==i and counterdict[x]>1):
                check=True
                val=i
            elif(x!=i and x in counterdict):
                val=i
                break
                
        
        indexval=[]
        if(check):
            print("check")
            for i in range(len(nums)):
                if(nums[i]==val):
                    indexval.append(i)
        else:
            print("no check")
            print(val)
            indexval.append(nums.index(i))
            indexval.append(nums.index(target-i))
            sorted(indexval)
        
        return indexval