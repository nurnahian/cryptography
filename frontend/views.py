from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # ALPHEBET = '0123456789abcdefghijklmnopqrstuvwxyz'
    # if request.method == 'POST':
    #     if encrypt == request.POST['encrypt']:
    #         plain_text = request.POST['plain_text']
    #         key = request.POST['key']
    #         plain_text1=encrypt(plain_text,key)
    #         return render(request,'index.html',{'plain_text1':plain_text1})
    #     else:
    #      decrypt = request.POST['decrypt']
    #      cipher_text = request.POST['cipher_text']
    #      key = request.POST['key']
    #      cipher_text1=decrypt(cipher_text, key)
    #      return render(request,'index.html',{'cipher_text1':cipher_text1})
    return render(request,'index.html')
    
    # return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def about(request):
    return HttpResponse("Hello About")

def caesarcipher(request):
    return render(request,'caesarcipher.html')
    # return HttpResponse("Hello About")

def encrypt(plain_text, key):
    cipher = ''
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
    return cipher


def decrypt(cipher_text, key):
    plain = ''
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
    return plain



