from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Static

from textual.binding import Binding
from textual.widgets import Footer 
class ButtonsApp(App[str]):
    CSS_PATH = "button.tcss"

    def compose(self) -> ComposeResult:
        yield Horizontal(
            VerticalScroll(
                Static("Saludar al mundo", classes="header"),
                Button("Saludar", id="hola"),
                Button.error("Salir", id="adios"),
            ),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
       # self.exit(str(event.button))
        if event.button.id == "hola":
            self.notify(
                "Desde el IES Haría"
                "[b]El 1º del Ciclo superior[/b]saluda al mundo",
                title="Saludo",
                severity="warning",
        )
        elif event.button.id == "adios":      
            self.exit(str(event.button))

    def footer() -> None:
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(
            key="question_mark",
            action="help",
            description="Show help screen",
            key_display="?",
        ),
        Binding(key="delete", action="delete", description="Delete the thing"),
        Binding(key="j", action="down", description="Scroll down", show=False),

    def compose(self,) -> ComposeResult:
        yield Footer()

if __name__ == "__main__":
    app = ButtonsApp()
    print(app.run())