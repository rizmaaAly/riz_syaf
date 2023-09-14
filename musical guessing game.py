def main():
    print("⭐Welcome to Musical Challenge⭐")
    print("Please enter the username for your account")
    global user_name
    user_name = str(input())
    save = open(user_name + '.txt', 'w')
    
    PasswordCheck= True
    while PasswordCheck:
        user_password = input("\nType in your password: ")
        if len(user_password) < 8:
            print("\nYour password must be 8 characters long")
        elif not any(i.isdigit() for i in user_password):
            print("\nYou need a number in your password")
        elif not any(i.isupper() for i in user_password):
            print("\nYou need a capital letter in your password")
        elif not any(i.islower() for i in user_password):
            print("\nYou need a lowercase letter in your password")
        else:
            PasswordCheck = False

    import random
    print("\nHi player >< ! Wanna try to guess the music genre ?")
    
    
    
    genre = [    
        "indie",
        "pop",
        "rock",
        "disco",
        "electronic",
        "jazz",
        "hip hop",
        "kpop"
        ]
    
    x = random.choice(genre)
    print(genre)
    guess = None
    pop = None
    rock = None
    disco = None
    electronic = None
    jazz = None
    hip_hop = None
    kpop = None
    indie = None
    while x != guess:
        
        guess = str(input("\ncan you guess the correct music genre ?? "))
                
        if x == guess:
            print("\nCongratulations you got it right dear><!❤.")
            clue = None
            
        elif x == indie:
            print (" start with i ")
                
        elif x == disco:
            print (" start with d ")
                
        elif x == electronic:
            print (" start with e ")
                
        elif x == hip_hop:
            print (" start with h ")
                
        elif x == pop:
            print (" start with p ")
                
        elif x == kpop:
            print (" start with k ")
                
        elif x == rock:
            print (" start with r ")
                
        elif x == jazz:
            print (" start with j ")
        
        else:
            print("\nsorry love but that is incorrect.you can try again <3!.")
            
    
main()
