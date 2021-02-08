### in progress (trash version done):
 * thesis statement)
 * lit review 
    * ggplot is in bullet points
 * math/theory
    * math is in bullet points/glossery
    * simplex & render figures, 
 * implementation
    * line, scatter, bar, grouped bar
    * k=0 simplex, k=1 simplex, Iris data, Iris aggregated
 ### outstanding
 * background/lit review
 * math in paragraph write ups
 * implementation write up tied back to math
 * conclusion/proposal for further work - can steal from proposal?
        
# tasks: moved to https://github.com/story645/proposal/projects/3
- [x] in progress: math in paragraph write up + figures
    - [x] pin down equation pipeline
         - [x] Data fiberbundle: (E, F, \pi, K, \tua)
         - [x] Render fiberbundle: (H, D, \pi, S, \rho)
         - [x] Visual fiberbundle: (V, P, \pi, K, \mu)
         - [x] screen-data: \xi: S->K
         - [x] style hop: \nu: E-> V
         - [x] assembly hop: Q: V-> H (\mu holds together the aesthetics on each K so Q doesn't have to
         - [x] artist: Q(\xi\mu) <-> rho, A: E-> H    
    - [x] go back in and latex define:
         - [x] fiber bundles:(total space, basespace, \pi, fiber)
         - [x] sections: \tau, \mu, \rho
         - [x] transforms between bundles: \nu, Q <- input/output - what do these transforms mean?
         - [x] maps between base spaces: \xi
         - [x] all together thing: A
    - [x] write through end to end equations w/ explaination and stand in figures
         - [x] different k
         - [x] different f
         - [x] render with D = {x,y,z, r,g,b}
         - [x] \nu examples w/ scales + visual variables
         -[x] q example?
    - [] full draft of section (w/ actual figures)
- [x] implementation 
    - [x] scatter 
    - [x] line
    - [x] bar + multibar
- []  background/intro
   - [] visual basics: bertin/munzner/carpendale
   - [] math framework: gog
   - [] pipeline: vtk
- []  what's next? + operator, build a library

