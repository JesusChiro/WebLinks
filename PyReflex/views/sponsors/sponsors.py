import reflex as rx
import PyReflex.constants as const
from PyReflex.components.title import title
from PyReflex.components.link_sponsor import link_sponsor
from PyReflex.styles.styles import Size


def sponsors() -> rx.Component:
    return rx.vstack(
        title(
            "Colaboran",
        ),
        rx.responsive_grid(
            link_sponsor(
                "elgato.png",
                const.ELGATO_URL,
                "Logotipo de ELgato"
            ),
            link_sponsor(
                "mvp.png",
                const.MVP_URL,
                "Logotipo de Microsoft de MVP"
            ),
            spacing=Size.BIG.value,
            columns=[1,2]
        ),
        width="100%",
        align_items="start",
        spacing=Size.MEDIUM.value,
    )
