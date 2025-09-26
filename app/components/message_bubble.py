import reflex as rx
from app.components.typing_indicator import typing_indicator


def user_message_bubble(text: str) -> rx.Component:
    """A message bubble for user messages."""
    return rx.el.div(
        rx.el.p(text, class_name="text-base font-medium"),
        class_name="bg-emerald-500 text-white p-3 rounded-2xl rounded-br-none max-w-[80%] self-end shadow-md",
    )


def ai_message_bubble(text: str, is_last: bool) -> rx.Component:
    """A message bubble for AI messages, with a typing indicator."""
    return rx.el.div(
        rx.image(
            src="https://api.dicebear.com/9.x/notionists/svg?seed=AI",
            class_name="w-8 h-8 rounded-full border-2 border-gray-200",
            alt="AI Avatar",
        ),
        rx.el.div(
            rx.cond(
                (text == "") & is_last,
                typing_indicator(),
                rx.el.p(text, class_name="text-base font-medium"),
            ),
            class_name="bg-gray-100 text-gray-800 p-3 rounded-2xl rounded-bl-none shadow-sm min-h-[44px] flex items-center",
        ),
        class_name="flex items-start gap-3 max-w-[80%] self-start",
    )


from app.states.chat_state import ChatState


def message_bubble(message: dict, index: int) -> rx.Component:
    """Dynamically renders a user or AI message bubble."""
    return rx.cond(
        message["is_user"],
        user_message_bubble(message["text"]),
        ai_message_bubble(message["text"], index == ChatState.messages.length() - 1),
    )