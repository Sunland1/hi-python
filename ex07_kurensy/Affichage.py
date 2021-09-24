import tkinter as tk


def calcChange(change1,change2, nb_to_change2) : 
    return (change1 * nb_to_change2)/change2



class Affichage(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        #Top of page 
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Calculate"
        self.hi_there["command"] = self.getChange
        self.hi_there.pack(side="top")

        #middle of the page
        self.etiquette = tk.Label(self, text='Mot de passe :')
        self.etiquette.pack(padx=5, pady=5, side=tk.LEFT)

        self.entree1 = tk.Entry(self, width=50, show="*")
        self.entree2 = tk.Entry(self, width=50, show="*")
        self.entree1.pack(padx=5, pady=5, side=tk.LEFT)
        self.entree2.pack(padx=5, pady=5, side=tk.LEFT)

        #Bottom of the page
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def getChange(self):
        global entree1
        print(entree1.getdouble())
    
    def calcChange(change1,change2, nb_to_change2) : 
        return (change1 * nb_to_change2)/change2

root = tk.Tk()
app = Affichage(master=root)
app.mainloop()