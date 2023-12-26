from kivy.app import App
from kivy.uix.image import Image

class MainApp(App):
    def build(self):
        img = Image(source=r"C:\Users\dudus\OneDrive\Área de Trabalho\Nova pasta\pao.png",
                    #Contribuição de uma pessoa que ama pães
            size_hint=(1, .5),
            pos_hint={'center_x': 0.5, 'center_y': 0.5})
        return img

if __name__ == "__main__":
    app = MainApp()
    app.run()

