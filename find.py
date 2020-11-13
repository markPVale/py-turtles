# strng = "bobmac"
# ix = 1

# print(strng[ix])


# print(strng.find("o", ix))


# strng1 = "bobmaco"
# nx = 1

# print(strng1[nx])


# print(strng1.find("o", nx) + 1)


# def str_sub(str, sub):
#     count = 0
#     start = -1
#     while start < len(str):
#         start = str.find(sub, start + 1)
#         if str.find(sub, start) == -1:
#             return count
#         else:
#             count += 1
#     print(start)


# str_sub("banana", "an")


# def str_sub(sub, str):
#     """Count the number of times a substring appears in a string"""
#     count = 0
#     start = -1
#     while True:
#         start = str.find(sub, start + 1)
#         if start == -1:
#             print(count)
#         else:
#             count += 1


# str_sub("an", "banana")


# def count(sub_string, string):
#     """Count the numbers of times sub_string appears in string."""
#     appearances = 0
#     last_found_at = -1
#     while True:
#         last_found_at = string.find(sub_string, last_found_at + 1)
#         if last_found_at == -1:
#             return appearances
#         else:
#             appearances += 1


# print(count("an", "banana"))

def sub_str(str, sub, start=-1):
    count = 0
    start = start
    while str.find(sub) != -1:
        start = str.find(sub, start + 1)
        if start == -1:
            return count
        else:
            count += 1


print(sub_str("banana", "an"))
