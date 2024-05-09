from customtkinter import *
from ..routes.routes import imagenes as ruta
from modules.funcionesBasicas.importaciones import *

ocultarMarcos = [vehiculo.marco_RegistroVehiculo, servicioParticular.marco_RegistroServicioParticular, inicio.marco_WidgetsInicio, clienteEmpresa.marco_RegistroEmpresa, clienteParticular.marco_RegistroParticular, marca.marco_RegistroMarca, modelo.marco_RegistroModelo, h_servicioParticular.marco_registro_servicio_particular, ListaVehiculo.marco_ListaVehiculo, ListaConductor.marco_ListaConductor, DatosVehiculo.marco_DatosVehiculo, ActualizarDatos.marco_ActualizarDatos]
# ACA SE CREAN LOS WIDGETS DE LAS OPCIONES QUE SALEN ENEL MENU
def WidgetsMenu(self):
    
    # | ~ Widgets Menu ~ |
    
    self.LogoServiExpress_image = CTkLabel(
                                self.PanelMenu,
                                corner_radius=0,
                                text='',
                                image=CTkImage(ruta['logoServiExpress'], size=(166, 76))
                            )
        
    self.ClienteLabel = CTkLabel(
                                    self.PanelMenu,
                                    width=220,
                                    height=30,
                                    text='Cliente',
                                    font=self.Fuente_MontserratBold,
                                    fg_color=self.color_azulSecundario,
                                    text_color=self.color_blancoPrimario,
                                    corner_radius=20,
                                    anchor="w"
                                )
    
    self.RegistroParticular_Boton = CTkButton(
                                                self.PanelMenu,
                                                text='Registrar Particular',
                                                height=0,
                                                width=150,
                                                font=self.Fuente_MontserratSemiBold,
                                                fg_color='transparent',
                                                hover=False,
                                                cursor='hand2',
                                                anchor='w',
                                                command=lambda mostrar=clienteParticular.marco_RegistroParticular, ocultar=ocultarMarcos: funci.mostrarVistas(mostrar, ocultar, clienteParticular.widgetsEntry_RegistraClienteParticular)
                                            )
    
    self.RegistroEmpresa_Boton = CTkButton(
                                                self.PanelMenu,
                                                text='Registrar Empresa',
                                                height=0,
                                                width=150,
                                                font=self.Fuente_MontserratSemiBold,
                                                fg_color='transparent',
                                                hover=False,
                                                cursor='hand2',
                                                anchor='w',
                                                command=lambda mostrar=clienteEmpresa.marco_RegistroEmpresa, ocultar=ocultarMarcos: funci.mostrarVistas(mostrar, ocultar, clienteEmpresa.widgetsEntry_RegistraClienteEmpresa)
                                            )
    
    self.ListaClienteParticular_boton = CTkButton(
                                                self.PanelMenu,
                                                text='Lista Clientes Particular',
                                                height=0,
                                                width=150,
                                                font=self.Fuente_MontserratSemiBold,
                                                fg_color='transparent',
                                                hover=False,
                                                cursor='hand2',
                                                anchor='w'
                                            )
    
    self.ListaClienteEmpresa_boton = CTkButton(
                                                self.PanelMenu,
                                                text='Lista Clientes Empresa',
                                                height=0,
                                                width=150,
                                                font=self.Fuente_MontserratSemiBold,
                                                fg_color='transparent',
                                                hover=False,
                                                cursor='hand2',
                                                anchor='w'
                                            )
    
    
    
    self.ServicioLabel = CTkLabel(
                                    self.PanelMenu,
                                    width=220,
                                    height=30,
                                    text='Servicio',
                                    font=self.Fuente_MontserratBold,
                                    fg_color=self.color_azulSecundario,
                                    text_color=self.color_blancoPrimario,
                                    corner_radius=20,
                                    anchor="w"
                                )
    
    self.NuevoServicioParticular_boton = CTkButton(
                                                self.PanelMenu,
                                                text='Nuevo Servicio Particular',
                                                height=0,
                                                width=150,
                                                font=self.Fuente_MontserratSemiBold,
                                                fg_color='transparent',
                                                hover=False,
                                                cursor='hand2',
                                                anchor='w',
                                                command=lambda mostrar=servicioParticular.marco_RegistroServicioParticular, ocultar=ocultarMarcos: funci.mostrarVistas(mostrar, ocultar, servicioParticular.widgetsEntry_RegistroServicioParticular)
                                            )
    
    self.NuevoServicioEmpresa_boton = CTkButton(
                                                self.PanelMenu,
                                                text='Nuevo Servicio Empresa',
                                                height=0,
                                                width=150,
                                                font=self.Fuente_MontserratSemiBold,
                                                fg_color='transparent',
                                                hover=False,
                                                cursor='hand2',
                                                anchor='w'
                                            )
    
    self.HistorialServiciosParticular_boton = CTkButton(
                                                self.PanelMenu,
                                                text='Historial Servicios Particular',
                                                height=0,
                                                width=150,
                                                font=self.Fuente_MontserratSemiBold,
                                                fg_color='transparent',
                                                hover=False,
                                                cursor='hand2',
                                                anchor='w',
                                                command=lambda mostrar=h_servicioParticular.marco_registro_servicio_particular, ocultar=ocultarMarcos: funci.mostrarVistas(mostrar, ocultar, h_servicioParticular.widgetsEntry_HistorialServicioParticular)
                                            )
    
    self.HistorialServiciosEmpresa_boton = CTkButton(
                                                self.PanelMenu,
                                                text='Historial Servicios Particular',
                                                height=0,
                                                width=150,
                                                font=self.Fuente_MontserratSemiBold,
                                                fg_color='transparent',
                                                hover=False,
                                                cursor='hand2',
                                                anchor='w'
                                            )
    
    
    
    self.VehiculosLabel = CTkLabel(
                                    self.PanelMenu,
                                    width=220,
                                    height=30,
                                    text='Vehiculos',
                                    font=self.Fuente_MontserratBold,
                                    fg_color=self.color_azulSecundario,
                                    text_color=self.color_blancoPrimario,
                                    corner_radius=20,
                                    anchor="w"
                                )
    
    self.RegistrarVehiculo_boton = CTkButton(
                                                self.PanelMenu,
                                                text='Registrar Vehiculo',
                                                height=0,
                                                width=150,
                                                font=self.Fuente_MontserratSemiBold,
                                                fg_color='transparent',
                                                hover=False,
                                                cursor='hand2',
                                                anchor='w',
                                                command=lambda mostrar=vehiculo.marco_RegistroVehiculo, ocultar=ocultarMarcos: funci.mostrarVistas(mostrar, ocultar, vehiculo.widgetsEntry_RegistroVehiculo)
                                            )
    
    self.ListaVehiculos_boton = CTkButton(
                                                self.PanelMenu,
                                                text='Lista Vehiculos',
                                                height=0,
                                                width=150,
                                                font=self.Fuente_MontserratSemiBold,
                                                fg_color='transparent',
                                                hover=False,
                                                cursor='hand2',
                                                anchor='w',
                                                command=lambda mostrar=ListaVehiculo.marco_ListaVehiculo, ocultar=ocultarMarcos: funci.mostrarVistas(mostrar, ocultar, ListaVehiculo.widgetsEntry_ListaVehiculo)
                                            )
    
    
    self.ListaConductores_boton = CTkButton(
                                                self.PanelMenu,
                                                text='Lista Conductores',
                                                height=0,
                                                width=150,
                                                font=self.Fuente_MontserratSemiBold,
                                                fg_color='transparent',
                                                hover=False,
                                                cursor='hand2',
                                                anchor='w',
                                                command=lambda mostrar=ListaConductor.marco_ListaConductor, ocultar=ocultarMarcos: funci.mostrarVistas(mostrar, ocultar, ListaConductor.widgetsEntry_ListaConductor)
                                            )
    
    
    
    self.UsuariosLabel = CTkLabel(
                                    self.PanelMenu,
                                    width=220,
                                    height=30,
                                    text='Usuario',
                                    font=self.Fuente_MontserratBold,
                                    fg_color=self.color_azulSecundario,
                                    text_color=self.color_blancoPrimario,
                                    corner_radius=20,
                                    anchor="w"
                                )
    
    self.CrearUsuario_boton = CTkButton(
                                                self.PanelMenu,
                                                text='Crear Usuario',
                                                height=0,
                                                width=150,
                                                font=self.Fuente_MontserratSemiBold,
                                                fg_color='transparent',
                                                hover=False,
                                                cursor='hand2',
                                                anchor='w'
                                            )
    

    
    
    self.LogoServiExpress_image.place(x=32, y=25)
    
    self.ClienteLabel.place(x=5, y=127)
    self.RegistroParticular_Boton.place(x=20, y=162)
    self.RegistroEmpresa_Boton.place(x=20, y=186)
    self.ListaClienteParticular_boton.place(x=20, y=209)
    self.ListaClienteEmpresa_boton.place(x=20, y=232)
    
    self.ServicioLabel.place(x=5, y=263)
    self.NuevoServicioParticular_boton.place(x=20, y=298)
    self.NuevoServicioEmpresa_boton.place(x=20, y=321)
    self.HistorialServiciosParticular_boton.place(x=20, y=344)
    self.HistorialServiciosEmpresa_boton.place(x=20, y=367)
    
    self.VehiculosLabel.place(x=5, y=402)
    self.RegistrarVehiculo_boton.place(x=20, y=437)
    self.ListaVehiculos_boton.place(x=20, y=460)
    self.ListaConductores_boton.place(x=20, y=483)
    
    self.UsuariosLabel.place(x=5, y=518)
    self.CrearUsuario_boton.place(x=20, y=553)