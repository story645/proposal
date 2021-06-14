
# topline
Although the paper is rejected, all reviewers definitely encourage the authors to continue on this very important and promising endeavor and to resubmit a revised version taking into account their feedback and suggestions.
# Notation/Math
- Many mathematical concepts and notations are not defined or sufficiently explained, in particular for a Visualization audience (R1, R2, R3, R4)

(1) Clearly name define the notations at their introduction
(2) Illustrate the concepts introduced with claim

The paper, in the current form, is not written for a general visualization audience. Many mathematical terms are used without definitions, for instance, "fiber", "schema", etc.

 Please provide more context and a precise definition of the ``fiber". The more common one is that the fiber of the element y in the set Y under a map $f: X \to Y$ is the inverse image of the singleton $y \in Y$ under $f$.

"By encoding this continuity in the model as K the data model now explicitly carries information about its structure such that the implicit assumptions of the visualization algorithms are now explicit. " What are the ``implicit assumptions" of the visualization? How does this happen? Is this a conjecture/hypothesis/fact?

- the presentation of the mathematical framework lacks clarity for readers less familiar with theory on mappings from data to visualition and the leveraged topological concepts

## proposal 
1) illustrated equations
2) define math term when first mentioned

## --- Figures are hardly illustrative of the text:
In figure 2, is the only figure I can understand well (although it misses variable names for the top-left data table).
Figure 3 seems related to figure 2 with time and temperature but the wind speed and direction appear for the first time. The text referring to figure 3 below the caption of figure 3 tells a different story. We shall see in figure 3 the fiber tuples in full as they are written in the text.

Definition in 3.1.1 goes deeper with no more link with that use case, presenting yet new symbols and mathematical terms.
The caption of Figure 4 is not linked to the picture either. I can recognize the square as the time x temperature space, the line segment must represent the [0,1] interval, and the pile of squares the continuous set of time x temperature spaces for values of that interval. But what is K? Why is the picture not annotated with F, time, temperature, R? It makes it very hard to read the illustrations and connect them to the core text they are supposed to illustrate.

In figure 5, we should clearly see annotated in the picture: a fiber, a fiber bundle, the base space, the set of records... without the need to read the caption. The caption would come as complementary.

Figure 7 evokes a Bayesian network connecting elements from the use case in figure 2, but I couldn't figure out what the arrows mean. It seems related to partial order but I could not get the point. I see standard connectors like \geq are used in the caption but they certainly mean something else than order on the real numbers as rain and storm are text values of some "weather" categorical variable (missing in figure 2). The text referring to Figure 7 tells: "An example of monoid action equivariance is the
preservation of partial ordering illustrated in Fig. 7" which falls short to give much-needed insights.

Looking at the pieces of Python codes in section 4, I cannot tell what is new. If the novelty lies in the algorithm or the type of input and output, I suggest using a pseudo-code syntax.

+ Fig 2: There is not sufficient justification that a bar plot is continuity preserving. If this is a claim, the rigorous proof is needed.
## proposal
- overhaul figures, make them concrete and also a throughline through the whole paper -> in effect, think of it as a picture book 


# math explainations
+ There are a number of conjectures and claims throughout the paper that were made without justification/proofs.

- let for the discussion section every advanced theoretical aspect that is important but not necessary to understand the basics. Ignore others that are not relevant to the application of this model for developing coding libraries. For instance, is it really important to know right in the introduction of section 3.1 that "fiber bundles are locally trivial, meaning that over a localized neighborhood U the total space is the cartesian product KxF"? Can't it wait until the end of the paper to discuss for instance the generality of the model? Or can't it be simply removed without any practical consequence?

- The main references for using fiber bundles are Butler [19,20] and Spivak [60,61] (these references lack web link, editors, and/or doi) which are not published in visualization venues. So it is important to explain these concepts in full detail and with clear illustrations to the visualization audience likely new to them.

- For example, the detailed discussion of how zero-dimensional points and one-dimensional lines are rendered into two-dimensional objects on screen could be moved to a supplemental appendix. Both the necessity of this process and how it can be achieved are common basic computher graphics knowledge. Moving some of the non-essential detail to a supplementary appendix would provide the authors with more space to discuss potential implementations of their framework.
# proposal
i. add links/dois to those papers
ii. maybe replace spivak equation with a small diagram or pare down to just the most important bit (schemas)
iii. write a graphics appendix 
    i. this gets the S/Q figures + the G diagram
# Concrete Examples
A running end-to-end example for basic graphical representations from early concepts up to their practical implementation in Matplotlib is lacking (R1, R2, R3, R4)

- Figures are not well captioned, poorly connected to the text, and lack annotation and clarity (R1, R2)

(3) Provide an end-to-end example of how different data types (say a relational table and a graph) are represented using the model.

- define all symbols and notation in text connecting them to a single running example like the weather use case in the whole section 3.

- annotate the figures with the new mathematical symbols linked to the old graphical elements known to the visualization community. Illustrations should be the Rosetta Stone of the paper. For instance, in 3.1.1, I expect to see in figure 3 all the symbols introduced in that section connected to a familiar example, so not only F and R, but also the U, \sigma, c, T, 0...i...n from equations 3,4,5, all connected to familiar graphical elements and variables from the use case in figure 2.
## proposal
1) make all diagrams concrete, run it through the whole paper

# extensibility
- have a section to illustrate the new concepts and how they can be used to encode data and graphics in a unified space, on an additional set of different visualization use cases. That will illustrate the generality of your model evoked in the introduction (images, network, tabular data...)
## proposal
- add/replace the Q example section with this, (R4 suggests moving Q section to appendix)
- maybe have a network feeding the scatter, table feeding the line, and image feeding the image
    -> but use my one point diagrams (fade out the rest of the data in the structure)

# Aims/framing
- The model is proposed to facilitate the development of visualization libraries, but it is not clear what tasks are left to programmers and how it compares to existing approaches based on the grammar of graphics (R4)
- Many claims and conjectures linking topological concepts and graphical design are not properly proved or justified (R3, R4)
+ The paper would be made more readable if motivations of introducing fiber spaces and Monoid Actions were provided before their technical descriptions.
+ he presentation leaves it largely unclear, which parts of the visualization generation can potentially be taken over by modules based on their framework and which parts are left to the programmer or designer. Other than the specification how to access the data format, this seems to apply to the choices of suitable visual represenations, especially where semantics are concerned. For the purpose the authors address, ignorance of semantics is fine. However, the problems of this restriction should be addressed in more detail, espeically since ATP, the Grammar of Graphics, and the algebraic approach of Kindlman and Sheidegger address these issues - even though sometimes they are only considered implicitly in the choices made for the generation of examples. The consequences of this limitation become evident in the example shown in Figure 7. To solve the violation of equivariance, it would be perfectly sound mapping "rain" to the "closed umbrella", yielding v(rain) = v(storm) and thus reestablishing equivariance. However, in this case, the opened umbrella would never be rendered to the screen. The authors should openly address this issue and be clear about the tasks and responsibilities left to programmers an designers in their comparison to related work as well as in the discussion.
- it remains largely unclear what tasks are left to programmers

## proposal 
- make clearer that GoG is solving a different problem 
- make clearer that graphical design is not the right level

# comparison to matplotlib
-The paper could be greatly improved if it includes a clear high-level picture of how a morphism $A$ between the data bundle and the graphic bundle is translated into programming for Matplotlib.
- explain how the current way (say with Matplotlib) to specify visualization in code is broken (not consistent) on the same examples (images, network, tabular data...). Detail
the consequences for programmers or designers of these examples?
If possible use pseudo-code instead of Python, unless your model is specific to Python.
- then explain how your model can solve these problems and compare it to the old way (current Maplotlib). Use pieces of Python code with both the old way and the new way to ease comparison, as not everyone knows how Matplotlib works for coding visualizations.
- it remains largely unclear how exactly the framework should fit in a visualization library
- the provided examples and discussion are not convincingly addressing the claimed benefits

# proposal
- rework the framing and focus of the programming section
- possibly use my histogram figure  [data -> whole figure, data->broken out into multiples] instead of code since code is gonna get hairy

# Related work
 Discussion of some related work is missing (R2)

- C. Demiralp, C. Scheidegger, G. Kindlmann, D. Laidlaw and J. Heer, "Visual Embedding: A Model for Visualization" in IEEE Computer Graphics and Applications, vol. 34, no. 01, pp. 10-15, 2014.
https://doi.org/10.1109/MCG.2014.18

- Natalia V. Andrienko, Gennady L. Andrienko, Silvia Miksch, Heidrun Schumann, Stefan Wrobel:
A theoretical model for pattern discovery in visual analytics. Vis. Informatics 5(1): 23-42
https://doi.org/10.1016/j.visinf.2020.12.002

## proposal
these point to a failure of framing
i. visual embedding is about automatically generating and validating visualizations, but might be worth taking the notation from there - is about mapping from domain of data to range of visual embeddings/mapped perceptual space ()
ii. theory model for pattern discovery? -> has some stuff adjacent to equivariance, but is also at the automatic graphic design layer

 so can discuss them as part of what this model is not trying to do






