from customtkinter import *
import modules.Menu.menu as menu
from modules.funcionesBasicas.importaciones import *
from modules.CTkSelector.ctk_scrollable_dropdown import *

class VentanaPrincipal(CTk):
    
    def __init__(self):
        super().__init__()
        
        self.anchoX = int(funci.calcular_centrado(self.winfo_screenwidth(), 1250)) # Variable con el centrado de la resolucion de la pantalla y de la ventana enel ancho
        self.altoY = int(funci.calcular_centrado(self.winfo_screenheight(), 670)) # Variable con el centrado de la resolucion de la pantalla y de la ventana enel alto
        
        self.geometry(f'1250x670+{self.anchoX}+{self.altoY}')
        self.title('Serviexpress')
        self.resizable(0,0)
        
        # Fuentes
        self.Fuente_MontserratBold = CTkFont('Montserrat', weight='bold', size=20)
        self.Fuente_MontserratBold_Titulos = CTkFont('Montserrat', weight='bold', size=36)
        self.Fuente_MontserratBold_SubTitulos = CTkFont('Montserrat', weight='bold', size=30)
        self.Fuente_MontserratBold_Labels = CTkFont('Montserrat', weight='bold', size=21)
        self.Fuente_MontserratSemiBold = CTkFont('Montserrat SemiBold', size=13)
        self.Fuente_MontserratSemiBold_Options = CTkFont('Montserrat SemiBold', size=15)
        self.Fuente_MontserratSemiBold_PlaceHolder = CTkFont('Montserrat SemiBold', size=18)
        self.Fuente_MontserratBoldTreeView = CTkFont('Montserrat', weight='bold', size=16)
        # |~~~~~~~~~~~~~~~~~~|
        
        # Paleta de Colores
        self.color_azulPrimario = '#1C2F6E'
        self.color_azulSecundario = '#2589BD'
        self.color_azulHoverSecundario = '#2e74bf'
        self.color_azulHover = '#26429E'
        self.color_azulComboBox = '#274196'
        self.color_blancoPrimario = '#F0F3F9'
        self.color_grisPlaceholder = '#AEB7Cf'
        self.color_rojoPrimario = '#E12223'
        self.color_rojoSecundario = '#F52526'
        # |~~~~~~~~~~~~~~~~~~|
        
        self.Vista_Inicio()
        
        
    def Vista_Inicio(self):
        # Panel Menu, Donde sale las opciones
        self.PanelMenu = CTkFrame(
                                self,
                                height=670,
                                width=230,
                                fg_color=self.color_azulPrimario,
                                corner_radius=0
                            )
        # Panel Informacion, Donde va a salir las vista de la mayoria de opciones
        self.PanelInformacion = CTkFrame(
                                self,
                                height=670,
                                width=970,
                                fg_color=self.color_blancoPrimario,
                                corner_radius=0
                            )
        # Esto ya es decoracion solamente
        self.LineaDerecha = CTkFrame(
                                self,
                                height=670,
                                width=50,
                                fg_color=self.color_azulPrimario,
                                corner_radius=0
                            )
        # Posicionamiento
        self.PanelMenu.grid(row=0, column=0)
        self.PanelInformacion.grid(row=0, column=1)
        self.LineaDerecha.grid(row=0, column=2)
        
        
        # | ~ Widgets Menu ~ | NO TOCAR
        
        menu.WidgetsMenu(self) # Se Muestan las opciones, NO TOCAR
        
        # |~~~~~~~~~~~~~~~~~~| NO TOCAR
        
        
        
        
        # |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        # | ~ ACA CREARAN SUS WIDGETS DE SU RESPECTIVA VISTA ~ |
        # Recuerden Colocar donde el master "self.PanelInformacion"
    
        # BORRAR ESTE PARTE DE CODIGO YA QUE ES UN EJEMPLO
        # NombreElemento Se Coloca el nombre del componente/elemento que va hacer, ejemplo InputCedula_Entry
        # _label Hay se coloca el nombre del widget ejemplo Cliente_label
        
       
        # titulo de la vista
       
        self.CrearUsuario_label = CTkLabel(
                            self.PanelInformacion,
                            text=" Crear Usuario ",
                            text_color=self.color_azulPrimario,
                            width=700,
                            height=0,
                            font=self.Fuente_MontserratBold_Titulos,
                            anchor="w"
            
            
        )
        self.CrearUsuario_label.place(x=30, y=35 )
        
        # nombre y apellido
        self.NombreyApellido_label = CTkLabel(
                            self.PanelInformacion,
                            text="Nombre y Apellido",
                            text_color= self.color_azulPrimario,
                            fg_color= "transparent",
                            font=self.Fuente_MontserratBold_Labels
                                    
        )
        self.NombreyApellido_label.place(x=35, y=90)
        
        
        #Ingresar nombre y apellido
        self.NombreyApellido_entry = CTkEntry(
                            self.PanelInformacion,
                            text_color='#000',
                            width=400,
                            height=47,
                            fg_color='transparent',
                            corner_radius=15,
                            border_width=3,
                            border_color=self.color_azulPrimario,
                            font=self.Fuente_MontserratSemiBold_PlaceHolder
         )
    
        self.NombreyApellido_entry.place(x=30, y=130)
        
        # Cargo
        self.Cargo_label= CTkLabel(
                            self.PanelInformacion,
                            text="Cargo",
                            text_color= self.color_azulPrimario,
                            fg_color="transparent",
                            font=self.Fuente_MontserratBold_Labels
            
        )
        self.Cargo_label.place(x=500, y=90)
        
        # Ingrese el cargo
        self.Cargo_entry = CTkEntry(
                            self.PanelInformacion,
                            text_color='#000',
                            width=300,
                            height=47,
                            fg_color='transparent',
                            corner_radius=15,
                            border_width=3,
                            border_color=self.color_azulPrimario,
                            font=self.Fuente_MontserratSemiBold_PlaceHolder
         )
    
        self.Cargo_entry.place(x=500, y=130)
        
        
         # Usuario
        self.Usuario_label= CTkLabel(
                            self.PanelInformacion,
                            text="Usuario",
                            text_color= self.color_azulPrimario,
                            fg_color="transparent",
                            font=self.Fuente_MontserratBold_Labels
            
        )
        self.Usuario_label.place(x=35, y=200)
        
        # Ingrse usuario
        self.Usuario_entry = CTkEntry(
                            self.PanelInformacion,
                            text_color='#000',
                            width=200,
                            height=47,
                            fg_color='transparent',
                            corner_radius=15,
                            border_width=3,
                            border_color=self.color_azulPrimario,
                            font=self.Fuente_MontserratSemiBold_PlaceHolder
         )
    
        self.Usuario_entry.place(x=35, y=240)
        
        # Contraseña
        self.Contraseña_label= CTkLabel(
                            self.PanelInformacion,
                            text="Contraseña",
                            text_color= self.color_azulPrimario,
                            fg_color="transparent",
                            font=self.Fuente_MontserratBold_Labels
            
        )
        self.Contraseña_label.place(x=300, y=200)
        
        # Ingrse contraseña
        self.Contraseña_entry = CTkEntry(
                            self.PanelInformacion,
                            text_color='#000',
                            width=200,
                            height=47,
                            fg_color='transparent',
                            corner_radius=15,
                            border_width=3,
                            show="*",
                            border_color=self.color_azulPrimario,
                            font=self.Fuente_MontserratSemiBold_PlaceHolder
         )
    
        self.Contraseña_entry.place(x=300, y=240)
        
        # Nivel de acceso
        self.NiveldeAcceso_label = CTkLabel(
                            self.PanelInformacion,
                            text=" Nivel de Acceso",
                            text_color= self.color_azulPrimario,
                            font= self.Fuente_MontserratBold_Labels,
                        )

        self.NiveldeAcceso_label.place( x = 600, y = 200)

        self.comboboxNivelAcceso = CTkComboBox(
                                    self.PanelInformacion,
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
                         

        CTkScrollableDropdown(
                            self.comboboxNivelAcceso,
                            values = [ "Administrador", "Empleado"],
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

        self.comboboxNivelAcceso.place( x = 600, y = 240)

        
        
app = VentanaPrincipal()

app.mainloop()