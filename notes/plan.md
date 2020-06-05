Highlevel story:
----------------
Proposal:
What is the problem I'm trying to solve?
* starting at data, wind up at visual thing - what takes you from one to the other? 
* has structure- attempts at giving structure formal language
* can build implementations based on structure that we can then reason about it 
* talk about how other visualization libraries approach this 
* trying to derive structure on category of artists 
### from data to pictures
    1. there's zoo + inductive work
    2. review libraries <- place why ggplot/vega/d3 doesn't work for matplotlib?
        * doesn't preserve data structure/makes assumptions of type
        * need a category that goes from data to visualization w/o assumptions of structure
            * lets call it an artist 
    3. introduce notation on data + mvp of data 
    4. pixel is CW simplex  
    5. bulk of dissertation: formalizing the artists + cw complex + pushing on it 
        what is the right mathematical object that sits between data and picture?

1. syncing between thesis/proposal/matplotlib
2. functional representation
    i. objects in data space w/ morphisms -> maps of that as source into retinal categories/visual categories 
    ii. mapping is category of artists: codds -> CW simplex space (kind of function of little simplexes into color/transparency layers, don't have to worry about resolution)
3. meta rules - we're trying to formalize the rules for writing something like altair - how do you write a thing you can build a robust domain specific altair/ggplot 


Scipy
------
- the status quo and the drawbacks
    - data agnostic while also being able to unpacking 
- high-level overview of the proposal and its benefits
- a survey of the state-of-the art in the field
- the algebra to describe the data model
- report on prototypes

Tasks
-----
1. daily check ins:
    * daily updates
    * code/ note commits
    * rambly text message 

2. Get what's working for the array working for the dataframe
3. Reading list of stuff to understand algebra
4. figuring out how to decompose the visuailzation:
    1. what's the data piece
    2. artist piece
    3. visual part? 
5. figure out minimal set of functions for implementing bertin variables (w/ factor out on either end) to get a plot - how to factor that out further so that I can get graphs on either side, trying to seperate out things more:
    1. trying to do what html & css are doing - 
        * structural part mapped to abstract visual variable
        * styling - like `RcParams` can meet up w/ other side to draw thing

6. frame lit review within context of Bertin's visual variables. 

To Do:
------
1. get at least one plot working for dataframe
    2. which visualzation, what variable do you want to map, .....
    3. want to map from raw data to array of numbers (x position, y position)
    4. other side - fill in aesthetic
3. then do unitized dataframe:
    * one column categorical, one column dates, one floats
    * scikit-image convertors should live on datasource
    * pass axes object into request for data 
        * convertors are a method on axis
        * x/y coupled to spatial aesthetics - all x data needs to be transformed to same units
            * axis locking PR

5. make it clear which piece: data, binding, visual
    6. what is the minimal basis of visualization/binding - what are the minimum sets of projections we need?
7. summarize key points from FC in DB systems + slide
8. Spivak Codd/databases paper + slide

# (ax.text should take formatters)

Updates:
* schedule regular meetings - 2:00 Wednesday
