

def palindromeRecursivo(word):
    
    if len(word)<=1:
        return True
    
    if word[0] == word[-1]:
        return palindromeRecursivo(word[1:-1])
    else:
        return False
    
def palindromeIterativo(word):

    izqDer= list(word)
    derIzq=[]

    for letter in range(len(word) -1, -1, -1):
        derIzq.append(word[letter])

    if izqDer == derIzq:
        return True
    else:
        return False
        
    