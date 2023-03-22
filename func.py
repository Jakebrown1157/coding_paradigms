def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)


# This solution returns a new sorted array that cant be changed, only added to.

# No external variables are ever changed, and the function has one input and one output

# No this function is not a higher order function cause it dosent recieve a function as an argument

# It Depends maybe it would have been simpler if i used built in methods, but im not too familiar with them yet

# Its usefull to keep functions pure because you dont have to pass a solution between multipul functions 
# making it pretty simple to use one input and have one output

