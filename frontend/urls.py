from django.contrib import admin
from django.urls import path
from frontend import views

urlpatterns = [
    path("",views.index,name='Home'),
    path("about/",views.about,name='About'),
    path("caesarcipher/",views.caesarcipher,name='caesarcipher'),
    path("caesarcipherEncrypt/",views.caesarcipherEncrypt,name='caesarcipherEncrypt'),
    path("caesarcipherDecrypt/",views.caesarcipherDecrypt,name='caesarcipherDecrypt'),
    
    path("playfair/",views.playfair,name='playfair'),
    path("PlayfairEncrypt/",views.PlayfairEncrypt,name='PlayfairEncrypt'),
    path("PlayfairDecrypt/",views.PlayfairDecrypt,name='PlayfairDecrypt'),

    path("vigener/",views.vigener,name='vigener'),
    path("vigenerEncrypt/",views.vigenerEncrypt,name='vigenerEncrypt'),
    path("vigenerDecrypt/",views.vigenerDecrypt,name='vigenerDecrypt'),

    path("transposition/",views.transposition,name='transposition'),
    path("transpositionEncrypt/",views.transpositionEncrypt,name='transpositionEncrypt'),
    path("transpositionDecrypt/",views.transpositionDecrypt,name='transpositionDecrypt'),

    path("substitution/",views.substitution,name='substitution'),
    path("substitutionEncrypt/",views.substitutionEncrypt,name='substitutionEncrypt'),
    path("substitutionDecrypt/",views.substitutionDecrypt,name='substitutionDecrypt'),

    # path("hellman/",views.hellman,name='hellman'),
    # path("substitutionEncrypt/",views.substitutionEncrypt,name='substitutionEncrypt'),
    # path("substitutionDecrypt/",views.substitutionDecrypt,name='substitutionDecrypt'),

    path("chineseremainder/",views.chineseremainder,name='chineseremainder'),
    path("chineseremaindervalue/",views.chineseremaindervalue,name='chineseremaindervalue'),

    path("rsa/",views.rsa,name='rsa'),
    path("rsaEncrypt/",views.rsaEncrypt,name='rsaEncrypt'),
    path("rsaDecrypt/",views.rsaDecrypt,name='rsaDecrypt'),

    path("fermat/",views.fermat,name='fermat'),
    path("fermatvalue/",views.fermatvalue,name='fermatvalue'),

    path("extendedeuclidean/",views.extendedeuclidean,name='extendedeuclidean'),
    path("extendedeuclideanvalue/",views.extendedeuclideanvalue,name='extendedeuclideanvalue'),

    path("railfence/",views.railfence,name='railfence'),
    path("railfenceEncrypt/",views.railfenceEncrypt,name='railfenceEncrypt'),
    path("railfenceDecrypt/",views.railfenceDecrypt,name='railfenceDecrypt'),

]
