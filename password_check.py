
def password_check():
    password = "lock123"
    right = 0
    for right in (right < 5):
        
        password_try = input("enter your password:")
            

        if (password_try == "lock123"):
            print("permission granted. . .")
            break
            
        else:
            right += 1
            print("Try again, you have {} attempts left".format(5-right))
                

    
    print("maximum number of attempts exceeded,good bye")
        
        

        


password_check()
