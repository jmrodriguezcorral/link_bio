import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Brais Moure", 
                size="xl",
                src = "avatar.jpg",
                color= TextColor.BODY.value,
                bg = Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading(
                    "José Mª Rodriguez",
                    size = "lg"
                ),
                rx.text(
                    "@jmchema", 
                    margin_top=Size.ZERO.value,
                    color = TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon("icons/twitch.svg","https://x.com/jmchema"),
                    link_icon("icons/twitch.svg","https://x.com/jmchema"),
                    link_icon("icons/twitch.svg","https://x.com/jmchema"),
                    spacing = Size.DEFAULT.value
                ),
                align_items="start"
            ),
            spacing=Size.BIG.value
        ),

        rx.flex(
            info_text("+13", "Años de experiencia"),
            rx.spacer(),
            info_text("+13", "Años de experiencia"),
            rx.spacer(),
            info_text("+13", "Años de experiencia"),
            width="100%"
        ),

        rx.text(
            f"""
            Soy ingeniero de software desde hace más de 12 años. 
            Actualmente trabajo como freelance full-stack developer iOS y Android. 
            Además creo contenido formativo sobre programación y tecnología en redes. 
            Aquí podrás encontrar todos mis enlaces de interés. ¡Bienvenid@!
            """,
            font_size = Size.DEFAULT.value,
            color=TextColor.BODY.value),
        spacing = Size.BIG.value,
        align_items = "start"

    )