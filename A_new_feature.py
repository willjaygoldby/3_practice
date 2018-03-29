def newfeature():
	print("All this does is print")


def bs_helper(datalist, key, lower, upper):
    if lower + 1 == upper:    # base case: range empty
        return None
    mid = (lower + upper)//2
    if key == datalist[mid]:  # base case: found key
        return mid
    if key < datalist[mid]:
        return bs_helper(datalist, key, lower, mid)
    else:
        return bs_helper(datalist, key, mid, upper)

def bsearch(datalist, key):
    return bs_helper(datalist, key, -1, len(datalist))

my_list = [1,3,5,6,7,8,88,99,111,345,677,8765,23456,23454343,675464,2343536546]
print(bsearch(my_list, 345))


"""This are some technical specifications for this code"""