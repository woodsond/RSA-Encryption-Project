#Project 3: Diante Woodson, Christopher Stinson, Daniel Ashcraft
import sys
import random

def main():
    publicOrPrivate()

def publicOrPrivate():
    print("1. Owner") #provide option for owner
    print()
    print("2. Public User")#provide option for public user
    
    userChoice = input("""Are you a private or a public user (Please enter 1 or 2):  """) #take user input and check if they are an owner or public user
    while (userChoice != 1 or userChoice != 2): #this loop will handle the error checking if user input does not equal exactly 1 or 2
        userChoice = input("""Please enter 1 or 2:  """)


    if userChoice == 1:
        publicUserMenu()
    elif userChoice == 2:
        ownerMenu()


def publicUserMenu():
    print("1. Encrypt a message") #will lead to RSA encryption for public user and will provide a digital signature for the user as well
    print("2. Authenticate digital signature") #this will just check if the digital signature is authentic, and if not it will make a new digital signature that is authentic

    userChoice = input("""Do you want to encrypt a message or authenticate your digital signature (Please enter 1 or 2):  """)
    while (userChoice != 1 or userChoice != 2):
        userChoice = input("""Please enter 1 or 2:  """)

    if userChoice == 1:
        keyGeneration()
    elif userChoice == 2:
        checkDS()

def ownerMenu():
    print("1. Decipher text") #will decipher text that public users have that are encrypted
    print("2. Generate digital signature") #this will create a digital signature that can then be check by public users for if it is authentic or not

    userChoice = input("""Do you want to decipher text or generate a new digital signature (Please enter 1 or 2):  """)
    while (userChoice != 1 or userChoice != 2):
        userChoice = input("""Please enter 1 or 2:  """)

    if userChoice == 1:
        decrypt()
    elif userChoice == 2:
        generateSignature()

def keyGeneration():
    primeOne, primeTwo, n, r = 0 # initializing the variables that will be used in encrypting. p and q will be the two prime/pseudoprime numbers

    generatePrimeNumber(primeOne)
    generatePrimeNumber(primeTwo)

    n = primeOne * primeTwo # here we are getting ready to check for the gcd of n and r. we will use the extended Euclid's algorithm for this to maintain efficiency 
    r = (primeOne - 1) * (primeTwo - 1) #r is going to be used for the gcd(e,r) = 1 where e is the public key and we have already initialized r. if condition is true, we have a public key.
                          #if it is false, we need to try another another public key e for gcd(e,r) so that we can verify if it returns 1.
    publicKeyE = random.randint(1, r)

    while gcd(e,r) != 1: #this loop will only enter if it does not equal 1. when it doesn't, then it will generate a new public key e until it does equal 1
        e = random.randint(1, r)

    d = extendedEuclid(e, r)
    d = d[1] % r

    encrypt(n, publicKeyE)


def encrypt(x, publicKeyE):

    #change plaintext into hex string based on ascii value of each character
    hex = binascii.hexlify(plaintext.encode('utf-8'))
    #get the integer value of the hex string, then encrypt it
    try:
        ciphertext = pow(int(hex, 16), key, x)
        return(ciphertext)
    except:
        print("WARNING: You cannot encrypt an empty string!")


def extendedEuclid(e,r):
    if (r == 0):
        return (1, 0, e)
    (d, x, y) = extendedEuclid(r, e % r)
    return y, (x - e // r*y), d

def decrypt():


def generatePrimeNumber(x):
    x = random.randint(10000, 100000) #chooses a prime number between 10000 and 100000
    checkX = random.randint(2, x) #checkX is going to be used to test for the primality of the number using Fermat's test

    checkIfPrime(x, checkX) #pass x and checkX in as the two variables for checkIfPrime()
    


def checkIfPrime(x, checkX):
    counter = 0 #this counter is going to be used to loop for 30 tests of the prime/pseudoprime numbers of p and q and check if they are prime
    while counter != 30:
        if (pow(checkX, x-1, x) != 1): #fermat's test algorithm. O(n) time complexity. if it does not equal one, 
                                       #it will regenerate a new prime number and set counter back to zero to retest for 30 times
            generatePrimeNumber(x)
            counter = 0
        counter += 1

    print("Successful Generation....") #console message to display that there was a successful generation of a prime number

def generateSignature():


def checkDS():



#main driver function
while (rerun):
    main()
    userChoice = input("""Would you like to rerun (Y/N): """)
    if (userChoice == "Y" or userChoice == "y"):
        rerun = 1
    else:
        rerun = 0