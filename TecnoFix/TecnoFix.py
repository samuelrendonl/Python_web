import reflex as rx
from rxconfig import config
from TecnoFix.Componentes.navbar import navbar
from TecnoFix.Componentes.Login  import Login
from TecnoFix.Vistas.Administrador.Body import BodyAdmin
from TecnoFix.Vistas.Administrador.Header import HeaderAdmin
from TecnoFix.Componentes.Footer import footer
from TecnoFix.Componentes.sidebar import sidebar
from TecnoFix.Estilos.Estilo import Size 

class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        rx.hstack(
          bg  = "white",
          position = "sticky",
          padding_x = Size.BIG.value,
          padding_y = Size.BIG.value,
          z_index = "999",
          ),
        Login(),
        align = "center",
     ),


def Administrador() -> rx.Component:
    return rx.box(
        
        sidebar(),
        navbar(),
        BodyAdmin(),  
        #HeaderAdmin(),
        
    )

def Registro() -> rx.Component:
    return rx.box(
        navbar(),
    )


app = rx.App()
app.add_page(index)
app.add_page(Administrador, route="/admin")
app.add_page(Registro, route="/registro")
