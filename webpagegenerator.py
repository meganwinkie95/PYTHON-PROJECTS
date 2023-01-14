import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10) , pady=(10,10))

        #Creates button to select destination of files from destination directory
        self.btn = Button(text="Submit Custom Text",  width=30, height=2, command=self.customtext)
        #Positions destination button in GUI using tkinter grid()
        #on the next row under the source button
        self.btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #Creates entry for web selection
        self.btn = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.btn.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

        
    def customtext(self):
        customText = self.btn.get()
        customFile = open("index.html", "w")
        customContent = "<html>\n<body>\n<h1>" + customText + "</h1>\n</body>\n</html>"
        customFile.write(customContent)
        customFile.close()
        webbrowser.open_new_tab("index.html")
        
        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
