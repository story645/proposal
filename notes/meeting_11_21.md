Thomas C, Thomas F, Hannah

# To Do
* container_of_axes.set_title
* figure is container of containers of axes
    - figure is the scope of atomic draws/ 
* intermediate level tooling
    - multi-axes things that I need to logically lay out sensibly
    - don't want user to pass in the figure 
* subplots_kwarg dict on subplots should maybe be a list of same size for setting projections
# 
* axes bound method reprs looking like pyplot reprs
* html injections into docstrings <- throw images into docstrings> (doctest/docstring)

# scikit learn discussions
* throws warning using heuristic if axis is used
    - monkey patch or sentinel to flag usage through sklearn / overwrites it
    - also suggest that they use child_axes to stash their new axes
* proper thing would be that MPL should write an intermediate library that 
    - hijack projection machinery 
        * usually returns polar or 3d or the like
        * instead projection='factory'
    - provides an artist container class that can drop in as an axes, has two or so methods:
        * subplot
        * title 
        * figure level styling - background patches and the ilk
        * methods required to duck-type as an Artist into the Figure's draw tree
    - sample:
        * `fig, list_of_axes = plt.subplots()`
        * `fig, list_of_grids = plt.subplots(..., projection='factory')`
        * `[subgrid.subplots(2, 2) fro subgrid in list_of_grids]`

    machinery to change 

# Milestones

milestones for near future
 - want to put paper in to viz week due, early march
        - http://ieeevis.org/year/2020/welcome
 - Hannah needs a thesis proposal
 - Meeting with Tom and Hannah week after thanks giving
    - Agenda:
     - make sure T and H are on same page about paper
     - have a plan to get it done
- week after after thanksgiving meeting with CUNY profs
   - Make sure they are all on board with paper + thesis plan as well
