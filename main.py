from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.mapview import MapView

class MapScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Create a MapView with specified zoom level and center coordinates
        self.map_view = MapView(zoom=10, lat=37.7749, lon=-122.4194)  # Centered on San Francisco
        self.add_widget(self.map_view)

class MapApp(App):
    def build(self):
        return MapScreen()

if __name__ == "__main__":
    MapApp().run()
