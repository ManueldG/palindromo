def isPal(letter):
                
        return letter==letter[::-1]
        
    


test = input("inserisci testo da verificare: ")
print("è palindromo" if isPal(test) else "non è palindromo")
