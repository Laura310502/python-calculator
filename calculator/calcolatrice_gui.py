import tkinter as tk
from tkinter import messagebox

# Funzione per aggiungere caratteri al display
def aggiungi_carattere(char):
    current = display_var.get()
    display_var.set(current + char)

# Funzione per cancellare tutto il display
def cancella():
    display_var.set("")

# Funzione per cancellare l'ultimo carattere (backspace)
def backspace():
    current = display_var.get()
    if current:
        display_var.set(current[:-1])

# Funzione per invertire segno del numero corrente
def inverti_segno():
    expr = display_var.get()
    try:
        import re
        pattern = re.compile(r'(\-?\d+\.?\d*)$')
        match = pattern.search(expr)
        if match:
            num = match.group(1)
            start, end = match.span(1)
            if num.startswith('-'):
                nuovo_num = num[1:]
            else:
                nuovo_num = '-' + num
            nuovo_expr = expr[:start] + nuovo_num + expr[end:]
            display_var.set(nuovo_expr)
    except:
        pass

# Funzione per calcolare il risultato
def calcola():
    espressione = display_var.get()
    try:
        risultato = eval(espressione)
        display_var.set(str(risultato))
    except ZeroDivisionError:
        messagebox.showerror("Errore", "Divisione per zero!")
        cancella()
    except Exception:
        messagebox.showerror("Errore", "Espressione non valida!")
        cancella()

# Blocca input da tastiera fisica (non scrive nulla)
def blocca_tastiera(event):
    return "break"

# Aspetto e stile
BG_COLOR = "#2E2E2E"
BTN_COLOR = "#4CAF50"
BTN_HOVER = "#45A049"
DISPLAY_BG = "#1C1C1C"
DISPLAY_FG = "#000000"
FONT = ("Consolas", 20)

root = tk.Tk()
root.title("Calcolatrice Avanzata")
root.geometry("360x480")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

display_var = tk.StringVar()

# Display Entry in readonly per bloccare digitazione tastiera
display = tk.Entry(root, textvariable=display_var, font=FONT, bd=0,
                   bg=DISPLAY_BG, fg=DISPLAY_FG, justify="right", insertbackground='white',
                   state='readonly')
display.pack(fill=tk.BOTH, padx=10, pady=15, ipady=15)

# Blocca input tastiera 
display.bind("<Key>", blocca_tastiera)

frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(padx=10, pady=10)

# Pulsanti e loro posizioni 
buttons = [
    ('C', 0, 0, 'red'), ('⌫', 0, 1, 'orange'), ('(', 0, 2, BTN_COLOR), (')', 0, 3, BTN_COLOR),
    ('7', 1, 0, BTN_COLOR), ('8', 1, 1, BTN_COLOR), ('9', 1, 2, BTN_COLOR), ('/', 1, 3, 'orange'),
    ('4', 2, 0, BTN_COLOR), ('5', 2, 1, BTN_COLOR), ('6', 2, 2, BTN_COLOR), ('*', 2, 3, 'orange'),
    ('1', 3, 0, BTN_COLOR), ('2', 3, 1, BTN_COLOR), ('3', 3, 2, BTN_COLOR), ('-', 3, 3, 'orange'),
    ('+/-', 4, 0, 'purple'), ('0', 4, 1, BTN_COLOR), ('.', 4, 2, BTN_COLOR), ('+', 4, 3, 'orange'),
    ('=', 5, 0, '#2196F3', 4)
]

def on_enter(e):
    e.widget['background'] = BTN_HOVER

def on_leave(e, color):
    e.widget['background'] = color

def comando_pulsante(char):
    if char == 'C':
        cancella()
    elif char == '⌫':
        backspace()
    elif char == '=':
        calcola()
    elif char == '+/-':
        inverti_segno()
    else:
        aggiungi_carattere(char)

# Creazione pulsanti
for (text, r, c, color, cs) in [(b[0], b[1], b[2], b[3], b[4] if len(b) > 4 else 1) for b in buttons]:
    btn = tk.Button(frame, text=text, bg=color, fg='white', font=FONT, bd=0,
                    activebackground=BTN_HOVER, activeforeground='white',
                    command=lambda x=text: comando_pulsante(x))
    btn.grid(row=r, column=c, columnspan=cs, sticky="nsew", padx=5, pady=5)
    if text != '=':
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", lambda e, col=color: on_leave(e, col))

# Configura griglia per pulsanti
total_rows = 6
total_cols = 4

for i in range(total_rows):
    frame.rowconfigure(i, weight=1)
for i in range(total_cols):
    frame.columnconfigure(i, weight=1)

root.mainloop()
