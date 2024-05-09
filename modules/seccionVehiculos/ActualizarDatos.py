from customtkinter import *
from ..CTkSelector.ctk_scrollable_dropdown import *
import modules.funcionesBasicas.funcionesBasicas as funci
from modules.CTkMessageBox.ctkmessagebox import CTkMessagebox

marcas = ['Chevrolet', 'Mack', 'Ford', 'Encava', 'Toyota', 'Volvo']

marco_ActualizarDatos = []

widgetsEntry_ListaConductor = []

def ActualizarDatos(self, mostrar, ocultar):
    
    self.MarcoActualizarDatos = CTkFrame(
                                self,
                                height=670,
                                width=970,
                                fg_color=self.color_blancoPrimario,
                                corner_radius=0
                            )
    
    marco_ActualizarDatos.append(self.MarcoActualizarDatos)
    
    #Titulo Principal
    self.ConductorVehiculo_label = CTkLabel(
                                    self.MarcoActualizarDatos,
                                    text='Actualizar Datos de Conductor y Vehiculo',
                                    text_color=self.color_azulPrimario,
                                    width=700,
                                    height=0,
                                    font=self.Fuente_MontserratBold_Titulos,
                                    anchor='w'
                                )
    
    #SubTitulo Datos Conductor
    self.DatosConductor_label = CTkLabel(
                                    self.MarcoActualizarDatos,
                                    text='Datos Conductor',
                                    text_color=self.color_azulPrimario,
                                    width=300,
                                    height=0,
                                    font=self.Fuente_MontserratBold_SubTitulos,
                                    anchor='w'
                                )
    
    #Label Nombres y Apellidos Conductor
    self.NombresApellidos_label = CTkLabel(
                                    self.MarcoActualizarDatos,
                                    text='Nombres y Apellidos',
                                    text_color=self.color_azulPrimario,
                                    height=0,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='w'
                                )
    #Entry Nombre y Apellidos Conductor
    self.NombresApellidos_entry = CTkEntry(
                                    self.MarcoActualizarDatos,
                                    width=370,
                                    height=47,
                                    font=self.Fuente_MontserratSemiBold_PlaceHolder,
                                    fg_color='transparent',
                                    text_color='#000',
                                    border_color=self.color_azulPrimario,
                                    border_width=3,
                                    corner_radius=15
                                )
    
    widgetsEntry_ListaConductor.append(self.NombresApellidos_entry)
    
    
    #Label Cedula Conductor
    self.Cedula_label = CTkLabel(
                                    self.MarcoActualizarDatos,
                                    text='Cedula',
                                    text_color=self.color_azulPrimario,
                                    height=0,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='w'
                                )
    #Entry Cedula Conductor
    self.Cedula_entry = CTkEntry(
                                    self.MarcoActualizarDatos,
                                    width=162,
                                    height=47,
                                    font=self.Fuente_MontserratSemiBold_PlaceHolder,
                                    fg_color='transparent',
                                    text_color='#000',
                                    border_color=self.color_azulPrimario,
                                    border_width=3,
                                    corner_radius=15,
                                    justify='center'
                                )
    
    widgetsEntry_ListaConductor.append(self.Cedula_entry)
    
    #Label Telefono Conductor
    self.Telefono_label = CTkLabel(
                                    self.MarcoActualizarDatos,
                                    text='Telefono',
                                    text_color=self.color_azulPrimario,
                                    height=0,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='w'
                                )
    #Entry Telefono Conductor
    self.Telefono_entry = CTkEntry(
                                    self.MarcoActualizarDatos,
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
    
    widgetsEntry_ListaConductor.append(self.Telefono_entry)
    
    #Label Fecha de Nacimiento Conductor
    self.FechaNacimiento_label = CTkLabel(
                                    self.MarcoActualizarDatos,
                                    text='Fecha de Nacimiento',
                                    text_color=self.color_azulPrimario,
                                    height=0,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='w'
                                )
    #Entry Fecha de Nacimiento Conductor
    self.FechaNacimiento_entry = CTkEntry(
                                    self.MarcoActualizarDatos,
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
    
    widgetsEntry_ListaConductor.append(self.FechaNacimiento_entry)
    
    #Label Licencia Conductor
    self.Licencia_label = CTkLabel(
                                    self.MarcoActualizarDatos,
                                    text='Licencia',
                                    text_color=self.color_azulPrimario,
                                    height=0,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='w'
                                )
    #selector Licencia Conductor
    self.Licencia_selector = CTkComboBox(
                                    self.MarcoActualizarDatos,
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
    
    widgetsEntry_ListaConductor.append(self.Licencia_selector)
    
    CTkScrollableDropdown(
                            self.Licencia_selector,
                            values=['Tercera', 'Cuarta', 'Quinta'],
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
    
    #SubTitulo Datos Vehiculo
    self.DatosVehiculo_label = CTkLabel(
                                    self.MarcoActualizarDatos,
                                    text='Datos Vehículo',
                                    text_color=self.color_azulPrimario,
                                    width=300,
                                    height=0,
                                    font=self.Fuente_MontserratBold_SubTitulos,
                                    anchor='w'
                                )
    
    #Label Marca Vehiculo
    self.Marca_label = CTkLabel(
                                    self.MarcoActualizarDatos,
                                    text='Marca',
                                    text_color=self.color_azulPrimario,
                                    height=0,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='w'
                                )
    
    #Selector Marca Vehiculo
    self.Marca_selector = CTkComboBox(
                                    self.MarcoActualizarDatos,
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
    
    widgetsEntry_ListaConductor.append(self.Marca_selector)

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
                        ).cambiarVista('Nueva Marca', self.color_blancoPrimario, self.Fuente_MontserratSemiBold_Options, mostrar[0], ocultar)
    
    #Label Modelo Vehiculo
    self.Modelo_label = CTkLabel(
                                    self.MarcoActualizarDatos,
                                    text='Modelo',
                                    text_color=self.color_azulPrimario,
                                    height=0,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='w'
                                )
    
    #Selector Modelo Vehiculo
    self.Modelo_selector = CTkComboBox(
                                    self.MarcoActualizarDatos,
                                    width=292,
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
    
    widgetsEntry_ListaConductor.append(self.Modelo_selector)
    
    CTkScrollableDropdown(
                            self.Modelo_selector,
                            values=['Chevrolet Express', 'Ford Super Duty', 'Mack Granite'],
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
                        ).cambiarVista('Nuevo Modelo', self.color_blancoPrimario, self.Fuente_MontserratSemiBold_Options, mostrar[1], ocultar)
    
    #Label Tipo Servicio Vehiculo
    self.Servicio_label = CTkLabel(
                                    self.MarcoActualizarDatos,
                                    text='Tipo de Servicio',
                                    text_color=self.color_azulPrimario,
                                    height=0,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='w'
                                )
    
    #Selector Tipo Servicio Vehiculo
    self.Servicio_selector = CTkComboBox(
                                    self.MarcoActualizarDatos,
                                    width=292,
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
    
    widgetsEntry_ListaConductor.append(self.Servicio_selector)
    
    CTkScrollableDropdown(
                            self.Servicio_selector,
                            values=['Transporte de Carga', 'Transporte de Pasajeros'],
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
    
    #Label Placa Vehiculo
    self.Placa_label = CTkLabel(
                                    self.MarcoActualizarDatos,
                                    text='Placa',
                                    text_color=self.color_azulPrimario,
                                    height=0,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='w'
                                )
    #Entry Placa Vehiculo
    self.Placa_entry = CTkEntry(
                                    self.MarcoActualizarDatos,
                                    width=162,
                                    height=47,
                                    font=self.Fuente_MontserratSemiBold_PlaceHolder,
                                    fg_color='transparent',
                                    text_color='#000',
                                    border_color=self.color_azulPrimario,
                                    border_width=3,
                                    corner_radius=15,
                                    justify='center'
                                )
    
    widgetsEntry_ListaConductor.append(self.Placa_entry)
    
    #Label Color Vehiculo
    self.Color_label = CTkLabel(
                                    self.MarcoActualizarDatos,
                                    text='Color',
                                    text_color=self.color_azulPrimario,
                                    height=0,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='w'
                                )
    
    #Entry Color Vehiculo
    self.Color_entry = CTkEntry(
                                    self.MarcoActualizarDatos,
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
    
    widgetsEntry_ListaConductor.append(self.Color_entry)
    
    #Label Capacidad de Carga Vehiculo
    self.CapacidadCarga_label = CTkLabel(
                                    self.MarcoActualizarDatos,
                                    text='Carga',
                                    text_color=self.color_azulPrimario,
                                    height=0,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='w'
                                )
    
    #Entry Capacidad de Carga Vehiculo
    self.CapacidadCarga_entry = CTkEntry(
                                    self.MarcoActualizarDatos,
                                    width=162,
                                    height=47,
                                    font=self.Fuente_MontserratSemiBold_PlaceHolder,
                                    fg_color='transparent',
                                    text_color='#000',
                                    border_color=self.color_azulPrimario,
                                    border_width=3,
                                    corner_radius=15,
                                    justify='center'
                                )
    
    widgetsEntry_ListaConductor.append(self.CapacidadCarga_entry)
    
    #Label Capacidad de Personas Vehiculo
    self.CapacidadPersonas_label = CTkLabel(
                                    self.MarcoActualizarDatos,
                                    text='Personas',
                                    text_color=self.color_azulPrimario,
                                    height=0,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='w'
                                )
    
    #Entry Capacidad de Personas Vehiculo
    self.CapacidadPersonas_entry = CTkEntry(
                                    self.MarcoActualizarDatos,
                                    width=162,
                                    height=47,
                                    font=self.Fuente_MontserratSemiBold_PlaceHolder,
                                    fg_color='transparent',
                                    text_color='#000',
                                    border_color=self.color_azulPrimario,
                                    border_width=3,
                                    corner_radius=15,
                                    justify='center'
                                )
    
    widgetsEntry_ListaConductor.append(self.CapacidadPersonas_entry)
    
    def ActualizarDatos():
        
        msg = CTkMessagebox(
                            title='Datos',
                            message='¿Actualizarás los Datos?',
                            icon="info",
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
            funci.mostrarVistas(mostrar[2], ocultar)
            # Aca va la consulta que Actualizara la fila con los datos
        else:
            print('No')
    
    self.boton_guardar = CTkButton (
                        self.MarcoActualizarDatos,
                        bg_color = self.color_blancoPrimario,
                        width= 180,
                        height= 50,
                        fg_color= self.color_azulPrimario,
                        border_color= self.color_azulPrimario,
                        font= self.Fuente_MontserratBold,
                        text_color = self.color_blancoPrimario,
                        corner_radius=15,
                        hover_color=self.color_azulHover,
                        text="Actualizar",
                        cursor="hand2",
                        command=ActualizarDatos
    )
    
    #Boton Cancelar
    self.Boton_Cancelar = CTkButton (
                    self.MarcoActualizarDatos,
                    bg_color = self.color_blancoPrimario,
                    width= 180,
                    height= 50,
                    fg_color= self.color_rojoPrimario,
                    border_color= self.color_rojoPrimario,
                    font= self.Fuente_MontserratBold,
                    text_color = self.color_blancoPrimario,
                    corner_radius=15,
                    hover_color=self.color_rojoSecundario,
                    text="Cancelar",
                    cursor="hand2",
                    command= lambda : funci.mostrarVistas(mostrar[2], ocultar)
    )
    
    
    self.ConductorVehiculo_label.place(x=30, y=25)
    
    
    self.DatosConductor_label.place(x=30, y=90)
    
    self.NombresApellidos_label.place(x=30, y=140)
    self.NombresApellidos_entry.place(x=30, y=170)
    
    self.Cedula_label.place(x=445, y=140)
    self.Cedula_entry.place(x=445, y=170)
    
    self.Telefono_label.place(x=652, y=140)
    self.Telefono_entry.place(x=652, y=170) #862
    
    self.FechaNacimiento_label.place(x=30, y=240)
    self.FechaNacimiento_entry.place(x=30, y=270)
    
    self.Licencia_label.place(x=290, y=240)
    self.Licencia_selector.place(x=290, y=270)
    
    
    self.DatosVehiculo_label.place(x=30, y=335)

    self.Marca_label.place(x=30, y=385)
    self.Marca_selector.place(x=30, y=415)

    self.Modelo_label.place(x=260, y=385)
    self.Modelo_selector.place(x=260, y=415)
    
    self.Servicio_label.place(x=570, y=385)
    self.Servicio_selector.place(x=570, y=415)
    
    self.Placa_label.place(x=30, y=485)
    self.Placa_entry.place(x=30, y=515)
    
    self.Color_label.place(x=227, y=485)
    self.Color_entry.place(x=227, y=515)
    
    self.CapacidadCarga_label.place(x=472, y=485)
    self.CapacidadCarga_entry.place(x=472, y=515)
    
    self.CapacidadPersonas_label.place(x=669, y=485)
    self.CapacidadPersonas_entry.place(x=669, y=515)
    
    self.boton_guardar.place(x=750, y=600)
    self.Boton_Cancelar.place(x=550, y=600)  