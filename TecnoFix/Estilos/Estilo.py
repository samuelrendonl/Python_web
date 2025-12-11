import reflex as rx
from enum import Enum

# Constantes
# width
class Width(Enum):
    BIG_WIDTH = "600px"
    NOBIG_WIDTH = "500px"
    MEDIUM_BIG_WIDTH = "400px"
    MEDIUM_WIDTH = "300px"
    MEDIUMSMALL_WIDTH = "200px"
    NOSMALL_WIDTH = "100px"
    SMALL_WIDTH = "50px"

#Sizes 
class Size(Enum):
   pass
   SMALL = "0.5em" 
   MEDIUM = "0.85em"
   DEFAULT = "1em"
   NOBIG = "1.5em"
   BIG = "2em"

# Styles 
# Campos de texto
INPUTS_LOGIN = {
    rx.input: {
        "width": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.MEDIUM.value,
        "font_size": Size.MEDIUM.value,
        "background_color": "#f5f5f5",
        "border": "1px solid #ccc",
        "border_color": "#000000",
        "outline": "none",
        "transition": "all 0.2s ease-in-out",
        "align": "center",

        "_focus": {
            "border": "1px solid red",
            "box_shadow": "0 0 8px rgba(255, 0, 0, 0.5)",
        },

        "_hover": {
            "background_color": "white",
            "box_shadow": "0 0 6px rgba(255, 255, 255, 0.5)",
            "transform": "scale(1.01)",
        },
    }
}

#Botones
   #botonoes login
BUTTONS_LOGIN = {
   rx.button: {
      "width": "50%",
      "height": "50%",
      "display": "block",
      "padding": Size.SMALL.value,
      "border_radius": Size.MEDIUM.value,
      "background_color": "Black",
      "color": "white",
      "white_space": "normal",
      "radius": "full",
      "cursor": "pointer",
      "align": "center",

      "_hover": {
            "background_color": "gray",  # define un color en tu enum
            "box_shadow": "0 0 12px rgba(255, 255, 255, 0.6)",  # efecto de brillo
            "transform": "scale(1.03)",                         # efecto POP opcional
            "transition": "all 0.2s ease-in-out",
        },
   }
}

#botones interfaz
BUTTONS_ICON = {
    rx.button: {
        "width": "10    0%",
        "height": "100%",
        "display": "flex",
        "flex_direction": "column",
        "justify_content": "center",
        "align_items": "center",
        "padding": Size.SMALL.value,
        "border_radius": Size.MEDIUM.value,

        "background_color": "#FFFFFF",  # color gris suave como en tu mockup
        "color": "black",
        "cursor": "pointer",
        "transition": "all 0.25s ease",

        # Quitar borde y seleccionar comportamiento visual
        "border": "none",
        "outline": "none",

        "_hover": {
            "background_color": "#5f5f5f",
            "box_shadow": "0 0 14px rgba(0, 0, 0, 0.25)",  # sombra leve hacia afuera
            "transform": "scale(1.03)",                   # POP suave
        },
    }
}

#imagen
IMAGEN_STYLE = {
    "width": Width.MEDIUM_WIDTH.value,
    "padding_y": Size.MEDIUM.value,
    "padding_x": Size.NOBIG.value,
}



GRID_STYLE = {
    "gap": "20px",
    "width": "100%",
    "padding_x": Size.SMALL.value,
    "padding_y": Size.MEDIUM.value,
}