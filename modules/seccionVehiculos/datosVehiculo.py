from customtkinter import *
import modules.funcionesBasicas.funcionesBasicas as funci
from modules.CTkMessageBox.ctkmessagebox import CTkMessagebox

marco_DatosVehiculo = []

widgetsLabel_DatosVehiculo = []

def datosVehiculo(self, mostrar, ocultar):
    
    self.MarcoDatosVehiculo = CTkFrame(
                                self,
                                height=670,
                                width=970,
                                fg_color=self.color_blancoPrimario,
                                corner_radius=0
                            )
    
    marco_DatosVehiculo.append(self.MarcoDatosVehiculo)
    
    self.Regresar_boton = CTkButton(
                        self.MarcoDatosVehiculo,
                        text='<',
                        width=0,
                        height=0,
                        fg_color='transparent',
                        hover=False,
                        font=CTkFont('Montserrat', weight='bold', size=46),
                        text_color=self.color_azulPrimario,
                        cursor='hand2',
                        command= lambda : funci.mostrarVistas(mostrar[0], ocultar)
                    )
    
    # Titulo
    self.DatosVehiculo_titulo = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Datos del Vehiculo',
                                    text_color= self.color_azulPrimario,
                                    font=self.Fuente_MontserratBold_Titulos,
                                )
    
    # Datos Labels
    self.VehiculoID_label = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='ID Vehiculo',
                                    text_color= self.color_azulPrimario,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    self.VehiculoID_data = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='ID',
                                    text_color= '#000',
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    widgetsLabel_DatosVehiculo.append(self.VehiculoID_data)
    
    
    self.Conductor_label = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Conductor',
                                    text_color= self.color_azulPrimario,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    self.Conductor_data = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Conductor',
                                    text_color= '#000',
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    widgetsLabel_DatosVehiculo.append(self.Conductor_data)
    
    self.Placa_label = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Placa',
                                    text_color= self.color_azulPrimario,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    self.Placa_data = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Placa',
                                    text_color= '#000',
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    widgetsLabel_DatosVehiculo.append(self.Placa_data)
    
    self.Marca_label = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Marca',
                                    text_color= self.color_azulPrimario,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    self.Marca_data = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Marca',
                                    text_color= '#000',
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    widgetsLabel_DatosVehiculo.append(self.Marca_data)
    
    self.Modelo_label = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Modelo',
                                    text_color= self.color_azulPrimario,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    self.Modelo_data = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Modelo',
                                    text_color= '#000',
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    widgetsLabel_DatosVehiculo.append(self.Modelo_data)
    
    self.Color_label = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Color',
                                    text_color= self.color_azulPrimario,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    self.Color_data = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Color',
                                    text_color= '#000',
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    widgetsLabel_DatosVehiculo.append(self.Color_data)

    self.Servicio_label = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Tipo de Servicio',
                                    text_color= self.color_azulPrimario,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    self.Servicio_data = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Tipo de Servicio',
                                    text_color= '#000',
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    widgetsLabel_DatosVehiculo.append(self.Servicio_data)

    self.capCarga_label = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Capacidad de Carga',
                                    text_color= self.color_azulPrimario,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    self.capCarga_data = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Capacidad de Carga',
                                    text_color= '#000',
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    widgetsLabel_DatosVehiculo.append(self.capCarga_data)

    self.capPersonas_label = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Capacidad de Personas',
                                    text_color= self.color_azulPrimario,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    self.capPersonas_data = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Capacidad de Personas',
                                    text_color= '#000',
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    widgetsLabel_DatosVehiculo.append(self.capPersonas_data)

    self.Disponible_label = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Disponible',
                                    text_color= self.color_azulPrimario,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    self.Disponible_data = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Disponible',
                                    text_color= '#000',
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    widgetsLabel_DatosVehiculo.append(self.Disponible_data)

    self.motivoDisponible_label = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Motivo de Disponible',
                                    text_color= self.color_azulPrimario,
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    self.motivoDisponible_data = CTkLabel(
                                    self.MarcoDatosVehiculo,
                                    text='Motivo de Disponible',
                                    text_color= '#000',
                                    font=self.Fuente_MontserratBold_Labels,
                                    anchor='center',
                                    width=260,
                                )
    
    widgetsLabel_DatosVehiculo.append(self.motivoDisponible_data)
    
    #Boton Guardar
    self.boton_Editar = CTkButton (
                    self.MarcoDatosVehiculo,
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
                    command= lambda : funci.mostrarVistas(mostrar[1], ocultar)
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
            funci.mostrarVistas(mostrar[0], ocultar)
            # Aca iria la consulta que eliminaria la fila con los
        else:
            print('No')
    
    #Boton Borrar
    self.boton_Eliminar = CTkButton (
                    self.MarcoDatosVehiculo,
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
    
    self.Regresar_boton.place(x=30, y=-5)
    
    self.DatosVehiculo_titulo.place(x=313, y=25)
    
    self.VehiculoID_label.place(x=150, y=110)
    self.VehiculoID_data.place(x=550, y=110)
    
    self.Conductor_label.place(x=150, y=150)
    self.Conductor_data.place(x=550, y=150)
    
    self.Placa_label.place(x=150, y=190)
    self.Placa_data.place(x=550, y=190)
    
    self.Marca_label.place(x=150, y=230)
    self.Marca_data.place(x=550, y=230)
    
    self.Modelo_label.place(x=150, y=270)
    self.Modelo_data.place(x=550, y=270)
    
    self.Color_label.place(x=150, y=310)
    self.Color_data.place(x=550, y=310)
    
    self.Servicio_label.place(x=150, y=350)
    self.Servicio_data.place(x=550, y=350)
    
    self.capCarga_label.place(x=150, y=390)
    self.capCarga_data.place(x=550, y=390)
    
    self.capPersonas_label.place(x=150, y=430)
    self.capPersonas_data.place(x=550, y=430)
    
    self.Disponible_label.place(x=150, y=470)
    self.Disponible_data.place(x=550, y=470)
    
    self.motivoDisponible_label.place(x=150, y=510)   
    self.motivoDisponible_data.place(x=550, y=510)
    
    self.boton_Editar.place(x=295, y=600)     
    self.boton_Eliminar.place(x=495, y=600)  