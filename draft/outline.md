# new outline
1. intro:
    - frame problem around libraries/architecture
    - pull libraries section from related work here
2. related work
    - continuity: butler, munzner, introduce fiber bundles, define continuity
    - equivariance: apt, schidigger, define equivariance
3. contribution ?
    - introducing constraint driven model that builds on c+e work to solve architecture problems. 
    - case study to demonstrate how it works in architecture
    - caveat: not claiming new way to get parallel, etc, just that this functional approach will get there
        - confluence between theory & applied w/ category theory
4. TEAM
    1. framing: libraries implement the artist, which is the function encapsulating the data to visual transforms. first though must introduce the input (domain) and output (codomain) of those functions so we can discuss which/how functions preserve the properties of these objects. 
    2. modeling data & graphics as fiber bundles (& maybe visual so we can say we model the 3 stages Schedigger introduced as...)
        1. what is a fiber bundle? 
            1. continuity: base space k
            2. equivariance: fiber space f
            3. encoding data: section tau
        2. graphic bundle: continuity S, equivariance D, encoding graphic rho
    3. Artist 
        1. what is artist? broad strokes, functor or cofunctor or something
        2. continuity: xi
        3. equivarince:
            * nu
            * q & qhat
        4. building out of blocks: composition & equivalence   
5. code: (maybe weave code in w/ math?)
    - start at artist
    - pull back to data (xi, continuity)
    - how do we encode? push forward through nu and q
    - where is this model powerful? step vs. continuous example

# big picture takeaway: 
trying to do way too much w/ every sentence/paragraph/figure, end up w/ too much tell & not enough show, also look at the proposal revisions & see what/if stuff was addressed in rewrite

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

__revision__: flip the script
1. start w/ 9, build out rest of sentences to show how this model achieves goals stated in 9. 

## 1: Intro:
p1:  who, what, why? 
* 1-2: trying to lay out problem (needs evidence)
* 3-8: why, what (lead w/ this, then lay out why this is a problem that needs to be solved which is fleshing out 1-2)
* 8-10: identifying audience, can maybe be omitted if 3-8 is better fleshed out
* 10-13: as w/ 8-10, trying to tell what the scope is (architecture vs graphic design)
* __revision__: start with a sentence or two about architecture - > not what libraries have to do, but how they're structured - why do constraints matter? <- TOPIC: Constraints of Graphics - How do we build good cogs? -the visualization algorithm is assembled out of those cogs <-can also be a good lead in to the libraries section of the related work

p2: continuity & equivariance

* __revision__: give these concepts breathing room by seperating them and pushing them to each of the related work sections they have to do w/, & change the figures to 
* topology: heatmap vs lineplot + backwards arrows
* equivariance: ? commutative diagram of equiv (direct reference to schidegger)

p3: roadmap 
* 27-30: what
* 31-36: why
* 37-44: roadmap
* __revision__ move after related work, concepts should probably be at same levels (3.2, vs. 3.3), 

## 2: related work
p1:
* 48-52: situate the related work
* 52-68: equivariance (but I haven't realy mentioned topology yet)
* __revision__: don't try to situate all at once, instead break down into situate equivariance, add a paragraph for continuity (bring in butler + figures), and what current libraries do

p2: 
* 70-73: framing tools in terms of continuity
* 73-84: summaries of libraries
* 84-88: why this framing
* 89-94: what problems the library is trying to solve 
* __revision__  pull this paragraph up to the top of the intro as part of the framing for the problem we're trying to solve, break up heer/core data structure - ggplot, imagej, networkx, into one short paragraph, muller/algorithm & continuity - - d3, matplotlib, vtk, into another  - basically what do these libraries have in common? what are the rules they need to follow? Related work gets strictly focused on continuity+equivariance as the previous work on identifying these constraints 

## S3: TEAM
* 96-notion of an artist A as a map 
* 98-101: more roadmapping
* __revision__ needs context/definition/why we're calling this an artist. This dives straight into math. 
### 3.1 Data Bundle
* 103-107: drop straight from butler (who hasn't really been introduced) to fiber bundles (which also haven't really been introduced)
* 108-110: locally trivial
* __revision__ introduce concepts of Butler & bundles in related work, leave this just for the mathematical definition, maybe move locally trivial to a footnote w/ a why it's useful to know this

### 3.1.1
* 112-114: this gives why, but first needs an explanation of what is a fiber
* 114-127: soup about U and sigma and T
* 129-132:  example that misses the why this is helpful
* __revision__ most of 114-127 should be an appendix, but that's really just Spivak's paper, so pare down to something like 
> Spivak provides notation for describing the set of all possible values $U_{\sigma}$ of a single column with name $c$ and type $T$. This set of values is the fiber "F"
$F = U_{\sigma}(c)$.  When data is multivariate, the fiber F is the cartesian product of each columns fiber space (5)

change to dot, line, image, maybe network figures w/ different fibers, push explanation down 'til is all worked through?
### 3.1.2
* 134-139: structures on set into monoids
* 137-139: kinda clunky why monoids
* 140-147: textbook def of monoids and groups
* 149-154: foreshadowing invariance & weak tie to functional
* __revision__ switch to categories? use monoids as example of why that flexibility is helpful, keep the math very small (Scheidigger doesn't even formally define & they're basis of his group)

### 3.1.3
* 156-157: base space defined in terms of Butler, but if you're not firm on him doesn't make any sense
* 158-166: munzer tie in about keys that goes into a thing about independent & dependent variables
* 167-168: points back to figure but is a bit "see figure, see"
* 169-173: math def w/o grounding in why you need to know this
* 173-175: decomposition doesn't break k - rework as something like 
    > this allows us to seperate a complex dataset into smaller datasets - for example a time, temp, pres set becomes a time, temp set and a time, pres set - that share continuity. This means that the time, temp in one dataset is at the same point k as the (time, pres) in the other dataset. 
* 176-181: filler about concrete why K, but can be pulled up into related work
* __revision__ pull Munzner up to related work continuity section, maybe omit dependent/independent var discussion, swap out figure to the one w/ all the pieces together, rework this section to just be math now that you know about continuity from related works section
### 3.1.4
* 156-195: defines a section
* __revision__ needs a why do you need the math in all the places + maybe some pairing down/move to appendix, might also need a larger rework of 3.1 that goes continuity, fiber, (to match related works), section 

### 3.1.5
* 200-207: mathematical definition of sheafs
* __revision__ move up to continuity section b/c that's where it's most relevant, + animation & stuff bolster the "why do we care?" for continuity, especially if we invert. Sheafs let us do these things, how-b/c they bookkeep 
## 3.2
* 209-211: why graphic bundle
* 211-218: more definition
* 216-217: is context free unless you already know why triviality means this
* 219-221: practical benefit but missing the how, so might be worth putting first
* __revision__ pare down to just what they need to know to follow the paper & tell them that's why we're telling them:
    > Since we propose that the artist (visualization) is a continuity preserving equivariant map from data to graphic, we also model the graphic as the fiber bundle H. 
        * D for equivariance
        * S for continuity
        * rho so there's an actual graphic
### 3.2.1
* 223-224: why
* 225-226: math def, but homotopy isn't defined so this doesn't mean anything to someone w/o the math background
* 228 -234: thickening
* 235-239: querying/interactivity
* __revision__ pull this down into the artist section? first figure so it's clearer how the screen fits in/why this is thickened, possibly add a new figure that more fully pulls in the related point on screen, maybe a modified version of my graphic figure? - maybe graphic figure/illustration of bundle first, then the S to K figure - overview, drill down, if this structure

## 3.3 artist
* 241-248: formal definition of artist
* 249-252: introducing 16 (but needs to unpack)
* 253-264: explaining V 
* 264-269: the why
* __revision__ maybe pull up (16) since that's the overview of what we're on about or pull it all the way to the end of the section, or replace 14/15 w/ categorical commutative diagram, - between three spaces so it's basically eq (1) from "Algebraic Process for Visualization Design" (K&S), maybe pull up V discussion to fiber bundles/setting up objects section so it doesn't get muddled w/ function section, instead becomes transition between two sections - V is the object implemented by the library/on library terms while data is defined by provider & graphic by display space, pull "why" up and "artist named for mpl" is really a footnote

### 3.3.1
* 271-272: definition of $\nu$ w/o explaining what/why
* 272-293: conjecture of monoid equivariance 
* 294-297: steven's
* __revision__ explain what nu is and why it matters, either swap out 272-293 w/ category version or rewrite as proper conjecture, one of the reviewers had a suggestion for tightening up figure 7 & it (or something like it-look at draft revision) needs to be incorporated better into the text (there's a lot of text text see figure see text text). Either frame steven's better as an example or move it to appendix. 
### 3.3.2
* 301-302: introduce Q?
* 302-313: dense introduction of Q notation
* 316-322: proposition 
* 323-327: talks about figure (like others lack of figure annotations makes this feel disjointed)
* 328-338: glyph
* 339-351: rendering of graphic + pipeline 
* __revision__ don't start w/ figure, start with what we mean by assembly
> As discussed in sec~nu, nu functions convert data components in visual components, for example category into color. We propose functions Q that compose the visual components in V into a graphical element, for example x and y position and color into a scatter. 

Figure 8 is the generalized version of this, where...figure 8 should maybe be pulled to the top of the section & here should be the semi concrete version - for example the diagrams from the scipy talk or something stripped down that produces the first annulus in fig 9.  Break out intro of Q notation into bullet points. Maybe break out figure 9-> diff scatter or maybe even box commutative diagram of V -> H, with top & bottom, bottom is thickened annulus/equivalent). Maybe move glyph discussion up since that's a term the viz community understands & it'll maybe help situate what Q produces [or even move glyph definition up to rho introduction]. Rework pipeline discussion section around different case studies (network, image, scatter?) and arrows, push graphics discussion/figures into appendix like reviewer suggested?
### 3.3.3
* 353-359: notation and math working through that \hat{Q} can generate Q
* __revision__ pull figure & language from proposal rewrite, figure out which bit is actually important for somebody implementing code, maybe push all the math into appendix and then this section is something like
> The function Q described above takes as input V* which has a base space S. The graphic base space is not accessible in many architectures, so instead we construct a factory function Q hat. Q hat takes as input V over base space K, which as described in sec is... Q hat returns the function Q... This works b/c V-V* figure from proposal redo and shorter explaination of that figure. A mathematica; description can be found in appendix []
### 3.3.4
* 392-396: what
* 397-399: why kinda 
* 399-403: what/why
* __revision__
start w/ why & then do why, frame this section better - first sentence should probably tie into section header
## 4
* 405-407: jump straight into Matplotlib (not really telling anybody why)
* 408-413: hedging on why OO
* 413-414: floating code here
* 414-415: incomplete sentence
* 416-432: describing the artistclass code block
* 433-436: nu
* 436-444: Q
* __revision__ probably use basically pseudo-code, I think reviewers are right that it's both too much and not enough mpl, would also be easier to make it more functional, break it down line by line as annotated code instead of block of explanation (look at revised proposal) - streamline so that nu isn't explained first as part of object and then again when talking about nu objects. Also, framing is "the authors need to make clear the difference between and benefits for an actual programmer following their approach rather than, for example, a grammar-based specification such as Vega-Lite." (review 4)
### 4.1
* 446-451: what is this, what this section is about
* 452-456: view method, what does it do
* 457-459: qhat
* 460-462: line view
* 462-466: qhat
* 466-468: view and feels incomplete (last is a tell not show)
* __revision__ 4 should probably go away and mostly should jump straight into this discussion, (image artist would be good but probably can't happen in time frame), missing the why again, start w/ "the difference between a scatter and a line is in []" probably need a figure annotated w/ code or step through of what the code is doing to the figure, focus on one thing (xi, nu, q) at a time
### 4.1.1
* 470-477: nu dictionary + functions
* 478-479: testing nu equivariance
* __revision__ streamline - this feels more implementation detail than unpacking of model, delete the test function especially since that should really work like any composition test, or pull a different example from the table for Stevens
### 4.1.2
* 482-485: what is a wrapper (missing why)
* 487-494: comparing tau
* 496-497: tau returns a table
* 498-508: continuous vs. step
* __revision__ focus should be on continuous vs step, strip out the tau and wrapper stuff that should just be mentioned in xi section, pare down to "where does data model help?"
## 5
* 510-515: restate of contributions
* 515-535: mostly summary of work
* __revision__ rework to focus on the payoffs of this work, how the things discussed yield maintainability, extendability, scaling, & concurrency, as reviewers said the practical payoffs
### 5.1
* 537-540: technical unknowns
* 544-547: effectiveness
* __revision__ reviewer suggestion of move all the math caveats here & frame this section as limitations of the math
### 5.2
* 549- better math on A'
* 550-552: implement more artists
* 553-555: papers I like (don't go into why/how the model is good here)
* 556-559: category theory (which yes have to do)
* __revision__ replace w/ future work plan from my proposal since that's scaffolded how this model can practically do things
## 6
* 561-563: takeaway 1: better downstream support b/c of generalized data model
* 566-569: why good for matplotlib
* 570-572: tools & ecosystem
* __revision__ center on main themes: continuity, equivariance, maintainability, extensibility, scaling, concurrency
