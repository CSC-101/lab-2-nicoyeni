# def smallest(n:float, m:float) -> float:
#     if n < m:
#         return n             # neither call below evaluates this statement
#     else:
#         return m
#
# first = smallest(3, 2)       # the value of first is 2
# second = smallest(2, 2)      #the value of second is 2. This is because the if statement was false,
#                                     #so the else statement evaluated and the value was 2.
#                                     #This is the one case that the function doesn't work
#                                     #well because both values are the same
# print()
#
# def function2(a:int, b:int, c:int) -> int:
#     if a > b and a > c:
#         return a - b             # when a is the largest number out of all of them
#     elif b > c:
#         return b + c             # when b is the largest number
#     else:
#         return 2 * c             # when c is the largest number
#
#
# answer1 = function2(3, 2, 1)     # answer1 is 1
# answer2 = function2(2, 3, 1)     # answer2 is 4
# answer3 = function2(2, 1, 3)     # answer3 is 6
# print()
#
# from typing import Optional             # gain access to the Optional[X] type hint
#
#
# def checked_access(L:list[int], idx:int) -> Optional[int]:
#     test = idx >= 0 and idx < len(L)    # boolean value
#     if test:                            # if test is true
#         return L[idx]
#     else:
#         return None
#
#
# first = checked_access([1, 0, 1], 9)     # first is None
# second = checked_access([1, 0, 1], 2)    # second is 1
# print()
#
# def length_sum(L:list[str]) -> int:
#     if len(L) > 2:
#         result = len(L[0]) + len(L[1]) + len(L[2])    # it is being evaluated when first is called
#     elif len(L) > 1:                                  #   and the value 4+2+3=9
#         result = len(L[0]) + len(L[1])                # it is being evaluated when third is called
#     elif len(L) > 0:                                  #   and the value is 7+4=11
#         result = len(L[0])                            # it is being evaluated when second is called
#     else:                                             #   and the value is 11
#         result = 0
#     return result
#
#
# first = length_sum(["this", "is", "the", "first", "call"])
# second = length_sum(["second call"])
# third = length_sum(["another", "call"])
# print()
#
# def surprising(L:list[str], other:str) -> list[str]:
#     L.append(other.upper())
#     return L
#
#
# words = ["this", "is", "confusing", "code."]
# first = surprising(words, "Avoid")
# second = surprising(words, "such.")
#          # the value of words is ["this", "is", "confusing", "code.", "AVOID", "SUCH"]
#          # the value of first is ["this", "is", "confusing", "code.", "AVOID", "SUCH"]
#          # and the value of second is ["this", "is", "confusing", "code.", "AVOID", "SUCH"]
#          # Lists are mutable, that's why with the addition of every string, the value of all the lists changed
# print()
#
#
# def double(n):
#     return 2 * n
#
#
# def square_perimeter(length):
#     two_sides = double(length)
#     return two_sides + two_sides
# result = square_perimeter(2)
# print()


# lista = [3,4,5,7]
# listb =[x+1 for x in lista]
# print (listb)
#
# listc = [x%2 for x in lista if x > 4]
# print(listc)

# listd = ['canada', 'america', 'france']
# liste = [x.upper() for x in listd]
# print(liste)
#
# # for x in listd:
# #     print(x[0])
#
# listf = [x.upper()[0] for x in listd]
# print (listf)


# a_list = [2,3]
# a_list.append(9)
# b_list = a_list
# b_list = []
# a_list.append(0)
# b_list.append(7)
# print()

def second(nums):
    if len(nums) > 1:
        return nums[1]
    else:
        return None
theList = [4, 2, 9]
result = second(theList)
print()