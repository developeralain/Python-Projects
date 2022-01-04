#WEB PAGE GENERATOR PART ONE ASSIGNMENT 
"""


Now that you have created a tool that can automatically create a basic HTML web
page, the content on the page is hard-coded as "Stay tuned for our amazing
summer sale!"


Users have now asked you to create an option for them to set the body of the
text themselves.


Your task is to create a GUI with Tkinter that will enable the users to set
the body text for a newly-created web page. There should also be a control
in the GUI that initiates the process of making the new web page.


Set a new body text of your choice.


The GUI should open the html file in a new tab within your browser that
displays the newly added text from the user.

"""



#imports module and all its "widgets" from tkinter
import tkinter
from tkinter import *
import webbrowser 
#frame is the parent class within tkinter module. You're creating a child
#from tkinter\'s parent Frame class. That's how you interact with Tkinter


#the below 3 lines of code are generic block needed to start using tkinter

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

#we pass value of master to variable named self.master ... we always use
#self when referencing things within the class
        self.master = master

        #this line of code makes the user window fixed in size
        self.master.resizable(width=False, height=False)

        #this gives the window a specific size in pixels
        self.master.geometry('{}x{}'.format(500,250))
        
        #adds title to window
        self.master.title('Webpage Generator')

        self.master.config(bg='lightgray')

        self.varWebpageName = StringVar()#you can affect what is in a text box
        #by storing that info here
        self.varWebpageContent = StringVar()
        


        
        #We pass arguments to and instantiate the Label object ... 
        self.lblWebpageName = Label(self.master,text='Webpage File Name: ',font=('Helvetica',16),fg='black',\
                               bg='lightgray')
        #below we specify the placement of the label object via grid geometry
        self.lblWebpageName.grid(row=0,column=0,padx=(10,0),pady=(10,0))

                 
        self.lblWebpageContent = Label(self.master,text='Webpage Content: ',font=('Helvetica',16),fg='black',\
                               bg='lightgray')
        self.lblWebpageContent.grid(row=1,column=0,padx=(10,0),pady=(10,0))


       
        #this passes arguments to and instantiates the Entry object, which is a text box
        #the self.master tells it WHERE to place the text box
        #self.txt.WebpageName is a variable we created and is where this object will be stored
        self.txtWebpageName = Entry(self.master,text=self.varWebpageName,font=('Helvetica',16),fg='black',\
                               bg='lightblue')
        #this line calls a geometry manager (various kinds available) ...here we use the grid()
        #a geometry manager is what 'paints' the box, form, window, etc.
        self.txtWebpageName.grid(row=0,column=1,padx=(10,0),pady=(10,0))

        self.txtWebpageContent = Entry(self.master,text=self.varWebpageContent,font=('Helvetica',16),fg='black',\
                               bg='lightblue')
        self.txtWebpageContent.grid(row=1,column=1,padx=(10,0),pady=(10,0))


        #below we create some buttons for our GUI
        self.btnSubmit = Button(self.master,text='Generate Webpage',width=20,height=2, command=self.submit)
        self.btnSubmit.grid(row=2,column=1,padx=(15,0),pady=(10,0),sticky=NW)

        self.btnCancel = Button(self.master,text='Cancel',width=10,height=2, command=self.cancel)
        self.btnCancel.grid(row=2,column=0,padx=(0,90),pady=(10,0),sticky=NE)

    #we create a submit method that activates when user clicks submit button
    #upon clicking submit, the method runs and collects the values in the
    #first and last name fields. It then prints these in a string in a label box.
    def submit(self):
        page_name = self.varWebpageName.get()
        content = self.varWebpageContent.get()
        pageopen = page_name + ".html"
 
        #creates an html file if one does not already exist
        createHTML = open(pageopen,"w")

        #opens the html file and appends to it
        openwebpage = open(pageopen,"a")

        openwebpage.write("<html>")
        
        openwebpage.write("\n\t<body>")
       
        openwebpage.write("\n\t\t<h1>" + content + "</h1>")
        
        openwebpage.write("\n\t<body>")
        
        openwebpage.write("<html>")

        openwebpage.close()

        url = pageopen
        #opens webpage in new tab using default browser
        webbrowser.open_new_tab(url)
        

    #we create a cancel method that closes the master window when the cancel
    #button is clicked by the user
    def cancel(self):
        self.master.destroy()








if __name__ == '__main__':
    #this instantiates the Tk object and stores it in root variable
                             
    root = Tk() 
    #this instantiates the ParentWindow object as deriving from the
    #Tk parent class ... so Tk --> Frame --> ParentWindow is chain it seems
    App = ParentWindow(root) #pass Tk() as root into our object
    root.mainloop()#allows persistence in the window; prevents it from closing
    

