import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.views.sponsors.sponsors import sponsors
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size


class State(rx.State):
    pass

def index() -> rx.component:
    #return rx.text("Hola CaraCola!", color="blue")
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(      
                header(),
                links(),
                sponsors(),
                max_width = styles.MAX_WIDTH,
                width = "100%",
                margin_y = Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )

#app = rx.App(style=styles.BASE_STYLE)
app = rx.App( style= styles.BASE_STYLE)
app.add_page(
    index,
    title="jmchema 👋 | Cositas de IT y La Rioja en general 🍇",
    description="Soy ingeniero informatico de hace mas de 18 años. Me gusta la técnologia y mi tierra, La Rioja",
    image="avatar.png"
)
app.compile()