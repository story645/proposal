set 
- finite or infinite collection of objects (elements), (grimaldi)
- elements are members of a set (grimaldi)
- order has no significance (wolfram)
- repetition (multiplicity) may or may not be ignored (wolfram)
    - sets w/ repetition are bags and/or multisets

poset (Grimaldi)
- set w/ partial ordering
- partial ordering defined by relation R that is (D7.6)
    - reflexive:  x \in A, (x,x) in R (D7.2)
    - transitive: x,y,z \in A, if (x,y), (y,z) \in R then (x,z) in R (D7.4)
    - antisymmetric: a,b in A, (a,b), (b,a) \in R iff a=b (D7.5)
- notation: (a,b) \in R <=> aRb

operator (mif)
- a function that combines members of a set
- binary operation -> function w/ 2 arguments
- well defined: the operation is a function
    - input maps to 1 output
- * <- generic symbol for operations

group (mif)(grimaldi: D16.1)
- set  X + closed operator *
- identity: e, a \in X s.t. e*a = a
- inverses: a,b \in X s.t. a*b = e
- associative: a,b, c \in X s.t. a*(b*c) = (a*b)*c 
- closed: a, b, a*b \in X
- abelian: a*b = b*a (commutativity) 
- theorems: (T16.1)
    1. identity is unique
    2. inverse of each element is unique
    3. left cancellation: a, b, c \in G, ab = ac then b=c
    4. right cancellation: a, b, c \in G, ba = ca, then b=c

function types:
![](figures\function-mapping.png)
https://www.mathsisfun.com/sets/injective-surjective-bijective.html
- functions: (grimaldi: D5.3)
    - $f: A \rightarrow B$ is a relation in which every element of A appears exactly once as the first component -> (function must be deterministic, each input has one output)
    - image: $(a,b) \in f$, 
        - b is image under a f
        - a is preimage of b under f 
- one-to-one/injective: (grimaldi: D5.5)
    - b is the image of at most one a, for all $a1, a2 \in A$, f(a1) = f(a2), a1=a2
- onto/surjective: (grimaldi: D5.9)
    - f(A) = B, for $b \in B$ at least one $a \in A$ s.t. f(a)=b

- morphisms: (Grimaldi) 
    - given (G, $\circ$), (H,*), $f: G \rightarrow H$
    - homomorphism: f is group homomorphism (D16.4)
        - a,b $\in$ G, f(a $\circ$ b) = f(a) * f(b) 
    - isomorphism: 
        - f is a a one-to-one (injective) and onto (surjective) homomorphism
action: 


category
- notation
    - fx <=> f(x)

-


monoid
- group w/o inverses
- category theory: object M w/ two morphisms:
    - multiplication: $\mu: M \bigotimes M \rightarrow M$ 
        - domain: product category
    - unit: $nu: I \rightarrow M$

    - 
(2) 


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