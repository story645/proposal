There are a few key principles we are trying to achieve here. The first principle is a functional framework. Even though a library may be implemented in an object oriented, declarative or imperative language, we are trying to factor the code to be nearly purely functional. There should be almost no state needed in the description, and IO, as in languages like Haskell, is kept under tight control. Again, the actual implementation may break this, but the mathematical description is to remain close to pure functional. The reasons for this are the usual list, robustness, ease of extension, parallelism, ability to handle stream processing, speed, etc.

Retinal variable transformations determine or change the aesthetics of a visualization (in the language of GoG/ggplot), but in this realm we do not change its semantics. For example a label would be bound to a color in this realm, or colors could be permuted. Other examples might include setting or changing an overall aspect ratio, or change in font. A key contribution here is in a mathematical model for the output of this layer as a well formed mathematical object.

and more. It should also handle naturally composing multiple plots. While in some cases, data first must go through a number of data transformations, eg. computing a histogram in the data transformation side, using the three realms we should be able to express all of these figures as fully as they currently are. This pushes back against the minimality of the middle realm, and the interfaces between the realms. The interfaces are only as wide as minimally needed to make it possible to create this list.





* reached: 
- Start dialog with downstream libraries
We presented our new architecture model to the scientific library development community at the SciPy 2020 maintainers track.
- Start to identify the categories of `DataSource`s and `Artist`s and their relationships
We are refactoring the library component roles and responsibility using functional programming ideas and have begun a list of constraints the library should preserve in transforming data visual representation. 
-Work out API between `Artist` and `DataSource`
* We are building prototypes of common visual representations to test if the new architecture is expressive enough to support current Matplotlib visualizations. 


moved:
- Review of architecture of other plotting packages, ready for submission to journal
In working out the architecture, we delayed the literature review to scope it based on the proposed architecture changes. 


* missed: 
- collect user stories of plotting needs
We have been collecting user stories informally but need to document this formally.
- Build a `DataSource` and `Artist` pair Minimal Viable Product with downstream partner
- Prototype a high-level API with downstream partner
We need to more thoroughly work out our prototypes before partnering with a downstream library. 
