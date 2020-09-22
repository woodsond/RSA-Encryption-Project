#Project 3: Diante Woodson, Christopher Stinson, Daniel Ashcraft
import random
import binascii

def main():
    n, userPublicKey, userPrivateKey = keyGeneration()
    menu(n, userPublicKey, userPrivateKey)

def menu(n, publicKey, privateKey):
    print("Your private key: ", privateKey)
    print("Your public key: ", publicKey)
    print("Hello user, this is an RSA encryption program. Make sure to keep your private key safe and secure!")
    print("Here are your options:")
    print()
    print("1. Encrypt a personal message")
    print("2. Decrypt a personal message")
    print("3. Verify your personal signature")
    print("4. Sign your personal message")
    print("5. Exit the program")
    userChoice = input("What would you like to do (Please enter 1-5): ")

    if userChoice == "1":
        userInput = input("Please enter you message: ")
        encryptedUserInput = encrypt(n, publicKey, userInput)
        if encryptedUserInput is not None:
            print("Encrypted message: ", encryptedUserInput)
    elif userChoice == "2":
        userInput = input("Please enter the encrypted message you would like to decrypted: ")
        try:
            decryptedUserInput = decrypted(privateKey, n, userInput)
        except:
            print("Warning: Cannot decrypt an empty message")
            continue 

        if decryptedUserInput is not None:
            print("Decrypted message: ", decryptedUserInput)
    elif userChoice = "3":

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

    privateKey = extendedEuclid(e, r)
    privateKey = privateKey[1] % r

    return (n, publicKeyE, privateKey)


def encrypt(x, publicKeyE, userText):

    #change plaintext into hex string based on ascii value of each character
    hex = binascii.hexlify(userText.encode('utf-8'))
    #get the integer value of the hex string, then encrypt it
    try:
        encryptedText = pow(int(hex, 16), key, x)
        return(ciphertext)
    except:
        print("Warning: Your input is empty!")


def extendedEuclid(e,r):
    if (r == 0):
        return (1, 0, e)
    (d, x, y) = extendedEuclid(r, e % r)
    return y, (x - e // r*y), d

def decrypt(privateKey, n, userText):
    #get the plaintext integer back by using the opposite key used for encryption
	plain_int = pow(ciphertext, key, n)
	#change integer into hex value, then strip the first to characters off ie. "0x"
	p = hex(plain_int)[2:]
	#change the hex values into ascii integer, then change that integer to character

	try:
		plaintext = binascii.unhexlify(p).decode('utf-8')
		return(plaintext)
	except:
		print("warning: Your encrypted message is either too long or not a valid encrypted message!")

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