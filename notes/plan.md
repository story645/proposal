# Proposal old schedule
* vacation 26-2
* RH: sept 18-20
* YK: sept 27-28
* Succoth: oct 2-11, CH:5-9
* thanksgiving Nov 19

# Paper Review Draft by End of October 30
 
## intro/lit review [1 week - Oct 12 start]
* intro
    * make any stupid plot you want in robust & rigourous way
        * need rich description langauge + right choice of paradigm (functional) 
        * ability to mathemetaically formalize/conceptual framework for doing this
        * data -> artist, need to preserved the structure of the data moreso than the data 
            * how points are connected to each other
    * targeted implementation rather than protocal (numpy)
        * visualization libraries bound to the datastructures (concrete implementation)
            * encode a lot of assumptions about data in the data structure
            * MPL assume x/y plotted in order you want them in 
            * topology makes the assumptions explicit
            * explicit->math->functional  
    * spell out the layers of visualization libaries:
        * Data + computation -> visualization composites -> drawing library
        * domain specific library
        * utility library <- formalize this piece (SciPy Diagram)
    * viz - Munzner + Bertin
    * functional programming makes sense 
* architecture review [1 week]
    * how does < > think about data? (scope it to the viz theoretic implementations)
    * grammer of graphics/ggplot
    * vega (altair)
    * bokeh 
    * d3
    * vtk

## why/what? [finished by Oct 1st]
* table - [ongoing, GSOD starts Sept 14]
    * table - why is indexer geometry?
        * : http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7192636&isnumber=7307919
        * https://en.wikipedia.org/wiki/Visual_hierarchy
* spell out the math (topology informed visualization library)
    * math - carry them through 
        * line vs scatter
        * imshow vs pcolormesh 
* software process/diagram [2 days]
  
* toy implementation [4 weeks]
    * line/scatter/imshow/pcolormesh basic - [1 week]
    * transforms [3 weeks]
        * x, y, [area]
        * linestyle, markerstyle
        * colormap/norm

ORDER OF THINGS NEED TO BE DONE:
1. enough of table for categories to be met:
    1. multiples Ms
    2. computational + direct
2. toy implementation
    3. rework the API given 1 for internal representation 
        artist/data
    4. fold in enough transforms that non-geometric bertin is there
3. math
    4. defintions/notation - what is M/m/F/sigma?
        5. diagram associated w/ it
        5. why? why why? why why why?
        6. case study - marked up line/scatter & how they differe
            7. what are the implicit assumptions of M in the artist/plot type?
            8. 
5. * diagram is also developer documentation of how the pieces fit
    4. object process diagram

tomorrow night - skelton w. section headings
come back - intro + lit review


outline of the answer for line:
    end-to-end for line
    
### Schedule 
* Sept 14: Terrible version 1
    * intro (no transitions)
        * Bertin retinal variable encodings
        * Munzner keys/value
    * lit review 
        * is in bullet points
        * only ggplot/bokeh/d3/vtk
    * math/theory
        * math is in bullet points/glossery
            * M, F, V, m, sigma
        * explain line & scatter in terms of M, F, V
    * implementation
        * mark up toy data (Iris, GHCN)
        * artist/datasource for line, scatter    
        * maybe linestyle aesthetic encoding (optional)
        

