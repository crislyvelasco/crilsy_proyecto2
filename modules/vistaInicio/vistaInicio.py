from customtkinter import *

marco_WidgetsInicio = []

def VistaInicio(self):
    
    self.PanelInformacion = CTkFrame(
                                self,
                                height=670,
                                width=970,
                                fg_color=self.color_blancoPrimario,
                                corner_radius=0
                            )
    
    marco_WidgetsInicio.append(self.PanelInformacion)