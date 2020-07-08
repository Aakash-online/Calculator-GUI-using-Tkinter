from tkinter import *
root = Tk()
root.resizable(False, False)
root.title("CALCULATOR")

#Frame for Text screen
textF = Frame(root)
textF.pack(fill="both")

#input-output variable which will be showed o screen as input (question) and output (Answer)
io = Variable()

#Screen Frame which contains Input and outputs
screen = Entry(textF, font = "Helvetica 30 bold", textvariable=io,width=11, justify=RIGHT).pack(padx=10, pady=5)


#Click function which manages the input given by user
def click(event):
    #calling input-output variable from outside
    global io

    #using "cget" method to get preassigned text on perticuler button ( which is clicked)
    var = event.widget.cget("text")

    # "=" returns the answer of  input given hence have to be processed separately
    if var == "=" :
        #checking if input is in form of digit when "=" is clicked
        if io.get ( ).isdigit ( ) :
            #coverting digits into float
            value = float (io.get ( ))
            #setting the output
            io.set (value)
        else :
            #  Indeterminate forms can cause Error so have to display error
            try :
                # "eval()" function evalutes the string input and gives answer
                value = eval (io.get ( ))
                #Displaying the result
                io.set(value)

            except Exception as e :
                print (e)
                value = "Error"
                #Displaying The Error
                io.set(value)

    #When AC is pressed we will clear the screen
    elif var == "AC":
        #settting the io to empty
        io.set("")


     #Adds numbers
    else :
        io.set(io.get() + var)


#Frame for Buttons
butF = Frame(root)
butF.pack(fill="both")

#Row Configuration
butF.rowconfigure (4, {'minsize' : 30})
#Column Configuration
butF.columnconfigure (3, {'minsize' : 30})


                      #BUttons Which will be displayed in second frame below the screen

onebutton = Button (butF, text="1", fg="yellow",height = 1, width = 5, font = "Helvetica 10 bold")
onebutton.grid (row=1, column=0,pady=10,padx=10)
onebutton.bind("<Button>" , click )
fourebutton = Button (butF, text="4", fg="yellow",height = 1, width = 5, font = "Helvetica 10 bold")
fourebutton.grid (row=2, column=0,pady=10,padx=10)
fourebutton.bind("<Button>" , click )
sevenbutton = Button (butF, text="7", fg="yellow",height = 1, width = 5, font = "Helvetica 10 bold")
sevenbutton.grid (row=3, column=0,pady=10,padx=10)
sevenbutton.bind("<Button>" , click )
dotbutton = Button (butF, text=".", fg="yellow",height = 1, width = 5, font = "Helvetica 10 bold")
dotbutton.grid (row=4, column=0,pady=10,padx=10)
dotbutton.bind("<Button>" , click )
twobutton = Button (butF, text="2", fg="yellow",height = 1, width = 5, font = "Helvetica 10 bold")
twobutton.grid (row=1, column=1,pady=10,padx=10)
twobutton.bind("<Button>" , click )
fivebutton = Button (butF, text="5", fg="yellow",height = 1, width = 5, font = "Helvetica 10 bold")
fivebutton.grid (row=2, column=1,pady=10,padx=10)
fivebutton.bind("<Button>" , click )
eightbutton = Button (butF, text="8", fg="yellow",height = 1, width = 5, font = "Helvetica 10 bold")
eightbutton.grid (row=3, column=1,pady=10,padx=10)
eightbutton.bind("<Button>" , click )
zerobutton = Button (butF, text="0", fg="yellow",height = 1, width = 5, font = "Helvetica 10 bold")
zerobutton.grid (row=4, column=1,pady=10,padx=10)
zerobutton.bind("<Button>" , click )
threebutton = Button (butF, text="3", fg="yellow",height = 1, width = 5, font = "Helvetica 10 bold")
threebutton.grid (row=1, column=2,pady=10,padx=10)
threebutton.bind("<Button>" , click )
sixbutton = Button (butF, text="6", fg="yellow",height = 1, width = 5, font = "Helvetica 10 bold")
sixbutton.grid (row=2, column=2,pady=10,padx=10)
sixbutton.bind("<Button>" , click )
ninebutton = Button (butF, text="9", fg="yellow",height = 1, width = 5, font = "Helvetica 10 bold")
ninebutton.grid (row=3, column=2,pady=10,padx=10)
ninebutton.bind("<Button>" , click )
divbutton = Button (butF, text="/", fg="yellow",height = 1, width = 5, font = "Helvetica 10 bold")
divbutton.grid (row=4, column=2,pady=10,padx=10)
divbutton.bind("<Button>" , click )
acbutton = Button (butF, text="AC", fg="yellow",height = 1, width = 5, font = "Helvetica 10 bold")
acbutton.grid (row=0, column=3,pady=10,padx=10)
acbutton.bind("<Button>" , click )
plusbutton = Button (butF, text="+", fg="yellow",height = 1, width = 5, font = "Helvetica 10 bold")
plusbutton.grid (row=1, column=3,pady=10,padx=10)
plusbutton.bind("<Button>" , click )
minbutton = Button (butF, text="-", fg="yellow",height = 1, width = 5, font = "Helvetica 10 bold")
minbutton.grid (row=2, column=3,pady=10,padx=10)
minbutton.bind("<Button>" , click )
mulbutton = Button (butF, text="x", fg="yellow",height = 1, width = 5, font = "Helvetica 10 bold")
mulbutton.grid (row=3, column=3,pady=10,padx=10)
mulbutton.bind("<Button>" , click )
equbutton = Button (butF, text="=", fg="yellow",height = 1, width = 5, font = "Helvetica 10 bold")
equbutton.grid (row=4, column=3,pady=10,padx=10)
equbutton.bind("<Button>" , click )


root.mainloop()

