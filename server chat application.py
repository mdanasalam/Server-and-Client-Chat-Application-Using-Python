from tkinter import*

# GUI function
def GUI():
    # Initialize tkinter object
    gui =Tk()
    # set title for the window
    gui.title("Server Chat")
    # set size for the window
    gui.geometry("380x430")
    
    # Text space to display message
    chatlog=Text(gui,bg='white')
    chatlog.config(state=DISABLED)
    
    # button to send messages
    sendbutton =Button(gui, bg='orange',fg='red',text='SEND')
    
    # textbox to type messages
    textbox = Text(gui,bg='white')
    
    # to place the component in the window
    chatlog.place(x=6, y=6,height=386,width=370)
    textbox.place(x=6,y=401,height=20,width=265)
    sendbutton.place(x=300,y=401,height=20,width=50)
    
    # to keep the window in loop 
    gui.mainloop()

if __name__=='__main__':
    GUI()