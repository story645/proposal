big picture takeaway: trying to do way too much w/ every sentence/paragraph/figure, end up w/ too much tell & not enough show

instead structure around benefits or change them:
1. maintainability
2. extendability
3. scaling
4. concurrency

what does this model give in this context?
 - side convo about data visualization is a profunctor
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
* 96-notion of an artist A as a map 
* 98-101: more roadmapping
__revision__ needs context/definition/why we're calling this an artist. This dives straight into math. 
#### 3.1 Data Bundle
* 103-107: drop straight from butler (who hasn't really been introduced) to fiber bundles (which also haven't really been introduced)
* 108-110: locally trivial
__revision__ introduce concepts of Butler & bundles in related work, leave this just for the mathematical definition, maybe move locally trivial to a footnote w/ a why it's useful to know this

#### 3.1.1
* 112-114: this gives why, but first needs an explanation of what is a fiber
* 114-127: soup about U and sigma and T
* 129-132:  example that misses the why this is helpful

__revision__ most of 114-127 should be an appendix, but that's really just Spivak's paper, so pare down to something like 
> Spivak provides notation for describing the set of all possible values $U_{\sigma}$ of a single column with name $c$ and type $T$. This set of values is the fiber "F"
$F = U_{\sigma}(c)$.  When data is multivariate, the fiber F is the cartesian product of each columns fiber space (5)

change to dot, line, image, maybe network figures w/ different fibers, push explanation down 'til is all worked through?
### 3.1.2
* 134-139: structures on set into monoids
* 137-139: kinda clunky why monoids
* 140-147: textbook def of monoids and groups
* 149-154: foreshadowing invariance & weak tie to functional

__revision__ switch to categories? use monoids as example of why that flexibility is helpful, keep the math very small (Scheidigger doesn't even formally define & they're basis of his group)

### 3.1.3
* 156-157: base space defined in terms of Butler, but if you're not firm on him doesn't make any sense
* 158-166: munzer tie in about keys that goes into a thing about independent & dependent variables
* 167-168: points back to figure but is a bit "see figure, see"
* 169-173: math def w/o grounding in why you need to know this
* 173-175: decomposition doesn't break k - rework as something like 
    > this allows us to seperate a complex dataset into smaller datasets - for example a time, temp, pres set becomes a time, temp set and a time, pres set - that share continuity. This means that the time, temp in one dataset is at the same point k as the (time, pres) in the other dataset. 
* 176-181: filler about concrete why K, but can be pulled up into related work

__revision__ pull Munzner up to related work continuity section, maybe omit dependent/independent var discussion, swap out figure to the one w/ all the pieces together, rework this section to just be math now that you know about continuity from related works section
### 3.1.4
* 156-195: defines a section
__revision__ needs a why do you need the math in all the places + maybe some pairing down/move to appendix, might also need a larger rework of 3.1 that goes continuity, fiber, (to match related works), section 

### 3.1.5
* 200-207: mathematical definition of sheafs
__revision__ move up to continuity section b/c that's where it's most relevant, + animation & stuff bolster the "why do we care?" for continuity, especially if we invert. Sheafs let us do these things, how-b/c they bookkeep 
## 3.2

