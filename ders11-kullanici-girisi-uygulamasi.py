import tkinter as tk

import PIL.ImageTk
from PIL import Image

app= tk.Tk()

app.state("normal")
app.minsize(400,400)
app.maxsize(400,400)
app.title("Ders-11 Kullanici Girisi Uygulamasi Denemesi")

app.geometry("300x300+200+200")

image=Image.open("C://Users//emre//PycharmProjects//tkinter-proje//imagess.jpg")

resize_image=image.resize((400,400))

img= PIL.ImageTk.PhotoImage(resize_image)
label1= tk.Label(image=img)
label1.image =img
label1.pack()
label3=tk.Label(app,text="------------------------------UYE GİRİS EKRANI------------------------------")
label3.place(x=0,y=10)
def giris_yap():
    dosya= open("Giris-yapan-kullanicilar.txt","a")
    dosya.write("Kullanici Adi: {} Sifre: {}\n".format(entry1.get(),entry2.get()))
    entry1.delete(0,"end")
    entry2.delete(0,"end")

a=1

def kayit_ol():
    global a
    label2=tk.Label(app,text="------------------------------KAYIT OLMA EKRANI------------------------------")
    label2.place(x=0,y=210)
    if a==1:
        def yeni_kayit():
            dosya1 = open("Kayit-olan-kullanicilar", "a")
            dosya1.write("Yeni Kullanici Adi: {} Yeni Sifre: {}\n".format(entry3.get(), entry4.get()))
            entry3.delete(0, "end")
            entry4.delete(0, "end")

        yazi1=tk.Label(app,text="Yeni Kullanici:")
        yazi1.place(x=100,y=250)
        entry3=tk.Entry(app,fg="white",bg="black")
        entry3.place(x=210,y=250)
        yazi2=tk.Label(app,text="Yeni Sifre:")
        yazi2.place(x=100,y=300)
        entry4 = tk.Entry(app, fg="white", bg="black")
        entry4.place(x=210,y=300)
        buton3=tk.Button(app,text="Giris",fg="black",bg="purple",command=yeni_kayit)
        buton3.place(x=180,y=350)

        a-=1
    else:
        pass

yazig1=tk.Label(app,text="Kullanici Adi:")
yazig1.place(x=100,y=100)
entry1=tk.Entry(app,fg="white",bg="black")
entry1.place(x=210,y=100)

yazig2=tk.Label(app,text="Sifre:")
yazig2.place(x=100,y=130)
entry2=tk.Entry(app,fg="white",bg="black",show="*")
entry2.place(x=210,y=130)

buton1=tk.Button(app,text="Giris",fg="black",bg="purple",command=giris_yap)
buton1.place(x=150,y=170)

buton2=tk.Button(app,text="Kaydol",fg="black",bg="purple",command=kayit_ol)
buton2.place(x=200,y=170)

app.mainloop()