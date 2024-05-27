# 10km를 뛰고 그 시간이 얼마나 걸렸는지 단순히 엔터 키만 사용해서 입력하도록 하고 사용자가 아무것도 입력하지 않고 엔터 키만 입력하면 평균시간 출력 후 프로그램 종료

def run_timing():
    result = 0
    cnt = 0
    while True:
        cnt += 1
        run_time = input("Enter 10km run time: ")
        if not run_time:
            break
        result += float(run_time)
        
    print("Average of " , result / (cnt - 1) , "over " , cnt - 1)
    
run_timing()