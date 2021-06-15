# Review
The paper proposes a functional model of the structure-preserving maps from data to visual representation. The idea is to use such a functional model to guide the design of visualization libraries such as Matplotlib. It describes the visualization of data as performing a ``monoidal action" homomorphism between a pair of fiber bundles. Specifically, the data is modeled as a fibered bundle (data bundle) and the visualization representation is modeled as another fibered bundle (graphic bundle).
The structure-preserving visualization is achieved by a mapping, called the "topological artist $A$" that satisfies a set of desirable properties. Specifically, $A$ is a morphism that maps sheaf on a data bundle to a sheaf on the graphic bundle.

## Strengths:
+ The high-level idea of the paper is interesting and seemingly plausible.

## Weaknesses:
+ The paper, in the current form, is not written for a general visualization audience. Many mathematical terms are used without definitions, for instance, "fiber", "schema", etc.
+ There are a number of conjectures and claims throughout the paper that were made without justification/proofs.
+ The paper could be greatly improved if it includes a clear high-level picture of how a morphism $A$ between the data bundle and the graphic bundle is translated into programming for Matplotlib.

Detailed Comments:

+ It appears that $A$ should be a functor, but it was never explicitly stated.

+ Fig 2: There is not sufficient justification that a bar plot is continuity preserving. If this is a claim, the rigorous proof is needed.

+ Please provide more context and a precise definition of the ``fiber". The more common one is that the fiber of the element y in the set Y under a map $f: X \to Y$ is the inverse image of the singleton $y \in Y$ under $f$.

+ Line 175: "By encoding this continuity in the model as K the data model now explicitly carries information about its structure such that the implicit assumptions of the visualization algorithms are now explicit. " What are the ``implicit assumptions" of the visualization? How does this happen? Is this a conjecture/hypothesis/fact?

+ The paper would be made more readable if motivations of introducing fiber spaces and Monoid Actions were provided before their technical descriptions.

+ Line 204: "The collation of sections enabled by sheaves is necessary for navigation techniques such as pan and zoom [51] and dynamically updated visualizations such as sliding windows [27, 28]". This is another example of a statement made without justification. The references cited above do not provide a justification for the entire statement. Why are sheaves necessary in the proposed framework?

+ Line 224: is "S" a base space for the graphic space? Why is homotopy/deformation retract necessary? Is it used to guarantee continuity or structure preservation? Then why not isomorphism?

+ Line 264: "The functional decomposition of the visualization artist facilitates building reusable components at each stage of the transformation because the equivariance constraints are defined on ν, Q, and ξ." The second part of the sentence "because the equivariance constraints are defined on ν, Q, and ξ" does not provide a reasoning for the first half of the claim that "The functional decomposition of the visualization artist facilitates building reusable components..."

+ There is some disconnect between the programming in Section 4 and the mathematical arguments in section 3. For example, in Line 490: "To generate the scatter plot and the line plot, the distinction is in the $\tau$ method that is the section." How is $\tau$ representing a section based on how it is programmed?

Minor:
The paper would benefit from some proofreading. Here are a few examples of sentences that are either confusing or incomprehensible.

+ Line 18-19: "If any action is applied to the data or the visual, for example, a rotation, permutation, translation, or rescaling, an equivalent action is applied on the other side." Does the "other side mean" visualization? This sentence is confusing.

+ Line 164: "...and changing the changing the coordinate system"

+ Line 434: "to generate the visual section μthat here is the object V." This sentence is hard to parse and understand.

# Justification

The high-level idea of the paper is interesting and seemingly plausible. However, the paper would need a substantial rewrite for both a visualization audience, as well as an algebraic topology audience. The main issues include:
+ Many mathematical terms are used without definitions. The paper could be improved substantially if first motivations are provided regarding why certain notions are needed for the proposed work.
+ There are a number of conjectures and claims throughout the paper that were made without justification/proofs.
+ The paper could be greatly improved if it includes a clear high-level picture of how a morphism $A$ between the data bundle and the graphic bundle is translated into programming for Matplotlib.s