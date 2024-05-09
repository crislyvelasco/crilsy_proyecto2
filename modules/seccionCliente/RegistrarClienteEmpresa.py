from customtkinter import *
from ..CTkSelector.ctk_scrollable_dropdown import *

marco_RegistroEmpresa = []

widgetsEntry_RegistraClienteEmpresa = []

def RegistraClienteEmpresa(self):
    
    self.marcoRegistroEmpresa = CTkFrame(
                                self,
                                height=670,
                                width=970,
                                fg_color=self.color_blancoPrimario,
                                corner_radius=0
                            )
    
    marco_RegistroEmpresa.append(self.marcoRegistroEmpresa)
    
    #Titulo de la vista
    self.TituloRegistroEmpresa_label = CTkLabel(
        self.marcoRegistroEmpresa,
        text="Registro de Empresa",
        text_color= self.color_azulPrimario,
        font= self.Fuente_MontserratBold_Titulos
    )
    
    self.TituloRegistroEmpresa_label.place(x=30, y=25)
    
    #Label Nombre Empresa
    self.NombreEmpresa_label = CTkLabel(
        self.marcoRegistroEmpresa,
        text='Nombre',
        text_color=self.color_azulPrimario,
        fg_color='transparent',
        font= self.Fuente_MontserratBold_Labels
    )
    
    self.NombreEmpresa_label.place(x=30, y=100)
    
    #Entry Nombre Empresa
    self.NombreEmpresa_entry = CTkEntry(
        self.marcoRegistroEmpresa,
        text_color='#000',
        width=300,
        height=47,
        fg_color='transparent',
        corner_radius=15,
        border_width=3,
        border_color=self.color_azulPrimario,
        font=self.Fuente_MontserratSemiBold_PlaceHolder
    )
    
    self.NombreEmpresa_entry.place(x=30, y=130)
    widgetsEntry_RegistraClienteEmpresa.append(self.NombreEmpresa_entry)
    
    #Label RIF
    self.Rif_label = CTkLabel(
        self.marcoRegistroEmpresa,
        text='RIF',
        text_color=self.color_azulPrimario,
        fg_color='transparent',
        font= self.Fuente_MontserratBold_Labels
    )
    
    self.Rif_label.place(x=350, y=100)
    
    #Entry RIF
    self.Rif_entry = CTkEntry(
        self.marcoRegistroEmpresa,
        text_color='#000',
        width=250,
        height=47,
        fg_color='transparent',
        corner_radius=15,
        border_width=3,
        border_color=self.color_azulPrimario,
        font=self.Fuente_MontserratSemiBold_PlaceHolder
    )
    
    self.Rif_entry.place(x=350, y=130)
    widgetsEntry_RegistraClienteEmpresa.append(self.Rif_entry)
    
    
    #Label Telefono
    self.Telefono_label = CTkLabel(
        self.marcoRegistroEmpresa,
        text='Teléfono',
        text_color=self.color_azulPrimario,
        fg_color='transparent',
        font= self.Fuente_MontserratBold_Labels
    )
    
    self.Telefono_label.place(x=620, y=100)
    
    #Entry Telefono
    self.Telefono_entry = CTkEntry(
        self.marcoRegistroEmpresa,
        text_color='#000',
        width=250,
        height=47,
        fg_color='transparent',
        corner_radius=15,
        border_width=3,
        border_color=self.color_azulPrimario,
        font=self.Fuente_MontserratSemiBold_PlaceHolder
    )
    
    self.Telefono_entry.place(x=620, y=130)
    widgetsEntry_RegistraClienteEmpresa.append(self.Telefono_entry)
    
    #Label Correo
    self.Correo_label = CTkLabel(
        self.marcoRegistroEmpresa,
        text='Correo Electrónico',
        text_color=self.color_azulPrimario,
        fg_color='transparent',
        font= self.Fuente_MontserratBold_Labels
    )
    
    self.Correo_label.place(x=30, y=200)
    
    #Entry Correo
    self.Correo_entry = CTkEntry(
        self.marcoRegistroEmpresa,
        text_color='#000',
        width=300,
        height=47,
        fg_color='transparent',
        corner_radius=15,
        border_width=3,
        border_color=self.color_azulPrimario,
        font=self.Fuente_MontserratSemiBold_PlaceHolder
    )
    
    self.Correo_entry.place(x=30, y=230)
    widgetsEntry_RegistraClienteEmpresa.append(self.Correo_entry)
    
    #Label Direccion
    self.Direccion_label = CTkLabel(
        self.marcoRegistroEmpresa,
        text='Dirección',
        text_color=self.color_azulPrimario,
        fg_color='transparent',
        font= self.Fuente_MontserratBold_Labels
    )
    
    self.Direccion_label.place(x=350, y=200)
    
    #Entry Direccion
    self.Direccion_entry = CTkEntry(
        self.marcoRegistroEmpresa,
        text_color='#000',
        width=520,
        height=47,
        fg_color='transparent',
        corner_radius=15,
        border_width=3,
        border_color=self.color_azulPrimario,
        font=self.Fuente_MontserratSemiBold_PlaceHolder
    )
    
    self.Direccion_entry.place(x=350, y=230)
    widgetsEntry_RegistraClienteEmpresa.append(self.Direccion_entry)
    
    #Titulo Datos Encargado
    self.TituloDatosEnc_label = CTkLabel(
        self.marcoRegistroEmpresa,
        text="Datos encargado de la empresa",
        text_color= self.color_azulPrimario,
        font= self.Fuente_MontserratBold_Titulos
    )
    
    self.TituloDatosEnc_label.place(x=30, y=310)
    
    #Label Nombre Encargado
    self.NombreEnc_label = CTkLabel(
        self.marcoRegistroEmpresa,
        text='Nombres y Apellidos',
        text_color=self.color_azulPrimario,
        fg_color='transparent',
        font= self.Fuente_MontserratBold_Labels
    )
    
    self.NombreEnc_label.place(x=30, y=380)
    
    #Entry Nombre Encargado
    self.NombreEnc_entry = CTkEntry(
        self.marcoRegistroEmpresa,
        text_color='#000',
        width=300,
        height=47,
        fg_color='transparent',
        corner_radius=15,
        border_width=3,
        border_color=self.color_azulPrimario,
        font=self.Fuente_MontserratSemiBold_PlaceHolder
    )
    
    self.NombreEnc_entry.place(x=30, y=410)
    widgetsEntry_RegistraClienteEmpresa.append(self.NombreEnc_entry)
    
    #Label Telefono Encargado
    self.TelefonoEnc_label = CTkLabel(
        self.marcoRegistroEmpresa,
        text='Teléfono',
        text_color=self.color_azulPrimario,
        fg_color='transparent',
        font= self.Fuente_MontserratBold_Labels
    )
    
    self.TelefonoEnc_label.place(x=350, y=380)
    
    #Entry Telefono Encargado
    self.TelefonoEnc_entry = CTkEntry(
        self.marcoRegistroEmpresa,
        text_color='#000',
        width=250,
        height=47,
        fg_color='transparent',
        corner_radius=15,
        border_width=3,
        border_color=self.color_azulPrimario,
        font=self.Fuente_MontserratSemiBold_PlaceHolder
    )
    
    self.TelefonoEnc_entry.place(x=350, y=410)
    widgetsEntry_RegistraClienteEmpresa.append(self.TelefonoEnc_entry)
    
    #Label Correo Encargado
    self.CorreoEnc_label = CTkLabel(
        self.marcoRegistroEmpresa,
        text='Correo Electrónico',
        text_color=self.color_azulPrimario,
        fg_color='transparent',
        font= self.Fuente_MontserratBold_Labels
    )
    
    self.CorreoEnc_label.place(x=620, y=380)
    
    #Entry Correo Encargado
    self.CorreoEnc_entry = CTkEntry(
        self.marcoRegistroEmpresa,
        text_color='#000',
        width=250,
        height=47,
        fg_color='transparent',
        corner_radius=15,
        border_width=3,
        border_color=self.color_azulPrimario,
        font=self.Fuente_MontserratSemiBold_PlaceHolder
    )
    
    self.CorreoEnc_entry.place(x=620, y=410)
    widgetsEntry_RegistraClienteEmpresa.append(self.CorreoEnc_entry)
    
    #Label Cargo Encargado
    self.CargoEnc_label = CTkLabel(
        self.marcoRegistroEmpresa,
        text='Cargo',
        text_color=self.color_azulPrimario,
        fg_color='transparent',
        font= self.Fuente_MontserratBold_Labels
    )
    
    self.CargoEnc_label.place(x=30, y=480)
    
    #Entry Cargo Encargado
    self.CargoEnc_entry = CTkEntry(
        self.marcoRegistroEmpresa,
        text_color='#000',
        width=300,
        height=47,
        fg_color='transparent',
        corner_radius=15,
        border_width=3,
        border_color=self.color_azulPrimario,
        font=self.Fuente_MontserratSemiBold_PlaceHolder
    )
    
    self.CargoEnc_entry.place(x=30, y=510)
    widgetsEntry_RegistraClienteEmpresa.append(self.CargoEnc_entry)
    
    #Boton Guardar
    self.boton_guardar = CTkButton (
                    self.marcoRegistroEmpresa,
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
                    self.marcoRegistroEmpresa,
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