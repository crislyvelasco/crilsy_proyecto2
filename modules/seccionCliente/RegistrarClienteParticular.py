from customtkinter import *
from ..CTkSelector.ctk_scrollable_dropdown import *

marco_RegistroParticular = []

widgetsEntry_RegistraClienteParticular = []

def RegistraClienteParticular(self):
    
    self.marcoRegistroParticular = CTkFrame(
                                self,
                                height=670,
                                width=970,
                                fg_color=self.color_blancoPrimario,
                                corner_radius=0
                            )
    
    marco_RegistroParticular.append(self.marcoRegistroParticular)
    
     #Titulo de la vista
    self.TituloRegistroPNatural_label = CTkLabel(
        self.marcoRegistroParticular,
        text="Registro de Cliente Particular",
        text_color= self.color_azulPrimario,
        font= self.Fuente_MontserratBold_Titulos
    )
    
    self.TituloRegistroPNatural_label.place(x=30, y=25)
    
    #Label primer nombre
    self.PriNombre_label = CTkLabel(
        self.marcoRegistroParticular,
        text='Primer nombre',
        text_color=self.color_azulPrimario,
        fg_color='transparent',
        font= self.Fuente_MontserratBold_Labels
    )
    
    self.PriNombre_label.place(x=30, y=100)
    
    #Entry, primer nombre
    self.PriNombre_entry = CTkEntry(
        self.marcoRegistroParticular,
        text_color='#000',
        width=250,
        height=47,
        fg_color='transparent',
        corner_radius=15,
        border_width=3,
        border_color=self.color_azulPrimario,
        font=self.Fuente_MontserratSemiBold_PlaceHolder
    )
    
    self.PriNombre_entry.place(x=30, y=130)
    widgetsEntry_RegistraClienteParticular.append(self.PriNombre_entry)
    
    #Label segundo nombre
    self.SegNombre_label = CTkLabel(
        self.marcoRegistroParticular,
        text='Segundo nombre',
        text_color=self.color_azulPrimario,
        fg_color='transparent',
        font= self.Fuente_MontserratBold_Labels
    )
    
    self.SegNombre_label.place(x=300, y=100)
    
    #Entry, segundo nombre
    self.SegNombre_entry = CTkEntry(
        self.marcoRegistroParticular,
        text_color='#000',
        width=250,
        height=47,
        fg_color='transparent',
        corner_radius=15,
        border_width=3,
        border_color=self.color_azulPrimario,
        font=self.Fuente_MontserratSemiBold_PlaceHolder
    )
    
    self.SegNombre_entry.place(x=300, y=130)
    widgetsEntry_RegistraClienteParticular.append(self.SegNombre_entry)
    
    #Label primer apellido
    self.PriApellido_label = CTkLabel(
        self.marcoRegistroParticular,
        text='Primer apellido',
        text_color=self.color_azulPrimario,
        fg_color='transparent',
        font= self.Fuente_MontserratBold_Labels
    )
    
    self.PriApellido_label.place(x=30, y=200)
    
    #Entry, primer apellido
    self.PriApellido_entry = CTkEntry(
        self.marcoRegistroParticular,
        text_color='#000',
        width=250,
        height=47,
        fg_color='transparent',
        corner_radius=15,
        border_width=3,
        border_color=self.color_azulPrimario,
        font=self.Fuente_MontserratSemiBold_PlaceHolder
    )
    
    self.PriApellido_entry.place(x=30, y=230)
    widgetsEntry_RegistraClienteParticular.append(self.PriApellido_entry)
    
    #Label segundo apellido
    self.SegApellido_label = CTkLabel(
        self.marcoRegistroParticular,
        text='Segundo Apellido',
        text_color=self.color_azulPrimario,
        fg_color='transparent',
        font= self.Fuente_MontserratBold_Labels
    )
    
    self.SegApellido_label.place(x=300, y=200)
    
    #Entry, segundo apellido
    self.SegApellido_entry = CTkEntry(
        self.marcoRegistroParticular,
        text_color='#000',
        width=250,
        height=47,
        fg_color='transparent',
        corner_radius=15,
        border_width=3,
        border_color=self.color_azulPrimario,
        font=self.Fuente_MontserratSemiBold_PlaceHolder
    )
    
    self.SegApellido_entry.place(x=300, y=230)
    widgetsEntry_RegistraClienteParticular.append(self.SegApellido_entry)
    
    
    #Label cedula
    self.Cedula_label = CTkLabel(
        self.marcoRegistroParticular,
        text='Cédula',
        text_color=self.color_azulPrimario,
        fg_color='transparent',
        font= self.Fuente_MontserratBold_Labels
    )
    
    self.Cedula_label.place(x=30, y=300)
    
    #Entry cedula
    self.Cedula_entry = CTkEntry(
        self.marcoRegistroParticular,
        text_color='#000',
        width=250,
        height=47,
        fg_color='transparent',
        corner_radius=15,
        border_width=3,
        border_color=self.color_azulPrimario,
        font=self.Fuente_MontserratSemiBold_PlaceHolder
    )
    
    self.Cedula_entry.place(x=30, y=330)
    widgetsEntry_RegistraClienteParticular.append(self.Cedula_entry)
    
    
    #Label telefono
    self.Telefono_label = CTkLabel(
        self.marcoRegistroParticular,
        text='Teléfono',
        text_color=self.color_azulPrimario,
        fg_color='transparent',
        font= self.Fuente_MontserratBold_Labels
    )
    
    self.Telefono_label.place(x=300, y=300)
    
    #Entry telefono
    self.Telefono_entry = CTkEntry(
        self.marcoRegistroParticular,
        text_color='#000',
        width=250,
        height=47,
        fg_color='transparent',
        corner_radius=15,
        border_width=3,
        border_color=self.color_azulPrimario,
        font=self.Fuente_MontserratSemiBold_PlaceHolder
    )
    
    self.Telefono_entry.place(x=300, y=330)
    widgetsEntry_RegistraClienteParticular.append(self.Telefono_entry)
    
    
    #Label direccion
    self.Direccion_label = CTkLabel(
        self.marcoRegistroParticular,
        text='Dirección',
        text_color=self.color_azulPrimario,
        fg_color='transparent',
        font= self.Fuente_MontserratBold_Labels
    )
    
    self.Direccion_label.place(x=30, y=400)
    
    #Entry direccion
    self.Direccion_entry = CTkEntry(
        self.marcoRegistroParticular,
        text_color='#000',
        width=520,
        height=47,
        fg_color='transparent',
        corner_radius=15,
        border_width=3,
        border_color=self.color_azulPrimario,
        font=self.Fuente_MontserratSemiBold_PlaceHolder
    )
    
    self.Direccion_entry.place(x=30, y=430)
    widgetsEntry_RegistraClienteParticular.append(self.Direccion_entry)
    
    #Boton Guardar
    self.boton_guardar = CTkButton (
                    self.marcoRegistroParticular,
                    bg_color = self.color_blancoPrimario,
                    width= 180,
                    height= 50,
                    fg_color= self.color_azulPrimario,
                    border_color= self.color_azulPrimario,
                    font= self.Fuente_MontserratBold,
                    text_color = self.color_blancoPrimario,
                    corner_radius=15,
                    hover_color=self.color_azulHover,
                    text="Guardar",
                    cursor="hand2"
    )
    
    self.boton_guardar.place(x=750, y=600)     
    
    #Boton Borrar
    self.boton_Borrar = CTkButton (
                    self.marcoRegistroParticular,
                    bg_color = self.color_blancoPrimario,
                    width= 180,
                    height= 50,
                    fg_color= self.color_rojoPrimario,
                    border_color= self.color_rojoPrimario,
                    font= self.Fuente_MontserratBold,
                    text_color = self.color_blancoPrimario,
                    corner_radius=15,
                    hover_color=self.color_rojoSecundario,
                    text="Borrar",
                    cursor="hand2"
    )
    
    self.boton_Borrar.place(x=550, y=600)  