## Goals
1) on track and back on track?
2) discuss to resolve it
### Proposal Due April 16
- [ ] revise and resubmit based on committee feedback 
    - [ ] (1) Audience: lower-level visualization library developers, domain specific library developers (continuing the architecture choices mpl made)
    - [ ] (2) Need: unified model: continuity + equivariance 
            - [ ] mpl works, unmaintainable, grew organically, this stuff is buried implicitly, gives a way to make it clear
            - [ ] interactivity screen space back to data space, different implicit data than API incoherancy than bug?
                - [ ] currently done in adhoc manner, want to enforce contracts for the interactivity 
            - [ ] redesign that reliably enforces these constraints 
            - [ ] library that supports all the data 
                - [ ] relational tables, and images, and data cubes (with coordinates), and networks, and other data structures
                - [ ] streaming and concurrency 
                - [ ] blob the same? - model explains why this should be true
            - [ ] framework to enforce invariance at the architecture level
            - [ ] match engineering w/ math
    - [ ] (3) Proposed solution: 
        - [ ] functional math model, structure/type preserving 
    - [ ] (4) Novelty:
        - [ ] functional architecture
        - [ ] explicitly expressing continuity
    - [ ] (5) Benefits: 
        - [ ] functional: robustness, concurrency, modularity, proves that reliably, backfit needs to this 
    - [ ] (6) Evaluation: The method of evaluation to verify that the proposed solution delivers the stated benefits must be given.
            The best justifications explicitly discuss particular choices in the context of several possible alternatives.
            1. Case studies in the form of implementations (is this feasible) 
            2. Comparison w/ existing implementation          
    - [ ] (7) More specific discussion of what will be done and on what timeline.
            [quarterly gantt charts?]
 [] close out board https://github.com/story645/proposal/projects/3
