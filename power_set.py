'''Power set is a set that contains all possible subsets of a certain order.

For exmaple:
powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
'''
def power_set(nums):
    power_set = [[]]
    for num in nums:
        power_set += [item + [num] for item in power_set]
        print power_set
    #return power_set

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(power_set(nums))
