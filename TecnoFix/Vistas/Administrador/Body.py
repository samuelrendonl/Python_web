import reflex as rx 
from TecnoFix.Estilos.Estilo import GRID_STYLE 
from TecnoFix.Estilos.Estilo import Size 
from TecnoFix.Vistas.Administrador.boton_icon import boton_icono
from TecnoFix.Estilos.Estilo import Width 
import datetime

sidebar_width = Width.MEDIUM_BIG_WIDTH.value  # "400px"
NAVBAR_HEIGHT ="117px"

def BodyAdmin() -> rx.Component:
   

    return rx.center(
        rx.grid(
            boton_icono("/GestionDispositivos.png", on_click=rx.redirect("/registro")),
            rx.vstack(
            rx.image(
            src="/Dispositivos (1).png",
            width= "auto",
            height="auto"
            
            ),
            rx.link("Samuel Rendon Lozano", href = "https://www.instagram.com/samuelrendonl/", is_external= True, color = "black"),
            rx.text(f"Desarrollador de Software 2024 - {datetime.date.today().year}", color="black"),
            align= "center",
            Width = "100%",
            padding_top = Size.BIG.value,
            padding_bottom = Size.BIG.value,


        ),
            columns="1",
            style=GRID_STYLE,
            spacing="2",
            width="100%",                   # ancho del grid dentro del body
            padding_bottom=Size.BIG.value
            
        ),
        width=f"calc(100% - {sidebar_width})",        # ocupa el resto del ancho
        height=f"calc(100vh - {NAVBAR_HEIGHT})",     # altura disponible debajo del navbar
        padding_y=Size.BIG.value,
        padding_x=Size.BIG.value,
        # important: shift body to the right so it starts where termina la sidebar
        margin_left=sidebar_width,                   # empuja el body a la derecha
        margin_top=NAVBAR_HEIGHT,                    # empieza donde termina la navbar
        overflow_y="auto",                            # permite scroll en el body si hace falta
        
    )