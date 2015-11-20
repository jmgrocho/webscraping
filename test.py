import re,time,tkinter
from tkinter import messagebox
a=time.clock()
print (a)
def scrape(city):
    filename = str(city) + "Farms.txt"
    print(filename)
     
     
scrape("Harare")

list1 = ["Detroit", "Lansing", "DETROIT", "dEtRoIt", "LANSInG", "detroit"]
for word in list1:
    if re.search("DETROIT", word, re.IGNORECASE):
        print("Found {}".format(word))
        
b=time.clock()
print("B = {}".format(b))
print(b-a)

print("Last updated:  {}".format(time.ctime()))

top = tkinter.Tk()
def helloCallBack():
    messagebox.showinfo("Hello Python","Hello World")

# B = tkinter.Button(top,text="Hello",command = helloCallBack())
# 
# B.pack()
# top.mainloop()
