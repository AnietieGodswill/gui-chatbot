from tkinter import *
import random
import requests
import wikipedia
import datetime
from datetime import date
from bs4 import BeautifulSoup
def ShowText(*args):
    #for calc of adding
    calc_add_entry = entry_box.get()
    calc_add_split = calc_add_entry.split(">")[-1]

    #for wiki
    new_wiki_entry = entry_box.get()
    wiki_split= new_wiki_entry.split(">")[-1]
    

    #for calc of sub
    calc_sub_entry = entry_box.get()
    calc_sub_split = calc_sub_entry.split(">")[-1]
    calc_split_sub_first = calc_sub_split.split("-")[0]
    calc_split_sub_second = calc_sub_split.split("-")[-1]

    #for weather
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    new_wea_entry = entry_box.get()
    wea_split = new_wea_entry.split(">")[-1]
    
    #start from here
    InsEntry = entry_box.get()
    text_area.configure(state=NORMAL)
    valIns = "You: " +InsEntry+"\n"
    text_area.insert(END,valIns)
    text_area.configure(state=DISABLED)
    entry_box.delete(0,END)
    
    if InsEntry =="hello":
        Response = ["hello","hii","howdy"]
        RandRes = "Bot: " + random.choice(Response)+"\n"
        #to open the state of textarea to write
        text_area.configure(state=NORMAL)
        text_area.insert(END,RandRes)
        #to close the state of textarea 
        text_area.configure(state=DISABLED)
    elif InsEntry =="date" or InsEntry == "today date":
        label_datebot = "bot: "
        tod_date = date.today()
        #to jump on new line
        new_datebot = "\n"
        text_area.configure(state=NORMAL)
        #always when u try to insert variable just use END always
        text_area.insert(END,label_datebot)
        text_area.insert(END,tod_date)
        text_area.insert(END,new_datebot)
        text_area.configure(state=DISABLED)
    elif InsEntry =="time" or InsEntry == "current time":
        label_timebot = "bot: "
        currtime = datetime.datetime.now().time()
        new_timebot = "\n"
        text_area.configure(state=NORMAL)
        text_area.insert(END,label_timebot)
        text_area.insert(END,currtime)
        text_area.insert(END,new_timebot)
        text_area.configure(state=DISABLED)
        
    elif InsEntry =="how are you":
        Response = ["fine","good","f9"]
        RandRes = "Bot: " + random.choice(Response)+"\n"
        text_area.configure(state=NORMAL)
        text_area.insert(END,RandRes)
        text_area.configure(state=DISABLED)

    
        
    elif InsEntry =="good morning":
        Response = ["morning","gm","goodie morn"]
        RandRes = "Bot: " + random.choice(Response)+"\n"
        text_area.configure(state=NORMAL)
        text_area.insert(END,RandRes)
        text_area.configure(state=DISABLED)
       
        
            
    elif InsEntry =="who created you" or InsEntry == "who developed you":
        Response = ["dx4iot"," Nishant Tiwari","Nishant Tiwari(dx4iot)"]
        RandRes = "Bot: " + random.choice(Response)+"\n"
        text_area.configure(state=NORMAL)
        text_area.insert(END,RandRes)
        text_area.configure(state=DISABLED)
        
    elif InsEntry == "wiki>"+wiki_split:
        WikiLabel = "Bot: "
        WikiSearch = wikipedia.summary(wiki_split)
        WikiEnter ="\n"
        text_area.configure(state=NORMAL)
        text_area.insert(END,WikiLabel)
        text_area.insert(END,WikiSearch)
        text_area.insert(END,WikiEnter)
        text_area.configure(state=DISABLED)
        
    elif InsEntry == "calc.add>"+calc_add_split:
        #print(calc_add_split)
        calc_split_add = []
        calc_split_add = calc_add_split.split("+")
        for i in range(0,len(calc_split_add)):
            calc_split_add[i] = int(calc_split_add[i])
        Sum = sum(calc_split_add)
        CalcLabel = "Bot: "
        CalcEnter ="\n"
        text_area.configure(state=NORMAL)
        text_area.insert(END,CalcLabel)
        text_area.insert(END,Sum)
        text_area.insert(END,CalcEnter)
        text_area.configure(state=DISABLED)
        
    elif InsEntry == "calc.sub>"+calc_split_sub_first+"-"+calc_split_sub_second:
        sub1 = int(calc_split_sub_first)
        sub2 = int(calc_split_sub_second)
        subbed = sub1 - sub2
        CalcLabel = "Bot: "
        CalcEnter ="\n"
        text_area.configure(state=NORMAL)
        text_area.insert(END,CalcLabel)
        text_area.insert(END,subbed)
        text_area.insert(END,CalcEnter)
        text_area.configure(state=DISABLED)

    else:
        else_res = "Bot: No result found" +"\n"
        text_area.configure(state=NORMAL)
        text_area.insert(END,else_res)
        text_area.configure(state=DISABLED)




root = Tk()
root.title('destor')
root.geometry('700x720')
root.resizable(0,0)

scroll = Scrollbar(root)
scroll.pack(side = RIGHT,fill = Y)
#To create text_area
text_area = Text(root,yscrollcommand = scroll.set,state=DISABLED,height=20,width=60,font='helvetica 15',bg='LightSkyBlue1',fg='gray17')
scroll.config(command=text_area.yview)
text_area.pack(expand=True, fill=BOTH)
#To create entry_box
entry_box = Entry(root,width=45,font='helvetica 14')
#To send 'enter key' to entry_box
entry_box.bind('<Return>',ShowText)
entry_box.pack()
#To create send_button
send_button = Button(root,text="Press ENTER",relief=RAISED,font='helvetica 14',command=ShowText,bg='Cornsilk2')
send_button.pack(expand=True,fill=BOTH)
root.mainloop()

