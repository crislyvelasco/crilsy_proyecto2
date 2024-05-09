from customtkinter import *
import modules.Menu.menu as menu
from modules.funcionesBasicas.importaciones import *


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
        
        # | ~ Principal ~ | 
        self.Vista_Inicio()
        
        # | ~ Login ~ | 
        # login.Vista_Login(self)
        
        
    def Vista_Inicio(self):
         # Panel Menu, Donde sale las opciones
        self.PanelMenu = CTkFrame(
                                self,
                                height=670,
                                width=230,
                                fg_color=self.color_azulPrimario,
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
        self.LineaDerecha.grid(row=0, column=2)
        

        
        menu.WidgetsMenu(self)
        datos.cargarWidgets(self)
        
        
app = VentanaPrincipal()

app.mainloop()