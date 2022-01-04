#FILE TRANSFER PART TWO ASSIGNMENT

"""
FILE TRANSFER PART THREE SUBMISSION ASSIGNMENT

Users are now asking for a user interface to make using the script easier and more versatile.


Desired features of the UI:


1)Allow the user to browse and choose a specific folder that will contain the files to be checked daily.

2)Allow the user to browse and choose a specific folder that will receive the copied files.

3)Allow the user to manually initiate the 'file check' process that is performed by the script.

!Add comments throughout your Python explaining your code.

You have been asked to create this UI.


"""
import shutil
import os
import time
import os.path
import tkinter
from tkinter import *
from tkinter import filedialog as fd



class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

        self.master = master
        #specify app window parameters
        self.master.geometry('{}x{}'.format(620,200))
        #specify app window title
        self.master.title('Check files')

        #this stores the source and destination directories the user selects within the StringVar() objects as a variables.
        #we will call on these variables in various functions, and so it is useful to have this declared here.
        self.pathSource = StringVar()

        self.pathDestination = StringVar()

        #labels
        self.label1 = Label(self.master,text="Select Source Folder")
        self.label2 = Label(self.master,text="Select Destination Folder")

        #label placement
        self.label1.grid(row=0,column=0,padx=(10,20),pady=(10,0))
        self.label2.grid(row=1,column=0,padx=(10,20),pady=(10,0))
            

        #buttons 
        self.browse1 = Button(self.master,text="Browse...",command=self.selectSource)
        self.browse2 = Button(self.master,text="Browse...",command=self.selectDestination)
        self.transferfiles = Button(self.master,text="Transfer Files...",height=2,command=self.getfiles)
        self.closeprogram = Button(self.master,text="Close Program",height=2,command=self.cancel)

        #button placement
        self.browse1.grid(row=0,column=2,padx=(10,20),pady=(10,0),sticky=E+W)
        self.browse2.grid(row=1,column=2,padx=(10,20),pady=(10,0),sticky=E+W)
        self.transferfiles.grid(row=3,column=0,padx=(10,20),pady=(10,0))
        self.closeprogram.grid(row=3,column=3,padx=(250,0),pady=(10,0))

        #entry fields
        self.entry1 = Entry(self.master,text=self.pathSource)
        self.entry2= Entry(self.master,text=self.pathDestination)
        #entry1 = Entry(win,

        #entry placement
        self.entry1.grid(row=0,column=3,pady=(10,0),columnspan=3,sticky=E+W)
        self.entry2.grid(row=1,column=3,pady=(10,0),columnspan=3,sticky=E+W) 

#this detects the modified time for each file

#this method uses a filedialog module method that opens a windows system window and shows you whichever directory you specify (here it is C:)        
#self.entry1.insert(0,self.pathSource) inserts a new value that corresponds to the path to the source directory selected by the user 
#the path to the directory is simultaneously stored in the pathSource variable
    def selectSource(self):
        self.pathSource = fd.askdirectory(title="Choose Directory",initialdir=
                                            "C:/",mustexist=True)

#path variable is printed, to verify it works (for dev purposes)
        print(self.pathSource)
        
        
#self.entry1.delete(0,END) deletes the current text value for widget entry1 (set to '')       
        self.entry1.delete(0,END)

#self.entry1.insert(0,path) inserts the path variable (a string) into the entry1 widget for a user to see.
        self.entry1.insert(0,self.pathSource)

    #this operates like the selectSource function, except it selects the destination directory
    def selectDestination(self):
        self.pathDestination = fd.askdirectory(title="Choose Directory",initialdir=
                                            "C:/",mustexist=True)

#path variable is printed, to verify it works (for dev purposes)
        print(self.pathDestination)
        
        
#self.entry1.delete(0,END) deletes the current text value for widget entry1 (set to '')       
        self.entry2.delete(0,END)

#self.entry1.insert(0,path) inserts the path variable (a string) into the entry1 widget for a user to see.
        self.entry2.insert(0,self.pathDestination)

    def getfiles(self):
        #this generates the current time 'since the epoch' in seconds (no decimals) using the time module we imported
        self.t = time.time()
        self.t_s = int(self.t)

        
        #the contains the user-selected source directory as a list of contained files within the self.files variable
        self.files = os.listdir(self.pathSource)
        #these print operations are for the developer, to see in the shell that it is capturing correctly the user directories
        print(self.pathSource)
        print(self.pathDestination)
        
              
        #The below for loop will find the time difference b/w present time and modified time as epoch time (seconds) and only move
        #those < 86400 seconds apart (<24 hrs)
        #this for loop iterates through all files within a chosen source directory
        for i in self.files:
            #switches into the user's chosen source directory as the working directory (otherwise errors are thrown)
            os.chdir(self.pathSource)
            #a formula to calculate current time as an integer as epoch time (seconds since 1970) and subtract the integer value of the file date modified time from it. 
            self.timediff = self.t_s - int((os.path.getmtime('{}'.format(i))))
            #if the difference in time between current time and file modified time is < 24 hrs (or 86400 seconds), then it will run and only target those files
            if self.timediff < 86400:
                #command to move from pathSource to pathDestination as selected by user.
                shutil.move(self.pathSource+'/'+i,self.pathDestination)


    #function to close app upon clicking the cancel button
    def cancel(self):
        self.master.destroy()
    
                                 
       
if __name__ == '__main__':
    
    #this instantiates the Tk object and stores it in root variable
                             
    root = Tk() 
    #this instantiates the ParentWindow object as deriving from the
    #Tk parent class ... so Tk --> Frame --> ParentWindow is chain it seems
    App = ParentWindow(root) #pass Tk() as root into our object
    root.mainloop()#allows persistence in the window; prevents it from closing



