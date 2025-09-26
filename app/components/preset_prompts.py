import reflex as rx
from app.states.chat_state import ChatState


def prompt_card(
    icon: str, title: str, on_click_event: rx.event.EventType
) -> rx.Component:
    """A card with a preset prompt to start a conversation."""
    return rx.el.button(
        rx.el.div(
            rx.icon(tag=icon, class_name="w-5 h-5 text-gray-500"),
            rx.el.p(
                title, class_name="text-base font-semibold text-gray-800 text-left"
            ),
            class_name="flex items-center gap-3",
        ),
        rx.icon(tag="arrow-up-right", class_name="w-4 h-4 text-gray-400"),
        on_click=on_click_event,
        class_name="flex justify-between items-center w-full p-4 bg-white border border-gray-200 rounded-2xl hover:bg-gray-50 hover:shadow-lg hover:-translate-y-1 transition-all duration-300 shadow-md",
    )


def preset_prompts() -> rx.Component:
    """A component for the initial screen with preset prompts."""
    prompts = [
        {"icon": "sun", "title": "Plan a day trip"},
        {"icon": "code-xml", "title": "Write a python script"},
        {"icon": "brain-circuit", "title": "Explain a complex topic"},
        {"icon": "lightbulb", "title": "Brainstorm creative ideas"},
    ]
    return rx.el.div(
        rx.el.div(
            rx.image(
                src="https://api.dicebear.com/9.x/initials/svg?seed=LLM",
                class_name="w-16 h-16 rounded-2xl border-4 border-white shadow-lg",
                alt="App Logo",
            ),
            rx.el.h1(
                "Hello! How can I assist you today?",
                class_name="text-3xl font-bold text-gray-800",
            ),
            class_name="flex flex-col items-center text-center gap-4",
        ),
        rx.el.div(
            rx.foreach(
                prompts,
                lambda p: prompt_card(
                    p["icon"],
                    p["title"],
                    lambda: ChatState.send_message({"message": p["title"]}),
                ),
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-4 w-full",
        ),
        class_name="flex flex-col items-center justify-center gap-8 w-full max-w-3xl mx-auto h-full px-4",
    )