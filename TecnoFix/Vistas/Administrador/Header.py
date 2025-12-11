import reflex as rx 

def HeaderAdmin() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.button(),
            rx.spacer(),
            rx.image(
                "/PERFILADMINISTRATIVO.png", 
                size = "10px"
            ),
        ),
        background_color = "#838382",
        padding_y = "10px",
        padding_x = "10px",
        width="100%",
        height = "100%",
        align = "center"
    )