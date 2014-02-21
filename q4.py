def findpalindrome(a,b):
    largest = 0
    for i in range(1, a+1):
        for j in range(1, b+1):
            num = i * j
            if str(num) == reverse(str(num)):
                if num > largest:
                    largest = num
    return largest

def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]

print(findpalindrome(999, 999))

