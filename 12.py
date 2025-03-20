def reverse_list(m):
    return m[::-1]
a=input("请输入：")
b=a.split(",")
print(",".join(reverse_list(b)))