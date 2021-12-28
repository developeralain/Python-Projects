import sqlite3

#conn holds the connection to the database ... it is a token ... if this db
#doesn't already exist, it makes one.
conn = sqlite3.connect('filetype.db')

#with loop tells it 'while we have this connection--while this token open--
#then do the following lines of code until we close our session

with conn: #the cursor will be the thing that will be operating on the database
    #when we want it to do something ... so when we want to do something on the
    #database, we invoke the cursor
    cur = conn.cursor() #we put cursor in a variable to make it shorter
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT)")
    conn.commit() #commits changes to the database


#below is a tuple of file names stored in the variable fileList
fileList = ('information.docx','Hello.txt','myImage.png',' \
            myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#reestablishes connection with our database
conn = sqlite3.connect('filetype.db')

#below is a for loop designed to iterate through each element (each file name)
#in the fileList tuple and identify files ending in .txt. 
for file in fileList:
    if file.endswith('.txt'):
        with conn: 
            cur = conn.cursor()
            #below you are asking for wild card values (?) to be inserted into
            #tbl_files column. The values to be entered will be each element
            #iterated through within the fileList tuple that ends in .txt ...
            #by writing (file,) you are saying you want each element to be
            #extracted as a one-element tuple and entered into the column
            cur.execute('INSERT INTO tbl_files (col_fileName) VALUES (?)', \
                        (file,))
            #this prints every qualifying one-element tuple i.e. all files
            #ending in .txt within the fileList tuple. 
            print(file)
            
conn.close()



with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_persons WHERE col_fname = 'Bella'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(item[0],item[1],item[2])
    print(msg)
