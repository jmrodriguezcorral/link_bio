import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Twitch",
            "Directos de lunes a virnes",
            "https://twitch.tv/moredev"),
        link_button(
            "YouTube",
            "Tutoriales semanales", 
            "https://youtube.com/@mouredev"),
        link_button(
            "YouTube (canal secundario)",
            "Tutoriales varios", 
            "https://youtube.com/@mouredev"),
        link_button(
            "Discord",
            "Para la comunidad",
            "https://youtube.com/@mouredev"),
        title("Contacto"),
        link_button(
            "MyPublicInbox",
            "Respuesta rápida y con preferencia", 
            "https://mypublicinbox.com/mouredev"),
        link_button(
            "Email",
            "jmchema@gmail.com",
            f"mailto:jmchema@gmail.com"),
        width="100%",
        spacing=Size.MEDIUM.value
    )