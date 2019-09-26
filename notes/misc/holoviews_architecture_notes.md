meeting w/ Jim, ? and Thomas 

# structured data
* metadata extraction - smart labeling 
# mpl current architecture
* compositional of all the elements of the screen
 + collection of artists is a semantic unit
 + need a semantic unit to map it to the data
    + combining axis label w/ tick to map to visual images
    + 
 + matplotlib core going to be designed to be thinner w/ ,3rd part libraries on top

Holoviews 
* interface class - supports xarray/pandas
* map to holoviz semantic object
* axis can be anything 

## Data layer
* basic primative is element 
* hvcurve is set of coordinates:
    + independent + dependent
    + constraint checking / functional mapping
    + enforce/reflect assumptions about the data 
* simulator project
    + tons of things, same metadata, 50 billion w/ same metadata
    + cached metadata
* orientation preference, selectivity
    kept having to type the same orientation preference
    + declaring attribute values at the top -> can sample/new type of plots, information gets passed down
    + kind of like xarray (the array -> hist, plot, map)
    + if passing in raw meta array, then you need to specify the metadata
        - overwrite the automagic labeling
        - units every like 5 years (neuroml uses units properly)
        - units is used just to label the string 

Holoviews:
data in whatever(xarray,pandas, dictionary)->shoved in element + metadata -> interface (type dispatch system, ) 
/ selects the right class to choose the methods  
data + metadata + semantic category that appropriate plot can be chosen. User chooses element (curve-continuous, 
scatter-discrete) which implies the plot type

holoviews does not try to plot stuff it doesn't think makes semantic sense 
holoviews: grammar of data (compositional system of things to plot)
holoviews - 


list of data interfaces it supports - goes in order


