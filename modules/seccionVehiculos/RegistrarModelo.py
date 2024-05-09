from customtkinter import *
from tkinter import ttk
from modules.CTkSelector.ctk_scrollable_dropdown import *
import modules.funcionesBasicas.funcionesBasicas as funci

marcas = ['Chevrolet', 'Mack', 'Ford', 'Encava', 'Toyota', 'Volvo']
Modelos = ['Express', 'Granite', 'Fiesta', 'DF400', '4Runner', 'XC90']

marco_RegistroModelo = []

widgetsEntry_Modelo = []

def RegistrarModelo(self, mostrar, ocultar):

    style = ttk.Style()
    style.theme_use('default')

    style.configure(
                'modelo.Treeview',
                background=self.color_blancoPrimario,
                fieldbackground=self.color_blancoPrimario,
                foreground='#000',
                font=self.Fuente_MontserratSemiBold_PlaceHolder,
                rowheight=50,
                relief=FLAT
                )

    style.configure(
                'modelo.Treeview.Heading',
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
    
    self.MarcoRegistroModelo = CTkFrame(
                                self,
                                height=670,
                                width=970,
                                fg_color=self.color_blancoPrimario,
                                corner_radius=0
                            )
    
    marco_RegistroModelo.append(self.MarcoRegistroModelo)
    
    self.Regresar_boton = CTkButton(
                                self.MarcoRegistroModelo,
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
    
    self.RegistroModelo = CTkLabel(
                                self.MarcoRegistroModelo,
                                text='Registro de Modelo',
                                text_color=self.color_azulPrimario,
                                width=700,
                                height=0,
                                font=self.Fuente_MontserratBold_Titulos,
                                anchor='w'
                            )
    
    self.Marca_label = CTkLabel(
                                self.MarcoRegistroModelo,
                                text='Marca',
                                text_color=self.color_azulPrimario,
                                width=300,
                                height=0,
                                font=self.Fuente_MontserratBold_Labels,
                                anchor='w'
                            )
    
    self.Marca_selector = CTkComboBox(
                                    self.MarcoRegistroModelo,
                                    width=210,
                                    height=47,
                                    font=self.Fuente_MontserratSemiBold_PlaceHolder,
                                    dropdown_font=self.Fuente_MontserratSemiBold_PlaceHolder,
                                    text_color='#000',
                                    border_color=self.color_azulPrimario,
                                    fg_color=self.color_blancoPrimario,
                                    button_color=self.color_azulPrimario,
                                    button_hover_color=self.color_azulHover,
                                    border_width=3,
                                    corner_radius=15,
                                    justify='center'
                                )
    
    widgetsEntry_Modelo.append(self.Marca_selector)

    CTkScrollableDropdown(
                            self.Marca_selector,
                            values=marcas,
                            autocomplete=True,
                            text_color=self.color_blancoPrimario,
                            arrow_color=self.color_blancoPrimario,
                            button_color=self.color_azulComboBox,
                            hover_color=self.color_azulPrimario,
                            text_noMatch='No Se Encuentra',
                            text_noMatch_color='#fff',
                            fg_color=self.color_azulComboBox,
                            font=self.Fuente_MontserratSemiBold_Options,
                            scrollbar_button_hover_color=self.color_azulComboBox,
                            scrollbar_button_color=self.color_azulComboBox,
                            frame_border_width=False,
                        )
    
    self.Modelo_label = CTkLabel(
                                self.MarcoRegistroModelo,
                                text='Modelo',
                                text_color=self.color_azulPrimario,
                                width=300,
                                height=0,
                                font=self.Fuente_MontserratBold_Labels,
                                anchor='w'
                            )
    
    self.Modelo_entry = CTkEntry(
                                self.MarcoRegistroModelo,
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

    widgetsEntry_Modelo.append(self.Modelo_entry)
    
    self.boton_guardar = CTkButton (
                        self.MarcoRegistroModelo,
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
                        self.MarcoRegistroModelo,
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
                        self.MarcoRegistroModelo,
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
                                self.MarcoRegistroModelo,
                                height=240,
                                width=459,
                                fg_color=self.color_blancoPrimario,
                            )
    
    self.tablaModelos = ttk.Treeview(
                                    self.marcoTabla_frame,
                                    columns=('marca', 'modelo'),
                                    show='headings',
                                    style='modelo.Treeview',
                                    )
    
    self.tablaModelos.column('marca', width=225, anchor='center')
    self.tablaModelos.column('modelo', width=225, anchor='center')
    
    self.tablaModelos.heading('marca', text='Marca')
    self.tablaModelos.heading('modelo', text='Modelo')
    self.tablaModelos.place(x=1, y=1, relwidth=1, relheight=1)
    
    for i in range(len(marcas)):
        self.tablaModelos.insert(parent='', index=END, values=(f'{marcas[i]}', f'{Modelos[i]}'))
        
    self.ModelScroll = CTkScrollbar(
                                    self.MarcoRegistroModelo,
                                    command=self.tablaModelos.yview,
                                    button_color=self.color_azulPrimario,
                                    button_hover_color=self.color_azulHover,
                                    height=240
                                )
    
    self.tablaModelos.configure(yscrollcommand=self.ModelScroll.set)
    
    self.ModelScroll.place(x=489, y=240)
    
    #Boton Guardar
    self.boton_guardar = CTkButton (
                        self.MarcoRegistroModelo,
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
                        self.MarcoRegistroModelo,
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
                        self.MarcoRegistroModelo,
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
    
    self.RegistroModelo.place(x=30, y=50)
    
    self.Marca_label.place(x=30, y=125)
    self.Marca_selector.place(x=30, y=155)
    
    self.Modelo_label.place(x=270, y=125)
    self.Modelo_entry.place(x=270, y=155)
    
    self.marcoTabla_frame.place(x=30, y=240)
    
    self.boton_guardar.place( x = 750, y = 600)
    self.boton_modificar.place( x = 550, y = 600)
    self.boton_borrar.place( x = 350, y = 600)