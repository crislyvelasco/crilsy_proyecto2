from modules.funcionesBasicas.importaciones import *

# Lista para que sirva la funcion de mostrar vistas, para ocultar vistas en las opciones de cambiar vista en la propia vista.
ocultarMarcos = [vehiculo.marco_RegistroVehiculo, servicioParticular.marco_RegistroServicioParticular, inicio.marco_WidgetsInicio, clienteEmpresa.marco_RegistroEmpresa, clienteParticular.marco_RegistroParticular, marca.marco_RegistroMarca, modelo.marco_RegistroModelo, h_servicioParticular.marco_registro_servicio_particular, ListaVehiculo.marco_ListaVehiculo, ListaConductor.marco_ListaConductor, DatosVehiculo.marco_DatosVehiculo, ActualizarDatos.marco_ActualizarDatos]

def cargarWidgets(self):
    
    # | ~~~~ SECCION Servicio ~~~~ |
    servicioParticular.RegistarServicioParticular(self)
    servicioParticular.marco_RegistroServicioParticular[0].grid(row=0, column=1)
    
    h_servicioParticular.historial_servicio_particular(self)
    h_servicioParticular.marco_registro_servicio_particular[0].grid(row=0, column=1)
    # | ~~~~~~~~~~~~~~~~~~~~~~~~~~ |
    
    # | ~~~~ SECCION Cliente ~~~~ |
    clienteParticular.RegistraClienteParticular(self)
    clienteParticular.marco_RegistroParticular[0].grid(row=0, column=1)
    
    clienteEmpresa.RegistraClienteEmpresa(self)
    clienteEmpresa.marco_RegistroEmpresa[0].grid(row=0, column=1)
    # | ~~~~~~~~~~~~~~~~~~~~~~~~~~ |
    
    # | ~~~~ SECCION VEHICULO ~~~~ |
    
    # Los Parametros que tienen algunas Funciones, son para las vistas que tienen que mostrar otras vistas en esa misma vista, entonces se pasa como parametros los marcos de la vista

    # el Que dice ocultarMarcos Son todos los marcos que hay, entonces cuando pasa a cada vista itera a cada marco para ocultarlo
    
    # y si hay funciones con 3 parametros, el tercer parametro es para  las vistas que muestran otras vistas, entonces se pasa como el tercer parametro los widgets que solamente son de Entrada (Osea Entrys), para Limpiar los Datos.
    
    vehiculo.RegistrarVehiculo(self, [marca.marco_RegistroMarca, modelo.marco_RegistroModelo], ocultarMarcos, marca.widgetsEntry_Modelo, modelo.widgetsEntry_Modelo)
    vehiculo.marco_RegistroVehiculo[0].grid(row=0, column=1)
    
    marca.RegistrarMarca(self, vehiculo.marco_RegistroVehiculo, ocultarMarcos)
    marca.marco_RegistroMarca[0].grid(row=0, column=1)
    
    modelo.RegistrarModelo(self, vehiculo.marco_RegistroVehiculo, ocultarMarcos)
    modelo.marco_RegistroModelo[0].grid(row=0, column=1)
    
    ListaVehiculo.ListaVehiculo(self, DatosVehiculo.marco_DatosVehiculo, ocultarMarcos)
    ListaVehiculo.marco_ListaVehiculo[0].grid(row=0, column=1)
    
    ListaConductor.ListaConductor(self, ActualizarDatos.marco_ActualizarDatos, ocultarMarcos, ActualizarDatos.widgetsEntry_ListaConductor)
    ListaConductor.marco_ListaConductor[0].grid(row=0, column=1)
    
    DatosVehiculo.datosVehiculo(self, [ListaVehiculo.marco_ListaVehiculo, ActualizarDatos.marco_ActualizarDatos], ocultarMarcos)
    DatosVehiculo.marco_DatosVehiculo[0].grid(row=0, column=1)
    
    ActualizarDatos.ActualizarDatos(self, [marca.marco_RegistroMarca, modelo.marco_RegistroModelo, ListaVehiculo.marco_ListaVehiculo], ocultarMarcos)
    ActualizarDatos.marco_ActualizarDatos[0].grid(row=0, column=1)

    # | ~~~~~~~~~~~~~~~~~~~~~~~~~~ |

    inicio.VistaInicio(self)
    inicio.marco_WidgetsInicio[0].grid(row=0, column=1)