import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
import link_bio.constants as const

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Twitch",
            "Transmisiones sobre programación de lunes a viernes",
            "icons/twitch.svg",
            const.TWITCH_URL
        ),
        link_button(
            "YouTube",
            "Tutoriales sobre desarrollo de software semanales",
            "icons/youtube.svg",
            const.TWITCH_URL
        ),
        link_button(
            "Discord",
            "El chat y lo grupos de estudio de la comunidad",
            "icons/discord.svg",
            const.DISCORD_URL
        ),
        link_button(
            "Retos de programación",
            "Ejercicios semanales para practicar lógica de programación",
            "icons/code.svg",
            const.CODE_CHALLENGES_URL
        ),
        link_button(
            "YouTube (canal secundario)",
            "Emisiones en directo destacadas",
            "icons/youtube.svg",
            const.YOUTUBE_SECONDARY_URL
        ),
        title("Contacto"),
        link_button(
            "MyPublicInbox",
            "Respuesta rápida y con preferencia",
            "icons/checkemail.svg",
            const.MYPUBLICINBOX_URL
        ),
        link_button(
            "Email",
            const.EMAIL,
            "icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
        width="100%",
        spacing=Size.MEDIUM.value
    )