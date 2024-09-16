import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import pathlib as p
import moviepy.video.io.ImageSequenceClip
from moviepy.editor import VideoFileClip
from PIL import Image

def res(file):
    if(file.suffix==".mp4"):
        vd = VideoFileClip(str(file))
        h = vd.w
        w = vd.h
        vd.close()
    else:
        image = Image.open(str(file))
        h,w = image.size

    if(h==1080 and w==1920):
        return "PION"
    if (h == 1920 and w == 1080):
        return "POZIOM"
    if (h == 1440 and w == 1080):
        return "KURTPOZ"
    if (h == 1620 and w == 1080):
        return "KURTWSCH"
    if (h == 1920 and w in range(916,920)):
        return "DWSROD"
    if (h == 1110 and w == 1630):
        return "PLU"
    if (h == 3840 and w == 1080):
        return "CORNERLONG"
    if ((h == 1112 and w in range(790, 794)) or (h in range(1514,1518) and w == 1080)):
        return "KURTKAT"
    if ((h in range(1038,1042)  and w in range(358,362)) or (h == 1920 and w in range(663,667))):
        return "KASPRZAKA"
    if (h in range(1918,1922)  and w in range(1014,1017)):
        return "MARRIOTT"
    if (h in range(2470,2474)  and w in range(306,309)):
        return "KURTCENT"
    else:
        return "INNE"

class Encode(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.minsize(230, 630)

        self.main = Main(self)

        self.mainloop()

class Con(tk.Frame):
    def __init__(self,list, path, kat, fre, nam, sta, end, dur, addname, corner, master=None):
        super().__init__(master)
        self.path = path
        self.master = master
        self.pack()
        self.create_widgets(list)
        self.kat = kat
        self.fre = fre
        self.nam = nam
        self.sta = sta
        self.end = end
        self.dur = dur
        self.addname = addname
        self.corner = corner

    def create_widgets(self, list):
        self.array = list
        self.labels = []
        self.buttons = []

        for i, element in enumerate(self.array):
            label = tk.Label(self, text=str(element))
            label.grid(row=i, column=0)
            self.labels.append(label)

            button = tk.Button(self, text="↑", command=lambda i=i: self.move_up(i))
            button.grid(row=i, column=1)
            self.buttons.append(button)

            button = tk.Button(self, text="↓", command=lambda i=i: self.move_down(i))
            button.grid(row=i, column=2)
            self.buttons.append(button)

        self.text_label = tk.Label(self, text="Długość jednego pliku: ")
        self.text_label.grid(row=len(self.array), column=0)

        self.text_entry = tk.Entry(self)
        self.text_entry.insert(0, "5")
        self.text_entry.grid(row=len(self.array), column=1)

        self.add_button = tk.Button(self, text="Połącz", command=lambda: self.rend())
        self.add_button.grid(row=len(self.array)+1, column=0)

        self.dragging = False
        self.dragged_index = None

        for label in self.labels:
            label.bind("<Button-1>", self.start_drag)
            label.bind("<ButtonRelease-1>", self.stop_drag)
            label.bind("<B1-Motion>", self.drag)

    def move_up(self, i):
        if i > 0:
            self.array[i], self.array[i-1] = self.array[i-1], self.array[i]
            for i, label in enumerate(self.labels):
                label.config(text=str(self.array[i]))

    def move_down(self, i):
        if i < len(self.array) - 1:
            self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
            for i, label in enumerate(self.labels):
                label.config(text=str(self.array[i]))

    def start_drag(self, event):
        self.dragging = True
        self.dragged_index = self.labels.index(event.widget)

    def stop_drag(self, event):
        self.dragging = False
        self.dragged_index = None

    def drag(self, event):
        if self.dragging:
            index = self.labels.index(event.widget)
            if index != self.dragged_index:
                self.array[self.dragged_index], self.array[index] = self.array[index], self.array[self.dragged_index]
                for i, label in enumerate(self.labels):
                    label.config(text=str(self.array[i]))
                self.dragged_index = index
    def rend(self):
        temp_path = f'{self.path}\my_video.mp4'
        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(self.array, fps=1/float(self.text_entry.get()))
        clip.write_videofile(temp_path)
        del clip
        Rend(self.kat, self.fre, self.nam, self.sta, self.end, self.dur, self.addname, self.corner, p.Path(temp_path))
        os.remove(temp_path)
        self.master.destroy()

class Cor(tk.Frame):
    def __init__(self, kat, fre, nam, sta, end, dur, addname, corner, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.pack()
        self.addname = addname
        if(corner==True):
            self.corner="CORNER"
        else:
            self.corner="CORNERLONG"
        self.nazwa = f"[{kat.get()}]_{nam.get()}_{fre.get()}h_{self.corner}_od_{sta.get()}_do_{end.get()}"

    def create_widgets(self):
        self.text_lewy = tk.Label(self, text="Lewy: ")
        self.text_plewy = tk.Label(self, text="[Brak]")
        self.lleft = tk.Button(self, text="Add", command=lambda: self.add_File(0))
        self.text_lewy.grid(row=0, column=0)
        self.text_plewy.grid(row=0, column=1)
        self.lleft.grid(row=0, column=2)
        self.text_prawy = tk.Label(self, text="Prawy: ")
        self.text_pprawy = tk.Label(self, text="[Brak]")
        self.bright = tk.Button(self, text="Add", command=lambda: self.add_File(1))
        self.text_prawy.grid(row=1, column=0)
        self.text_pprawy.grid(row=1, column=1)
        self.bright.grid(row=1, column=2)
        self.button = tk.Button(self, text="Połącz", command=lambda: self.rend())
        self.button.grid(row=2)
    def add_File(self, i):
        fp = fd.askopenfiles(title="Wybierz pliki", initialdir='/')
        if(i==0):
            self.left = p.Path(fp[0].name)
            self.text_plewy.config(text=fp[0].name)
        else:
            self.right = p.Path(fp[0].name)
            self.text_pprawy.config(text=fp[0].name)
        self.path = p.Path(fp[0].name).parent
    def rend(self):
        command = f"ffmpeg -i {self.left} -i {self.right} -codec:v libx264 -x264-params \"nal-hrd=cbr\" -an -b:v 7000k -r 24 -filter_complex hstack -s 3840x1080 {self.path}\\{self.nazwa}.mp4"
        os.system(command)
        print("\nZakończono!\n")
        self.master.destroy()


def con(kat, fre, nam, sta, end, dur, addname, corner):
    list = []
    fp = fd.askopenfiles(title="Wybierz pliki", initialdir='/')
    path = p.Path(fp[0].name).parent
    for i in fp:
        list.append(str(p.Path(i.name)))
    print(list)
    root = tk.Tk()
    Con(list, path, kat, fre, nam, sta, end, dur, addname, corner, master=root)

def cor(kat, fre, nam, sta, end, dur, addname, corner):
    root = tk.Tk()
    root.minsize(500,20)
    Cor(kat, fre, nam, sta, end, dur, addname, corner, master=root)

class Rend:
    rez = {"POZIOM": 0, "PION": 0, "KURTPOZ": 0, "KURTWSCH": 0, "DWSROD": 0, "PLU": 0, "CORNERLONG": 0, "KURTKAT": 0, "KASPRZAKA": 0, "MARRIOTT": 0, "KURTCENT": 0, "INNE": 0, }
    rez_u = {"POZIOM": [], "PION": [], "KURTPOZ": [], "KURTWSCH": [], "DWSROD": [], "PLU": [], "CORNERLONG": [], "KURTKAT": [], "KASPRZAKA": [], "MARRIOTT": [], "KURTCENT": [], "INNE": []}
    rezPom = rez.copy()
    freq=""
    date=""
    list_file = list()
    corner = ""
    Spec_Names = []
    kat = ""
    nam = ""
    dur = 5
    def __init__(self, kat, fre, nam, sta, end, dur, addname, corner, file):
        self.Spec_Names = addname.get().split()
        self.corner = corner
        self.kat = kat
        self.nam = nam
        self.setDur(dur)
        self.setFreq(fre)
        self.setDate(sta, end)
        if(file == 1):
            self.setFiles()
        else:
            self.list_file.append(file)
        self.setRez()
        self.startRender()
    def setFreq(self, fre):
        if (fre.get() == ""):
            self.freq = ""
        else:
            self.freq = fre.get() + "h_"
    def setDur(self, dur):
        if(dur.get()!=""):
            self.dur = 1/int(dur.get())
        else:
            self.dur = 0

    def setDate(self, sta, end):
        if (end.get() == ""):
            self.date = sta.get()
        else:
            self.date = "od_" + sta.get() + "_do_" + end.get()
    def setFiles(self):
        fp = fd.askopenfiles(title="Wybierz pliki", initialdir='/')
        path = p.Path(fp[0].name).parent
        wp = str(path)
        os.system("cd " + wp)
        for i in fp:
            self.list_file.append(p.Path(i.name))
        print(self.list_file)
    def setRez(self):
        for f in self.list_file:
            if (len(self.Spec_Names) == 0):
                reso = res(f)
                self.rez[reso] += 1
                self.rez_u[reso].append(str(self.rez[reso]))
            else:
                reso = res(f)
                self.rez[reso] += 1
                self.rez_u[reso] = self.Spec_Names
    def startRender(self):
        for f in self.list_file:
            reso = res(f)
            if (str(reso) == "CORNERLONG" and self.corner.get() == True):
                Namreso = "CORNER"
            else:
                Namreso = reso
            if (self.rez[reso] > 1):
                if (self.rezPom[reso] < len(self.rez_u[reso])):
                    name = f"[{self.kat.get()}]_{self.nam.get()}_{self.rez_u[reso][self.rezPom[reso]]}_{self.freq}{Namreso}_{self.date}.mp4"
                else:
                    name = f"[{self.kat.get()}]_{self.nam.get()}_{self.rezPom[reso] + 1}_{self.freq}{Namreso}_{self.date}.mp4"
                self.rezPom[reso] += 1
            else:
                name = f"[{self.kat.get()}]_{self.nam.get()}_{self.freq}{Namreso}_{self.date}.mp4"
            new = p.PureWindowsPath('\\'.join(str(f).split('\\')[:-1]) + '\\' + name)
            del reso
            if (f.suffix == '.jpg' or f.suffix == '.jpeg'):
                komp = "ffmpeg -framerate " + str(self.dur) + " -i \"" + str(
                    f) + "\" -codec:v libx264 -b:v 7000k -vf fps=25 -pix_fmt yuv420p \"" + str(new) + "\""
            elif (f.suffix == '.png'):
                komp = "ffmpeg -framerate " + str(self.dur) + " -i \"" + str(
                    f) + "\" -codec:v libx264 -b:v 7000k -vf fps=25 -pix_fmt yuv420p \"" + str(new) + "\""
            else:
                komp = "ffmpeg -i \"" + str(
                    f) + "\" -codec:v libx264 -x264-params \"nal-hrd=cbr\" -an -b:v 7000k -r 24 \"" + str(new) + "\""
            print(komp)
            os.system(komp)
        self.list_file.clear()
        print("\nZakończono!\n")
        



class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text=f"Kategoria: ")
        label.pack(padx=5, pady=5)
        choiceVar = tk.StringVar(self)
        kategorie = ['R1', 'R2', 'R3', 'R4', 'W', 'SP', 'NW', 'NP']
        choiceVar.set(kategorie[1])
        kat = ttk.Combobox(self, textvariable=choiceVar, values=kategorie)
        kat.pack(padx=5, pady=5)
        label = tk.Label(self, text=f"Czestotliwosc: ")
        label.pack(padx=5, pady=5)
        fre = tk.Entry(self)
        fre.pack(padx=5, pady=5)
        label = tk.Label(self, text=f"Nazwa: ")
        label.pack(padx=5, pady=5)
        nam = tk.Entry(self)
        nam.pack(padx=5, pady=5)
        label = tk.Label(self, text=f"Poczatek: ")
        label.pack(padx=5, pady=5)
        sta = tk.Entry(self)
        sta.pack(padx=5, pady=5)
        label = tk.Label(self, text=f"Koniec: ")
        label.pack(padx=5, pady=5)
        end = tk.Entry(self)
        end.pack(padx=5, pady=5)
        label = tk.Label(self, text=f"Czas trwania jpg: ")
        label.pack(padx=5, pady=5)
        dur = tk.Entry(self)
        dur.pack(padx=5, pady=5)
        label = tk.Label(self, text=f"Nazwy dodatkowe (wypisz po spacjach): ")
        label.pack(padx=5, pady=5)
        AddName = tk.Entry(self)
        AddName.pack(padx=5, pady=5)
        checkbox_var = tk.BooleanVar(self)
        Cor = tk.Checkbutton(self, text="CORNER", variable=checkbox_var)
        Cor.pack(padx=5, pady=5)
        button = tk.Button(self, text="Wybierz lokalizacje", width=15, height=5, bg="red", font=8, fg="white", command=lambda: Rend(kat, fre, nam, sta, end, dur, AddName, checkbox_var, 1))
        button_cor = tk.Button(self, text="Corner", width=10, height=1, font=4, command=lambda: cor(kat, fre, nam, sta, end, dur, AddName, checkbox_var))
        button_cor.pack()
        button_join = tk.Button(self, text="Połącz zdjęcia", width=10, height=1, bg="blue", font=4, fg="white", command=lambda: con(kat, fre, nam, sta, end, dur, AddName, checkbox_var))
        button_join.pack()
        button.pack()
        self.place(relx = 0, y = 1, relwidth=1)


Encode("Encode")