#variables are dynamically typed


if __name__ == '__main__':
    n=0
    print(f"the value of n is {n}")

    n= "new value" #since the type of n/variables is determined at runtime
    #they can be re-assigned with new data
    print(f"the value of n is now{n}")

    #multiple assingment
    a,b,c= 1,"hello",5.6
    print(f"a is {a}, b is {b}, c is {c}")

    value_1 = 3
    value_2 = 2

    print(f"the value of 1 is {value_1} and the value of 2 is {value_2}")
    value_1,value_2=value_2,value_1 #data can also be swapped like this via tuple unpacking (BUT ONLY IN PYHTON)
    print(f"the value of 1 is now {value_1} and the value of 2 is now {value_2}")

    #incrementing in python

    # n= n+1 # good
    # n+=1 # good
    # #n++ # bad (because of python interpretor
    # # If statements don't need parentheses
    # # or curly braces.
    n = 1
    if n > 2:
        n -= 1
    elif n == 2:
        n *= 2
    else:
        n += 2

    # Parentheses needed for multi-line conditions.
    # and = &&
    # or  = ||
    n, m = 1, 2
    if ((n > 2 and
         n != m) or n == m):
        n += 1
    j=0
    # #while loops in python
    # while j<5:
    #     print(j)
    #     j+=1
    #
    # #for loops in python

    for i in range(0,5): # I in the for loop is incremented implicity
        #range(start:stop:steps)
        print(i)
        #the stop parameter does not not include those values when printing
        #example range(0,5) would go up to 4
    # how to loop in reverse/decreasing order
    for i in range(5,1,-1):
        #range(start:stop:steps)
        # the -1(or some other value) in the steps parameter is what allows you to loop in decreaing order from 5
         print(i)

    print(5/2) # Divison is decimal by default while most use integer divison
    print(5//2)# double slash // gives you integer division

    # CAREFUL: most languages round towards 0 by default
    # So negative numbers will round down
    print("flag",-3 // 2)

    # A workaround for rounding towards zero
    # is to use decimal division and then convert to int.
    print(int(-3 / 2))

    # None is null (absence of value)
    n = 4
    n = None
    print("n =", n)

    # Modding is similar to most languages
    print(10 % 3)

    # Except for negative values
    print(-10 % 3)

    # To be consistent with other languages modulo
    import math
    from multiprocessing import heap

    print(math.fmod(-10, 3))

    # More math helpers
    print(math.floor(3 / 2))
    print(math.ceil(3 / 2))
    print(math.sqrt(2))
    print(math.pow(2, 3))

    # Max / Min Int
    float("inf")
    float("-inf")

    # Python numbers are infinite so they never overflow
    print(math.pow(2, 200))

    # But still less than infinity
    print(math.pow(2, 200) < float("inf"))


    #Array (are called lists in python) and they are dynamic
    #which means that they can be re-sized without needing to be re-initialized
    #like in java

    arr=[1,2,3]

    #since arrays(lists) are dynamic they be be used as stacks

    arr.append(4)
    arr.append(5)
    #the append method will append values to the end of the array/list
    # and the pop method will remove values from the end of the array/list
    print(arr)
    while arr:
        print(arr.pop())
    print(arr)

    #since the stack is also techincally still a list and not a true stack
    #we can insert into the middle of the list
    #insert(i, x)
    #Inserting into the middle of the array is a O(N) time operation
    arr=[1,2,3,4,5]
    arr.insert(2,6)
    print(arr)

    #but accessing or asigning specific indexes from the array is O(1) operation

    #link to all python list methods
    #https://docs.python.org/3/tutorial/datastructures.html

    arr[2]=9
    print(arr)

    # Initialize arr of size n with default value of 1 (or 0 in this case)
    n=10
    arr_2=[0] * n
    print(arr_2)
    # prints [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Careful: -1 is not out of bounds, it's the last value
    arr = [1, 2, 3]
    print(arr[-1])

    # Indexing -2 is the second to last value, etc.
    print(arr[-2])

    #array slicing/sublists
    arr=[1,2,3,4]
    print(arr[1:3]) # return sub list of 2 to 3

    # Similar to for-loop ranges, last index is non-inclusive
    print(arr[0:4])

    #unpacking
    a,b,c=[1,2,3]
    print(f"the values are {a,b,c}")
    # #however the number of values in your list MUST MATCH THE NUMBER OF VARIABLES
    # a,b=[1,2,4] # this won't store all the values

    #how to loop through an array
    nums=[1,2,3,4,5,6,7,8,9,10]

    #method 1:with index
    for i in range(len(nums)):
        print(nums[i])

    #method 2: access values without index
    for n in nums:
        print(n)

    #better/best way: with index and value using enumerate method
    for i,n in enumerate(nums):
        print(i,n)

    #how to loop through mulitple arrays at the same time
    #with unpacking
    a=[1,2,3]
    b=[4,5,6]
    for n1,n2 in zip(a,b):
        print(n1,n2)

    #how to reverse a list

    # method 1 using the index function to print
    print(nums[::-1])

    # method 2 using the reverse method
    nums.reverse()
    print(nums)

    #how to sort an array
    arr = [5, 4, 7, 3, 8]

    #method 1: use the built in sort method
    arr.sort()
    print(arr)

    #if you want to sort in reverse add reverse=True as a parameter
    arr.sort(reverse=True)
    print(arr)

    #if your sorting a list of strings BY DEFAULT they will be sorted in an alphabetical order
    arr = ["bob", "alice", "jane", "doe"]
    arr.sort()
    print(arr)

    #for a custom sort such as by length of each string you have to pass a lambda function as a parameter
    #how to define a lambda in python
    # lambda (variable/function name) :(code for what the function will do) (inputs)
    #lambda example
    print ((lambda x,y: x+y)(4,5))
    arr.sort(key=lambda x:len(x))
    print(arr)

    #list Comphersenions
    #syntax: [ expression using a value from an iterable, for iterable,  if conditions ]
    cubed_list=[x**3 for x in range(10) if x%3==0]
    print(cubed_list)

    # Strings are similar to arrays
    s = "abc"
    print(s[0:2])

    # But they are immutable
    # s[0] = "A"

    # So this creates a new string
    s += "def"
    print(s)

    # Valid numeric strings can be converted
    print(int("123") + int("123"))

    # And numbers can be converted to strings
    print(str(123) + str(123))

    # In rare cases you may need the ASCII value of a char
    print(ord("a"))
    print(ord("b"))

    # Combine a list of strings (with an empty string delimitor)
    strings = ["ab", "cd", "ef"]
    print("".join(strings))

    # Queues (double ended queue)
    from collections import deque

    queue = deque()
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    print(queue)

    queue.popleft()
    print(queue)

    queue.appendleft(1)
    print(queue)

    queue.pop()
    print(queue)

    queue.append(5)
    print(queue)

    # HashSet
    mySet = set()

    mySet.add(1)
    mySet.add(2)
    print(mySet)
    print(len(mySet))

    print(1 in mySet)
    print(2 in mySet)
    print(3 in mySet)

    mySet.remove(2)
    print(2 in mySet)

    # list to set
    print(set([1, 2, 3]))

    # Set comprehension
    mySet = {i for i in range(5)}
    print(mySet)

    # HashMap (aka dict)
    myMap = {}
    myMap["alice"] = 88
    myMap["bob"] = 77
    print(myMap.get("hello",3))
    print(myMap)

    myMap["alice"] = 80
    print(myMap["alice"])

    print("alice" in myMap)
    myMap.pop("alice")
    print("alice" in myMap)

    myMap = {"alice": 90, "bob": 70}
    print(myMap)

    # Dict comprehension
    myMap = {i: 2 * i for i in range(3)}
    print(myMap)

    # Looping through maps
    myMap = {"alice": 90, "bob": 70}
    for key in myMap:
        print(key, myMap[key])

    for val in myMap.values():
        print(val)

    for key, val in myMap.items():
        print(key, val)

    # Tuples are like arrays but immutable
    tup = (1, 2, 3)
    print(tup)
    print(tup[0])
    print(tup[-1])

    # Can't modify
    # tup[0] = 0

    # Can be used as key for hash map/set
    myMap = {(1, 2): 3}
    print(myMap[(1, 2)])

    mySet = set()
    mySet.add((1, 2))
    print((1, 2) in mySet)

    # Lists can't be keys
    # myMap[[3, 4]] = 5

    import heapq

    # under the hood are arrays
    minHeap = []
    heapq.heappush(minHeap, 3)
    heapq.heappush(minHeap, 2)
    heapq.heappush(minHeap, 4)

    # Min is always at index 0
    print(minHeap[0])

    while len(minHeap):
        print(heapq.heappop(minHeap))

    # No max heaps by default, work around is
    # to use min heap and multiply by -1 when push & pop.
    maxHeap = []
    heapq.heappush(maxHeap, -3)
    heapq.heappush(maxHeap, -2)
    heapq.heappush(maxHeap, -4)

    # Max is always at index 0
    print(-1 * maxHeap[0])

    while len(maxHeap):
        print(-1 * heapq.heappop(maxHeap))

    # Build heap from initial values
    arr = [2, 1, 8, 4, 5]
    heapq.heapify(arr)
    while arr:
        print(heapq.heappop(arr))

    
    def myFunc(n, m):
        return n * m
    
    
    print(myFunc(3, 4))
    
    
    # Nested functions have access to outer variables
    def outer(a, b):
        c = "c"
    
        def inner():
            return a + b + c
    
        return inner()
    
    
    print(outer("a", "b"))
    
    
    # Can modify objects but not reassign
    # unless using nonlocal keyword
    def double(arr, val):
        def helper():
            # Modifying array works
            for i, n in enumerate(arr):
                arr[i] *= 2
    
            # will only modify val in the helper scope
            # val *= 2
    
            # this will modify val outside helper scope
            nonlocal val
            val *= 2
    
        helper()
        print(arr, val)
    
    
    nums = [1, 2]
    val = 3
    double(nums, val)
    
    #for counting the totoal number of occurences in a hashmap
    #either A use a Counter
    from collections import  Counter
    
    word = "mississippi"
    #to use the counter initialze the iterable within the Counter parentheses
    c=Counter(word)
    print(c)
    
    #since the Counter is a subclass of the bulit in Dictonary under the hood it is using this syntax
    
    #the default way to count occurences using a hashmap
    word = "mississippi"
    counter=dict()
    
    for i in word:
        counter[i]=1+counter.get(i,0)
        #When you call .get() this way,
        # you get the current count of a given letter,
        # or 0 (the default) if the letter is missing.
        # Then you increment the count by 1 and store it under the corresponding letter in the dictionary.
        #this can also be written as
        #counter[i] += 1 # this is a shorthand for this counter[i]=1+counter.get(i,0)
        #but this only works for integers
    
    print(sorted(counter.values()))
    x=[4,11,10,2]
    heapq.heapify(x)
    print(x)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    











