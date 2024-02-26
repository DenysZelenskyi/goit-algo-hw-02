from collections import deque

def is_palindrome(string):
    string = string.lower().replace(" ", "")
    queue = deque()
    
    for char in string:
        queue.append(char)
    
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True

while True:
    phrase = input("Введіть фразу щоб перевірити чи це паліндром або 'exit', щоб вийти: ")
    if phrase.lower() == "exit":
        break
    if is_palindrome(phrase):
        print("Паліндромом")
    else:
        print("Ця фраза не є паліндромом.")