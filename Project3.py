#Project 3: Diante Woodson, Christopher Stinson, Daniel Ashcraft
import random
import binascii

def main():
    n, userPublicKey, userPrivateKey = keyGeneration()
    menu(n, userPublicKey, userPrivateKey)

def menu(n, publicKey, privateKey):
    print("Hello user, this is an RSA encryption program. Make sure to keep your private key safe and secure!")
    print()
    print("Your private key: ", privateKey)
    print()
    print("Your public key: ", publicKey)
    while True:
        print()
        print("Here are your options:")
        print()
        print("1. Encrypt a personal message")
        print("2. Decrypt a personal message")
        print("3. Verify your personal signature")
        print("4. Sign your personal message")
        print("5. Exit the program")
        print()
        userChoice = input("What would you like to do (Please enter 1-5): ")

        if userChoice == "1":
            userInput = input("Please enter you message: ")
            print()
            encryptedUserInput = encrypt(publicKey, n, userInput)
            if encryptedUserInput is not None:
                print("Encrypted message: ", encryptedUserInput)
                print()
        elif userChoice == "2":
            userInput = input("Please enter the encrypted message you would like to decrypt: ")
            print()
            try:
                decryptedUserInput = decrypt(privateKey, n, int(userInput))
            except:
                print("Warning: Cannot decrypt an empty message")
                print()
                continue 
            if decryptedUserInput is not None:
                print("Decrypted message: ", decryptedUserInput)
                print()
        elif userChoice == "3":
            userInput = input("Please enter the message you would like to sign: ")
            print()
            signedMessage = encrypt(privateKey, n, userInput)
            if signedMessage is not None:
                print("Signed message: ", signedMessage)
                print()
        elif userChoice == "4":
            userInput = input("Please enter the message that you would like to verify the signature of: ")
            print()
            try:
                verifiedMessage = decrypt(publicKey, n, int(userInput))
            except:
                print("Warning: Cannot verify an empty message")
                print()
                continue
            if verifiedMessage is not None:
                print("Verified Message: ", verifiedMessage)
                print()
        elif userChoice == "5":
            print()
            print("Thank you for using this program!")
            break
        else:
            print()
            print("PLEASE ENTER A NUMBER BETWEEN 1 AND 5!")
            pass

def greatestCommonDivisor(a,b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return greatestCommonDivisor(b, a % b)

def keyGeneration():
    primeOne = generatePrimeNum()
    primeTwo = generatePrimeNum() # initializing the variables that will be used in encrypting. p and q will be the two prime/pseudoprime numbers
    n = primeOne * primeTwo # here we are getting ready to check for the gcd of n and r. we will use the extended Euclid's algorithm for this to maintain efficiency 
    r = (primeOne - 1) * (primeTwo - 1) #r is going to be used for the gcd(e,r) = 1 where e is the public key and we have already initialized r. if condition is true, we have a public key.
                          #if it is false, we need to try another another public key e for gcd(e,r) so that we can verify if it returns 1.
    while True:
        publicKeyE = random.randint(1, r)
        if (greatestCommonDivisor(publicKeyE, r) == 1):
            break

    privateKey = extendedEuclid(publicKeyE, r)
    privateKey = privateKey[1]
    privateKey = privateKey % r

    return (n, publicKeyE, privateKey)


def encrypt(userKey, x, userText):

    #change userText into hex string based on ascii value of each character
    hex = binascii.hexlify(userText.encode('utf-8'))
    #get the integer value of the hex string, then encrypt it
    try:
        encryptedText = pow(int(hex, 16), userKey, x)
        return(encryptedText)
    except:
        print("Warning: Your input is empty!")


def extendedEuclid(a,b):
    #swap values if a is less than b
	if(a < b):
		a, b = b, a
	if(b == 0):
		return(1, 0, a)
	(x, y, d) = extendedEuclid(b, a%b)
	return(y, x - a//b*y, d)

def decrypt(userKey, n, userText):
    #get the userText integer back by using the opposite key used for encryption
	plain_int = pow(userText, userKey, n)
	#change integer into hex value, then strip the first to characters off ie. "0x"
	p = hex(plain_int)[2:]
	#change the hex values into ascii integer, then change that integer to character

	try:
		newText = binascii.unhexlify(p).decode('utf-8')
		return(newText)
	except:
		print("warning: Your encrypted message is either too long or not a valid encrypted message!")

def generatePrimeNum():
    while True:
        #generate prime numbers
        randomPrime = random.randint(10 ** 200, 2 * (10 ** 200))
        #go to fermat's theorem funct to check if it is prime
        if(checkIfPrime(randomPrime)):
            return randomPrime
    
def checkIfPrime(x):
   tests = 30
   for i in range(tests):

        primeNum = random.randint(2, x-1)
        if(pow(primeNum, x-1, x) != 1):
            return False

        return True
#main driver function
main()