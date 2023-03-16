"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
from pynecone import el

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    pass


def index():
    return el.div(
        el.div(
            el.h1("Welcome to Pynecone!", style={"font_size": "2em"}),
            el.div(
                "Get started by editing ",
                pc.code(filename, style={"font_size": "1em"}),
            ),
            el.a(
                "Check out our docs!",
                href=docs_url,
                style={
                    "color": "rgb(107,99,246)",
                    "border": "0.1em solid",
                    "padding": "0.5em",
                    "border_radius": "0.5em",
                    "display": "inline-block",
                },
            ),
            style={
                "font_size": "2em",
                "display": "flex",
                "flex_direction": "column",
                "align_items": "center",
            },
        ),
        style={
            "padding_top": "10%",
            "display": "flex",
            "justify_content": "center",
        },
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
