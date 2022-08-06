import sys


# sys.argv[0]은 실행된 파일 경로 

def print_help():
    print("안녕!!!")
    
if __name__ == "__main__":
    arguments = sys.argv
    # 즉 리스트 길이가 한개이면, sys.argv[0](실행된 파일 경로)만 있으면      
    if len(arguments) == 1: 
        print("인자가 없습니다. 해당되는 param을 입력해주세요!")    
    # 받은 인자가 --연아 또는 --연아2 면은 ?!     
    elif arguments[1] == "--연아" or arguments[1] == "--연아2":
        print_help()
    else:
        print("인자가 형식에 맞지 않습니다!")
        
        
# 출처: https://appia.tistory.com/507
        