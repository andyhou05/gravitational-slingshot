# CREATING DATABASE
key = "Leaderboard.db"

connexion = sqlite3.connect(key)
cursor = connexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS leaderboard(id INTEGER PRIMARY KEY, nom TEXT, time FLOAT)")
connexion.commit()
connexion.close()



# main menu for connection
clear_list = []
fen = Tk()
fen.geometry("400x300")
fen.title("Space Putt")
police = ("Comic sans MS",20,"bold")
title = Label(fen,text="Welcome to Space Putt!",font=police)
title.place(relx=.5,rely=.2,anchor=CENTER)



def signup():
    for items in clear_list:
        items.destroy()

    #Find ids already taken
    connexion = sqlite3.connect(key)
    cursor = connexion.cursor()
    result = cursor.execute("SELECT id FROM leaderboard")
    ids = [row[0] for row in result]
    connexion.commit()
    connexion.close()

    #give random id that doesnt exist
    id_generated = random.randint(1,1000)
    while id_generated in ids:
        id_generated = random.randint(1, 1000)

    info_id = Label(fen,text=f"your ID is {id_generated}\n Please enter your name!",font=police)
    info_id.place(relx=.5,rely=.3,anchor=CENTER)

    name = Entry(fen,font=police)
    name.place(relx=.5,rely=.6,anchor=CENTER)

    confirm = Button(fen,text="Confirm",font=police,command= lambda: database_info(id_generated,name.get()))
    confirm.place(relx=.5,rely=.8,anchor=CENTER)



def database_info(id,name):
    data = (id,name,0)
    print(data)
    connexion = sqlite3.connect(key)
    cursor = connexion.cursor()
    cursor.execute("INSERT INTO leaderboard(id,nom,time) VALUES (?,?,?)",data)

    connexion.commit()
    connexion.close()
    fen.destroy()

def confirmation(id,nom):
    #ids
    print(id,nom)
    connexion = sqlite3.connect(key)
    cursor = connexion.cursor()
    result = cursor.execute("SELECT id FROM leaderboard")
    ids = [row[0] for row in result]
    connexion.commit()
    connexion.close()
    #name
    connexion = sqlite3.connect(key)
    cursor = connexion.cursor()
    result = cursor.execute("SELECT nom FROM leaderboard")
    names = [row[0] for row in result]
    connexion.commit()
    connexion.close()
    try:
        if int(id) in ids:
            pos = ids.index(int(id))
            if nom == names[pos]:
                fen.destroy()
        else:
            top = Toplevel(fen,width=200,height=200)
            texte = Label(top,text="Invalid identification")
            texte.pack()
    except ValueError:
        top = Toplevel(fen, width=200, height=200)
        texte = Label(top, text="Invalid identification")
        texte.pack()



def signin():
    for items in clear_list:
        items.destroy()
    info_id = Label(fen, text=f"Enter your ID and name", font=police)
    info_id.place(relx=.5, rely=.2, anchor=CENTER)
    police2 = ("Comic sans MS",15,"bold")

    ID = Entry(fen,font=police2)
    ID.place(relx=.6,rely=.4,anchor=CENTER)
    name = Entry(fen,font=police2)
    name.place(relx=.6,rely=.6,anchor=CENTER)

    ID_label = Label(fen,text="ID:",font=police2)
    ID_label.place(relx=.2,rely=.4,anchor=CENTER)
    nom_label = Label(fen,text="Name:",font=police2)
    nom_label.place(relx=.2,rely=.6,anchor=CENTER)

    confirm = Button(fen,text="Confirm",font=police,command=lambda:confirmation(ID.get(),name.get()))
    confirm.place(relx=.5,rely=.8,anchor=CENTER)






sign_in = Button(fen,text="Sign in",font=police,bg="gray",width=12,command=signin)
sign_in.place(relx=.5,rely=.5,anchor=CENTER)

create_account = Button(fen,text="Create account",font=police,bg="gray",command=signup)
create_account.place(relx=.5,rely=.8,anchor=CENTER)


clear_list.append(title)
clear_list.append(sign_in)
clear_list.append(create_account)


fen.mainloop()