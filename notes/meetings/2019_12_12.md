Axis knows it has some sort of unit on its dimensions, can tell data object to do transform into units or exploding. 
default - no units, unitless floats
    unit aware data - unit registry converts to unitless floats (forget original data)

seperate in schema:
    artists: hold references to the data
    data: (how to represent this? ) is it just location to the data? (
            x-axis is some column of the database 
            : encode path to file + reader 
    )

possibly on load, pass in the data object/data objects
    * static computational graph (like dask)
    * here's the list of data objects we need 
    * here's the schema, here's the units, here's the constraints
    - whole thing no changes, reproducibility
    - whole thing, change the database
        .fig is now your library
streaming
    - incremental renders are hard
        -react model that user can assume things blow away (auto blitting)
encoding:
- sequences- this column is associated to:
    - position, size, texture

legend_elements:
- each artist provides their info - label, encodings, etc
    - should generate their own handles
- collect 'em all? to 
- better collections api
    - bundle up kwarg to pass through to legend
    - textcolor = your job to make text same color as face
    - textcolor = back in legend supersedes artists 
        - explicitly setting in legend signifies intent

new types:
multivariate AxesImage
univariate AxesImage

AbstractArtistClass
* scatter, error, etc...
