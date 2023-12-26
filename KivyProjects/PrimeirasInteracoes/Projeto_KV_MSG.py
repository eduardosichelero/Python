from kivy.app import App
from kivy.uix.label import Label


class MainApp(App):
    def build(self):
        my_label = Label(text="Olá eu me chamo Eduardo, muito Prazer!",
            size_hint=(.5, .5),
            pos_hint={'center_x': 0.5, 'center_y': 0.5})

        return my_label


if __name__ == "__main__":
    app = MainApp()
    app.run()


