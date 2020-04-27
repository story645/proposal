Tom, Hannah, Michael-transcription of blackboard notes

# Current pipeline
user: data (climate model)
|
3rd party package: unpacks data into mountain range/dem/geography `ds.plot()`
|
mpl: imshow + formatters + locators + legend
| 
.draw: walk the artists to make the image
## artist revision
* axes plotting methods return non-deterministic list of artists
* emulate something like Altair's 'chart object' - walkable deterministic tree of the plot

# Proof of concept/reference specification
Haskell:
new data + artist -> zipped json (modeled on collada/svg)

Python:
read file -> create data + artist objects in mpl -> render figure

## zipped json?? - serializable figure
* runnable spec bundle that mpl will read and instantiate into figure
* why zipped? 
    * functions as plot inputs and rcparams - can bundle as .py file
    *  based on shapefiles/.docs/etc

# ToDo: protocol to generate
* line - Line2D/simplest plot type
    * `plot([1,2,3])`
    * `plot(lambda x:x**2)
* contour - On the fly calculations
* hist - PatchCollections
* datetimes/categoricals - unit machinery
* streaming data
* concurrent data: large scatter/scatter density 

