* cartesian product - ordered pairs of all elements in A x B
### groups
* group $\subset$ monoid $\subset$ semigroups $\subset$ magma
* weak groups -
* general definition of group
    * set + binary operation *
    * closure:
        * $\forall a,b \in A,  (a*b) \in A$
    * associativity
        * $\forall a,b,c \in A, (a*b)*c = a *(b*c)$
    * has identity element 
        * $\exists e \in A \text{ s.t. } \forall a \in A: e * a = a * e = a$
    * has inverse elements
        * $\exists b\ in A \text{ s.t. } \forall a \in A: a*b=b*a=e$ 
    * commutativity:
         $\forall a,b \in A,  (a*b) = (b*a)$
* magma
    * set + closed operation
* semigroup
    * magma + associative operation
* monoid group
    * semigroup + identity
* group
    * monoid + inverse
* abelian group
    * group + commutativity

### functions
 $f: X \mapsto Y, f(x)=y$
* domain - input set X
* codomain - set of possible outputs Y
* range - set of elements $y \in Y$ that $f(x), x \in X$ maps to
* preimage/inverse: $f^{-1}$- set of elements $x \in X$ that are mapped into a given subset of $y in Y$,

* types:
    * general - many to one, range <= codomain
    * injective - one to one, range <= codomain
    * surjective - many to one, range == codomain
    * bijective - one to one, range == codomain
* functor goes between categories, satisfies properties 
    * monad is functor w/ extra structure
    * data structures are functors
    * not allowed to open up the structure, acts on containers


### topology
* simplex (simplices) - generalization of the notion of a 
triangle to arbitrary dimensions
* CW (cell) complex - set homeomorphic to a simplex 
    * C: "closure-finite"
    * W: "weak" topology.
    * kinda categorical simplices

* simplicial complex - set of simplices 
* simplicial set - 
* open set - set on space where boundary not in set, approx equiv to open interval on line
* topological space - set of points + neighborhoods for each point
    * neighborhood - set of points containing the point p where can move away from point in any direction w/o  leaving the set (wiki)
        * ex: A set V in the plane is a neighbourhood of a point p if a small disc around p is contained in V.
    * product space - cartesian product of topological spaces

* sheave - difference between fiber bundle?

* fiber bundle $(E, B, \pi, F)$
    * vector bundles are special case where fibers are vectors 
    * E - total space
        * 
    * B - base space
        * 
    * $\pi: E \mapsto B$  - projection map (continuos surjection) 
        * 
    * F - fiber
        * fiber as unit being plotted as a one thing 
            * box, line, dot, image
    * $\sigma$ - function that goes from K (index) to F
        * function like sine, cosine
        * data structure is also collection of functions:
            * data in table = functions that populate data into table
        * is instance of the data 
        * $\sigma$(k) equiv $\sigma[k]$
            * F is the Return signature of the indexing operation
#### Movie Frames
* 100, 64x64 Frames
* K = 0-100 (frame count), $k \in K$ 
* F - space of all possible pixel values 
    * [0-255] X 4096 cartesian product = $2^{8^{4096}}$
* sigma - particular movie or set of functions that generate that movie
* $\sigma(k)$ applying the function $\sigma$ on F to get back the frame at k

### Category theory
* category - objects & arrows that go between them
    * with associativity + identity
    * limited to small category
    * trying to replace set theory
    * private vs. public - 
    * objects may not be openable
        * class w/o instances
    * directed graphs w/ some extra info
    
* arrows - morphisms, orderings, functions, maps, relations, operators
* morphisms - map from one set to another set
    * homomorphism - structure preserving morphism 
* functor - maps between categories that preserve all arrows
    * has to preserve within category arrows
    * usually are containers
    * given {a,b}:
        * a->b, g(a) = b
        * F(a) = a, F(b) = b, F(g(F(a))) = F(b)
    * can implement map
    * can lift from single element function (transform) up to the section
        * arrows from one FB -> FB
    * homology is a functor, show that there's a natural transform and therefore all the same. 
* natural transfroms: arrows of functors 
    * preserve arrows between categories of functors
* limits - 
    * product - 
* colimits -
    * coproduct (sum) 
* initial object: {} (empty set)
    * arrow from it to every other set
* terminal object: () (one element set)
    * arrow from every other set to it
    * kind of like return None 
    * example: Error/Exception  
* Yoneda's Lemma:
    *

### homology
* general way of associating a sequence of algebraic objects (groups) to other mathematical objects such as topological spaces
    * topological space out of simplacial complex
    * sequence of groups
    * homology groups is 1 per dimension for each dimension of the topological
    * more general function (topological space) =sequence of groups <- 
    * map from one topological space to another is a map from one topoloical space is same as homology group to another homology group 
* computing the homology - get the homology groups of the space
    * homology - not a mapping from one space to other 
        * function from set of topological spaces to set of groups that preserve structure 
        * homology (whole torus, not points) -> groups
            * functions withen space preserved across to other space 
                * functions on elements should work on containers of those elements
                * functors are containarization  
* homology is 
    * define a group on the vertices, edges, faces
    * define a boundary map
    * B is little circle in big circle A
        * C is a collection of triangles between B and A
        * C_{i} boundary is A-B
        * since higher demension boundaries are considered 0, A=B
            * optimizing for something that doesn't depend on the topological space
            * set to 0 to remove dependency
            * cross sections of shape & is there a boundary between? hole boundary + inner circle of donut
    * singular homology - mathematical
        * any crazy space I can cover w/ triangle
    * simplacial homology - computational

### morphisms
structure preserving map from one mathematical structure to another of the same type
* homomorphism - continous mapping from one space to another, preserves topology
    * monomorphism - injective
    * epimorphism - surjective
    * isomorphism - bijective 
* {equi,in}variance
    * equivariance
    * invariance 

### visualization
#### Bertin
* invariant - what the viz shows that doesn't change (what is encoded in the composition of artists) 
    * multiple lines/scatters - what is the common thread? 
artist: data $\mapsto$ visual idom
* componenents - variables / what changes in the data (1 channel marks to one channel)
* marks/symbols - 
* impositions - 
* channels/visual variables - aesthetic attributes that are set relative to the data values in a component
transforms: component $\mapsto$ visual variable 
#### measurement type
* selective
* ordered 
* associative
* quantitative


#### Munzner
* visual idiom
* keys
* values
### Notes
Artists are maybe functors/acting kind of like them in a homology space 
$A: Data \mapsto RGBA...$

