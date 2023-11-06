import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span("moure", color = Color.PRIMARY.value),
            rx.span("dev", color = Color.SECONDARY.value),
            style = styles.navbar_title_style
        ),
        rx.text(
            "mouredev"
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top = "0"
    )