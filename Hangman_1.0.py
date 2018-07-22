"""
Hangman version 1.0
@Rd Dolor
"""

from tkinter import *
from PIL import Image, ImageTk
import os, random, time

GuiWidth=640
Guiheight=480
dir = os.getcwd()
picNumber=0
LARGE_FONT = ('Verdana',15)
newtext = ''
Words = ['red','blue','green']
randomWord = random.choice(Words)
newtext = len(randomWord) * '*'
letter = ''


class Window(Frame):


    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):
        global picNumber,letter

        self.master.title('HANGMAN v1')

        self.backgroundImg()

        self.pack(fill=BOTH,expand=1,anchor='center')

        #The buttons
        startButton = Button(self, text = "Start",padx = 15,command=lambda:[self.showImg(),quitButton.place_forget(),
                                                                  self.HangmanWord(),backButton.place(x=150,y=350),
                                                                  addCounter.place(x=80,y=350),startButton.place_forget()])

        quitButton = Button(self, text = "Quit", command=self.client_exit, padx=15)


        backButton = Button(self, text = 'Back',padx = 25, command=lambda:[startButton.place(x=300/2-30,y=400/2-50),
                                                                           quitButton.place(x=300/2-30,y=400/2),
                                                                           backButton.place_forget(),
                                                                           self.backCommands(),
                                                                           addCounter.place_forget()])

        addCounter = Button(self,text='add',padx=25,command=lambda:[self.addCounters(),self.showImg()])
        self.winText = Label(self,text='You Win!',font = LARGE_FONT,padx = 20,pady=15)

        startButton.place(x=300/2-30,y=400/2-50)

        quitButton.place(x=300/2-30,y=400/2)

    def addCounters(self):
        global picNumber, randomWord, newtext, entry, letter
        letter = self.entryText.get()
        if picNumber != 5:
            if letter not in randomWord:
                picNumber += 1
        if picNumber == 5:
            print('You lost')
        emptyString = ''
        print(letter)

        if letter in randomWord:
            for i in range(len(randomWord)):
                if letter == randomWord[i]:
                    emptyString += letter
                else:
                    emptyString += newtext[i]
            newtext = emptyString

        HangmanLabel = Label(self, text=newtext,font=LARGE_FONT, padx = 20)
        HangmanLabel.place(x=300/2-30,y=290)
        HangmanLabel.config(text=newtext)

        def Win():
            if newtext == randomWord:

                self.winText.place(x=300/2-30,y=400/2-50)
        Win()

    def backCommands(self):
        global picNumber, randomWord, newtext
        print(picNumber)
        picNumber = 0
        print(picNumber)
        HangmanLabel = Label(self, text=randomWord,font=LARGE_FONT, padx = 20)
        HangmanLabel.place(x=300/2-29,y=290)
        if newtext == randomWord:
            self.winText.place_forget()


    def showImg(self):

        global picNumber
        load = Image.open(dir+'\\Hangman_'+str(picNumber)+'.png')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=25,y=30)

    def HangmanWord(self):
        global newtext, randomWord, newtext
        print(newtext)
        self.entryText = Entry(self)
        self.entryText.place(x=300/2-50, y=400/2+130)
        randomWord = random.choice(Words)
        newtext = len(randomWord) * '*'
        HangmanLabel = Label(self, text=newtext,font=LARGE_FONT, padx = 25)
        HangmanLabel.place(x=300/2-30,y=290)

    def backgroundImg(self):

        load = Image.open(dir+'\\Hangman_bg.png')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0,y=0)


    def client_exit(self):
        quit()

if __name__ == "__main__":
    root = Tk()
    imgicon = PhotoImage(file='icon.gif')
    root.geometry('300x400')
    root.call('wm','iconphoto', root._w, imgicon)
    app = Window(root)
    root.mainloop()
