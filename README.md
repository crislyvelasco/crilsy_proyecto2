# ServiExpress
# Requisitos 

> [!NOTE]
> Estos requisitos que se estableceran enel **README**, se podrian Cambiar o Modificar por el Tiempo, Pero siempre hay que seguirlo para mantenerlo bien el orden.

## Nombre De Variables

**PascalCase**: Se usara cuando se crean widgets, Por ejemplo: estamos haciendo la Seccion de *Registrar Cliente*, y estan creando los widgets, siempre se guarda en una variable, Entonces la Variable Tendra un Nombre Especifico y usando **"PascalCase"** ejemplo:
 
> [!TIP]
> **ClienteParticular_label = CTkLabel()**

**o si quieren hacerlo mas simplificado**

> [!TIP]
> **CliParticular_label = CTkLabel()**

lo que se busca es que se entienda que Seccion usa ese widget.

## Orden de Colocar la Configuracion del Widget

Cuando estemos colocando la configuracion del widget (weight, height, fg_color, etc), se colocara en varias lineas de codigo para que se lea bien y se entienda bien ejemplo:

```
ClienteParticularLabel = CTkLabel(
                                NombreDelMarco,
                                width= 200,
                                height= 100,
                                fg_color= '#25ffff'
                            )
```

## Fuente del Diseño

Descargen y intalen todas los .ttf de Montserrat ¡¡OBLIGATORIO!!

> [!TIP] 
> https://fonts.google.com/specimen/Montserrat

## Paleta de Colores "Sacados del diseño"

Azul Primario: `#1c2f6e`
Azul Secundario: `#2589bd`
Blanco Primario: `#f0f3f9`
Gris Placeholder: `#aeb7cf`
Rojo Primario: `#e12223`

## Librerias a Descargar "POR EL MOMENTO" y ¡¡OBLIGATORIO!!

**CustomTkinter**
```
pip install customtkinter
```
**Pillow**
```
pip install pillow
```



# Parte 1: Hacer Secciones del sistema con CustomTkinter

> [!IMPORTANT]
> HACER LAS VISTAS DE LA SECCION EN *plantilla.py*

> [!IMPORTANT]
> Esta Parte le hable a cada uno en privado, y me dijieron que estaban de acuerdo del metodo que escogi. Se hizo por el motivo de  aprobechar el tiempo que nos queda y ala vez practicar tkinter a los que todavia no estan bien claro como es, **RECUERDE ES SOLAMENTE DISEÑO NO FUNCIONALIDAD**.

### ¿Que metodo usaremos?

Yo *Luis*, Voy a crear la vista donde se va a mostrar todas las opciones "Osea donde sale el menu de opciones y al lado blanco", en la zona donde es blanco, se dejara vacio, donde se lo pasare a cada quien para que haga una Seccion de las opciones que tenemos, Ya Cuando terminemos se Podria hacer una reunion entre los 4 para acomodar cada seccion y ya tenerlo agregado enel sistema.

### ¿Como Crearemos las Secciones?

En la zona Blanca sera un **CTkFrame** el cual el nombre es **PanelInformacion** el cual cuando lo vayan a usar en los widgets deberan colocar **self.PanelInformacion**, donde ustedes cuando creen los widgets lo colocan a ese Marco. ***¿Como Posicionaran los widgets?*** Eso ya depende de como ustedes quieran posicionarlo, el tema es que quiero que ya vayan agarrando como usar tkinter, Yo *Luis* voy a usar .place(x=,y=) ya que lo tengo un poco dominado.

### ¿Cual Seccion haremos cada uno?

*Alejandro:* Hara Toda la Seccion de **Cliente**

*Briayan:* Hara Toda la Seccion de **Servicio**

*Crisly:* Hara Toda la Seccion de **Usuario**

*Luis:* Hara la Vista de **Vehiculo**

# Vistas Terminadas

**Login** Hecha por Luis

**Registro Vehiculo** Hecha por Luis

**Registro Marca** Hecha por Luis

**Registro Modelo** Hecha por Luis

**Lista Conductor** Hecha por Luis

**Lista Vehiculo** Hecha por Luis

**Datos Vehiculo** Hecha por Luis

**Actualizar Datos Vehiculo/Conductor** Hecha por Luis


**Registro Servicio Particuar** Hecha por Briayan

**Historial Servicio Particuar** Hecha por Briayan


**Registro Cliente Particular** Hecha por Alejandro

**Registro Cliente Empresa** Hecha por Alejandro