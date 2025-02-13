print('''
Welcome to Treasure Island
Your mission is to find the treasure.
''')


q1 = input("You are at cross roads, Will you take 'right' or 'left'? ").lower()

if q1 == "left":
    q2 = input("Nice. Now you reached a lake. Will you 'swim', or 'wait'? ").lower()
    
    if q2 == "wait":
        q3 = input('You\'ve reached a mountain with three doors,'
                   'red, blue and yellow.'
                   'Which on you will open? ').lower()
        
        if q3 == "yellow":
            print("You Win!")
        
        else:
            print("You loose, Game over!")
    
    else:
        q2 == "swim"
        print("You loose, Game over!")

else:
    q1 == "rigt"
    print("You loose, Game Over!")
    
    
