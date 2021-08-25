# go to paper (dijkstra)
* https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf
* programmer's activity is coding, but important but is execution of code
* shorten gap between static program (code) & dynamic process (execution)
* textual index to successive actions (code is text space, execution is time)
* procedures/functions needs sequence of textual indices same length as depth of the call stack
* textual/dynamic indices provide independent coordinates for tracking program progress
* go to jumps all over the coordinate system
* satisfy the requirement that a programmer independent coordinate system can be maintained
* takeaway: code & execution should be in sync

# Seperation of Scales (pydata G 2020)
* https://www.youtube.com/watch?v=P85UIuMovnI
* seperation of scales versus concerns
    - scales:
    - concerns:
* layers: code -> atoms
* dijkstra: define wider class carefully & explicitly, choose helpful generalization
* abstraction layer - anything where you name the instructions/algorithm/block of work
    - ex: click and drag blocks, configure filter, formular in excel
* target level:
    - human, code, etc - different rules for the interfaces based on the user
* information flow 
    - what parts of the code need to know what?
    - what parts of the system talk to each other?
* locked down vs. free
    - free for user to extend (public?/has interface)
    - what is backed in/non customizable (private?/buried in functions?)
* start with the minimal viable product
    - simplest working prototype
    - start from the center/locked down bit & build out
    - do we see a path to adding [feature] in future?
* what makes a good layer?
    - human/easier to use <-> computer/harder to use
    - flexible enough to solve one problem
* separation of scales
    - narrow down the big problem to the bit that's reasonable and tractable
    - keep track of simplifications though
    - theories can be discovered and derived (observed empirically and from fundamentals)
* choosing coordinates: pick the right tool for the job
    - not general enough/too general will be overly complicated in specific case
* what does scales mean in code? 
    - `request.get` -> networking code/layers implemented by the library
* constraints: ability to control means responsibility of control
* layers mean implementation details can be swapped out 
    - duck typing, polymorphism, dependency injection
    - standards and protocols: also facilitate interoperability
* limits of layers
    - non-dischargeable complexity: inherent to problem
    - layers let you hide/shift/detangle complexities
    - abstractions/layers add complexity
    - can slow things down
    - abstractions are usually leaky
    - more stuff to implement, more places to break/badly implement
* encode assumptions
    - tools are designed to solve specific problems
    - languages are also designed around specific problems
    - functions, libraries, etc are tools
    - use tools to build new tools
* tools control the expression (like languages dictate grammar, syntax, nuance)
* code is for people, most often yourself
* why? islands in ocean 
    - islands are application, land under water is library
    - volcanos vs.  matchsticks
        - volcanoes: can build new islands on slopes of other volcanoes
        - matchsticks: need to build new stacks every time
        - opensource uses the volcano model


# top:down left-right (James Powell)
- mutable defaults bad, can kinda avoid via wrapping but not decorators
  - cause interior is executed every time 
- `locals` to list local values
- dis disassemble only on pure python
- when python sees a function or class defintion, is executable code/ run time code to define
  - is why can define class in python, is a statement
`LOAD_FAST`-default or local
`LOAD_DEREF` -closure
`LOAD_CONST` - literal
- python defers lots of decision making to run time
  - top to bottom, left to right to byte code 
  - python always runs modules once on import
- - from x pulls out current
nonlocal to flag that var is in deref scope 

# tutorial 2017 pydata seattle (James Powell)
- meta-objects are a way to enforce constraints on derived objects 