import reflex as rx
import datetime
import PyReflex.constants as const
from PyReflex.styles.styles import Size as Size
from PyReflex.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt='Logotipo de MoureDev. Una "eme" entre llaves.',
        ),
        rx.link(
            f"© {datetime.date.today().year} Jesus Chiroque Building Engineer System",
            href=const.MOUREDEV_URL,
            is_external=True,
            font_size=Size.MEDIUM.value,
        ),
        rx.text(
            "BUILDING SOFTWARE with ♥ from Lima to World",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value,
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        spacing=Size.DEFAULT.value,
        color=TextColor.FOOTER.value,
    )
