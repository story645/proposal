set 
- finite or infinite collection of objects (elements), (grimaldi)
- elements are members of a set (grimaldi)
- order has no significance (wolfram)
- repetition (multiplicity) may or may not be ignored (wolfram)
    - sets w/ repetition are bags and/or multisets

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

group (mif)(grimaldi: D16.1)
- set  X + closed operator *
- identity: $e, a \in X \;s.t.\; e*a = a$
- inverses: $a,b \in X \;s.t.\; a*b = e$
- associative: $a,b, c \in X \;s.t.\; a*(b*c) = (a*b)*c$
- closed: $a, b, a*b \in X $
- commutativity: $a*b = b*a$  
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
- Example: (16.10)
    - $a, b \in S$, $a\mathscr{R}b$ on S exists if there is an action $g \in G$ s.t. $\phi(g, a) = b$

function types:
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


- continuous map: functions between topological spaces (wolfram)
    - $F: X \rightarrow Y$ is continous iff the preimage of any open set is open


homomorphism: (Grimaldi) 
- given (G, $\circ$), (H,*), $f: G \rightarrow H$
- f is a group homomorphism (D16.4)
    -  a, b $\in$ G, f(a $\circ$ b) = f(a) * f(b) 
- isomorphism: one-to-one (injective) and onto (surjective) homomorphism

category
- notation
    - fx <=> f(x)
    - $g \circ f: X\rightarrow Z$, $x \mapsto g(f(x))$
    - category of all topological spaces:
        - X, Y,Z - topological spaces
        - f, g, h - continuous maps
    - category of all groups
        - X, Y, Z - groups
        - f, g, h - homomorphisms (homomorphic functions)



monoid (S+M, pg. 2)
- group w/o inverses (semi group w/ identity)
- category theory: 
-


(5) Action
(6) Functor
(7) Topology
(8) Open set
(9) Open cover
(10) Nerve (of a cover)
(11) Natural Transformation
(12) Fiber bundle
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
(24) PL manifold (piecwise linear maniofld)
(25) Triangulation
(26) CW complex
(27) contractable (topology)
(28) presheaf