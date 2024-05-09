from customtkinter import *
from tkinter import ttk
import modules.funcionesBasicas.funcionesBasicas as funci

marco_ListaVehiculo = []

widgetsEntry_ListaVehiculo = []

def ListaVehiculo(self, mostrar, ocultar):
    
    style = ttk.Style()
    style.theme_use('default')

    style.configure(
                    'ListaVehiculo.Treeview',
                    background=self.color_blancoPrimario,
                    fieldbackground=self.color_blancoPrimario,
                    foreground='#000',
                    font=self.Fuente_MontserratSemiBold,
                    rowheight=30,
                    relief=FLAT,
                )

    style.configure(
                    'ListaVehiculo.Treeview.Heading',
                    background=self.color_azulPrimario,
                    fieldbackground=self.color_azulPrimario,
                    foreground=self.color_blancoPrimario,
                    font=self.Fuente_MontserratBoldTreeView,
                    relief=FLAT,
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
    
    self.MarcoListaVehiculo = CTkFrame(
                                self,
                                height=670,
                                width=970,
                                fg_color=self.color_blancoPrimario,
                                corner_radius=0
                            )
    
    marco_ListaVehiculo.append(self.MarcoListaVehiculo)
    
    #Titulo de Lista Vehiculo
    self.ListaVehiculo_titulo = CTkLabel(
                            self.MarcoListaVehiculo,
                            text='Lista de Vehiculos',
                            text_color= self.color_azulPrimario,
                            font=self.Fuente_MontserratBold_Titulos,
                        )
    
    # Buscar Label
    self.Buscar_label = CTkLabel(
                            self.MarcoListaVehiculo,
                            text='Buscar',
                            text_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratBold_SubTitulos,
                        )

    # Buscar Input
    self.Buscar_entry = CTkEntry (
                                self.MarcoListaVehiculo,
                                bg_color = self.color_blancoPrimario,
                                width= 200,
                                height= 47,
                                fg_color= self.color_blancoPrimario,
                                border_color= self.color_azulPrimario,
                                font= self.Fuente_MontserratSemiBold_PlaceHolder,
                                text_color = 'black',
                                corner_radius= 15,
                                justify = "center",
                                border_width=3,
                                placeholder_text= "Buscar por Placa"
    )

    widgetsEntry_ListaVehiculo.append(self.Buscar_entry)

    # Frame de la Lista

    self.Lista_frame = CTkFrame(
                           self.MarcoListaVehiculo,
                            bg_color = self.color_blancoPrimario,
                            width= 910,
                            height= 440,
                            fg_color= self.color_blancoPrimario,
    )

    #Lista
    self.ListaVehiculo = ttk.Treeview(
                                self.Lista_frame,
                                columns= ("idVehiculo", "placa", "modelo", "color", "tipoServicio", "disponible"),
                                show='headings',
                                style= "ListaVehiculo.Treeview"
                                )
    
    self.ListaVehiculo.column("idVehiculo", width = 50, anchor='center')
    self.ListaVehiculo.column("placa", width = 150, anchor='center')
    self.ListaVehiculo.column("modelo", width = 235, anchor='center')
    self.ListaVehiculo.column("color", width = 235, anchor='center')
    self.ListaVehiculo.column("tipoServicio", width = 120, anchor='center')
    self.ListaVehiculo.column("disponible", width = 120, anchor='center')

    self.ListaVehiculo.heading("idVehiculo", text = "ID")
    self.ListaVehiculo.heading("placa", text = "Placa")
    self.ListaVehiculo.heading("modelo", text = "Modelo")
    self.ListaVehiculo.heading("color", text = "Color")
    self.ListaVehiculo.heading("tipoServicio", text = "Tipo Servicio")
    self.ListaVehiculo.heading("disponible", text = "Disponible")

    for i in range(1, 20):
        self.ListaVehiculo.insert(parent='', index=END, values=(f'{i}', f'A{i}B{i}3Z{i}', f'Chevrolet Aveo{i}', f'Azul Azulado{i}', f'Servico {i}', f'{i}'))
    

    self.vehiculoScroll = CTkScrollbar(
                                            self.MarcoListaVehiculo,
                                            command=self.ListaVehiculo.yview,
                                            button_color=self.color_azulPrimario,
                                            button_hover_color=self.color_azulHover,
                                            height=440
                                        )

    self.ListaVehiculo.configure(yscrollcommand=self.vehiculoScroll.set)



    # Boton Ver Más
    self.VerMas_boton = CTkButton (
                            self.MarcoListaVehiculo,
                            bg_color = self.color_blancoPrimario,
                            width= 180,
                            height= 50,
                            fg_color= self.color_azulPrimario,
                            border_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratBold,
                            text_color = self.color_blancoPrimario,
                            text="Ver más",
                            cursor="hand2",
                            corner_radius= 15,
                            hover_color= self.color_azulHover,
                            command= lambda : funci.mostrarVistas(mostrar, ocultar)
        )
    
    self.ListaVehiculo_titulo.place(x=30, y=25)
    
    self.Buscar_label.place( x = 30, y = 100)
    self.Buscar_entry.place( x = 150, y = 100)
    
    self.Lista_frame.place(x = 30 , y = 150)
    self.ListaVehiculo.place(x= 1, y = 1, relwidth=1, relheight=1)
    self.vehiculoScroll.place(x=940, y=150)
    
    self.VerMas_boton.place( x = 760, y = 600)