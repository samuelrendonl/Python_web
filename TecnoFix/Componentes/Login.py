import reflex as rx
from TecnoFix.Estilos.Estilo import Width 
from TecnoFix.Estilos.Estilo import INPUTS_LOGIN
from TecnoFix.Estilos.Estilo import BUTTONS_LOGIN
from TecnoFix.Estilos.Estilo import Size 

def Login() -> rx.Component:
     return rx.center(  
       rx.vstack(
            rx.image(
              "/LogoTecnoFix.png",
              width= Width.MEDIUM_BIG_WIDTH.value , 
              height="auto",
              padding_y = Size.BIG.value,
              ),
                 
              rx.input(
                    placeholder="Usuario",
                    style= INPUTS_LOGIN[rx.input]
              ),
                
              rx.input(
                    placeholder="Password",
                    type = "password",
                    style= INPUTS_LOGIN[rx.input]
               ),

              rx.button(
                   "Iniciar Sesion",
                   style=BUTTONS_LOGIN[rx.button],
                   on_click=rx.redirect("/admin"),
              ),
              rx.button(
                   "Crear Cuenta",
                   style=BUTTONS_LOGIN[rx.button],
                   on_click=rx.redirect("/registro"),
              ),
              align="center",
              padding_y = Size.MEDIUM.value,
               spacing="6"
       ),
     )