big picture takeaway: trying to do way too much w/ every sentence/paragraph/figure, end up w/ too much tell & not enough show

instead structure around benefits or change them:
1. maintainability
2. extendability
3. scaling
4. concurrency

what does this model give in this context?

### abstract:
1. what it is: functional model
2. what it does: language for formalizing constraints
3. how: formalize as actions....
4. why: abstraction allows us to, by doing so 
5. what: equiv maps preserve (also possibly too much details)
6. what: we briefly sketch...
7. what: utility via case study
8. how: case study
9. what/why propose functional model

Revision: flip the script
1. start w/ 9, build out rest of sentences to show how this model achieves goals stated in 9. 

### S1: Intro:
p1:  who, what, why? 
* 1-2: trying to lay out problem (needs evidence)
* 3-8: why, what (lead w/ this, then lay out why this is a problem that needs to be solved which is fleshing out 1-2)
* 8-10: identifying audience, can maybe be omitted if 3-8 is better fleshed out
* 10-13: as w/ 8-10, trying to tell what the scope is (architecture vs graphic design)
__revision__: start with a sentence or two about architecture - > not what libraries have to do, but how they're structured - why do constraints matter? <- TOPIC: Constraints of Graphics - How do we build good cogs? -the visualization algorithm is assembled out of those cogs <-can also be a good lead in to the libraries section of the related work

p2: continuity & equivariance

__revision__: give these concepts breathing room by seperating them and pushing them to each of the related work sections they have to do w/, & change the figures to 
* topology: heatmap vs lineplot + backwards arrows
* equivariance: ? commutative diagram of equiv (direct reference to schidegger)

p3: roadmap 

27-30: what
31-36: why
37-44: roadmap

__revision__ move after related work, concepts should probably be at same levels (3.2, vs. 3.3), 

### S2: related work
p1:
48-52: situate the related work
52-68: equivariance (but I haven't realy mentioned topology yet)

__revision__: don't try to situate all at once, instead break down into situate equivariance, add a paragraph for continuity (bring in butler + figures), and what current libraries do

p2: 
* 70-73: framing tools in terms of continuity
* 73-84: summaries of libraries
* 84-88: why this framing
* 89-94: what problems the library is trying to solve 

__revision__  pull this paragraph up to the top of the intro as part of the framing for the problem we're trying to solve, break up heer/core data structure - ggplot, imagej, networkx, into one short paragraph, muller/algorithm & continuity - - d3, matplotlib, vtk, into another  - basically what do these libraries have in common? what are the rules they need to follow? Related work gets strictly focused on continuity+equivariance as the previous work on identifying these constraints 

### S3: TEAM


