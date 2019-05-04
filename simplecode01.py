#coding=utf-8
def twototle(nums,totle):
    for i in range(len(nums)):
        j=i+1
        for j in range(len(nums)):
            if (nums[i]+nums[j]==totle):
                return i,j

if __name__ == '__main__':
    print(twototle([1, 4, 3, 5, 2], 7))
