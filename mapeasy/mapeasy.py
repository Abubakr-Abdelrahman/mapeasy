"""Main module."""

import random
import string
import ipyleaflet

class Map(ipyleaflet.Map):

    def __init__(self, center=[20, 0], zoom=2, **kwargs) -> None:

        if "scroll_wheel_zoom" not in kwargs:
            kwargs["scroll_wheel_zoom"] = True

        super().__init__(center=center, zoom=zoom, **kwargs)

        if "layers_control" not in kwargs:
            kwargs["layers_control"] = True

        if kwargs["layers_control"]:
            self.add_layers_control()
        
        if "fullscreen_control" not in kwargs:
           kwargs["fullscreen_control"] = True
        
        if kwargs["fullscreen_control"]:
            self.add_fullscreen_control()
    
    def add_search_control(self, position="topleft", **kwargs):
        """Adds a search control to the map.

        Args:
            kwargs: Keyword arguments to pass to the search control.
        """   
        if "url" not in kwargs:
            kwargs["url"] = 'https://nominatim.openstreetmap.org/search?format=json&q={s}'

        search_control = ipyleaflet.SearchControl(position=position, **kwargs)
        self.add_control(search_control)

    def add_draw_control(self, **kwargs):
        """Adds a draw control to the map.

        Args:
            kwargs: Keyword arguments to pass to the draw control.
        """        
        draw_control = ipyleaflet.DrawControl(**kwargs)

        draw_control.polyline =  {
            "shapeOptions": {
                "color": "#6bc2e5",
                "weight": 8,
                "opacity": 1.0
            }
        }
        draw_control.polygon = {
            "shapeOptions": {
                "fillColor": "#6be5c3",
                "color": "#6be5c3",
                "fillOpacity": 1.0
            },
            "drawError": {
                "color": "#dd253b",
                "message": "Oups!"
            },
            "allowIntersection": False
        }
        draw_control.circle = {
            "shapeOptions": {
                "fillColor": "#efed69",
                "color": "#efed69",
                "fillOpacity": 1.0
            }
        }
        draw_control.rectangle = {
            "shapeOptions": {
                "fillColor": "#fca45d",
                "color": "#fca45d",
                "fillOpacity": 1.0
            }
        }
        self.add_control(draw_control)
    
    

def generate_lucky_number(length=1):
    """Generate a random number of a given length.

    Args:
        length (int, optional): The length of the number to generate. Defaults to 1.

    Returns:
        int: The generated number.
    """    
    result_str = ''.join(random.choice(string.digits) for i in range(length))
    return int(result_str)
