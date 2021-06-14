# The Review
The paper proposes a model to map from data to visual encoding with very useful properties, such as equivariance that enables converting from the visual encoding back to the data.

The main issue I have with the submission is readability, even for a theory paper.

# Justification
The submission proposes a model to map data to visual representation such that visualization libraries can be data-type agnostic and to ensure mapping continuity between data and representation. These are very useful and beneficial properties for a model and can greatly formalize the development of visualization libraries.

The main concern I have with the submission is its lack of readability. To me, it is unacceptable that notations are not clearly defined when introduced. Take Section 3.1 as an example, the first paragraph introduces a tuple (E, K, π, F). None of the notations are defined in that paragraph. F is mentioned as "data in F", K is " continuity represented in K", and neither E nor π is mentioned. Strangely, a new concept of "a localized neighborhood U" is introduced that is not represented in (2). I have to confess I have no idea what this paragraph means by the time I finished reading it. To be fair, the meaning of these variables are revealed in subsequent sections, but I believe it will help the readers if these variable are at least named, if not defined, in the introductory paragraph, especially since there are a lot of variables and concepts in this submission. Some concepts and notations seem not be defined. For example, continuity, pull back, and the arrow with a curly hook at the left side.

Perhaps due to the amount of concepts and notations, it is hard to see how the claims are realized in the submission. The model is data-agnostic, so how does it encode trees and graphs? I suspect it is achieved in the base space K, but it is not explicitly stated.

The model proposed is rich and flexible, which can be beneficial but may also make the model difficult to apply in practice. Applying the model to datasets and visual encodings will illustrate the need of the richness.

In short, I'd recommend:
(1) Clearly name define the notations at their introduction
(2) Illustrate the concepts introduced with claims
(3) Provide an end-to-end example of how different data types (say a relational table and a graph) are represented using the model.




