# datasource maps D->Projection for artist (query)
# aesthetic maps P-> retinal variables (red, sqaure)
# artist maps retinal variables -> pixels (CW-complex)

# What artists end up:
#1. get plotting data (pull set of rows) - 
    # comes in as dict of bertin variables 
#2. dict of maps of floats to visual propeties
#    'size array' -> actual marker sizes
#    'data units' -> pixels
#3. push to vector model
    #goes in matplotlib cbook
    
def check_constraints(required, optional, encodings):
    """
    required: set
        Encodings required by the artists
    optional: set
        Encodings the artist supports
    encodings:
        Set of encodings the datasource is providing
    """
    # check required encodings are there
    if not (required <= encodings):
        raise ValueError(f"Required encodings {required}")
    # check optional encodings 
    if not ((encodings - required) 
            <= optional):
        raise ValueError(f"Valid optional encodings: {optional}")

"""
def draw_alt(...):
    # do the external monad
    data_view = self.data.view(self.axes)

    # do functional AES / transforms / ..
    # required + optional (matplotlib def)
    transfromed = {k: self.transform [k](data_view.get(k))
                    for k in data_view}
    # do renderer monad
    super()._sekret_draw(transfromed, renderer)

def _sekret_draw(self, transformed, renderer):
    # what ever terrible thing we have to do to get MPL to draw
    gc = rendere.get_new_gc()
    gc.set_foreground_color(transform['color'])
    renderer.draw_path(transformed['x'], transformed['y'], )
"""