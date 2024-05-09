import customtkinter as ctk

def calcular_centrado(padre, hijo):

    total = (padre // 2) - (hijo // 2)

    return total

def mostrarVistas(mostrar, ocultar, entrys=[]):
  
    LimpiarTexto(entrys)
    
    for lista in ocultar:
        for frame in lista:
            frame.grid_forget()
    
    for frame in mostrar:
        frame.grid(row=0, column=1)
        
def LimpiarTexto(listaEntry=[]):
    for widget in listaEntry:
        if isinstance(widget, ctk.CTkEntry):
            widget.delete(0, ctk.END)
        elif isinstance(widget, ctk.CTkComboBox):
            widget.set('')
            widget.update_idletasks()