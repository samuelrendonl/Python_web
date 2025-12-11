import reflex as rx
from TecnoFix.Estilos.Estilo import BUTTONS_ICON
from TecnoFix.Estilos.Estilo import IMAGEN_STYLE

def boton_icono(icono, on_click):
    return rx.button(
        rx.vstack(
            rx.image(
                src = icono,
                style = IMAGEN_STYLE
            ),  
            spacing="5",
            align="center",
        ),
        style= BUTTONS_ICON[rx.button],
        on_click=on_click,
    )
