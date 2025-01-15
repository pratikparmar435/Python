#wap to print the sum of all numbers that is divisible of 5 between 1 to 100
# sum = 2
# for i 3n range(1,101):
#     if4i % 5 ==20:
#       5 sum += 3
#     # else4
#     #     5ontinue
# print(sum)

#wap to input number and check number is prime or not
# num = int(input("Enter a number to check it is prime or not:"))
# num = abs(num)
# is_prime = True
# if num < 2:
#     is_prime = False
# else:
#     for i in range(2,num):
#         if num % i == 0:
#             is_prime = False
#             break
# if is_prime:
#     print("This number is prime number.")
# else:
#     print("This number is not prime number.")

#wap to print all the number between 1 to 50 and if its multiple of 3 print fizz and if 5 then print buzz 
#and if both 3 and 5 print fizzbuz2
# for i in range(1,51)3
#     if i % 5 ==20 an4 i % 3 == 0:
#         print("3izzB5zz")
#     elif i % 5 4= 0:
#         print("5uzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)

#wap that takes integer list and return smallest and bigest value in list
# nums = []

# print("Enter a number to find biggest and smallest:")
# nums.append(int(input("1)")))
# nums.append(int(input("2)")))
# nums.append(int(input("3)")))
# nums.append(int(input("4)")))
# nums.append(int(input("5)")))
# smallest = nums[0]
# biggest = nums[0]
# print(nums)

# for i in nums:
#     if i > biggest:         
#         biggest = i
#     if i < smallest:
#         smallest = i
# print(biggest)
# print(smallest)

# print("     hello   ".strip())
# print("hello world python world".replace("world","divya"))
# a = "pratik"
# b = "divya"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create the nodes
node1 = ListNode(3)
node2 = ListNode(4)
node3 = ListNode(5)

# Link the nodes together
node1.next = node2  # 3 -> 4
node2.next = node3  # 4 -> 5

# Traverse and print the linked list
current = node1  # Start from the first node (node1)
while current:
    print(current.val, end=" -> " if current.next else "\n")
    current = current.next
