import reflex as rx
import PyReflex.styles.styles as styles
from PyReflex.components.navbar import navbar
from PyReflex.views.header.header import header
from PyReflex.views.links.links import links
from PyReflex.views.sponsors.sponsors import sponsors
from PyReflex.components.footer import footer
from PyReflex.styles.styles import Size


def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
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
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)
app.add_page(
    index,
    title="MoureDev | Te enseño programación y desarrollo de software",
    description="Hola, mi nombre es Brais Moure. Soy ingeniero de software, desarrollador freelance full-stack y divulgador.",
    image="avatar.jpg",
)

app.compile()
