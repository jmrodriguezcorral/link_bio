import reflex as rx
from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsor
from link_bio.styles.styles import Size as Size

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.hstack(
            link_sponsor(
                image="elgato.png",
                url="http://www.elgato.es"
            ),
            link_sponsor(
                image="mvp.png",
                url="http://www.mvp.es"
            ),
            spacing = Size.DEFAULT.value
        ),
        width="100%",
        align_items="start",
        spacing = Size.MEDIUM.value
    )