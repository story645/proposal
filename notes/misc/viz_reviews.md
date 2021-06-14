
# topline
Although the paper is rejected, all reviewers definitely encourage the authors to continue on this very important and promising endeavor and to resubmit a revised version taking into account their feedback and suggestions.


# Notation
- Many mathematical concepts and notations are not defined or sufficiently explained, in particular for a Visualization audience (R1, R2, R3, R4)

(1) Clearly name define the notations at their introduction
(2) Illustrate the concepts introduced with claim

## proposal 
1) illustrated equations
2) define math term when first mentioned

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
- add/replace the Q example section with this, 
- maybe have a network feeding the scatter, table feeding the line, and image feeding the image
    -> but use my one point diagrams (fade out the rest of the data in the structure)

# Aims/framing
- The model is proposed to facilitate the development of visualization libraries, but it is not clear what tasks are left to programmers and how it compares to existing approaches based on the grammar of graphics (R4)
- Many claims and conjectures linking topological concepts and graphical design are not properly proved or justified (R3, R4)

## proposal 
- make clearer that GoG is solving a different problem 
- make clearer that graphical design is not the right level


# Related work
 Discussion of some related work is missing (R2)

- C. Demiralp, C. Scheidegger, G. Kindlmann, D. Laidlaw and J. Heer, "Visual Embedding: A Model for Visualization" in IEEE Computer Graphics and Applications, vol. 34, no. 01, pp. 10-15, 2014.
https://doi.org/10.1109/MCG.2014.18

- Natalia V. Andrienko, Gennady L. Andrienko, Silvia Miksch, Heidrun Schumann, Stefan Wrobel:
A theoretical model for pattern discovery in visual analytics. Vis. Informatics 5(1): 23-42
https://doi.org/10.1016/j.visinf.2020.12.002

## proposal
these point to a failure of framing, so can discuss them as part of what this model is not trying to do






