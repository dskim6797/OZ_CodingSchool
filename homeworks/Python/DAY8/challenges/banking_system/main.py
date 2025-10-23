from services.banking_service import BankingService 
from utils.exceptions import UserNotFoundError

def main():
    banking_service = BankingService()
    
    while True:
        try:
            option = input("1. 사용자 추가, 2: 사용자 찾기, 3: 사용자 메뉴, 4: 종료 : ")
            
            if option == '1':
                add_username = input("사용자 추가. 사용자 명:")
                banking_service.add_user(add_username)
                
            elif option == '2':
                find_username = input("사용자 찾기. 사용자 명:")
                banking_service.find_user(find_username)
                
            elif option == '3':
                username = input("메뉴를 이용할 사용자 명:")
                banking_service.user_menu(username)
                
            elif option == '4':
                print("서비스를 종료합니다.")
                break
            
            else:
                print("잘못된 입력입니다. 다시 시도하세요.")
                
        except ValueError as e:
            print(f"잘못된 입력입니다: {e}")
        except UserNotFoundError as e:
            print(f"오류: {e}")
        except Exception as e:
            print(f"알 수 없는 오류가 발생했습니다: {e}")
        
        print("\n")
        
if __name__ == "__main__":
    main()