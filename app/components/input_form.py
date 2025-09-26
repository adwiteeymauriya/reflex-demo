import reflex as rx
from app.states.chat_state import ChatState


def input_form() -> rx.Component:
    """The chat input form at the bottom of the screen."""
    return rx.el.div(
        rx.el.form(
            rx.el.input(
                name="message",
                placeholder="Type your message here...",
                class_name="w-full px-5 py-3 text-base text-gray-800 bg-white border-2 border-gray-200 rounded-full focus:outline-none focus:ring-2 focus:ring-emerald-400 transition-all duration-300",
                required=True,
            ),
            rx.el.button(
                rx.cond(
                    ChatState.is_typing,
                    rx.icon(tag="loader-circle", class_name="animate-spin"),
                    rx.icon(tag="arrow-up"),
                ),
                type="submit",
                disabled=ChatState.is_typing,
                class_name="absolute right-2 top-1/2 -translate-y-1/2 bg-emerald-500 text-white rounded-full w-10 h-10 flex items-center justify-center shadow-md hover:bg-emerald-600 focus:outline-none focus:ring-2 focus:ring-emerald-400 disabled:bg-gray-400 disabled:cursor-not-allowed transition-all duration-300",
            ),
            on_submit=ChatState.send_message,
            reset_on_submit=True,
            class_name="relative w-full",
        ),
        rx.el.button(
            rx.icon(tag="rotate-cw", class_name="w-4 h-4"),
            on_click=ChatState.clear_chat,
            class_name="bg-gray-100 text-gray-600 rounded-full w-10 h-10 flex items-center justify-center shadow-sm hover:bg-gray-200 transition-colors",
            title="Start New Chat",
        ),
        class_name="fixed bottom-0 left-0 right-0 p-4 bg-white/80 backdrop-blur-md border-t border-gray-200 flex items-center justify-center gap-4",
    )