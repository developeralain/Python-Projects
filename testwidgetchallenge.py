import tkinter
from tkinter import *
from tkinter import filedialog as fd


class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

        self.master = master

        self.master.geometry('{}x{}'.format(500,180))

        self.master.title('Check files')

        self.pathName = StringVar()


            

        #buttons 
        self.browse1 = Button(self.master,text="Browse...",command=self.callback)
        self.browse2 = Button(self.master,text="Browse...")
        self.checkforfiles = Button(self.master,text="Check for files...",height=2)
        self.closeprogram = Button(self.master,text="Close Program",height=2)

        #button placement
        self.browse1.grid(row=0,column=0,padx=(10,20),pady=(45,10),sticky=E+W)
        self.browse2.grid(row=1,column=0,padx=(10,20),pady=(0,10),sticky=E+W)
        self.checkforfiles.grid(row=3,column=0,padx=(10,20))
        self.closeprogram.grid(row=3,column=3,padx=(250,0))

        #entry fields
        self.entry1 = Entry(self.master,text='')
        self.entry2= Entry(self.master)
        #entry1 = Entry(win,

        #entry placement
        self.entry1.grid(row=0,column=1,pady=(45,10),columnspan=3,sticky=E+W)
        self.entry2.grid(row=1,column=1,pady=(0,10),columnspan=3,sticky=E+W)        

        
            


#this method uses a filedialog module method that opens a windows system window and shows you whichever directory you specify (here it is C:)        
#self.entry1.insert(0,path) inserts a new value that corresponds to the path to the directory selected by the user 
#the path to the directory is simultaneously stored in the path variable
    def callback(self):
        path = fd.askdirectory(title="Choose Directory",initialdir=
                                            "C:/",mustexist=True)

#path variable is printed, to verify it works (for dev purposes)
        print(path)
        
        
#self.entry1.delete(0,END) deletes the current text value for widget entry1 (set to '')       
        self.entry1.delete(0,END)

#self.entry1.insert(0,path) inserts the path variable (a string) into the entry1 widget for a user to see.
        self.entry1.insert(0,path)


if __name__ == '__main__':
    #this instantiates the Tk object and stores it in root variable
                             
    root = Tk() 
    #this instantiates the ParentWindow object as deriving from the
    #Tk parent class ... so Tk --> Frame --> ParentWindow is chain it seems
    App = ParentWindow(root) #pass Tk() as root into our object
    root.mainloop()#allows persistence in the window; prevents it from closing






