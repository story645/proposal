meeting w/ professor haralick

Boolean     operation   truth table    tuples  
whole                                  scatterplot (ordering)
natural

character   meaning     partial order, 
                        linear order
                        lattices
                        graph
                        digraph
                        monograph
regular

sequences   objects (nouns)           [O1]->(P1)->[O2]
            process (verbs)           graph -> label 
                                      like flow chart ->
                                      [datatype] -> [process]
                                      
w___w___w
 words,     level of observation       recursive levels of details
            overview -> filter -> detail on demand
 sentences,                             labeled graph - nodes labled, edges labeled
 paragraphs, 

 turned disparate volatages into clean sequence of sounds
        process
        ------>
        ^
 object |

 can also be 
        object 
 process

process into object, object into process - akin to adjacency matrix

can be group of objects, group of process

||---|----|----|-----|--
objects (words) + grouping (covering/partition + overlap) 
objects -> kinds of objects
process -> kinds of process

cooccurance of things in complex graphs 

optimum partition of objects process
----->
|
|
|
partition of objects of N kinds, or process of N kinds
way of reordering so that resulting picture is as simple as possible

bar graph as ordering on elements:
| | | | |
---------
\alpha, \beta, \gamma, \delta -> eigenvalue drop off 

semantics are in object->process diagram, with partitions/groupings/covers
wordnet, propnet, verbnet, 

work out for text:
* relationships
* aggregations - > set of words/process/verbs 
* ordering
 
 set builder/logic notation

 visualization system
    * raw data to data structure - transform/aggregation
    * data structures to primitive

object/process/state
aggregation via partition - optimization problem 
go through all possible cross products of the partition after properly ordering, 
produce partitions such that visualization is simplest - layout engines

data visualization + category theory
* formalized data visualization + category theory
* existing paper is shallow

* build in terms of turing machines/functional programming, no real world consequence
* real world implication - testing + verification
* rules for pipeline + 
** viz class + test correct visualization
** serializibility

functional framework for visualization
* make more rigourous statements:
+ math prove things
+ CS test things

React shadow DOM
* tries to be functional programming es
* write code to render whole page out
* change little piece that renders small piece out
* behind the scenes - fake copy of dom in memory, renders whole page, checks what really change, only hits slow part when it hits diff/implements dif
++ state object, all state of a page 

Missing 1 piece
+ categgory theory  - theorems for free
- set up category, functor + natural transformation
- lots of lots of theorems come for free

What can we get for free from categorical theory? implications for ML/Viz

So what? 
Want to reproduce finite set, element of set is map of point to other set + morphism 
* functions all the way down - 
++ triangle edges and vertices
++ triangle made up of 3 functions - sides of triangle (triple
dont have to worry about elements 'cause identity 

category theory: maps between objects are more important than objects themselves 
set theory: things + things, cartesian product: function for set 
1st order - elemenets, sets of elements 





