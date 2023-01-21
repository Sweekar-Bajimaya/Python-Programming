dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
itemDic1 = list(dic1.items())
itemDic2 = list(dic2.items())
itemDic3 = list(dic3.items())
itemNums = itemDic1 + itemDic2 + itemDic3
nums = dict(itemNums)
print(nums)
maxNum = max(nums.values())
print(maxNum)
minNum = min(nums.values())
print(minNum)





