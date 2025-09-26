import reflex as rx


def typing_indicator() -> rx.Component:
    """A simple three-dot typing animation."""
    return rx.el.div(
        rx.el.div(class_name="w-2 h-2 bg-gray-400 rounded-full animate-bounce"),
        rx.el.div(
            class_name="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:0.2s]"
        ),
        rx.el.div(
            class_name="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:0.4s]"
        ),
        class_name="flex gap-1.5 p-2",
    )