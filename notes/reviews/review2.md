# The Review
The paper proposes a functional model of maps between data and their graphical representation which aims to guide the development of visualization code. The model preserve continuity (type of data matches with the type of visual encoding) and equivariance (change in data matches with change in graphics).
The model uses topological concepts of bundles and fibers to generalize to any type of data and data changes. Concepts are defined and a prototype based on Matplotlib is proposed for simple graphics.

*** Major strengths: ***
+++ The proposed model is very generic to encompass any type of data and mapping.
+++ The model can help develop robust, modular, extendable code for a visualization based on its coherent and consistent framework.

*** Major weaknesses: ***
--- The paper presents many mathematical concepts new to most of the Visualization audience but without sufficient clarity. For instance, some symbols like the curvy arrow and other abstract notations are used without a clear definition. In equation (2), what are F, E, \pi, and K based on the element I could find in the illustration in figure 2 (date, temperature, frequency, weather category, data table, line chart, bar chart, color, arrow, text, color channels, glyphs, position...)?

--- Figures are hardly illustrative of the text:
In figure 2, is the only figure I can understand well (although it misses variable names for the top-left data table).
Figure 3 seems related to figure 2 with time and temperature but the wind speed and direction appear for the first time. The text referring to figure 3 below the caption of figure 3 tells a different story. We shall see in figure 3 the fiber tuples in full as they are written in the text.

Definition in 3.1.1 goes deeper with no more link with that use case, presenting yet new symbols and mathematical terms.
The caption of Figure 4 is not linked to the picture either. I can recognize the square as the time x temperature space, the line segment must represent the [0,1] interval, and the pile of squares the continuous set of time x temperature spaces for values of that interval. But what is K? Why is the picture not annotated with F, time, temperature, R? It makes it very hard to read the illustrations and connect them to the core text they are supposed to illustrate.

In figure 5, we should clearly see annotated in the picture: a fiber, a fiber bundle, the base space, the set of records... without the need to read the caption. The caption would come as complementary.

Figure 7 evokes a Bayesian network connecting elements from the use case in figure 2, but I couldn't figure out what the arrows mean. It seems related to partial order but I could not get the point. I see standard connectors like \geq are used in the caption but they certainly mean something else than order on the real numbers as rain and storm are text values of some "weather" categorical variable (missing in figure 2). The text referring to Figure 7 tells: "An example of monoid action equivariance is the
preservation of partial ordering illustrated in Fig. 7" which falls short to give much-needed insights.

Looking at the pieces of Python codes in section 4, I cannot tell what is new. If the novelty lies in the algorithm or the type of input and output, I suggest using a pseudo-code syntax.

--- In general, I struggled to understand the syntax so I could not access the semantics. Illustrations are mostly useless as they do not connect well to the concepts and symbols in the text. Lacking a base understanding of section 3, I could not evaluate the remaining of the work.

--- Missing related work:
The related work section misses a discussion of the following references:

- C. Demiralp, C. Scheidegger, G. Kindlmann, D. Laidlaw and J. Heer, "Visual Embedding: A Model for Visualization" in IEEE Computer Graphics and Applications, vol. 34, no. 01, pp. 10-15, 2014.
https://doi.org/10.1109/MCG.2014.18

- Natalia V. Andrienko, Gennady L. Andrienko, Silvia Miksch, Heidrun Schumann, Stefan Wrobel:
A theoretical model for pattern discovery in visual analytics. Vis. Informatics 5(1): 23-42
https://doi.org/10.1016/j.visinf.2020.12.002


*** Suggestion to improve the presentation of this work: ***

- define all symbols and notation in text connecting them to a single running example like the weather use case in the whole section 3.

- annotate the figures with the new mathematical symbols linked to the old graphical elements known to the visualization community. Illustrations should be the Rosetta Stone of the paper. For instance, in 3.1.1, I expect to see in figure 3 all the symbols introduced in that section connected to a familiar example, so not only F and R, but also the U, \sigma, c, T, 0...i...n from equations 3,4,5, all connected to familiar graphical elements and variables from the use case in figure 2.

- have a section to illustrate the new concepts and how they can be used to encode data and graphics in a unified space, on an additional set of different visualization use cases. That will illustrate the generality of your model evoked in the introduction (images, network, tabular data...)

- explain how the current way (say with Matplotlib) to specify visualization in code is broken (not consistent) on the same examples (images, network, tabular data...). Detail
the consequences for programmers or designers of these examples?
If possible use pseudo-code instead of Python, unless your model is specific to Python.

- then explain how your model can solve these problems and compare it to the old way (current Maplotlib). Use pieces of Python code with both the old way and the new way to ease comparison, as not everyone knows how Matplotlib works for coding visualizations.

- let for the discussion section every advanced theoretical aspect that is important but not necessary to understand the basics. Ignore others that are not relevant to the application of this model for developing coding libraries. For instance, is it really important to know right in the introduction of section 3.1 that "fiber bundles are locally trivial, meaning that over a localized neighborhood U the total space is the cartesian product KxF"? Can't it wait until the end of the paper to discuss for instance the generality of the model? Or can't it be simply removed without any practical consequence?

The main references for using fiber bundles are Butler [19,20] and Spivak [60,61] (these references lack web link, editors, and/or doi) which are not published in visualization venues. So it is important to explain these concepts in full detail and with clear illustrations to the visualization audience likely new to them.

# Justification
## Major strengths:
+++ The proposed model is very generic to encompass any type of data and mapping.
+++ The model can help develop robust, modular, extendable code for a visualization based on its coherent and consistent framework.

## Major weaknesses:
--- The paper presents many mathematical concepts new to most of the Visualization audience but without clarity.
--- Figures are hardly illustrative of the text
--- In general, I struggled to understand the syntax so I could not access the semantics.
--- Missing related work

In short, the paper is very interesting and commendable to advance the theory of visualization but calls for advanced topological concepts and is targeted to programmers of visualization libraries.
A very tiny niche of the visualization audience is likely to master both Topology and the art and science of coding visualization libraries, so could grasp this paper effortlessly. Therefore, the paper requires a thorough effort in presentation and clarity.

# Summary
The four reviewers consider the topic of this paper is of great interest.
However, it requires additional effort on presentation and justification that would take more than the time given for the revision cycle, hence the consensus on taking a reject and resubmit decision.

Here below is a summary of the major weaknesses:
- Many mathematical concepts and notations are not defined or sufficiently explained, in particular for a Visualization audience (R1, R2, R3, R4)
- Many claims and conjectures linking topological concepts and graphical design are not properly proved or justified (R3, R4)
- Figures are not well captioned, poorly connected to the text, and lack annotation and clarity (R1, R2)
- A running end-to-end example for basic graphical representations from early concepts up to their practical implementation in Matplotlib is lacking (R1, R2, R3, R4)
- The model is proposed to facilitate the development of visualization libraries, but it is not clear what tasks are left to programmers and how it compares to existing approaches based on the grammar of graphics (R4)
- Discussion of some related work is missing (R2)

Reviewers also provide more detailed comments and propose suggestions that we strongly recommend considering for improving the presentation of this work.

Although the paper is rejected, all reviewers definitely encourage the authors to continue on this very important and promising endeavor and to resubmit a revised version taking into account their feedback and suggestions.