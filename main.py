import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import pathlib as p
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

def fileN(kat, fre, nam, sta, end, dur, addname, corner):
    Spec_Names = addname.get().split()
    print(len(Spec_Names))
    if(fre.get() == ""):
        freq = ""
    else:
        freq = fre.get()+"h_"
    if (end.get()==""):
        date = sta.get()
    else:
        date = "od_"+sta.get() + "_do_"+end.get()
    rez = {"POZIOM":0, "PION":0, "KURTPOZ":0, "KURTWSCH":0, "DWSROD":0, "PLU":0, "CORNERLONG":0, "KURTKAT":0, "KASPRZAKA":0,"MARRIOTT":0,"KURTCENT":0,  "INNE":0, }
    rez_u = {"POZIOM":[], "PION":[], "KURTPOZ":[], "KURTWSCH":[], "DWSROD":[], "PLU":[], "CORNERLONG":[], "KURTKAT":[], "KASPRZAKA":[],"MARRIOTT":[],"KURTCENT":[], "INNE":[] }
    fp = fd.askdirectory(title="Wybierz folder", initialdir='/')+"\\"
    os.system("cd " + fp)
    path = p.Path(fp)
    list_file = list(path.glob('*.mp4'))+list(path.glob('*.jpg'))+list(path.glob('*.jpeg'))+list(path.glob('*.png'))
    print(list_file)
    for f in list_file:
        if(len(Spec_Names)==0):
            reso = res(f)
            rez[reso] += 1
            rez_u[reso].append(str(rez[reso]))
        else:
            reso = res(f)
            rez[reso] += 1
            rez_u[reso] = Spec_Names
    i = {"POZIOM": 0, "PION": 0, "KURTPOZ": 0, "KURTWSCH": 0, "DWSROD": 0, "PLU": 0, "CORNERLONG": 0, "KURTKAT": 0, "KASPRZAKA": 0,"MARRIOTT":0,"KURTCENT":0, "INNE": 0, }
    for f in list_file:
        reso = res(f)
        if(str(reso) == "CORNERLONG" and corner.get()== True):
            Namreso = "CORNER"
        else:
            Namreso = reso
        if(rez[reso]>1):
            if(i[reso]<len(rez_u[reso])):
                name = f"[{kat.get()}]_{nam.get()}_{rez_u[reso][i[reso]]}_{freq}{Namreso}_{date}.mp4"
            else:
                name = f"[{kat.get()}]_{nam.get()}_{i[reso]+1}_{freq}{Namreso}_{date}.mp4"
            i[reso]+=1
        else:
            name = f"[{kat.get()}]_{nam.get()}_{freq}{Namreso}_{date}.mp4"
        new = p.PureWindowsPath('\\'.join(str(f).split('\\')[:-1])+'\\'+name)
        del reso
        if(f.suffix=='.jpg' or f.suffix=='.jpeg'):
            dur_rat = 1/int(dur.get())
            komp = "ffmpeg -framerate "+str(dur_rat)+" -i \""+str(f)+"\" -codec:v libx264 -b:v 7000k -vf fps=25 -pix_fmt yuv420p \""+str(new)+"\""
        elif(f.suffix=='.png'):
            dur_rat = 1 / int(dur.get())
            komp = "ffmpeg -framerate "+str(dur_rat)+" -i \""+str(f)+"\" -codec:v libx264 -b:v 7000k -vf fps=25 -pix_fmt yuv420p \"" + str(new) + "\""
        else:
            komp = "ffmpeg -i \""+str(f)+"\" -codec:v libx264 -x264-params \"nal-hrd=cbr\" -an -b:v 7000k -r 24 \""+str(new)+"\""
        os.system(komp)
    print("\nZakończono!\n")

def print_hi():
    window = tk.Tk()
    window.columnconfigure(2, weight=1, minsize=70)
    window.rowconfigure(2, weight=1, minsize=40)
    label = tk.Label(text=f"Kategoria: ")
    label.pack(padx=5, pady=5)
    choiceVar = tk.StringVar()
    kategorie = ['R1', 'R2', 'R3', 'R4', 'W', 'SP', 'NW', 'NP']
    choiceVar.set(kategorie[1])
    kat = ttk.Combobox(textvariable=choiceVar, values=kategorie)
    kat.pack(padx=5, pady=5)
    label = tk.Label(text=f"Czestotliwosc: ")
    label.pack(padx=5, pady=5)
    fre = tk.Entry()
    fre.pack(padx=5, pady=5)
    label = tk.Label(text=f"Nazwa: ")
    label.pack(padx=5, pady=5)
    nam = tk.Entry()
    nam.pack(padx=5, pady=5)
    label = tk.Label(text=f"Poczatek: ")
    label.pack(padx=5, pady=5)
    sta = tk.Entry()
    sta.pack(padx=5, pady=5)
    label = tk.Label(text=f"Koniec: ")
    label.pack(padx=5, pady=5)
    end = tk.Entry()
    end.pack(padx=5, pady=5)
    label = tk.Label(text=f"Czas trwania jpg: ")
    label.pack(padx=5, pady=5)
    dur = tk.Entry()
    dur.pack(padx=5, pady=5)
    label = tk.Label(text=f"Nazwy dodatkowe (wypisz po spacjach): ")
    label.pack(padx=5, pady=5)
    AddName = tk.Entry()
    AddName.pack(padx=5, pady=5)
    checkbox_var = tk.BooleanVar()
    Cor = tk.Checkbutton(text="CORNER", variable=checkbox_var)
    Cor.pack(padx=5, pady=5)
    button = tk.Button(text="Wybierz lokalizacje", width=15, height=5, bg="red", font=8, fg="white", command=lambda: fileN(kat,fre,nam,sta,end,dur,AddName,checkbox_var))
    button.pack()
    window.mainloop()



if __name__ == '__main__':
    print_hi()


