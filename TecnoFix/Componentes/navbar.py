import reflex as rx
from TecnoFix.Estilos.Estilo import Width 
from TecnoFix.Estilos.Estilo import Size 


def navbar() -> rx.Component:
     return  rx.hstack(
          rx.image(
              "/Dispositivos (1).png",
              width= Width.MEDIUMSMALL_WIDTH.value , 
               padding_x = Size.SMALL.value,
               padding_y = Size.MEDIUM.value
          ),
          rx.spacer(), 
          rx.button(
               rx.hstack(
                    rx.avatar(
                         fallback = "SR",
                         radius = "full",
                         size = "6",
                         color_scheme = "gray",
                         variant = "solid",
                    ),
               ),
               height="45px",
               width="45px",
               radius = "full",
               padding_x = Size.BIG.value,
               padding_y = Size.BIG.value,
          ),        

          position = "sticky",
          background_color = "#838382",
          padding_x = Size.NOBIG.value,
          padding_y = Size.NOBIG.value,
          z_index = "999",
          top = 0
     ) 
     