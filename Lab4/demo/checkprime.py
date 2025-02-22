from pyscript import document

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def checkPrime(event):
    n = document.querySelector("#num-prime").value
    output_div = document.querySelector("#prime")
    if isPrime(int(n)):
        output_div.innerText = "Prime"
    else:
        output_div.innerText = "Not Prime"
    