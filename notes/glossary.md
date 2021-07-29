set 
- cardinality: # of elements in this set
- finite or infinite collection of objects (elements), (grimaldi)
- elements are members of a set (grimaldi)
- order has no significance (wolfram)
- repetition (multiplicity) may or may not be ignored (wolfram)
    - sets w/ repetition are bags and/or multisets
- side note: sets of all sets w/ some constraints (class)

operations on sets $A, B \subset U$: 
- union: elements in A or B
- intersection: elements in A and B
- difference: elements in A not in B 

- disjoint union: append?
- halloween pumpkin set operations: 

class (Spanier):
- aggregate not assumed to be a set
- ex: class of all sets

function (functions between sets):
![](figures\function-mapping.png)
https://www.mathsisfun.com/sets/injective-surjective-bijective.html
- functions: (grimaldi: D5.3)
    - $f: X \rightarrow Y$ is a relation in which every element of A appears exactly once as the first component -> (function must be deterministic, each input has one output)
    - image: $(x,y) \in f$, 
        - y is image of x under f
        - x is preimage of y
* domain - input set X
* codomain - set of possible outputs Y
* range - set of elements $y \in Y$ that $f(x), x \in X$ maps to
* preimage/inverse: $f^{-1}$- set of elements $x \in X$ that are mapped into a given subset of $y in Y$,

* general:  (grimaldi: D5.3)
    - many to one, range <= codomain
- one-to-one/injective: (grimaldi: D5.5)
    - range <= codomain
    - y is the image of at most one x, for all $x1, x2 \in X$, f(x1) = f(x2), x1=x2
- onto/surjective: (grimaldi: D5.9)
    - range == codomain
    - f(X) = Y, for $y \in Y$ at least one $x \in X$ s.t. f(x)=y
- bijective: 
    - range == codomain
    - one-to-one & onto 

 |      | ~one-to-one | one-to-one
 |-----| ------------|-----------
 | ~onto | general     | injective
| onto | surjective  | bijective 

inclusion map:
- $A^{\prime} \subset A$
- $i: A^{\prime}\rightarrow A$, $i:A^{\prime} \subset A$

identity map:
- $1_a: A \rightarrow A$

restriction: (restrict domain)
- $A^{\prime} \subset A$, $f:A \rightarrow B$
- $f|A^{\prime}:A^{\prime} \rightarrow B$

extension: (extend domain)
- $f|A^{\prime} = f\circ i$, $i:A^{\prime} \subset A$
- f is extension of $f|A^{\prime}$ applied to A


relations
- notation: $(a,b) \in \mathscr{R}$ <=> $a\mathscr{R}b$
- reflexive:  $x \in A, (x,x) \in \mathscr{R}$ (D7.2)
- symmetric: $x,y \in A, (x,y), (y,x) \in \mathscr{R}$ (D7.3)
- transitive: $x,y,z \in A, if\; (x,y), (y,z) \in \mathscr{R} \;then\; (x,z) \in \mathscr{R}$ (D7.4)
- antisymmetric: $a,b \in A, (a,b), (b,a) \in \mathscr{R} \;iff\; a=b$ (D7.5)
- equivalence relation on A is reflexive, symmetric, transitive
- poset: set w/ partial ordering 
    - defined by R that is reflexive, transitive, antisymmetric(D7.6)
 - equality relation: equivalence + partial order

operator (mif)
- a function that combines members of a set
- binary operation -> function w/ 2 arguments
- well defined: the operation is a function
    - input maps to 1 output
- * <- generic symbol for operations

rings: 
- set R + two binary operators $(+, \cdot)$ if for all $a,b, c \in X$ (D14.1)
    - commutative +: $a + b = b + a$
    - associative +: $a + (b + c) = (a + b) + c$
    - identity +: exists $z \in R$ s.t $a + z = a$
    - inverse +: exists $b \in R$ s.t. $a + b = z$ 
    - associative .: $a\cdot (b\cdot c) = (a\cdot b)\cdot c$
    - distributive $\cdot$ over + : 
        - $a \cdot (b + c) = a\cdot b + a \cdot c$
        - $(b + c) \cdot a = b\cdot a + c \cdot a$
- commutative ring: $a\cdot b=b \cdot a$ for $a, b \in R$
- nonzero ring: (D14.2) (z is the additive identity)
    - no proper divisors of zero if $a, b \in R, a \cdot b=z$ then $a=z $or b=z$
- ring w/ unity:(D14.2) 
    - multiplicative identity: (z is additive identity)
        - unity $u$: $u \in R$ s.t. $u \neq z$ and $au=ua=a, a \in X$
    - multiplicative inverse: (D14.3) 
        - $a, b \in X$ s.t. $a \cdot b = b \cdot a = u$
        - b is called a multiplicative inverse of a, a & b are units of R
        - unit is any element w/ a multiplicative inverse in R (wiki: Unit(ring theory))
- integral domain ring: nonzero commutative ring w/ unit (D14.4)
- field: commutative ring w/ unity where every nonzero element is a unit (D14.4) 

group (mif)(grimaldi: D16.1)
- set  G + closed operator $*:G \times G \rightarrow G$ that satisfies
    - identity: $e, a \in G \;s.t.\; e*a = a$
    - inverses: $a,b \in G \;s.t.\; a*b = e$
    - associative: $a,b, c \in G \;s.t.\; a*(b*c) = (a*b)*c$
    - closed: $a, b, a*b \in G $
commutative (abelian): $a*b = b*a$

- theorems: (T16.1)
    1. identity is unique
    2. inverse of each element is unique
    3. left cancellation: $a, b, c \in G, ab = ac \;then\; b=c$
    4. right cancellation: $a, b, c \in G, ba = ca, \;then\; b=c$


types of groups:
* group $\subset$ monoid $\subset$ semigroups $\subset$ magma 
* magma: set + closed operation
* semigroup: magma + associative operation
* monoid group: semigroup + identity
* group: monoid + inverse
* abelian group: group + commutativity

group action 
- $\phi: G \times X \rightarrow X$
    - identity: $\phi (e, x) = x$, $x \in X, e\in G$
    - $\phi(g, \phi(h, x)) = \phi(g*h, x)$, $g, h \in G$, $x \in X$
- Example: (E16.10)
    - $a, b \in S$, $a\mathscr{R}b$ on S exists if there is an action $g \in G$ s.t. $\phi(g, a) = b$

open set
- generalization of open intervals (wiki), 
- given a closed curve, set of points within curve but not on boundary


topological space $(X,\mathscr{T})$ (TC)
- https://www.youtube.com/watch?v=tdOaMOcxY7U
- set $X$ and a topology $\mathscr{T}$ 
- topology $\mathscr{T}$ on $X$ is a collection of open sets of $X$ that satisfy the following properties: 
    - empty set $\varnothing$ and $X$ are in $\mathscr{T}$ 
    - union of elements in $\mathscr{T}$ are also in $\mathscr{T}$ 
    - any finite intersection of elements in $\mathscr{T}$ is also in $\mathscr{T}$ 
- notation: $X$ <=> $(X,\mathscr{T})$ when topology is understood
- a topology - axiomatic way to construct topological space

finer/coarser
- two comparable topologies $\mathscr{T} \subset \mathscr{T}^{\prime}$
- coarser: $\mathscr{T}$
- finer: $\mathscr{T}^{\prime}$
- data can always be represented using coarser topologies
- coarser->finer: more open sets to describe the same space

basis:
- collection of subsets $\mathcal{B}$ of $X$ is a basis for a topology on $X$ iff:
    - for each $x\in X$ there is $B \in \mathcal{B}$ s.t. $x\in B$
    - $x \in A \cap B$, $A, B \in\mathcal{B}$, at least one $C \in \mathcal{B}$ s.t. $x \in C \subseteq A \cap B$
        - if x is in the intersection of two open sets, x is in the set formed by the intersection of the sets 
    - $\mathscr{T}$ generated by $\mathcal{B}$ is coarsest topology containing $\mathcal{B}$
    - $U \subseteq X$ is open  in $\mathscr{T}$ iff for every $x\in U$, there is a $B \in \mathcal{B}$, s.t. $x \in B \subseteq U$
        - U is open if it contains a smaller open neighborhood that contains x
    - primitive elements that generate everything
open neighborhood (wolfram)
- open neighborhood $U$ of a point x is an open set containing x, $x \in U \subseteq X$
- set of open neighborhoods $U$ = $\mathscr{T}_x$
- related to free groups which are basis for other groups (something w/ minimum constraints)

continuous map: functions between topological spaces (wolfram)
- $f: X \rightarrow Y$ is continous iff the preimage of any open set is open
    - $f^{-1}U$ is open in $X$ whenever $U$ is open in Y  
- identity and composition are continuous, and the composition is associative
- topological spaces + continuous functions form a category

metagraph (S+M)
- objects a, b, c
- arrows/morphisms: f, g, h
- operations: assign to each arrow and object
    - domain: a = dom f
    - codomain: b = cod f
    - $f: a \rightarrow b$ (domain to codomain)

metacategory: metagraph + (S+M) 
- identity (operation): each object $a$ is assigned an arrow $id_a=1_a:a\rightarrow a$
- composition (operation): each pair of arrows $<g,f>$ with dom $g$=cod $f$ is assigned an arrow $g\circ f$
    - $g \circ f$: dom $f \rightarrow$ cod $g$
    - output of f is input to g
- associativity (axiom): for $a \xrightarrow{f} b \xrightarrow{g} c \xrightarrow{k}d$
    - $k\circ(g\circ f) = (k\circ g) \circ f)$ 
- unit law (axiom): for all arrows $f: a \rightarrow b$ and $g: b\rightarrow c$
    - $1_b \circ f: f$ and $g \circ 1_b: g$
    - b\c $\#1 \circ \#2$-output of #2 is input to #1

category 
- notation (S+M)
    - fx <=> f(x)
    - $g \circ f: X\rightarrow Z$, $x \mapsto g(f(x))$
    - category of all topological spaces:
        - X, Y,Z - topological spaces
        - f, g, h - continuous maps
    - category of all groups
        - X, Y, Z - groups
        - f, g, h - homomorphisms (homomorphic functions)
- category C consists of data:
    - class (aggregate) of objects
    - for every two objects $X,Y$, set $C(X,Y)$ of morphisms $f:X\rightarrow Y$ (also known as $hom_C(X, Y)$)
    - composition rule for morphisms: if $f:X \rightarrow Y$ and $g:Y \rightarrow Z$ then $gf: X\rightarrow Z$
    - composition is associative: 
        - if $h: X\rightarrow Y$, $g:Y\rightarrow Z$, $f:Z\rightarrow W$ then f(gh) = (fg)h 
        - derived from composition rule
    - identity morphism: for every object $X$,  (wiki)
        - identity $id_x:X \rightarrow X$
        - s.t for every $f: X \rightarrow Y$ there exists $f \circ id_x = f = id_y \circ f$

monoid (S+M, pg. 2)
- group w/o inverses (semi group w/ identity)
- category theory: 


homomorphism: (arrows that commute)
- f is a function homomorphism: bijection
- f is a ring homomorphism(D14.8)
    - given $(R, +, \cdot)$ and $(S, \oplus, \odot)$, $f: R \rightarrow S$
    - for all $a, b \in R$
        - $f(a + b) = f(a) \oplus f(b)$
        - $f(a \cdot b) = f(a) \odot (b)$
    - when f is onto (surjective, S is a homomorphic image of R)
- f is a group homomorphism (D16.4):
    - given $(G, \circ)$ and , $(H,*)$, $f: G \rightarrow H$ 
    - for all $a, b \in G$ , $f(a \circ b) = f(a) * f(b)$ 
    - diagram commutes:
        $G_1 \times G_1 \xrightarrow{f} G_2 \times G_2$

- isomorphism: one-to-one (injective) and onto (surjective) homomorphism
- category: function preserving composites & units 
- equivalence: bijection of a group to itself
    - identity is a homomorphism  
- homeomorphism (wiki)
    - isomorphisms in the category of topological spaces
    - mappings that preserve topological properties of a given space
- homotopy (1.6 in TC)
    - isomorphisms 

   categories:
   what are the objects, arrows, and notions of equivalence:
   - categories that have a map into set, (everything can be kinda turned into a set)
   - if we have an arrow from A to B
    - A, B are sets
    - arrow is a functor (forgetful functor)
   - equivalence
   - what is different about arrows between category of sets and category of groups? 
   - notion of equivalence:
        - isomorphism: bijection + homomorphism

Functor (covariant): from category C to category D
- object $FX$ of the category D for each object X in C
- morphism $Ff:FX \rightarrow FY$ for every morphism $f:X\rightarrow Y$
- composition: $(Fg)(Ff) = F(gf)$ for any morphism $f: X\rightarrow Y$, $g: Y\rightarrow Z$
- identity: $F id_x = id_FX$

Contravariant Functor(pull back)
- reverse arrows: for every $f:X\rightarrow Y$, the contravariant functor $F:C^{op} \rightarrow D$ assigns a morphism $Ff:FY\rightarrow FX$ 

(5) Action
(7) lense/prism/optics/profunctor
(9) Open cover
(10) Nerve (of a cover)
(11) Natural Transformation
(12) Fiber bundle
(12b) Fibration
(13) Vector bundle
(14) Covering space (see how this is just a fiber bundle with descrete fibers)
(15) section
(17) Sheaf
(18) germ
(19) Space of Continous sections related to sheaf
(20) Topological Manifold
(21) Smooth Manifold
(22) Jet 
(23) chart (local coordinates)
charts and atlas are part of the definition of a smooth manifold
the formal definition
(24) PL manifold (piecewise linear manifold)
(25) Triangulation
(26) CW complex
(27) contractable (topology)
(28) presheaf