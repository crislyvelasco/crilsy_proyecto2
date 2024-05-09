from customtkinter import *
from ..routes.routes import imagenes as ruta

def Vista_Login(self):
    
    self.Fuente_MontserratSemiBold_InicioSesion = CTkFont('Montserrat SemiBold', weight='bold', size=33)
    
    # Panel donde se muestra la Imagen
    self.PanelImagen = CTkFrame(
                            self,
                            height=670,
                            width=626,
                            fg_color=self.color_azulPrimario,
                            corner_radius=0
                        )
    # Panel donde se muestra el formulario       
    self.PanelFormulario = CTkFrame(
                            self,
                            height=670,
                            width=625,
                            fg_color=self.color_azulPrimario,
                            corner_radius=0
                        )
    # Posicionamiento
    self.PanelImagen.grid(row=0, column=0)
    self.PanelFormulario.grid(row=0, column=1)
    
    # Imagen de Presentacion
    
    self.Presentacion_image = CTkLabel(
                                self.PanelImagen,
                                corner_radius=0,
                                text='',
                                image=CTkImage(ruta['imagenPresentacion'], size=(626, 670))
                            )
    self.Presentacion_image.place(x=0.5, y=0.5)
    
    #|~~~~~~~~~~~~~~~~~~~~~~~~|
    
    
    # Widgets del Formulario
    
    self.LogoServiExpress_image = CTkLabel(
                                self.PanelFormulario,
                                corner_radius=0,
                                text='',
                                image=CTkImage(ruta['logoServiExpress'], size=(333, 155))
                            )

    self.IniciarSesion_label = CTkLabel(
                                    self.PanelFormulario,
                                    text='Inicio de sesion',
                                    width=300,
                                    height=40,
                                    font=self.Fuente_MontserratSemiBold_InicioSesion,
                                )
    
    
    
    self.iconUsuario_image = CTkLabel(
                                self.PanelFormulario,
                                corner_radius=0,
                                text='',
                                image=CTkImage(ruta['iconUsuario'], size=(21, 24))
                            )
    
    self.LoginUsuario_entry = CTkEntry(
                                    self.PanelFormulario,
                                    width=240,
                                    height=40,
                                    font=self.Fuente_MontserratSemiBold_PlaceHolder,
                                    placeholder_text='Usuario',
                                    placeholder_text_color=self.color_blancoPrimario,
                                    fg_color="transparent",
                                    border_width=False
                                )
    
    self.LoginUsuario_linea = CTkLabel(
                                    self.PanelFormulario,
                                    width=270,
                                    height=4,
                                    text='',
                                    font=CTkFont('Montserrat SemiBold', size=1),
                                    fg_color=self.color_blancoPrimario
                                )
    
    
    
    self.iconPassword_image = CTkLabel(
                                self.PanelFormulario,
                                corner_radius=0,
                                text='',
                                image=CTkImage(ruta['iconPassword'], size=(21, 24))
                            )
    
    
    self.LoginContraseña_entry = CTkEntry(
                                    self.PanelFormulario,
                                    width=240,
                                    height=40,
                                    font=self.Fuente_MontserratSemiBold_PlaceHolder,
                                    placeholder_text='Contraseña',
                                    placeholder_text_color=self.color_blancoPrimario,
                                    fg_color="transparent",
                                    border_width=False
                                )
    
    self.LoginContraseña_linea = CTkLabel(
                                    self.PanelFormulario,
                                    width=270,
                                    height=4,
                                    text='',
                                    font=CTkFont('Montserrat SemiBold', size=1),
                                    fg_color=self.color_blancoPrimario
                                )
    
    self.LoginIngresar_boton = CTkButton(
                                    self.PanelFormulario,
                                    text='Ingresar',
                                    fg_color=self.color_blancoPrimario,
                                    text_color=self.color_azulPrimario,
                                    hover_color=self.color_grisPlaceholder,
                                    font=self.Fuente_MontserratBold,
                                    width=150,
                                    height=40,
                                    corner_radius=20,
                                    cursor='hand2'
                                )

    self.LogoServiExpress_image.place(x=146.5, y=95)
    
    self.IniciarSesion_label.place(x=163, y=290)
    
    self.iconUsuario_image.place(x=185, y=388)
    self.LoginUsuario_entry.place(x=210, y=384)
    self.LoginUsuario_linea.place(x=178, y=420)
    
    self.iconPassword_image.place(x=185, y=458)
    self.LoginContraseña_entry.place(x=210, y=454)
    self.LoginContraseña_linea.place(x=178, y=490)
    
    self.LoginIngresar_boton.place(x=238, y=535)


    #|~~~~~~~~~~~~~~~~~~~~~~~~|