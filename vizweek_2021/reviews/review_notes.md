# review notes
## Review 1

### The Review
The paper proposes a model to map from data to visual encoding with very useful properties, such as equivariance that enables converting from the visual encoding back to the data.

The main issue I have with the submission is readability, even for a theory paper.

### Justification
The submission proposes a model to map data to visual representation such that visualization libraries can be data-type agnostic and to ensure mapping continuity between data and representation. These are very useful and beneficial properties for a model and can greatly formalize the development of visualization libraries.
    * break away from data type agnostic, define type + continuity agnostic but not in an auto generation 
    * generalize about continuity rather than data type agnostics
    * sections are instances of types defined by the class fiber, sections are points, schema is fiber is return type of the section
    * be clearer that it's type of data rather than data type -> have enough examples w/ enough complexity, so if misunderstanding it's clear where the misunderstanding shakes out
        * sections of line bundles on a sphere, wind bundles on a sphere, 
        * fiber type + base space + tangent bundles, multiple two plane bundles over the sphere - 
            * sphere cross R2<- different total space than wind direction
            * no corners in smooth function, constraints on functions that can be sections is part of the type
    * how much to simplify and present simplification w/o losing the generality
    * if you want to do in the general case, things get more complicated/ b\c have to be more careful w/ith what you say. Examples become more complex -> restrict to the set. 
    * are there any locally trivial bundles which are non-trivial - maybe make the sphere the worked example of the paper
        * windfield, functions on the sphere -> tell people we need to devide sphere into regions + rules for how function agress on overlaps, function which translates from one to the other, 
            - temperature: just define in terms of theta and phhi
            - windfield: can't do the above, need the non-triviality
            - needs not strong enough to carry the extra sophistication, 
            - backed into a corner where any non-trivial situation is either to do non-trivial
            - maybe move into discussion?
    * full model of these sections, 
        * covering of the earth, nerve is tetrahedera
            - cover the sphere w/ contractable open sets?
            - any intersection of open sets that cover a space 
                - elements of the open cover & intersections are contractable
                - all these intersections are simple
        * can we break it into simple pieces and move the complexity into gluing rules
        * maybe move the discussion of sheaves up as part of the FB intro (or maybe move into an implementation math section or frame them that way?)
        ) 
        * break space up into pieces where each piece is a simplacial complex
            * fiber bundles are most powerful w/ gluing rules, structure of the section is gonna have the nerve baked into it 
            * size and gridding and the like are part of the type 

The main concern I have with the submission is its lack of readability. To me, it is unacceptable that notations are not clearly defined when introduced. 
    * can introduce/define as part of introduction

Take Section 3.1 as an example, the first paragraph introduces a tuple (E, K, π, F). None of the notations are defined in that paragraph. F is mentioned as "data in F", K is " continuity represented in K", and neither E nor π is mentioned.
    * put it all in a paragraph, actually explain these things,
        * F is the fiber of a fiber bundle with total space E, base space K, projection map E->K, type of the inverse map of ... w. references -> we think of these things as encoding data, type, continuity, we're generalizing functions, 
        * section can be thought of as a function from K to F
        * F as a fiber is a model of the return type of the section -> schema
        * locally trivial means is a cartesian product of
        * we will argue that for representing data as a section of the fiber bundle, benefit of that is ways of representing continuity, decompose complex data into pieces in a sensible way, 
            * section of the fiber bundle
            * tuple E..., F is ... inverse image...model for point over the base space...
            * in the case base space trivial, then F is the return type


Strangely, a new concept of "a localized neighborhood U" is introduced that is not represented in (2).
    * track down what this even was 
    * locally trivial bundle -> take any point in k, can find an open neighborhood U \subset K, makes FB into trivial pieces
    * functions on sphere as quotients on polynomials, group of functions: can instead think of them as coefficients/collections over polynomials, u1/u2/u3/u4 and forget about the space - coefficients from one space to another, don't need space anymore, coefficents from one part to the other 
        * different perspectives of manifolds, can generate rules on how those coeffecients are connected to each other, space can disappear -> sheaf is rule for going from one section to another, how we can derive rules given new subset of sections
        * what are the rules for a section on an overlap?  sheaf is bookeeping how functions are related to each other
            * sheaf is gluing the rules
            * presheaf is coherence on restriction? # look this up more
            * temperature on earth sampled on points in numpy array, 3 meter triangle universal addressing system - over those things, any wind field is trivial, a million tables and high resolution tables , working with compute functions how to go from patches of addresses to wind field, have to agree on boundary, transfrom functions from into other and how it looks like on overlap, - temperature needs to agree on intersection 
            * sheaf  is the glue rules -> is a black box which lets us kick out the structure 
            * presheaf is to restricted part? 
            * category theory just kicks it up to being maps and functors

I have to confess I have no idea what this paragraph means by the time I finished reading it. To be fair, the meaning of these variables are revealed in subsequent sections, but I believe it will help the readers if these variable are at least named, if not defined, in the introductory paragraph, especially since there are a lot of variables and concepts in this submission. Some concepts and notations seem not be defined. For example, continuity, pull back, and the arrow with a curly hook at the left side.

Perhaps due to the amount of concepts and notations, it is hard to see how the claims are realized in the submission. The model is data-agnostic, so how does it encode trees and graphs? I suspect it is achieved in the base space K, but it is not explicitly stated.

The model proposed is rich and flexible, which can be beneficial but may also make the model difficult to apply in practice. Applying the model to datasets and visual encodings will illustrate the need of the richness.

In short, I'd recommend:
(1) Clearly name define the notations at their introduction
    * 
(2) Illustrate the concepts introduced with claims
    * 
(3) Provide an end-to-end example of how different data types (say a relational table and a graph) are represented using the model.
    * 



