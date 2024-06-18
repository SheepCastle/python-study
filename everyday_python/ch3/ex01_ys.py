# 처음과 마지막 요소 찾기

def first_last(sequence):
    return sequence[:1] + sequence[-1:]

test = (1, 2, 3, 4, 5)

print(first_last(test))


# 책에서는 이 아래에 것을 sequence[0] + sequence[-1]로 해서 문제가 있고, 그래서 꼭 위의 함수와 같이 
# 슬라이싱 하는 코드로 작성을 해야만 하는 것 처럼 얘기를 하고 있는데 사실 가운데를 , 로 바꾸면 전혀 상관없이 같은 결과가 나오는데 꼭 슬라이싱을 해야하는 상황인건가?

def first_last_err(sequence):
    return sequence[0] , sequence[-1]

print(first_last_err(test))