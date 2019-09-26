# Stages
1. vtk, ggplot, vega, d3, parviz, imagej, bokeh, holoviews

survey of existing 3rd party packages: ytastro, 

2. abstract out into something functional 

3. separate out functional core from 
imperative stuff 


subpiece: redo data model
* monkey patch in your own reductions (ytastro)

publication: 
    show how abstracting out data into its own 
    data model reduces spaghetti and gives you new 
    features

# structured data:
    data has aspect of its ND data 

Formally: 
abstraction/specification is functional
implementation has objects 

Scope/plan:
1. rewrite data model + don't fail tests 
2. figure out where to target on the matplotlib functionality stack
    1. target scatterplot/bar graph/whatever - hits API & where do we hit our piece

# To Do:
Build out/plan use cases:
* mpl core functionality
* involve types + (awkward to do, incorporates the ideas)
* motivating examples
* trace through whole library to see what gets hit to understand purely functional programming language

for next week:
* mpl architecture diagram
* some sample use cases
* mpl data object flag xor