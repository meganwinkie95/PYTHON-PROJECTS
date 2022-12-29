import sqlite3
conn = sqlite = sqlite3.connect('test2.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_myfiles(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_filedata TEXT)")
    conn.commit()

conn = sqlite3.connect('test2.db')

#tuple of data names
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
# loop through each object in the tuple to find the datatype that end in .txt

for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        #The value for each row will be one datatype of the tuple(x,)
        #will denote a one element tuple for each datatype ending in .txt
            cur.execute("Insert INTO tbl_myfiles (col_filedata) VALUES (?)",(x,))
            print(x)

conn.close

        
