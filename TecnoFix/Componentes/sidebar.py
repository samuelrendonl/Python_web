import reflex as rx
from TecnoFix.Vistas.Administrador.boton_icon import boton_icono
from TecnoFix.Estilos.Estilo import GRID_STYLE 
from TecnoFix.Estilos.Estilo import Size 
from TecnoFix.Estilos.Estilo import Width 
from TecnoFix.Componentes.Footer import footer

NAVBAR_HEIGHT ="117px"

def sidebar():
    return rx.vstack(
        rx.grid(
            boton_icono( "/GestionDispositivos.png", on_click=rx.redirect("/registro")),
            boton_icono( "/gestion de piezas.png", on_click=rx.redirect("/registro")),
            boton_icono( "/Gestion de reparaciones.png", on_click=rx.redirect("/registro")),
            boton_icono( "/Gestion de trabajadores.png", on_click=rx.redirect("/registro")),
            boton_icono( "/estadisticas.png", on_click=rx.redirect("/registro")),
            boton_icono( "/INFORMACION.png", on_click=rx.redirect("/registro")),
            
            columns="1",
            style = GRID_STYLE,
            spacing="2",
            width="100%",
            padding_bottom = Size.BIG.value
        ),
        width= Width.MEDIUM_BIG_WIDTH.value,
        height=f"calc(100vh - {NAVBAR_HEIGHT})",
        bg="#838382",
        position="fixed",
        left="0",
        top="117px",
        align="center",
        overflow_y="auto",
        padding_x = Size.MEDIUM.value,
        padding_y = Size.MEDIUM.value,
    )
