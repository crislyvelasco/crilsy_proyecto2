from customtkinter import *
from modules.CTkSelector.ctk_scrollable_dropdown import *

marco_RegistroServicioParticular = []

widgetsEntry_RegistroServicioParticular = []

def RegistarServicioParticular(self):
    
        self.MarcoRegistroServicioParticular = CTkFrame(
                                self,
                                height=670,
                                width=970,
                                fg_color=self.color_blancoPrimario,
                                corner_radius=0
                            )
        
        marco_RegistroServicioParticular.append(self.MarcoRegistroServicioParticular)
    
        #Titulo
        self.titulo = CTkLabel(
                            self.MarcoRegistroServicioParticular,
                            text='Registrar Servicio Particular',
                            text_color= self.color_azulPrimario,
                            font=self.Fuente_MontserratBold_Titulos,
                        )
        
        self.titulo.place(x=30, y=25)  
        
        #Cliente
        self.label_cliente = CTkLabel(
                            self.MarcoRegistroServicioParticular,
                            text='Cliente',
                            text_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratBold_Labels,
                        )

        self.label_cliente.place( x = 30, y = 100)

        self.comboboxCliente = CTkComboBox(self.MarcoRegistroServicioParticular,
                                    width=480,
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
                                    justify='center')
        
        widgetsEntry_RegistroServicioParticular.append(self.comboboxCliente)

        CTkScrollableDropdown(
                            self.comboboxCliente,
                            values = [ "Luis Jose Lopez Ramirez", "Crisly Valentina Velasco Flores", "Francisco Pablo de Miranda"],
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
        

        self.comboboxCliente.place( x = 30, y = 130)

        #Servicio
        self.label_servicio = CTkLabel(
                            self.MarcoRegistroServicioParticular,
                            text='Servicio',
                            text_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratBold_Labels,
                        )

        self.label_servicio.place( x = 530, y = 100)

        self.comboboxServicio = CTkComboBox(self.MarcoRegistroServicioParticular,
                                    width=270,
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
                                    justify='center')

        widgetsEntry_RegistroServicioParticular.append(self.comboboxServicio)                            

        CTkScrollableDropdown(
                            self.comboboxServicio,
                            values = [ "Traslado de Pasajeros", "Traslado de Carga"],
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

        self.comboboxServicio.place( x = 530, y = 130)
        
        #Vehiculo
        self.label_vehiculo = CTkLabel(
                            self.MarcoRegistroServicioParticular,
                            text='Vehículo',
                            text_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratBold_Labels,
                        )

        self.label_vehiculo.place( x = 30, y = 200)
        
        self.comboboxVehiculo = CTkComboBox(self.MarcoRegistroServicioParticular,
                                    width=380,
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
                                    justify='center')
        
        widgetsEntry_RegistroServicioParticular.append(self.comboboxVehiculo)

        CTkScrollableDropdown(
                            self.comboboxVehiculo,
                            values = [ "Chevrolet - Spark - AA508BH", "Chevrolet - Optra - AA145AG"],
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

        self.comboboxVehiculo.place( x = 30, y = 230)

        self.label_fecha = CTkLabel(
                            self.MarcoRegistroServicioParticular,
                            text='Fecha',
                            text_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratBold_Labels,
                        )

        self.label_fecha.place( x = 430, y = 200)

        self.entry_fecha = CTkEntry (
                            self.MarcoRegistroServicioParticular,
                            bg_color = self.color_blancoPrimario,
                            width= 180,
                            height= 47,
                            fg_color= self.color_blancoPrimario,
                            border_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratSemiBold_PlaceHolder,
                            text_color = 'black',
                            corner_radius= 15,
                            justify = "center",
                            border_width=3

        )

        self.entry_fecha.place( x = 425, y = 230)
        widgetsEntry_RegistroServicioParticular.append(self.entry_fecha)

        self.label_hora = CTkLabel(
                            self.MarcoRegistroServicioParticular,
                            text='Hora',
                            text_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratBold_Labels,
                        )

        self.label_hora.place( x = 620, y = 200)

        self.entry_hora = CTkEntry (
                            self.MarcoRegistroServicioParticular,
                            bg_color = self.color_blancoPrimario,
                            width= 180,
                            height= 47,
                            fg_color= self.color_blancoPrimario,
                            border_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratSemiBold_PlaceHolder,
                            text_color = 'black',
                            corner_radius= 15,
                            justify = "center",
                            border_width=3
        )

        self.entry_hora.place( x = 620, y = 230)
        widgetsEntry_RegistroServicioParticular.append(self.entry_hora)

        self.label_lugarOrigen = CTkLabel(
                            self.MarcoRegistroServicioParticular,
                            text='Lugar de Origen',
                            text_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratBold_Labels,
                        )

        self.label_lugarOrigen.place( x = 30, y = 300)
        
        self.entry_lugarOrigen = CTkEntry (
                            self.MarcoRegistroServicioParticular,
                            bg_color = self.color_blancoPrimario,
                            width= 770,
                            height= 47,
                            fg_color= self.color_blancoPrimario,
                            border_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratSemiBold_PlaceHolder,
                            text_color = 'black',
                            corner_radius= 15,
                            justify = "center",
                            border_width=3
        )

        self.entry_lugarOrigen.place( x = 30, y = 330)
        widgetsEntry_RegistroServicioParticular.append(self.entry_lugarOrigen)

        self.label_lugarDestino = CTkLabel(
                            self.MarcoRegistroServicioParticular,
                            text='Lugar de Destino',
                            text_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratBold_Labels,
                        )

        self.label_lugarDestino.place( x = 30, y = 400)

        self.entry_lugarDestino = CTkEntry (
                            self.MarcoRegistroServicioParticular,
                            bg_color = self.color_blancoPrimario,
                            width= 770,
                            height= 47,
                            fg_color= self.color_blancoPrimario,
                            border_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratSemiBold_PlaceHolder,
                            text_color = 'black',
                            corner_radius= 15,
                            justify = "center",
                            border_width=3
        )

        self.entry_lugarDestino.place( x = 30, y = 430)
        widgetsEntry_RegistroServicioParticular.append(self.entry_lugarDestino)

        self.label_costo = CTkLabel(
                            self.MarcoRegistroServicioParticular,
                            text='Costo',
                            text_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratBold_Labels,
                        )

        self.label_costo.place( x = 30, y = 500)

        self.entry_costo = CTkEntry (
                            self.MarcoRegistroServicioParticular,
                            bg_color = self.color_blancoPrimario,
                            width= 250,
                            height= 47,
                            fg_color= self.color_blancoPrimario,
                            border_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratSemiBold_PlaceHolder,
                            text_color = 'black',
                            corner_radius= 15,
                            justify = "center",
                            border_width=3
        )

        self.entry_costo.place( x = 30, y = 530)
        widgetsEntry_RegistroServicioParticular.append(self.entry_costo)

        self.label_métodoPago = CTkLabel(
                            self.MarcoRegistroServicioParticular,
                            text='Método de Pago',
                            text_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratBold_Labels,
                        )

        #Metodo de Pago
        self.label_métodoPago.place( x = 310, y = 500)

        self.comboboxMetodoPago = CTkComboBox(self.MarcoRegistroServicioParticular,
                                    width=200,
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
                                    justify='center')
        
        widgetsEntry_RegistroServicioParticular.append(self.comboboxMetodoPago)

        CTkScrollableDropdown(
                            self.comboboxMetodoPago,
                            values = [ "Efectivo", "Transferencia", "Pago Móvil"],
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

        self.comboboxMetodoPago.place( x = 310, y = 530)

        #Divisa
        self.label_divisa = CTkLabel(
                            self.MarcoRegistroServicioParticular,
                            text='Divisa',
                            text_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratBold_Labels,
                        )

        self.label_divisa.place( x = 550, y = 500)

        self.comboboxDivisa = CTkComboBox(self.MarcoRegistroServicioParticular,
                                    width=250,
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
                                    justify='center')
        
        widgetsEntry_RegistroServicioParticular.append(self.comboboxDivisa)

        CTkScrollableDropdown(
                            self.comboboxDivisa,
                            values = [ "Bolívares", "Pesos Colombianos", "Dólares"],
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

        self.comboboxDivisa.place( x = 550, y = 530)

        #Boton Guardar
        self.boton_guardar = CTkButton (
                            self.MarcoRegistroServicioParticular,
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

        self.boton_guardar.place( x = 750, y = 600)

        #Boton Borrar
        self.boton_borrar = CTkButton (
                            self.MarcoRegistroServicioParticular,
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
                            hover_color = "red"
        )

        self.boton_borrar.place( x = 550, y = 600)