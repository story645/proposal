# Plan?
Goal: TCVG paper 

Deadlines: Vizweek April 20th, April 30th for paper, but TCVG is floating 
http://ieeevis.org/year/2020/info/coronavirus-info
https://www.computer.org/csdl/journal/tg

What does the paper need? 
1. Lit review
    1. mathemitical representaions/data models
        1. semantics of data/semantics of visualzation
        2. relational algebra stuff
    2. visualization architectures

2. Math working through
    1. Data -> Artist (aesthecs are functional transforms {need to sort out range / domain}) -> CW simplex -> machine rendering ()
3. proof of concept
    1. array prototype
    2. data frame prototype
    3. analytic function
    4. trees


# Immediate To Dos:
## PoC
1. finish array bit:
    2. bars
    3. histogram
        * Drawstyles PR
            * histogram can take in 2 1D vectors that are different sizes:
                * need to access both the values and the bins 
2. start dataframe

# status update meeting thursday

# MG meeting wed - Artist side 
* projection as iterator, data on demand
* have iterator, looking at next point, in order to know`` what to do  w/ data point
    * retinal variables - color, size, whatever
    * have data point, need color
    * fc(D, ) - > RGBA <- call back so that I'm gonna give you data, you go off and right the rgba
    * .plot(D, color = 'red', linestyle='thick')
        * f_color(D_i)
        * f_linestyle_thick(D_i)
        * f_position_xy(D_i)
        * f(f_pos, f_colo, f_line)->drawer -> CWsimplex (pixel)

    * grouped callback to create heirarchical/tree structure 

plot(Di, color='red', linestyle='think')

is really

```python
newscatter(Di, x=f_x_takes_position0, y=f_y_takes_positon1, color=f_color_red, linestyle=f_linestyle_thick)

def f_x_takes_position0(Di):
    return Di[0]

def f_x_takes_position1(Di):
    return Di[1]
    
def f_color_red(Di):
    return (1,0,0,1)
    
def f_linestyle_thick(Di):
    return 2
```

catagory of artists, categories made up of 1 function to another, categories going to data to cw complex
implementation of elements of this category are basically sets of functions called out to othr functions and collected to return thing that can be passed into draw 

# Possible data category

[Siplicial Databases](http://math.mit.edu/~dspivak/informatics/SD.pdf)

# Proposed Retinal catigory for 2D static visualizations

Maps of CW complexes into $R^7$ (x,y,depth,red, green, blue, alpha)

# Paper visual abstract:
![](https://i.imgur.com/tWvdDqS.png)

# Friday Tom

add parallel units transform machinery which needs rich data information so checking can be done ahead of time. 

add transform to some of the aesthetics 

multicolorline - passing in cmap/norm to line
aesthetics ping data source for version they need to do their thing
- art: I know how to control these RVs, what's the data I need?
    - categorical becomes pick N things in cycle

- artist runs through chain of functions to get RVs - can involved callbacks back to artists to query units
- artist responsible for broadcasting like red to 1000,1000 image
- How do we check/error out early? 
    - method on the datasource that we can ask info about itself 
        - don't now what query will return in general, then we need to remap
        - create query_metadata method: unit, type, abstract shape ()
            - abstract_shape - analytic function doesn't have shape, 
                            - gives symbolic shape (n, n-1)
                            - like generics in templates/mypi
                            - need to support ragged 
                                - x, y each n in outmost dimension, 
                                    - xi, yi need to be of same size
                                    - x0....xn don't need to be of equal size
                                - also support broadcasting rules like `plot(x, [y0...yn])`
                                    - under the hood probably how color broadcasting goes
                                        - i am shape scaler, my type is color
                                        - i am shape scaler, my type is categorical
                                            - if they pass a datasource as a color kwarg
                                            - what's currently passed in as color gets checked 
                                                - if not color, wrapped as data source
    - test goes in artist object init (which basically f_check)
        - ask this in the artist init (constraint statist)
- scatter has kwargs that belong to data and artist
    - factory function that sorts kwargs into correct place: datasource or artist

- can a tree go into a heatmap (AxesImage)?
    - yes if there's a projection that pushes it into an adjaceny matrix
    - have a projection that  provides tree in walkable way for artist
    - mpl should maybe support a treemap (or mpl-graph/tree that does the standards: 
        - dendrogram, adjancent matrix, tree-map
    - mvp can be a tree library

- Showcase Idea (year out): build library for DuBois's Data Portraits