from customtkinter import *
from tkinter import ttk
import modules.funcionesBasicas.funcionesBasicas as funci
from modules.CTkMessageBox.ctkmessagebox import CTkMessagebox

marco_ListaConductor = []

widgetsEntry_ListaConductor = []

def ListaConductor(self, mostrar, ocultar, EntryActualizarDatos=[]):
    
    style = ttk.Style()
    style.theme_use('default')

    style.configure(
                    'ListaConductor.Treeview',
                    background=self.color_blancoPrimario,
                    fieldbackground=self.color_blancoPrimario,
                    foreground='#000',
                    font=self.Fuente_MontserratSemiBold,
                    rowheight=30,
                    relief=FLAT,
                )

    style.configure(
                    'ListaConductor.Treeview.Heading',
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
    
    self.MarcoListaConductor = CTkFrame(
                                self,
                                height=670,
                                width=970,
                                fg_color=self.color_blancoPrimario,
                                corner_radius=0
                            )
    
    marco_ListaConductor.append(self.MarcoListaConductor)
    
    #Titulo de Lista de Conductores
    self.ListaConductor_titulo = CTkLabel(
                            self.MarcoListaConductor,
                            text='Lista de Conductores',
                            text_color= self.color_azulPrimario,
                            font=self.Fuente_MontserratBold_Titulos,
                        )
    
    # Buscar Label
    self.Buscar_label = CTkLabel(
                            self.MarcoListaConductor,
                            text='Buscar',
                            text_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratBold_SubTitulos,
                        )

    # Buscar Input
    self.Buscar_entry = CTkEntry (
                                self.MarcoListaConductor,
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

    widgetsEntry_ListaConductor.append(self.Buscar_entry)

    # Frame de la Lista

    self.Lista_frame = CTkFrame(
                           self.MarcoListaConductor,
                            bg_color = self.color_blancoPrimario,
                            width= 910,
                            height= 440,
                            fg_color= self.color_blancoPrimario,
    )

    # Tabla
    self.ListaConductor = ttk.Treeview(
                                self.Lista_frame,
                                columns= ("idConductor", "nombreapellido", "cedula", "telefono", "edad", "licencia"),
                                show='headings',
                                style= "ListaConductor.Treeview"
                                )
    
    self.ListaConductor.column("idConductor", width = 50, anchor='center')
    self.ListaConductor.column("nombreapellido", width = 300, anchor='center')
    self.ListaConductor.column("cedula", width = 150, anchor='center')
    self.ListaConductor.column("telefono", width = 170, anchor='center')
    self.ListaConductor.column("edad", width = 120, anchor='center')
    self.ListaConductor.column("licencia", width = 120, anchor='center')

    self.ListaConductor.heading("idConductor", text = "ID")
    self.ListaConductor.heading("nombreapellido", text = "Nombres y Apellidos")
    self.ListaConductor.heading("cedula", text = "Cedula")
    self.ListaConductor.heading("telefono", text = "Telefono")
    self.ListaConductor.heading("edad", text = "Edad")
    self.ListaConductor.heading("licencia", text = "Licencia")

    for i in range(1, 20):
        self.ListaConductor.insert(parent='', index=END, values=(f'{i}', f'Francisco Pablo Miranda Hernadez', f'{(i+3) * 5212341}', f'0412-{(i+2) * 2132112}', f'Servico {i}', f'{i}'))
    

    self.vehiculoScroll = CTkScrollbar(
                                            self.MarcoListaConductor,
                                            command=self.ListaConductor.yview,
                                            button_color=self.color_azulPrimario,
                                            button_hover_color=self.color_azulHover,
                                            height=440
                                        )

    self.ListaConductor.configure(yscrollcommand=self.vehiculoScroll.set)



    #Boton Guardar
    self.Boton_Editar = CTkButton (
                    self.MarcoListaConductor,
                    bg_color = self.color_blancoPrimario,
                    width= 180,
                    height= 50,
                    fg_color= self.color_azulPrimario,
                    border_color= self.color_azulPrimario,
                    font= self.Fuente_MontserratBold,
                    text_color = self.color_blancoPrimario,
                    corner_radius=15,
                    hover_color=self.color_azulHover,
                    text="Editar",
                    cursor="hand2",
                    command= lambda : funci.mostrarVistas(mostrar, ocultar, EntryActualizarDatos)
    )
    
    def EliminarDatos():
        
        msg = CTkMessagebox(
                            title='Datos',
                            message='¿Estas seguro que quieres Eliminar estos datos?',
                            icon="warning",
                            option_1="No",
                            option_2="Si",
                            font=self.Fuente_MontserratSemiBold_Options,
                            fg_color=self.color_blancoPrimario,
                            bg_color=self.color_azulPrimario,
                            button_color=self.color_azulSecundario,
                            button_hover_color=self.color_azulHoverSecundario,
                            border_width=0,
                            text_color='#000',
                            title_color=self.color_blancoPrimario
                        )
        
        response = msg.get()
    
        if response=="Si":
            print('Se Eliminaria Los Datos del Conductor')
            # Aca iria la consulta que eliminaria la fila con los
        else:
            print('No')
    
       
    #Boton Borrar
    self.Boton_Eliminar = CTkButton (
                    self.MarcoListaConductor,
                    bg_color = self.color_blancoPrimario,
                    width= 180,
                    height= 50,
                    fg_color= self.color_rojoPrimario,
                    border_color= self.color_rojoPrimario,
                    font= self.Fuente_MontserratBold,
                    text_color = self.color_blancoPrimario,
                    corner_radius=15,
                    hover_color=self.color_rojoSecundario,
                    text="Eliminar",
                    cursor="hand2",
                    command=EliminarDatos
    )
    
    
    
    self.ListaConductor_titulo.place(x=30, y=25)
    
    self.Buscar_label.place( x = 30, y = 100)
    self.Buscar_entry.place( x = 150, y = 100)
    
    self.Lista_frame.place(x = 30 , y = 150)
    self.ListaConductor.place(x= 1, y = 1, relwidth=1, relheight=1)
    self.vehiculoScroll.place(x=940, y=150)
    
    self.Boton_Editar.place(x=760, y=600) 
    self.Boton_Eliminar.place(x=550, y=600)