import reflex as rx
import link_bio.styles.styles as styles

def link_button(text: str, body :str , image: str, url: str) -> rx.Component:
    return rx.link(
        # rx.button(text, width="100%"),  <-- Lo dejo de una version anterior
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Size.LARGE.value,
                    height=styles.Size.LARGE.value,
                    margin=styles.Size.MEDIUM.value  
                ),
                rx.vstack(
                    rx.text(text, style=styles.button_title_style),
                    rx.text(text, style=styles.button_body_style),
                    align_items="start",
                    spacing=styles.Size.SMALL.value,
                    padding_y=styles.Size.SMALL.value,
                    padding_right=styles.Size.SMALL.value
                ),
                width="100%"
            )
        ),
        href=url,
        is_external=True, # Hace que se abra en una ventana nueva
        width="100%",
        text_decoration="none"
    )


"""              
                rx.icon(  --> Lo dejo como recuerdo de pintar iconos
                    tag="arrow_forward", # Imagen por defecto de reflex. Hay varias
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin=styles.Size.MEDIUM.value  
                ),
"""