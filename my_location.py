import geocoder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.mapview import MapView, MapMarker

class MapScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Get approximate location based on IP address
        g = geocoder.ip('me')
        latitude, longitude = g.latlng if g.latlng else (37.7749, -122.4194)  # Default to San Francisco if location not found
        
        # Create a MapView centered around the retrieved coordinates
        self.map_view = MapView(zoom=17, lat=latitude, lon=longitude)
        self.add_widget(self.map_view)
        
        # Create a MapMarker and add it to the MapView at the current location
        marker = MapMarker(lat=latitude, lon=longitude)
        self.map_view.add_marker(marker)

class MapApp(App):
    def build(self):
        return MapScreen()

if __name__ == "__main__":
    MapApp().run()
