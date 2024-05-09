from customtkinter import *
from tkinter import ttk

marco_registro_servicio_particular = []

widgetsEntry_HistorialServicioParticular = []

def historial_servicio_particular(self):
    
    self.Marco_HistorialServicioParticular = CTkFrame(
                                self,
                                height=670,
                                width=970,
                                fg_color=self.color_blancoPrimario,
                                corner_radius=0
                            )
    
    marco_registro_servicio_particular.append(self.Marco_HistorialServicioParticular)
    
    #Titulo
    self.titulo = CTkLabel(
                            self.Marco_HistorialServicioParticular,
                            text='Historial Servicio Particular',
                            text_color= self.color_azulPrimario,
                            font=self.Fuente_MontserratBold_Titulos,
                        )
    self.titulo.place(x=30, y=25) 

    #titulo buscar
    self.label_buscar = CTkLabel(
                            self.Marco_HistorialServicioParticular,
                            text='Buscar',
                            text_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratBold_SubTitulos,
                        )

    self.label_buscar.place( x = 30, y = 100)

    #buscar
    self.entry_buscar = CTkEntry (
                                self.Marco_HistorialServicioParticular,
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
                                placeholder_text= "Buscar por Cédula"
    )

    self.entry_buscar.place( x = 150, y = 100)

    widgetsEntry_HistorialServicioParticular.append(self.entry_buscar)

    #marco treview

    self.marco = CTkFrame(
                           self.Marco_HistorialServicioParticular,
                            bg_color = self.color_blancoPrimario,
                            width= 910,
                            height= 440,
                            fg_color= self.color_blancoPrimario,
    )

    self.marco.place(x = 30 , y = 150)

    #Treeview
    self.marcoTreeview = ttk.Treeview(self.marco, columns= ("col2", "col3", "col4", "col5", "col6", "col7"), style= "marcoTreeview.Treeview")
    
    self.marcoTreeview.column("#0", width = 50)
    self.marcoTreeview.column("col2", width = 100, anchor='center')
    self.marcoTreeview.column("col3", width = 150, anchor='center')
    self.marcoTreeview.column("col4", width = 180, anchor='center')
    self.marcoTreeview.column("col5", width = 170, anchor='center')
    self.marcoTreeview.column("col6", width = 170, anchor='center')
    self.marcoTreeview.column("col7", width = 70, anchor='center')

    self.marcoTreeview.heading("#0", text = "ID")
    self.marcoTreeview.heading("col2", text = "FECHA", anchor='center')
    self.marcoTreeview.heading("col3", text = "TIPO", anchor='center')
    self.marcoTreeview.heading("col4", text = "CLIENTE", anchor='center')
    self.marcoTreeview.heading("col5", text = "ORIGEN", anchor='center')
    self.marcoTreeview.heading("col6", text = "DESTINO", anchor='center')
    self.marcoTreeview.heading("col7", text = "COSTO", anchor='center')

    self.marcoTreeview.configure(height = 15) # numero de columnas visibles
    self.marcoTreeview.place(x= 1, y = 1, relwidth=1, relheight=1)

    self.marcoTreeview.insert("", END , text = "1", values = ("19/04/2024", "Transporte de Personas", "Francisco de Miranda", "Táriba", "Barrio Obrero" , "15000"))
    self.marcoTreeview.insert("", END , text = "2", values = ("19/04/2024", "Transporte de Personas", "Simón Bolívar", "San Cristóbal", "El piñal" , "7000"))
    self.marcoTreeview.insert("", END , text = "3", values = ("19/04/2024", "Transporte de Carga", "Crisly Valentina Velasco Flores", "Maracaibo", "San Cristóbal" , "200000"))
    

    self.treeView_scrollBar = CTkScrollbar(
                                            self.Marco_HistorialServicioParticular,
                                            command=self.marcoTreeview.yview,
                                            button_color=self.color_azulPrimario,
                                            button_hover_color=self.color_azulHover,
                                            height=440
                                        )
    self.treeView_scrollBar.place(x=940, y=150)

    self.marcoTreeview.configure(yscrollcommand=self.treeView_scrollBar.set)

    style = ttk.Style()
    style.theme_use('default')

    style.configure(
                    'marcoTreeview.Treeview',
                    background=self.color_blancoPrimario,
                    fieldbackground=self.color_blancoPrimario,
                    foreground='#000',
                    font=self.Fuente_MontserratSemiBold,
                    rowheight=30,
                    relief=FLAT,
                )

    style.configure(
                    'marcoTreeview.Treeview.Heading',
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

    #boton ver mas
    self.boton_verMas = CTkButton (
                            self.Marco_HistorialServicioParticular,
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
                            hover_color= self.color_azulHover
        )

    self.boton_verMas.place( x = 760, y = 600)