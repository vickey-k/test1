def longest_substring(s):
    longest = ""
    current = ""
    for i in s:
        if i in current:
            index = current.index(i)
            current = current[index+1 :]
        current = current + i

        if len(current) > len(longest):
            longest = current
    return longest
s = input("enter the substring : ")
print(f"the longest nonrepeating substring is {longest_substring(s)}")
