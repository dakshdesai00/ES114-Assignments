
from pyscript import document

def printEachChar(event):
    input_text = document.querySelector("#string")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = ""
    for c in english:
        output_div.innerText += c + "\n"