# Write a python programe to remove duplicate items from a list
def removeDuplicateItems(l: list):
    nd: list = []
    for element in l:
        if element not in nd:
            nd.append(element)
    return nd


# Write  a python programe using function to return true if there are any common elements between two list
def duplicate(l1: list, l2: list) -> bool:
    for e in l1:
        for f in l2:
            if e == f:
                return True
    return False


# Write a python programe to create a list by cancatenating a given list with a range from 1 to n.
def createlist(l: list, n: int) -> list:
    cl: list = []
    for i in range(n):
        for e in l:
            e += str(i + 1)
            cl.append(e)
    return cl


# write a python programe to get a list,sorted in increasing order by the last element in tuple from a given non-empty tuples.
def sortList(l: list[tuple]) -> list[tuple]:
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i][1] > l[j][1]:
                l[j], l[i] = l[i], l[j]

    return l


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5, 6, 7]
    l2 = [8, 9, 10]
    print(duplicate(l1, l2))
    li = [
        1,
        2,
        3,
        5,
        6,
        7,
        8,
        3,
        23,
        3,
        46,
        5,
        567,
        56,
        45,
        35,
    ]
    print(removeDuplicateItems(li))
    conjugate = ["p", "q"]
    print(createlist(conjugate, 5))
    print(sortList([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
