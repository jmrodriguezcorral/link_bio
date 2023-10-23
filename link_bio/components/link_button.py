import reflex as rx
import link_bio.styles.styles as styles

def link_button(text: str, body :str ,url: str) -> rx.Component:
    return rx.link(
        # rx.button(text, width="100%"),  <-- Lo dejo de una version anterior
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_forward", # Imagen por defecto de reflex. Hay varias
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value  
                ),
                rx.vstack(
                    rx.text(text, style=styles.button_title_style),
                    rx.text(text, style=styles.button_body_style),
                    align_items="start"
                )
            )
        ),
        href=url,
        is_external=True, # Hace que se abra en una ventana nueva
        width="100%",
        text_decoration="none"
    )