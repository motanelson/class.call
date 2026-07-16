import os
import tkinter as tk
from PIL import Image, ImageTk

#----------------------------------------

class VideoPlayer:

    def __init__(self, root, directory):

        self.root = root
        self.directory = directory

        self.root.title("JABA Video Player")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        self.label = tk.Label(self.root,bg="black")
        self.label.pack(fill="both",expand=True)

        # procura todos os ficheiros .bmp
        self.files = []

        for f in os.listdir(directory):
            if f.lower().endswith(".bmp"):
                self.files.append(f)

        # ordena 0.bmp,1.bmp,2.bmp,...
        try:
            self.files.sort(
                key=lambda x:int(
                x.replace(".bmp",""))
                )
        except:
            self.files.sort()

        self.counter = 0

        self.play()


    #---------------------------------

    def play(self):

        if len(self.files)==0:
            self.root.after(250,self.play)
            return

        if self.counter>=len(self.files):
            self.counter=0

        filename=os.path.join(
                    self.directory,
                    self.files[self.counter]
                    )

        try:

            image=Image.open(filename)

            # adapta ao tamanho da janela
            image=image.resize(
                (self.root.winfo_width(),
                 self.root.winfo_height())
                 )

            self.photo=ImageTk.PhotoImage(image)

            self.label.configure(
                image=self.photo)

        except:
            pass

        self.counter+=1

        # 250 milisegundos
        self.root.after(250,self.play)


#----------------------------------------

# directoria onde ficaram os bitmaps
directory="video"

root=tk.Tk()

app=VideoPlayer(root,directory)

root.mainloop()
