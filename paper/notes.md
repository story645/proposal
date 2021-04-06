Eric
- [x] It might be helpful to briefly define a homomorphism
- [x] Starting with fig. 2 on line 117, I think you may have thrown the baby out with the bath water here.  In your proposal, I feel like you motivated and explained the examples of using semantic components like time and temperature really well.  Here it just feels kinda tacked on?  If I had only read this paper I would think: I don't understand why you have this example.  What is it's point?
- [x] In this line: "A secondary 135 advantage of defining structure in terms of monoids is that they 136 are commonly found in functional programming because they 137 specify compositions of transformations" starting on 135 you say something pretty important.  Since this is kinda the crux of making this useful it would have been nice to show an example or something here.  I know you link out to two references.  But the first one 404's when I tried to click on it: https://medium.com/@michelestieven/a-monad-is-just-a-monoid-%20728%20a02bd2524f66 And the second one seems to be both hard to find, I could find it with a google search. So I definitely think it would be worth it to provide some more context here.

- [x] starting on like 142 - "For example, K can encode that the timeseries data described in Sect. 3.1.1 is continuous, but is doing so independent of the timestamps."  This actually confused me a little bit.  You might need another sentence here explaining this.

- [x] "The explicit topology is a concise way of distinguishing  visualizations that appear identical, for example heatmaps and images." starting on 156 - I love this sentence.  It is practical clear and gets the point across.

- [x] Diagram (12) definitely feels a little bit busy but at the same time I think it also is _explicit_ which is very important for conveying understanding.  I guess I don't really have much commentary here beyond that.  Maybe make the diagram a little bigger so it's easier to read?  I definitely think you need everything you put in there.

- [x] Lines 180 to 183 are great!  You continue this "theme" of explaining the mathematics well and then tying it back to something practical.

- [x] The first time I saw (17) in your proposal it honestly confused me.  But!  I feel like you've really built it up over the course of the paper and now it feels _almost_ natural.  

- [ ] lines 247 to 250 - it would be nice if you linked to a proof of this statement or maybe proved it in an appendix.  It almost feels like you are proving it from lines 250 to 268.  So maybe it would be easy to make this a proof more formally?

- [x] Fig. 6 kinda confused me more than helped me understand.

- [x] Fig 7. was very helpful!

- [x] On line 356 - 364 the line numbers for the code run a little close to the words.

Nick
- [x] My best paraphrasing of the main idea would be that this paper takes the ideas of going from data to graphic along with some important constraints that people generally agree are important and formalizes them into a topological model, then shows how that model can map into a concrete implementation. 
The important part of this model is that it models the data sufficiently abstractly that it's able to work with basically any form or type of data. The sentence starting at line 489 seems to be the big "aha" to me, basically saying something like "if you implement things such that the code equivalents of these terms are separated in some specific way, then you get these important formally-describable properties". Is that right? If so, I'm left very curious about what alternative (possibly already-existing?) Artist implementations there might be that seem to work, but don't decompose things in this way, and therefore don't have these important properties. Or maybe the existing implementations do have these properties but aren't general enough? I know there are space constraints etc but if there was some way of showing how the current Matplotlib artists work and how they fall short of this model, that would be very enlightening I think.
- [x] On line 8 there is a reference to [40] after the word "continuity" and I didn't grasp the implications of that word, so I looked at the reference and I couldn't figure out how this reference informs that one statement. I'm still not sure about the importance and meaning of "continuity" in the way that the paper uses it. I also looked at [68] but I didn't see that paper use that word in the same way as yours. Your paper uses this word a fair bit so maybe a short definition would be helpful?
- [x] On line 42 there is a sentence starting "this same limitation" but I'm not sure what limitation this refers to? There wasn't a previous sentence that called out a limitation that I could see.
- [x] I really liked the explicit modelling of the graphic bundle as essentially "pixel space", it's really concrete and I'm not used to thinking in these terms, as I usually "stop" at a vector representation of things and let some other framework translate that to pixels (betraying my infovis orientation and that I don't tend to think of images/heatmaps first!)
- [x] I must say that I really didn't grok at all what Figure 6 is showing and how it relates to the text but I didn't dig into the references for the Steven measurement scales
- [x] In the Data Model section, I didn't understand the concept of the simplicial triangulation scheme and how it would relate to building this adaptation layer from the abstract FiberBundle and something the artist could consume: I wasn't able to make the leap from what's written here to how I might write such a wrapper/adapter from something like a data frame or numpy array into these simplices... Basically here the math-to-code equivalence is not as clear as in the other parts. My best guess is that the tau functions return things that look a fair bit like data frame rows, and the view method seems to return something that looks a bit like a data frame?

Tom
the first two sentences of the abstract are I think the clearest explanation of what you are doing!
general comments:
- [x] be careful about jargon.  e.g. L3-4 is not clear at all. I get the sense those words have very specific meanings, but not sure exactly what
- [x] can all of section 2 be distributed into the rest of text?  Make a much bigger deal about the comment on L40-42 about how you are proposing a framework to understand how to design / build the _backend_.  If this section is going to stay I would LEAD with this idea and then end with "there are many spec lanugages [47-70]
- [x] add the rocket example or something that has more than one "obviously right" key to the discussion of munzner
- [x] L84-90 the sentence is very hard to follow
- [x] can we drop the spivak commutative diagrams?  There is not enough in the text to actually explain them.  What is the _minimal_ amount of notation / explaination we can get away with here?  We mostly seem to need "we _can_ describe the individual fibers" but do not do anything with that description other than assert it exists
- [x] fix the figures so the labels are not pixelated, the script font is cute, but is a bit hard to read
- [x] describe a monoid's properties in words not equations as I do not think you ever refer back to them and I think we can assume the reader knows what assciativity and an identity element is
- [x] drop quotient space comment, it is not used again
- [x] notation around eq 10 and the text below seems a bit miss-matched?
- [ ] in eq 11 it is a bit off to me that  k went away entirely
- [x] description of why we need sheafs is a bit too informal (L180)
- [x] L208 "a k that is 0D in K" is a bit odd as k is a point, it is K that has 0D connectivity. Good example, but the wording needs to be clearer
- [x] L231 Are you sure "latent space" is safe to use here?
- [x] L271: is partial ordering the _only_ monoid of interest or one of many possible monoids (just as Steven's scales are each examples of groups)
- [x] the caption and figure in fig 7 are miss-matched on the space vs element of the space notation.
- [x] L286 I am skeptical that we can not find a valid mapping from V to H for ever section.  We have tools to build connected components and if we introduce mappings that depend on both the distance along and distance across a line what is a rho we can not find a section in V to map to?
- [x] eq25 to the one before 28 (which is not numbered?) do not share consiistent notation.  For example in 25 there is no mention of size, but it shows up in the un-number equations right below it
- [x] the hat on all of the n is miss-aligned
- [ ] is it worth mentioning that \rho looks a lot like a shader?
- [x] L384 do not be so apolgetic about using objects.  I would go with using objects to manage input to functions, transfrom + draw is still _structurally_ functional, but objects are way nicer to work with than closures
- [x] use the math terms as the variable names rather than as commens?
- [x] L400 refer back to sheafs
- [x] L421 no need to explain Matplotlib.collections
-  [x] class Point : no default values on parameters.  it is confusing to your point here and from a SWE perspective belongs higher up the stack
- [x] the FiberBundle should be an instance not class attribute
- [ ] I am not sure that this code actually makes things clearer.  To understand it you have to guess a lot about what various structures mean, which keys are "free" and which have special meaning and to have a deep understanding of mpl internals to understand the `self.set_xyz` calls.
- [x] start the discussion with the first two sentences of the abstract
- [x] the limitations section does not make sense to me.  Is this a mandated section?  I would not call "we have not done it yet" a limitation
- [x] in the conclusion I would again start with the first two sentences of the abstract and focus on we are not worried about _why_ the user wants to plot a thing or what it means _to the user_, we just want to make sure that we do the plotting they asked for in a way that it _formally_ correct (e.g. the continuity and the equivariance are preserved)
- [x] https://github.com/matplotlib/matplotlib/issues/19787 is I think a very good case study as to why we need this work
between PathCollection and PathCollection3D there is a big mush of data storage, mapping to V (in stages!) and assembly.  Because it was all mixed up it is super brittle and confusing and got broken.  I think there is a moral there about focusing solely on the user facing input and output, it is far too easy to lose sight of the importance of internal structure and design