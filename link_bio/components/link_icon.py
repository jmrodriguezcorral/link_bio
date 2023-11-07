import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

def link_icon(image: str, url : str) -> rx.Component:
    return rx.link(
        #rx.icon(tag = "link"), <- Version antigua
        rx.image(
            src=image,
            width = Size.DEFAULT.value
        ),
        href=url,
        is_external=True, # Hace que se abra en una ventana nueva
    )