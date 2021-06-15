# Review
The paper discusses a topological model for mapping data to graphical representations focusing on the preservation of continuity and equivariance. To this end, the authors adopt well-known formalisms of the generation of (compound) visual represenations from data and reinterpret them as morphisms on topological fibers, more precisely, homomorphisms on monoids. This enables the formation and specification of a mathematically sound underpining for a set of transformations that can be implemented into an automated visualization library following the paradigm of functional programming. In particular, the framework allows to abstract away from the strong binding between data structure and visualization generation that is common to most visualization applications. Its main contribution to the field thus is less on the side of the mathematical formalism but more on the perspective of a practical approach of decoupling data processing and visualization generation that should allow for easily exchangeable visualization composition modules being applicable to a variety of data sets in different formats.

The overall discussion of the paper focuses much more on the mathematical details than on the practical implications. Although the detailed discussion is to be valued, the amount of detail leaves only little space for the discussion of practical and implementation aspects.

Although the related work section is rather short and concentrates mainly on application libraries, the choice of references is sound given the very specific (but still quite influential!) issue addressed by this paper. The authors should, however, be more precise on how exactly their solution is meant to fit in those libraries. The presentation leaves it largely unclear, which parts of the visualization generation can potentially be taken over by modules based on their framework and which parts are left to the programmer or designer. Other than the specification how to access the data format, this seems to apply to the choices of suitable visual represenations, especially where semantics are concerned. For the purpose the authors address, ignorance of semantics is fine. However, the problems of this restriction should be addressed in more detail, espeically since ATP, the Grammar of Graphics, and the algebraic approach of Kindlman and Sheidegger address these issues - even though sometimes they are only considered implicitly in the choices made for the generation of examples. The consequences of this limitation become evident in the example shown in Figure 7. To solve the violation of equivariance, it would be perfectly sound mapping "rain" to the "closed umbrella", yielding v(rain) = v(storm) and thus reestablishing equivariance. However, in this case, the opened umbrella would never be rendered to the screen. The authors should openly address this issue and be clear about the tasks and responsibilities left to programmers an designers in their comparison to related work as well as in the discussion.

The mathematical framework itself is discussed in sufficiently detail. Although the presentation is very abstract, it can be followed well by a reader who is well familiar with topological fibers as well as the common formalisms of mappings from data to graphical representations. However, given the wideness of visualization as a field, it can be doubted that this is a common combination of knowledge within the visualization community - at least in the depth required to easily follow the mathematical discussion. Towards a more intuitive understanding of what the authors attempt to achieve, they should consider adding a running example along whith the various different mapping operations can be discussed. The weather-umbrella-example shown in Fig. 7 would certainly be a good candidate for such an attempt - it is sufficiently small and simple but still covers all the necessary components to understand the underlying idea. The choices of monoids as an underlying structure is sound as it integrates well with the ideas of functional programming. The detailed mathematical presentation is welcome but tends to exceed the necessary amount of detail to understand the underlying concepts at some points. For example, the detailed discussion of how zero-dimensional points and one-dimensional lines are rendered into two-dimensional objects on screen could be moved to a supplemental appendix. Both the necessity of this process and how it can be achieved are common basic computher graphics knowledge. Moving some of the non-essential detail to a supplementary appendix would provide the authors with more space to discuss potential implementations of their framework.

Clearly, the most significant weakness of this paper are the provided examples. They are simply too minimal to convincingly demonstrate the benefits of following th proposed formalism in application design. The authors claim that their approach improves maintainability, extendability, scalability, and concurrency in the architectural design of visualization software libraries. However, none of these aspects is addressed directly, neither in the mathematical discussion, nor in the implementation details provided for the results or in the discussion. Although a reader familiar with the underlying concepts and having a certain level of experience in the python programming language certainly will be able to infer the implications for software design decisions, they should be discussed explicitly as this is part of the paper's main contribution. Although the mathematics are discussed in deep detail, it is not immediately clear, how exactly the framework should be integrated into the design of a visualization library. The very minimalistic examples do not address this issue directly and appear to leave out important details about the implementation, especially concerning the specification of data access and the choice for an actual mapping. Again, the role of the framework in the visualization process has to be distinguidhed better from the roles of the programmer and the visualization designer. This should be supported by a proof of concept demonstrating the actual generation of a visualization from real-world data set and thereby giving an impression what makes the difference in using one of the common existing libraries compared to a library whose architecture would apply the formalism proposed in this paper. This kind of comparison is necessary to convincingly point out the benefits of the proposed mathematical framework for library development and application.

The discussion is rather short. The achievements claimed, especially the coverage of different data formats, are neither immediately clear, nor discussed in due detail. Although the mathematical framework is doubtlessly general enough to support this claim, it appears that the specification of the actual mappings will be quite non-trivial, especially for complex data structures. There seems to be a significant complexity gap between the mathematical formalism and the actual implementation that is neither resolved by the provided examples, nor by the discussion. Again, the authors need to make clear the difference between and benefits for an actual programmer following their approach rather than, for example, a grammar-based specification such as Vega-Lite.

In summary, while providing a very detailed discussion of the underlying mathematics, the provided examples, implemenation details, and discussion are not convinvingly supporting the potential major contribution of this paper - namely the provision of a mathematical framework that allows for an architecure of visualization libraries that are more maintainable, extendable, scalable, and provide better support for concurrency than existing libraries. Especially the apparant complexity gap between the mathematical formalism and the actual implementation has to be resolved. Other than that, the claimed benefits need to be discussed in more detail and the examples need to be extended in order to convincingly demonstrate that these claims are actually achievable. Towards better understandability, the authors should also consider providing a running example in the theory section and a more in-depth discussion of how exactly the proposed framework is meant to fit into a visualization library, what exactly it is meant to solve, and what it leaves to the programmer and the visualization designer.

Designing a mathematically sound underpinning for the support of visualization application libraries is admittedly quite an abstract and certainly a very challenging objective. There is also quite a lot potential to be seen in the approach discussed in this paper. However, in its current form, the discussion is too abstract and too technical to convincingly communicate the potential benefits of applying the proposed approach. Unfortunately, addressing these issues requires an amount of restructuring that can hardly be achieved within the short review cycle available for VIS. Therefore, the paper should not be accepted in its current form. However, the authors should be strongly encouraged to continue this very interesting work and to resubmit a revised version of this paper.
Marked-up Copy of the Paper
(no file)

# Justification
The paper discusses a potential mathematical framework for the architecture of visualization libraries. The underlying mathematical framework and the approach of specifying visualizations as mapping from data to graphical representations are not new. Therefor, the main contribution is the application of existing theory into a mathematically sound theoretical underpinning for a modular software architecture framework.

Major strengths:
+ solid mathematical underpinning
+ detailed discussion of the underlying mathematics

Major Weaknesses:
- it remains largely unclear what tasks are left to programmers
- it remains largely unclear how exactly the framework should fit in a visualization library
- the provided examples and discussion are not convincingly addressing the claimed benefits
- the presentation of the mathematical framework lacks clarity for readers less familiar with theory on mappings from data to visualition and the leveraged topological concepts

In summary, the weaknesses outweigh the strengths of this paper and the paper should therefore be rejected. However, there is undoubtedly some interesting potential in this approach and the authors should therefore be encouraged to resubmit a revised version of the paper