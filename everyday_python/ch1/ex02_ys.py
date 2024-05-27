# sum 함수 짝퉁인 mysum 함수를 만들어볼 것

def mysum(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result
user_input = input("Please write number for sum: ")

numbers = map(int, user_input.split())
print(mysum(*numbers))