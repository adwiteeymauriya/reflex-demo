import reflex as rx
from app.states.chat_state import ChatState
from app.components.message_bubble import message_bubble
from app.components.preset_prompts import preset_prompts
from app.components.input_form import input_form


def chat_view() -> rx.Component:
    """The main chat interface view."""
    return rx.el.div(
        rx.foreach(ChatState.messages, message_bubble),
        class_name="flex flex-col gap-4 p-4 pb-32",
        width="100%",
        max_width="48rem",
        margin_x="auto",
    )


def index() -> rx.Component:
    """The main page of the application."""
    return rx.el.main(
        rx.cond(ChatState.messages.length() > 0, chat_view(), preset_prompts()),
        input_form(),
        class_name="font-['Lato'] bg-gray-50 min-h-screen",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, title="LLM Chat")