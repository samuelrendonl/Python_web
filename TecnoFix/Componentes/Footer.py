import reflex as rx 
import datetime
from TecnoFix.Estilos.Estilo import Size

def footer() -> rx.Component:
        return rx.vstack(
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


        )