from django.shortcuts import render
from django.http import HttpResponse
import math,string

def index(request):
    return render(request,'index.html')
    # return HttpResponse("Hello, world. You're at the polls index."

def about(request):
    return HttpResponse("Hello About")

def caesarcipher(request):
    return render(request,'caesarcipher.html')
    # return HttpResponse("Hello About")

def caesarcipherEncrypt(request):
    ALPHEBET = '0123456789abcdefghijklmnopqrstuvwxyz'
    cipher = ''
    # plain_text, key
    if request.method == "POST":
        plain_text = request.POST['plain_text']
        key = int(request.POST['key'])
        # Iterates through the given plain_text
        for i in plain_text:
            # Lower the letter
            lower_i = i.lower()
            # If letter does occur in the ALPHEBET,
            # Encryption will be proceeded
            if lower_i in ALPHEBET:
                ciphered = ''
                # When letter index is higher than 32,
                # Letter can't change position by the KEY
                # So the ciphered letter will be started by the beginning
                if ALPHEBET.find(lower_i) > len(ALPHEBET) - (key + 1):
                    ciphered = ALPHEBET[(ALPHEBET.find(
                        lower_i) + key) % len(ALPHEBET)]
                else:
                    ciphered = ALPHEBET[ALPHEBET.find(lower_i) + key]
                # If the letter is an uppercase,
                # cipher letter will be uppercased too
                cipher += ciphered.upper() if i.isupper() else ciphered
            # If letter doesn't occur in the ALPHEBET,
            # the plain letter will be added to the cipher text
            else:
                cipher += i
        return render(request,'caesarcipher.html',{'cipher':cipher})
    else:
        return render(request,'caesarcipher.html',{'cipher':''})

def caesarcipherDecrypt(request):

    ALPHEBET = '0123456789abcdefghijklmnopqrstuvwxyz'
    plain = ''
    
    if request.method == "POST":
        cipher_text = request.POST['cipher_text']
        key = int(request.POST['key'])
        for i in cipher_text:
            lower_i = i.lower()
            # If letter does occur in the ALPHEBET,
            # Encryption will be proceeded
            if lower_i in ALPHEBET:
                decrypted = ''
                if ALPHEBET.find(lower_i) > len(ALPHEBET) - (key + 1):
                    decrypted = ALPHEBET[(ALPHEBET.find(
                        lower_i) - key) % len(ALPHEBET)]
                else:
                    decrypted = ALPHEBET[ALPHEBET.find(lower_i) - key]
                # If the letter is an uppercase,
                # decrypted letter will be uppercased too
                plain += decrypted.upper() if i.isupper() else decrypted
            # If letter doesn't occur in the ALPHEBET,
            # the plain letter will be added to the plain text
            else:
                plain += i
        return render(request,'caesarcipher.html',{'plain':plain})
    else:
        return render(request,'caesarcipher.html',{'plain':''})

def playfair(request):
    return render(request,'playfair.html')
    # return HttpResponse("Hello About")

def PlayfairEncrypt(request):

    if request.method == "POST":
        plain_text = request.POST['plain_text']
        key = request.POST['key']

        def toLowerCase(text):
            return text.lower()

        # Function to remove all spaces in a string


        def removeSpaces(text):
            newText = ""
            for i in text:
                if i == " ":
                    continue
                else:
                    newText = newText + i
            return newText

        # Function to group 2 elements of a string
        # as a list element


        def Diagraph(text):
            Diagraph = []
            group = 0
            for i in range(2, len(text), 2):
                Diagraph.append(text[group:i])

                group = i
            Diagraph.append(text[group:])
            return Diagraph

        # Function to fill a letter in a string element
        # If 2 letters in the same string matches


        def FillerLetter(text):
            k = len(text)
            if k % 2 == 0:
                for i in range(0, k, 2):
                    if text[i] == text[i+1]:
                        new_word = text[0:i+1] + str('x') + text[i+1:]
                        new_word = FillerLetter(new_word)
                        break
                    else:
                        new_word = text
            else:
                for i in range(0, k-1, 2):
                    if text[i] == text[i+1]:
                        new_word = text[0:i+1] + str('x') + text[i+1:]
                        new_word = FillerLetter(new_word)
                        break
                    else:
                        new_word = text
            return new_word


        list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        # Function to generate the 5x5 key square matrix


        def generateKeyTable(word, list1):
            key_letters = []
            for i in word:
                if i not in key_letters:
                    key_letters.append(i)

            compElements = []
            for i in key_letters:
                if i not in compElements:
                    compElements.append(i)
            for i in list1:
                if i not in compElements:
                    compElements.append(i)

            matrix = []
            while compElements != []:
                matrix.append(compElements[:5])
                compElements = compElements[5:]

            return matrix


        def search(mat, element):
            for i in range(5):
                for j in range(5):
                    if(mat[i][j] == element):
                        return i, j


        def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
            char1 = ''
            if e1c == 4:
                char1 = matr[e1r][0]
            else:
                char1 = matr[e1r][e1c+1]

            char2 = ''
            if e2c == 4:
                char2 = matr[e2r][0]
            else:
                char2 = matr[e2r][e2c+1]

            return char1, char2


        def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
            char1 = ''
            if e1r == 4:
                char1 = matr[0][e1c]
            else:
                char1 = matr[e1r+1][e1c]

            char2 = ''
            if e2r == 4:
                char2 = matr[0][e2c]
            else:
                char2 = matr[e2r+1][e2c]

            return char1, char2


        def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
            char1 = ''
            char1 = matr[e1r][e2c]

            char2 = ''
            char2 = matr[e2r][e1c]

            return char1, char2


        def encryptByPlayfairCipher(Matrix, plainList):
            CipherText = []
            for i in range(0, len(plainList)):
                c1 = 0
                c2 = 0
                ele1_x, ele1_y = search(Matrix, plainList[i][0])
                ele2_x, ele2_y = search(Matrix, plainList[i][1])

                if ele1_x == ele2_x:
                    c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
                    # Get 2 letter cipherText
                elif ele1_y == ele2_y:
                    c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
                else:
                    c1, c2 = encrypt_RectangleRule(
                        Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

                cipher = c1 + c2
                CipherText.append(cipher)
            return CipherText


        text_Plain = plain_text
        text_Plain = removeSpaces(toLowerCase(text_Plain))
        PlainTextList = Diagraph(FillerLetter(text_Plain))
        if len(PlainTextList[-1]) != 2:
            PlainTextList[-1] = PlainTextList[-1]+'z'

        key = key
        #print("Key text:", key)
        key = toLowerCase(key)
        Matrix = generateKeyTable(key, list1)

        #print("Plain Text:", text_Plain)
        CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)

        CipherText = ""
        for i in CipherList:
            CipherText += i
        #print("CipherText:", CipherText)

        # This code is Contributed by Boda_Venkata_Nikith

        return render(request,'playfair.html',{'playfaircipher':CipherText})
    else:
        return render(request,'playfair.html',{'playfaircipher':''})


def PlayfairDecrypt(request):
    
    if request.method == "POST":
        cipher_text = request.POST['cipher_text']
        key = request.POST['key']
       
        def toLowerCase(plain):
            # Convert all the characters of a string to lowercase
            return plain.lower()


        def removeSpaces(plain):
            # Remove all spaces in a string
            # can be extended to remove punctuation
            return ''.join(plain.split())


        def generateKeyTable(key):
            # generates the 5x5 key square
            keyT = [['' for i in range(5)] for j in range(5)]
            dicty = {chr(i + 97): 0 for i in range(26)}

            for i in range(len(key)):
                if key[i] != 'j':
                    dicty[key[i]] = 2
            dicty['j'] = 1

            i, j, k = 0, 0, 0
            while k < len(key):
                if dicty[key[k]] == 2:
                    dicty[key[k]] -= 1
                    keyT[i][j] = key[k]
                    j += 1
                    if j == 5:
                        i += 1
                        j = 0
                k += 1

            for k in dicty.keys():
                if dicty[k] == 0:
                    keyT[i][j] = k
                    j += 1
                    if j == 5:
                        i += 1
                        j = 0

            return keyT


        def search(keyT, a, b):
            # Search for the characters of a digraph in the key square and return their position
            arr = [0, 0, 0, 0]

            if a == 'j':
                a = 'i'
            elif b == 'j':
                b = 'i'

            for i in range(5):
                for j in range(5):
                    if keyT[i][j] == a:
                        arr[0], arr[1] = i, j
                    elif keyT[i][j] == b:
                        arr[2], arr[3] = i, j

            return arr


        def mod5(a):
            # Function to find the modulus with 5
            if a < 0:
                a += 5
            return a % 5


        def decrypt(str, keyT):
            # Function to decrypt
            ps = len(str)
            i = 0
            while i < ps:
                a = search(keyT, str[i], str[i+1])
                if a[0] == a[2]:
                    str = str[:i] + keyT[a[0]
                                        ][mod5(a[1]-1)] + keyT[a[0]][mod5(a[3]-1)] + str[i+2:]
                elif a[1] == a[3]:
                    str = str[:i] + keyT[mod5(a[0]-1)][a[1]] + \
                        keyT[mod5(a[2]-1)][a[1]] + str[i+2:]
                else:
                    str = str[:i] + keyT[a[0]][a[3]] + keyT[a[2]][a[1]] + str[i+2:]
                i += 2

            return str


        def decryptByPlayfairCipher(str, key):
            # Function to call decrypt
            ks = len(key)
            key = removeSpaces(toLowerCase(key))
            str = removeSpaces(toLowerCase(str))
            keyT = generateKeyTable(key)
            return decrypt(str, keyT)


        
        str = cipher_text
        key = key

        # Key to be encrypted
        #print("Key text: ", key)

        # Ciphertext to be decrypted
        #print("Plain text: ", str)

        # encrypt using Playfair Cipher
        CipherList = decryptByPlayfairCipher(str, key)

        playfairDecrypttext =""
        for i in CipherList:
            playfairDecrypttext +=i
        # Decrypted text
        #print("Deciphered text: ", str)
        return render(request,'playfair.html',{'plain':playfairDecrypttext})
        # Pyhton Code Written By Kushal Prajapati
    else:
        return render(request,'playfair.html',{'plain':''})
    
#vigener cipher

def vigener(request):
    return render(request,'vigener.html')
    # return HttpResponse("Hello About")

def vigenerEncrypt(request):

    if request.method == "POST":
        plain_text = request.POST['plain_text']
        key = request.POST['key']

        def generateKey(string, key): 
            key = list(key) 
            if len(string) == len(key): 
                return(key) 
            else: 
                for i in range(len(string) -len(key)): 
                    key.append(key[i % len(key)]) 
            return("" . join(key)) 
        
        def encryption(string, key): 
            encrypt_text = [] 
            for i in range(len(string)): 
                x = (ord(string[i]) +ord(key[i])) % 26
                x += ord('A') 
                encrypt_text.append(chr(x)) 
            return("" . join(encrypt_text)) 


        string = plain_text
        keyword = key
        key = generateKey(string, keyword) 
        encrypt_text = encryption(string,key) 
        #print("Encrypted message:", encrypt_text) 
       
        CipherText = ""
        for i in encrypt_text:
            CipherText += i

        return render(request,'vigener.html',{'vigenercipher':CipherText})
    else:
        return render(request,'vigener.html',{'vigenercipher':''})


def vigenerDecrypt(request):
    
    if request.method == "POST":
        cipher_text = request.POST['cipher_text']
        key = request.POST['key']

        def generateKey(string, key): 
            key = list(key) 
            if len(string) == len(key): 
                return(key) 
            else: 
                for i in range(len(string) -len(key)): 
                    key.append(key[i % len(key)]) 
            return("" . join(key)) 

        def decryption(encrypt_text, key): 
            orig_text = [] 
            for i in range(len(encrypt_text)): 
                x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
                x += ord('A') 
                orig_text.append(chr(x)) 
            return("" . join(orig_text)) 


        string = cipher_text
        keyword = key
        key = generateKey(string, keyword)  
        
        decryption_text = decryption(string, key)

        plain_cipher = ""
        for i in decryption_text:
            plain_cipher += i
        return render(request,'vigener.html',{'plain':plain_cipher})
        # Pyhton Code Written By Kushal Prajapati
    else:
        return render(request,'vigener.html',{'plain':''})


#Columnar Transposition Cipher

def transposition(request):
    return render(request,'transposition.html')
    # return HttpResponse("Hello About")

def transpositionEncrypt(request):

    if request.method == "POST":
        plain_text = request.POST['plain_text']
        key = request.POST['key']
        # Columnar Transposition

        # Encryption
        def encryptMessage(msg):
            cipher = ""

            # track key indices
            k_indx = 0

            msg_len = float(len(msg))
            msg_lst = list(msg)
            key_lst = sorted(list(key))

            # calculate column of the matrix
            col = len(key)
            
            # calculate maximum row of the matrix
            row = int(math.ceil(msg_len / col))

            # add the padding character '_' in empty
            # the empty cell of the matix
            fill_null = int((row * col) - msg_len)
            msg_lst.extend('_' * fill_null)

            # create Matrix and insert message and
            # padding characters row-wise
            matrix = [msg_lst[i: i + col]
                    for i in range(0, len(msg_lst), col)]

            # read matrix column-wise using key
            for _ in range(col):
                curr_idx = key.index(key_lst[k_indx])
                cipher += ''.join([row[curr_idx]
                                for row in matrix])
                k_indx += 1

            return cipher

        # Decryption
       
        # Driver Code
        msg = plain_text

        cipher = encryptMessage(msg)
        fchiper = format(cipher)
        # print("Encrypted Message: {}".format(cipher))

        # print("Decryped Message: {}".
        #     format(decryptMessage(cipher)))



        CipherText = ""
        for i in fchiper:
            CipherText += i

        return render(request,'transposition.html',{'transpositioncipher':CipherText})
    else:
        return render(request,'transposition.html',{'transpositioncipher':''})


def transpositionDecrypt(request):
    
    if request.method == "POST":
        cipher_text = request.POST['cipher_text']
        key = request.POST['key']

        def decryptMessage(cipher):
            msg = ""

            # track key indices
            k_indx = 0

            # track msg indices
            msg_indx = 0
            msg_len = float(len(cipher))
            msg_lst = list(cipher)

            # calculate column of the matrix
            col = len(key)
            
            # calculate maximum row of the matrix
            row = int(math.ceil(msg_len / col))

            # convert key into list and sort
            # alphabetically so we can access
            # each character by its alphabetical position.
            key_lst = sorted(list(key))

            # create an empty matrix to
            # store deciphered message
            dec_cipher = []
            for _ in range(row):
                dec_cipher += [[None] * col]

            # Arrange the matrix column wise according
            # to permutation order by adding into new matrix
            for _ in range(col):
                curr_idx = key.index(key_lst[k_indx])

                for j in range(row):
                    dec_cipher[j][curr_idx] = msg_lst[msg_indx]
                    msg_indx += 1
                k_indx += 1

            # convert decrypted msg matrix into a string
            try:
                msg = ''.join(sum(dec_cipher, []))
            except TypeError:
                raise TypeError("This program cannot",
                                "handle repeating words.")

            null_count = msg.count('_')

            if null_count > 0:
                return msg[: -null_count]

            return msg

        # Driver Code
        msg = cipher_text
        TransDecryped = format(decryptMessage(msg))
        return render(request,'transposition.html',{'plain':TransDecryped})
        # Pyhton Code Written By Kushal Prajapati
    else:
        return render(request,'transposition.html',{'plain':''})
    

# Classical substitution cipher

def substitution(request):
    return render(request,'substitution.html')

def substitutionEncrypt(request):

    if request.method == "POST":
        plain_text = request.POST['plain_text']
        key = int(request.POST['key'])
        # Python program to demonstrate
        # Substitution Cipher
        # A list containing all characters
        all_letters= string.ascii_letters

            
        """
        create a dictionary to store the substitution
        for the given alphabet in the plain text
        based on the key
        """

            
        dict1 = {}

        for i in range(len(all_letters)):
            dict1[all_letters[i]] = all_letters[(i+key)%len(all_letters)]


        cipher_txt=[]

        # loop to generate ciphertext

        for char in plain_text:
            if char in all_letters:
                temp = dict1[char]
                cipher_txt.append(temp)
            else:
                temp =char
                cipher_txt.append(temp)
                
        cipher_txt= "".join(cipher_txt)
        # print("Cipher Text is: ",cipher_txt)

        CipherText = ""
        for i in cipher_txt:
            CipherText += i

        return render(request,'substitution.html',{'substitution':CipherText})
    else:
        return render(request,'substitution.html',{'substitution':''})


def substitutionDecrypt(request):
    
    if request.method == "POST":
        cipher_text = request.POST['cipher_text']
        key = int(request.POST['key'])

        # A list containing all characters
        all_letters= string.ascii_letters

        """
        create a dictionary to store the substitution
        for the given alphabet in the cipher
        text based on the key
        """            
        dict2 = {}	
        for i in range(len(all_letters)):
            dict2[all_letters[i]] = all_letters[(i-key)%(len(all_letters))]
            
        # loop to recover plain text
        decrypt_txt = []

        for char in cipher_text:
            if char in all_letters:
                temp = dict2[char]
                decrypt_txt.append(temp)
            else:
                temp = char
                decrypt_txt.append(temp)
                
        decrypt_txt = "".join(decrypt_txt)
        # print("Recovered plain text :", decrypt_txt)

        CipherText = ""
        for i in decrypt_txt:
            CipherText += i
        return render(request,'substitution.html',{'plain':CipherText})
        # Pyhton Code Written By Kushal Prajapati
    else:
        return render(request,'substitution.html',{'plain':''})
    


# chineseremainder Theoream

def chineseremainder(request):
    return render(request,'chineseremainder.html')
    

def chineseremaindervalue(request):

    if request.method == "POST":
        key1 = request.POST['key1']
        key2 = request.POST['key2']

        num = list(map(int,key1.strip().split()))
        rem = list(map(int,key2.strip().split()))
        
        # A Python3 program to demonstrate
        # working of Chinise remainder Theorem

        # k is size of num[] and rem[].
        # Returns the smallest number x
        # such that:
        # x % num[0] = rem[0],
        # x % num[1] = rem[1],
        # ..................
        # x % num[k-2] = rem[k-1]
        # Assumption: Numbers in num[]
        # are pairwise coprime (gcd for
        # every pair is 1)
        def findMinX(num, rem, k):
            x = 1; # Initialize result

            # As per the Chinise remainder
            # theorem, this loop will
            # always break.
            while(True):
                
                # Check if remainder of
                # x % num[j] is rem[j]
                # or not (for all j from
                # 0 to k-1)
                j = 0;
                while(j < k):
                    if (x % num[j] != rem[j]):
                        break;
                    j += 1;

                # If all remainders
                # matched, we found x
                if (j == k):
                    return x;

                # Else try next number
                x += 1;

        k = len(num)
        xvalue=findMinX(num, rem, k)
        # print("x is", findMinX(num, rem, k))
        return render(request,'chineseremainder.html',{'chineseremainder':xvalue})
    else:
        return render(request,'chineseremainder.html',{'chineseremainder':''})

#RSA 
def rsa(request):
    return render(request,'rsa.html')
    

def rsaEncrypt(request):

    if request.method == "POST":
        key1 = request.POST['key1']
        key2 = request.POST['key2']

        num = list(map(int,key1.strip().split()))
        rem = list(map(int,key2.strip().split()))
        

        # print("x is", findMinX(num, rem, k))
        return render(request,'rsa.html',{'rsa':xvalue})
    else:
        return render(request,'rsa.html',{'rsa':''})

def rsaDecrypt(request):

    if request.method == "POST":
        key1 = request.POST['key1']
        key2 = request.POST['key2']

        num = list(map(int,key1.strip().split()))
        rem = list(map(int,key2.strip().split()))
        

        # print("x is", findMinX(num, rem, k))
        return render(request,'rsa.html',{'rsa':xvalue})
    else:
        return render(request,'rsa.html',{'rsa':''})



# Fermat’s Theoream

def fermat(request):
    return render(request,'fermat.html')
    

def fermatvalue(request):

    if request.method == "POST":
        key1 = int(request.POST['key1'])
        key2 = int(request.POST['key2'])

        # num = list(map(int,key1.strip().split()))
        # rem = list(map(int,key2.strip().split()))
        # Python program to find
        # modular inverse of a
        # under modulo m using
        # Fermat's little theorem.
        # This program works
        # only if m is prime.


        def __gcd(a, b):

            if(b == 0):
                return a
            else:
                return __gcd(b, a % b)

        # To compute x^y under modulo m


        def power(x, y, m):

            if (y == 0):
                return 1
            p = power(x, y // 2, m) % m
            p = (p * p) % m

            return p if(y % 2 == 0) else (x * p) % m

        # Function to find modular
        # inverse of a under modulo m
        # Assumption: m is prime


        def modInverse(a, m):

            if (__gcd(a, m) != 1):
                return "Inverse doesn't exist"
                # print("Inverse doesn't exist")

            else:

                # If a and m are relatively prime, then
                # modulo inverse is a^(m-2) mode m
                allmod=power(a, m - 2, m)
                return allmod
                
                    

        # Driver code


        a = key1
        m = key2
        modresult=modInverse(a, m)
        return render(request,'fermat.html',{'fermatvalues':modresult})
    else:
        return render(request,'fermat.html',{'fermatvalues':''})

#  Extend Edeuclidean Theoream

def extendedeuclidean(request):
    return render(request,'extendedeuclidean.html')
    

def extendedeuclideanvalue(request):

    if request.method == "POST":
        key1 = int(request.POST['key1'])
        key2 = int(request.POST['key2'])

        # Python program to demonstrate working of extended
        # Euclidean Algorithm

        # function for extended Euclidean Algorithm


        def gcdExtended(a, b):

            # Base Case
            if a == 0:
                return b, 0, 1

            gcd, x1, y1 = gcdExtended(b % a, a)

            # Update x and y using results of recursive
            # call
            x = y1 - (b//a) * x1
            y = x1

            return gcd, x, y


        # Driver code
        a, b = 35, 15
        g,x,y = gcdExtended(a, b)
        # print("gcd(", a, ",", b, ") = ", g)
        return render(request,'extendedeuclidean.html',{'extendedeuclideanvalues':g})
    else:
        return render(request,'extendedeuclidean.html',{'extendedeuclideanvalues':''})

# Rail Fence Cipher 

def railfence(request):
    return render(request,'railfence.html')

def railfenceEncrypt(request):

    if request.method == "POST":
        plain_text = request.POST['plain_text']
        key = int(request.POST['key'])
        
        # Python3 program to illustrate
        # Rail Fence Cipher Encryption
        # and Decryption

        # function to encrypt a message
        def encryptRailFence(text, key):

            # create the matrix to cipher
            # plain text key = rows ,
            # length(text) = columns
            # filling the rail matrix
            # to distinguish filled
            # spaces from blank ones
            rail = [['\n' for i in range(len(text))]
                        for j in range(key)]
            
            # to find the direction
            dir_down = False
            row, col = 0, 0
            
            for i in range(len(text)):
                
                # check the direction of flow
                # reverse the direction if we've just
                # filled the top or bottom rail
                if (row == 0) or (row == key - 1):
                    dir_down = not dir_down
                
                # fill the corresponding alphabet
                rail[row][col] = text[i]
                col += 1
                
                # find the next row using
                # direction flag
                if dir_down:
                    row += 1
                else:
                    row -= 1
            # now we can construct the cipher
            # using the rail matrix
            result = []
            for i in range(key):
                for j in range(len(text)):
                    if rail[i][j] != '\n':
                        result.append(rail[i][j])
            return("" . join(result))
            

        railfenceEncryptvalue = encryptRailFence(plain_text, key)
           

        # This code is contributed
        # by Pratik Somwanshi


        return render(request,'railfence.html',{'railfence':railfenceEncryptvalue})
    else:
        return render(request,'railfence.html',{'railfence':''})


def railfenceDecrypt(request):
    
    if request.method == "POST":
        cipher_text = request.POST['cipher_text']
        key = int(request.POST['key'])

                # This function receives cipher-text
        # and key and returns the original
        # text after decryption
        def decryptRailFence(cipher, key):

            # create the matrix to cipher
            # plain text key = rows ,
            # length(text) = columns
            # filling the rail matrix to
            # distinguish filled spaces
            # from blank ones
            rail = [['\n' for i in range(len(cipher))]
                        for j in range(key)]
            
            # to find the direction
            dir_down = None
            row, col = 0, 0
            
            # mark the places with '*'
            for i in range(len(cipher)):
                if row == 0:
                    dir_down = True
                if row == key - 1:
                    dir_down = False
                
                # place the marker
                rail[row][col] = '*'
                col += 1
                
                # find the next row
                # using direction flag
                if dir_down:
                    row += 1
                else:
                    row -= 1
                    
            # now we can construct the
            # fill the rail matrix
            index = 0
            for i in range(key):
                for j in range(len(cipher)):
                    if ((rail[i][j] == '*') and
                    (index < len(cipher))):
                        rail[i][j] = cipher[index]
                        index += 1
                
            # now read the matrix in
            # zig-zag manner to construct
            # the resultant text
            result = []
            row, col = 0, 0
            for i in range(len(cipher)):
                
                # check the direction of flow
                if row == 0:
                    dir_down = True
                if row == key-1:
                    dir_down = False
                    
                # place the marker
                if (rail[row][col] != '*'):
                    result.append(rail[row][col])
                    col += 1
                    
                # find the next row using
                # direction flag
                if dir_down:
                    row += 1
                else:
                    row -= 1
            return("".join(result))

        decryptRailFencevalues = decryptRailFence(cipher_text, key)
        
        return render(request,'railfence.html',{'plain':decryptRailFencevalues})
        # Pyhton Code Written By Kushal Prajapati
    else:
        return render(request,'railfence.html',{'plain':''})
    


