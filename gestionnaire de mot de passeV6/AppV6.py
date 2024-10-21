# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 18:28:45 2023

@author: Utilisateur
"""

import csv
import os
from cryptography.fernet import Fernet
import string
from random import *
from tkinter import *
from tkinter import messagebox
decrypt_check= FALSE
class App :
    def __init__(self):
        self.key_file = 'unlock.key'
        self.window = Tk()
        self.key = None 
        self.open = None
        self.window.title("Gestionnaire de mot de passe")
        self.window.geometry("720x480")
        self.window.minsize(480, 360)
        self.window.iconbitmap("keepass_logo.ico")
        self.window.config(background='#0095BD')
    #génere les différentes frame
        self.login_frame= Frame(self.window,bg='#0095BD')
        self.main_frame=Frame(self.window,bg='#0095BD')
        self.frame_left = Frame(self.main_frame, bg='#0095BD')
        self.frame_right = Frame(self.main_frame, bg='#0095BD')
        self.open_frame = Frame(self.window, bg ='#0095BD')
    #empacketage
        self.login_frame.pack(expand=TRUE)

        
    #creation des composants
        self.create_widget()
        
    #creation des widgets
    def create_widget(self):
        self.create_login_password_entry()
        self.create_login_id_entry()
        self.create_login_password_label()
        self.create_login_id_label()
        self.create_login_label()
        self.create_login_button()
        self.create_canvas()
        self.create_generate_button()
        self.create_confirm_button()
        self.create_site_entry()
        self.create_password_entry()
        self.password_open_button()
        self.password_delete_Entry()
        self.password_delete_button()
    #commande de login 
    
    def Login(self):
        identifiant = "1"
        password = "2"
        if  self.login_id_entry.get() == identifiant and self.login_password_entry.get() == password :
            self.login_frame.pack_forget()
            self.main_frame.pack(expand= TRUE)
            self.frame_left.grid(row=0, column=0)
            self.frame_right.grid(row=0,column=1)
            self.open_frame.pack()
            self.load_key()
            self.decrypt()
            global decrypt_check
            decrypt_check = TRUE
        else:
            messagebox.showinfo(title="Error", message="Invalid login")
        
    """boutons pour la page login"""    
    def create_login_password_entry(self):
        self.login_password_entry= Entry(self.login_frame,background='white')
        self.login_password_entry.grid(row=2,column=1)
    
    def create_login_password_label(self):
        self.login_password_label= Label(self.login_frame,text="Mot de passe :",background='#0095BD')
        self.login_password_label.grid(row=2,column=0)
    
    def create_login_id_entry(self):
        self.login_id_entry= Entry(self.login_frame,background='white')
        self.login_id_entry.grid(row=1,column=1)
    
    def create_login_id_label(self):
        self.login_id_label= Label(self.login_frame,text="Identifiant :",background='#0095BD')
        self.login_id_label.grid(row=1,column=0)
        
    def create_login_label(self):
        self.login_label= Label(self.login_frame,text="Login",background='#0095BD')
        self.login_label.grid(row=0,column=0,columnspan=2,pady=10)
        
    def create_login_button(self):
        self.login_label_button= Button(self.login_frame,text="Login",background='#D0EAFA', command= self.Login)
        self.login_label_button.grid(row=3,column=0,columnspan=2,pady=20)
        
        
        
    """boutons pour la page principale"""
    
    
    def create_canvas(self):
        self.width=300
        self.height=300
        self.image= PhotoImage(file="fond.png")
        self.canvas= Canvas(self.frame_left,width=self.width,height=self.height,bg='#0095BD', bd=0,highlightthickness=0)
        self.canvas.create_image(self.width/2, self.height/2, image=self.image)
        self.canvas.grid(row=0,column=0)
        
#fait les commandes
    def Generate_password(self):
        self.password_min=6
        self.password_max=12
        self.allchars = string.ascii_letters + string.punctuation + string.digits
        self.password = "".join(choice(self.allchars)for x in range(randint(self.password_min,self.password_max)))   
        self.password_entry.delete(0,END)
        self.password_entry.insert(0,self.password)
    
    def confirm(self):
        self.fichier =open("mdp.csv", "a")
        
        self.content = self.site_entry.get()
        
        if self.content != "" :
            self.fichier.write(self.content)
            self.fichier.write(" : ")
            self.fichier.write(self.password_entry.get())
            self.fichier.write("\n")
            self.fichier.close()
        if self.open ==1:
            self.update_password_entries()
        self.fichier.close()

        
    
    
        #cryptage 
    def load_key(self):
        with open(self.key_file, 'rb') as key_file:
                self.key = key_file.read()

             
    def crypt(self):
        print("opsdg,ioskgd")
        self.f = Fernet(self.key)
        with open('mdp.csv', 'rb') as original_file:
             original = original_file.read()
        encrypted = self.f.encrypt(original)
        with open ('enc_mdp.csv', 'wb') as encrypted_file:
             encrypted_file.write(encrypted)
             
    def decrypt(self):

        self.f = Fernet(self.key)
        with open('enc_mdp.csv', 'rb') as encrypted_file:
             encrypted = encrypted_file.read()
        decrypted = self.f.decrypt(encrypted)
        with open('mdp.csv', 'wb') as decrypted_file:
             decrypted_file.write(decrypted) 
             

    def password_open(self):
          
        self.canvas.grid_forget()
        self.canvas2 = Canvas(self.frame_left, width=200, height=1, bg='#0095BD', bd=0, highlightthickness=0)
        self.canvas2.grid(row=0, column=1)
        self.open = 1
        self.update_password_entries()  # Appel de la méthode pour mettre à jour les entrées
        fichier_csv = open("mdp.csv")
        fichier_csv.close()
        
    def update_password_entries(self):
        for widget in self.frame_left.winfo_children():
            widget.destroy()

        with open('mdp.csv',encoding='utf-8') as fichier_csv:
            self.reader = csv.reader(fichier_csv, delimiter=",")
            a = 0
            for ligne in self.reader:
                password_output = Entry(self.frame_left, bg='white')
                password_output.grid(row=a, column=0,padx=50)
                password_output.insert(0, ligne[0])
                a += 1
    
    def password_delete(self):
        id_password_delete = [self.password_delete_entry.get()]
        print(id_password_delete)

        fichier_csv = 'mdp.csv'
        ligne_a_supprimer = id_password_delete

        with open(fichier_csv, 'r', newline='') as file:
            lecteur = csv.reader(file)
            lignes = list(lecteur)
        # Rechercher et supprimer la ligne spécifique
        for ligne in lignes:
            if ligne == ligne_a_supprimer:
                lignes.remove(ligne)

        # Écrire la liste mise à jour dans le fichier CSV
        with open(fichier_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(lignes)


        # Mettre à jour les entrées après suppression
        self.update_password_entries()
        
#fait les boutons/ champs        
    def create_generate_button(self):
        generate_button= Button(self.frame_right,text="Générer",background='#0095BD',command=self.Generate_password)
        generate_button.grid(row=2, column=1)
        
    def create_confirm_button(self):
        confirm_button= Button(self.frame_right,text="Confirmer",background='#0095BD',command=self.confirm)
        confirm_button.grid(row=3, column=1)
        
        
    def create_site_entry(self):
        self.site_entry= Entry(self.frame_right,background='white')
        self.site_entry.grid(row=0,column=1)
        
    def create_password_entry(self):
        self.password_entry= Entry(self.frame_right,background='white')
        self.password_entry.grid(row=1,column=1)
    
    def password_open_button(self):
        generate_button= Button(self.open_frame ,text="Afficher les mot de passe",background='#0095BD',command=self.password_open)
        generate_button.pack()
    
    def password_delete_button(self):
        self.password_delete_button= Button(self.frame_right ,text="supprimer le mot de passe",background='#0095BD',command=self.password_delete)
        self.password_delete_button.grid(row=5,column=1,padx=50)
        
    def password_delete_Entry(self):
        self.password_delete_entry= Entry(self.frame_right,background='white')
        self.password_delete_entry.grid(row=4,column=1,padx=50)
        
        
app = App()
app.window.mainloop()
os.remove("enc_mdp.csv")
app.load_key()
app.crypt()
if decrypt_check == TRUE :
    os.remove("mdp.csv")