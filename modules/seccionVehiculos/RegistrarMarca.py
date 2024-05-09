from customtkinter import *
from tkinter import ttk
import modules.funcionesBasicas.funcionesBasicas as funci

marcas = ['Chevrolet', 'Mack', 'Ford', 'Encava', 'Toyota', 'Volvo']

marco_RegistroMarca = []

widgetsEntry_Modelo = []

def RegistrarMarca(self, mostrar, ocultar):

    style = ttk.Style()
    style.theme_use('default')

    style.configure(
                'marca.Treeview',
                background=self.color_blancoPrimario,
                fieldbackground=self.color_blancoPrimario,
                foreground='#000',
                font=self.Fuente_MontserratSemiBold_PlaceHolder,
                rowheight=50,
                relief=FLAT
                )

    style.configure(
                'marca.Treeview.Heading',
                background=self.color_azulPrimario,
                fieldbackground=self.color_azulPrimario,
                foreground=self.color_blancoPrimario,
                font=self.Fuente_MontserratBold_Labels,
                relief=FLAT
                )
    style.map(
            'Treeview',
            background=[('selected', '#a6c4ff')],
            foreground=[('selected', self.color_azulPrimario)]
            )

    style.map(
            'Treeview.Heading',
            background=[('active', self.color_azulPrimario)]
            )
    
    self.MarcoRegistroMarca = CTkFrame(
                                self,
                                height=670,
                                width=970,
                                fg_color=self.color_blancoPrimario,
                                corner_radius=0
                            )
    
    marco_RegistroMarca.append(self.MarcoRegistroMarca)
    
    self.Regresar_boton = CTkButton(
                                self.MarcoRegistroMarca,
                                text='<',
                                width=0,
                                height=0,
                                fg_color='transparent',
                                hover=False,
                                font=CTkFont('Montserrat', weight='bold', size=46),
                                text_color=self.color_azulPrimario,
                                cursor='hand2',
                                command=lambda : funci.mostrarVistas(mostrar, ocultar)
                            )
    
    self.RegistroMarca = CTkLabel(
                                self.MarcoRegistroMarca,
                                text='Registro de Marca',
                                text_color=self.color_azulPrimario,
                                width=700,
                                height=0,
                                font=self.Fuente_MontserratBold_Titulos,
                                anchor='w'
                            )
    
    self.Marca_label = CTkLabel(
                                self.MarcoRegistroMarca,
                                text='Marca',
                                text_color=self.color_azulPrimario,
                                width=300,
                                height=0,
                                font=self.Fuente_MontserratBold_Labels,
                                anchor='w'
                            )
    
    self.Marca_entry = CTkEntry(
                                self.MarcoRegistroMarca,
                                width=210,
                                height=47,
                                font=self.Fuente_MontserratSemiBold_PlaceHolder,
                                fg_color='transparent',
                                text_color='#000',
                                border_color=self.color_azulPrimario,
                                border_width=3,
                                corner_radius=15,
                                justify='center'
                            )
    
    widgetsEntry_Modelo.append(self.Marca_entry)
    
    self.MarcasRegistradas_label = CTkLabel(
                                self.MarcoRegistroMarca,
                                text='Marcas Registradas',
                                text_color=self.color_azulPrimario,
                                width=300,
                                height=0,
                                font=self.Fuente_MontserratBold_SubTitulos,
                                anchor='w'
                            )
    
    self.boton_guardar = CTkButton (
                        self.MarcoRegistroMarca,
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
    
    self.boton_modificar = CTkButton (
                        self.MarcoRegistroMarca,
                        bg_color = self.color_blancoPrimario,
                        width= 180,
                        height= 50,
                        fg_color= self.color_azulPrimario,
                        border_color= self.color_azulPrimario,
                        font= self.Fuente_MontserratBold,
                        text_color = self.color_blancoPrimario,
                        corner_radius=15,
                        hover_color=self.color_azulHover,
                        text="Modificar",
                        cursor="hand2"
                    )
    
    self.boton_borrar = CTkButton (
                        self.MarcoRegistroMarca,
                        bg_color = self.color_blancoPrimario,
                        width= 180,
                        height= 50,
                        fg_color= self.color_azulPrimario,
                        border_color= self.color_azulPrimario,
                        font= self.Fuente_MontserratBold,
                        text_color = self.color_blancoPrimario,
                        corner_radius=15,
                        hover_color=self.color_azulHover,
                        text="Eliminar",
                        cursor="hand2"
                    )
    
    self.marcoTabla_frame = CTkFrame(
                                self.MarcoRegistroMarca,
                                height=240,
                                width=459,
                                fg_color=self.color_blancoPrimario,
                            )
    
    self.tablaMarca = ttk.Treeview(
                                    self.marcoTabla_frame,
                                    columns=('marca'),
                                    show='headings',
                                    style='marca.Treeview'
                                    )
    
    self.tablaMarca.column('marca', width=450, anchor='center')
    
    self.tablaMarca.heading('marca', text='Marca')
    self.tablaMarca.place(x=1, y=1, relwidth=1, relheight=1)
    
    for i in range(len(marcas)):
        self.tablaMarca.insert(parent='', index=END, values=(f'{marcas[i]}'))
        
    self.MarcaScroll = CTkScrollbar(
                                    self.MarcoRegistroMarca,
                                    command=self.tablaMarca.yview,
                                    button_color=self.color_azulPrimario,
                                    button_hover_color=self.color_azulHover,
                                    height=240
                                )
    
    self.tablaMarca.configure(yscrollcommand=self.MarcaScroll.set)
    
    self.MarcaScroll.place(x=489, y=240)
    
    #Boton Guardar
    self.boton_guardar = CTkButton (
                        self.MarcoRegistroMarca,
                        bg_color = self.color_blancoPrimario,
                        width= 180,
                        height= 50,
                        fg_color= self.color_azulPrimario,
                        border_color= self.color_azulPrimario,
                        font= self.Fuente_MontserratBold,
                        text_color = self.color_blancoPrimario,
                        text="Guardar",
                        cursor="hand2",
                        corner_radius= 15,
                        hover_color= self.color_azulHover
    )


    #Boton Borrar
    self.boton_modificar = CTkButton (
                        self.MarcoRegistroMarca,
                        bg_color = self.color_blancoPrimario,
                        width= 180,
                        height= 50,
                        fg_color= self.color_azulSecundario,
                        border_color= self.color_azulSecundario,
                        font= self.Fuente_MontserratBold,
                        text_color = self.color_blancoPrimario,
                        text="Modificar",
                        cursor="hand2",
                        corner_radius= 15,
                        hover_color = self.color_azulHoverSecundario
    )
    
    #Boton Borrar
    self.boton_borrar = CTkButton (
                        self.MarcoRegistroMarca,
                        bg_color = self.color_blancoPrimario,
                        width= 180,
                        height= 50,
                        fg_color= self.color_rojoPrimario,
                        border_color= self.color_rojoPrimario,
                        font= self.Fuente_MontserratBold,
                        text_color = self.color_blancoPrimario,
                        text="Borrar",
                        cursor="hand2",
                        corner_radius= 15,
                        hover_color = self.color_rojoSecundario
    )

    
    self.Regresar_boton.place(x=30, y=-5)
    
    self.RegistroMarca.place(x=30, y=50)
    
    self.Marca_label.place(x=30, y=125)
    self.Marca_entry.place(x=30, y=155)
    
    self.marcoTabla_frame.place(x=30, y=240)
    
    self.boton_guardar.place( x = 750, y = 600)
    self.boton_modificar.place( x = 550, y = 600)
    self.boton_borrar.place( x = 350, y = 600)