from tkinter import *
import json


data = json.load(open("data.json"))
root = Tk()
root.iconbitmap("favicon.ico")
root.title("Dictionary")
root.geometry("1200x550")

def search_word(word):
    key_word = word.lower()
    if key_word in data:
        return data[key_word]
    else:
        return "Check spelling OR the word does not exist"


def displaydefinition():
    word = a.get()
    word_def = search_word(word)
    if type(word_def) == list:
        all_definition = '\n'.join(word_def)
    else:
        all_definition = word_def
    defintion.config(text=all_definition)

topframe = Frame(root)
topframe.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

#elements in top frame
label = Label(topframe, text="Enter a word:", font=("Ariel", 32))
label.pack()
a = StringVar()
inputField= Entry(topframe, textvariable=a, width=70,)
inputField.pack()
defintion = Label(topframe, text="Please enter a word above to know the definition", font=("Ariel", 16))
defintion.pack()

#elements in bottom frame
button = Button(bottomframe, text="Search", font=("Ariel black", 18), command=displaydefinition, width=15, height=2)
button.pack()


root.mainloop()
