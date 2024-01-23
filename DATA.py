import os
import pickle
from tkinter import Button, filedialog, Frame, Label
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

def select_image():
    image_path = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Sélectionnez une image",
        filetypes=[("Image Files", ("*.jpg", "*.png", "*.webp"))]
    )
    # Charger l'image et la prétraiter
    with open(image_path, 'rb') as f:
        #IG=Image.open(f)

        img = Image.open(f)
        IGR = img.resize((400, 400))
        img = img.resize((64, 64))  # Ajuster la taille de l'image pour l'affichage
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0  # Effectuer la mise à l'échelle des pixels

    # Faire la prédiction
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)
    predicted_class_name = class_names[predicted_class]

    # Afficher l'image dans la première frame
    img_tk = ImageTk.PhotoImage(IGR)
    image_label.config(image=img_tk,width=400, height=400)
    image_label.image = img_tk

    # Afficher la classe prédite dans la deuxième frame
    result_label.config(text="Classe prédite : " + predicted_class_name)


# Charger le modèle entraîné
folder = 'model.sav'
model = pickle.load(open(folder, 'rb'))

# Liste des noms de classe
class_names = ["astilbe", "bellflower", "black_eyed_susan", "calendula", "california_poppy", "carnation",
               "common_daisy", "coreopsis", "daffodil", "daisy", "dandelion", "iris", "magnolia", "rose",
               "sunflower", "tulip", "water_lily"]

# Créer une fenêtre Tkinter
window = tk.Tk()
window.iconbitmap("pink-cosmos.ico")
window.geometry("700x600")
window.title("Classification des fleurs")
window.configure(bg="#F3CFC6")

# Charger l'image
image = Image.open("background_image.jpg")
image = image.resize((700, 600))  # Redimensionner l'image selon la taille de la fenêtre

# Convertir l'image en format compatible avec Tkinter
image_tk = ImageTk.PhotoImage(image)

# Créer une étiquette avec l'image en tant qu'arrière-plan
background_label = Label(window, image=image_tk)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Créer le bouton de sélection d'image dans la première frame
select_button = Button(window, text="Sélectionner une image",font=("Arial", 9), bg="#F3CFC6", command=select_image)
select_button.pack(pady=30)

# Créer les deux frames
image_frame = Frame(window, width=500, height=600, bg='white')
image_frame.pack(pady=10)

result_frame = Frame(window, relief='solid')
result_frame.pack()

# Créer l'étiquette pour afficher l'image dans la première frame
image_label = Label(image_frame)
image_label.pack()

# Créer l'étiquette pour afficher la classe prédite dans la deuxième frame
result_label = Label(result_frame, text="Classe prédite : ", font=("Arial", 10), width=40, height=2, bg="#F3CFC6",relief='solid')
result_label.pack()

# Lancer la boucle principale de la fenêtre Tkinter
window.mainloop()


