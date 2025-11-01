
import math

#ESERCIZIO 1
def perimetro():
    print("Calcola perimetro figura\n - Quadrato >> 1\n - Rettangolo >> 2\n - Cerchio >> 3")
    try: s=int(input("Inserire la scelta: "))
    except: s=0
    if s==1:
        l=float(input("Lato quadrato: ")); print("Perimetro quadrato:", l*4)
    elif s==2:
        b=float(input("Base rettangolo: ")); h=float(input("Altezza rettangolo: "))
        print("Perimetro rettangolo:", 2*b+2*h)
    elif s==3:
        r=float(input("Raggio cerchio: ")); print("Circonferenza cerchio:", 2*r*3.14)
    else:
        print("Scelta non valida")
perimetro()

#ESERCIZIO 2 facoltativo
def calcola_perimetro_area_cerchio(r,a=None):
    if a is None: a=math.pi*(r**2)
    return 2*math.pi*r, a

def calcola_perimetro_area(fig,l1=None,l2=None,a=None):
    if fig=="Quadrato":
        if l1 is None: l1=float(input("Lato quadrato: "))
        p=4*l1;  
        if a is None: a=l1**2
    elif fig=="Rettangolo":
        if l1 is None: l1=float(input("Primo lato rettangolo: "))
        if l2 is None: l2=float(input("Secondo lato rettangolo: "))
        p=2*(l1+l2);  
        if a is None: a=l1*l2
    elif fig=="Cerchio":
        if l1 is None: l1=float(input("Raggio cerchio: "))
        p,a=calcola_perimetro_area_cerchio(l1,a)
    else:
        print("Figura non riconosciuta"); return
    print(f"Perimetro del {fig}: {p}"); print(f"Area del {fig}: {a}")
    return p,a

figs=["Quadrato","Rettangolo","Cerchio"]
v=float(input("\nInserisci il valore iniziale: "))
while figs:
    print("\nFigure disponibili:"); 
    for i,f in enumerate(figs,1): print(f"{i}: {f}")
    try: s=int(input("Scegli (numero): "))
    except: print("Scelta non valida"); continue
    if s<1 or s>len(figs): print("Scelta non valida"); continue
    f=figs.pop(s-1)
    if f=="Quadrato": v,v=calcola_perimetro_area(f,l1=v)
    elif f=="Rettangolo": v,v=calcola_perimetro_area(f,l1=v,l2=v/2)
    else: v,v=calcola_perimetro_area(f,l1=v)
    if input("Vuoi continuare? (s/n): ").lower()!="s": break
if not figs: print("Non ci sono più figure disponibili. Il programma termina.")

# In questo esercizio mi sono fatto strada sbirciando un po dalla soluzione
# e chiedendo a Codex di spiegarmi alcune cose e su come inserirle. 
