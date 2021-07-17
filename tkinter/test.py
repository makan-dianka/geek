#importation de tkinter, constructeur de l'interface graphique
from tkinter import *
#importation de webbrowser pour le lien
import webbrowser

#fonction de lien de la redirection vers youtube
def direction_youtube():
    webbrowser.open_new('http://makandianka.pythonanywhere.com')
 
#nom de l'application et => nom de la domaine ===> Tk()
window = Tk()

#nom de l'application suivi d'un et le préfixe à utiliser 
window.title("My Application")
window.geometry("780x460") 
#window.iconbitmap("C:\ApprentissagePython\icon\gest.ico")
window.config(background='#41B77F')

#frame
frame = Frame(window, bg='#41B77F')
frame.pack(expand=YES)

#label pour le titre principal
label_title = Label(frame, text='bienvenue sur l\'application', font=('courrier', 40), bg='#41B77F', fg='white')
label_title.pack()

#label pour la second titre
label_subtitle = Label(frame, text='hey ! salut à tous, c\'est Makan', font=('courrier', 25), bg='#41B77F', fg='white')
label_subtitle.pack()

#creation de button cliquable et redirection et un lien
LienButton = Button(frame, text='Mon portofolio', font=('courrier', 25), bg='white', fg='#41B77F', command=direction_youtube)
LienButton.pack(pady=25, fill=X)

#constructeur de graphique  (=>window =Tk())
#fermeture obligé par      (=>window.mainloop())
window.mainloop()