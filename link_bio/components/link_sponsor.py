import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

def link_sponsor(image: str, url : str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            html_height=Size.VERY_BIG.value,  #cmbiado por mi. moure lo pone sin html_
            width="auto"
        ),
        href=url,
        is_external=True
    )