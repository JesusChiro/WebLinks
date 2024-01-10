import reflex as rx
import PyReflex.styles.styles as styles
from PyReflex.components.navbar import navbar
from PyReflex.views.header.header import header
from PyReflex.views.links.links import links
from PyReflex.views.sponsors.sponsors import sponsors
from PyReflex.components.footer import footer
from PyReflex.styles.styles import Size
from PyReflex.styles.colors import Color as Color


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            rx.center(
                rx.vstack(
                    header(),
                    links(),
                    sponsors(),
                    max_width=styles.MAX_WIDTH,
                    width="100%",
                    margin_y=Size.BIG.value,
                    padding=Size.BIG.value,
                ),
            ),
            footer(),
        ),
        background_color=Color.BACKGROUND.value,
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)
app.add_page(
    index,
    title="Web de Links | Jesus Chiroque",
    description="Hola, mi nombre es Jesus Chiroque. Aficionado a la tecnología",
    image="avatar.jpg",
)
app.compile()