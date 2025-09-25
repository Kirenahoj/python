def flippblipp(n):
    if n%3 == 0 and n%5 == 0:
        return "flipp blipp"
    elif n%3 == 0:
        return"flipp"
    elif n%5 == 0:
        return "blipp"
    else:
        return str(n)

n = 1
print("      ", n)

while True:
    n = n+1
    svar = flippblipp(n)
    gissning = input("Nästa: ")
    
    if gissning != svar:
        print(f"Fel -  {svar}")
        print()
        print("Game Over")
        break
        
    
    
