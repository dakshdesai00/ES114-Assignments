from pyscript import document

def checkEvenOdd(event):
    input_text = document.querySelector("#num")
    num = int(input_text.value)
    output_div = document.querySelector("#evenOdd")
    if num % 2 == 0:
        output_div.innerText = "Even"
    else:
        output_div.innerText = "Odd"