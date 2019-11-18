
# ray tracing
* add up all of the rays from all the bouncing that that they do
    + infinitely many rays out of a light
    + infinitely many bounces
    + since don't care about light rays that don't go into camera, can go backward (bounces are kind of symmetric), still not tractable, amazing amount of tricks, two-three bounces, sample in different kinds of ways-trace backwards
    + shaders and shader language, 
    + world is triangle in vertices & mesh and pixels, triangles get smashed onto screen, take into account other triangles, not gonna worry about rays, this is how it effects this triangle, need more resolution take smaller triangles, (shader math, openGL)
* Nividia takes other approach - ray tracing
    + ray tracing small fraction of points, fill in rest using deep learning (can denoise), fancier version of stamp tool, noisy picture of door, so many examples of actual doors w/o noise, can infer and ray trace some of the scene and clean up
    + shader math is very pipeline functional oriented, can map well to these cards that have thousands of threads of executions
    + ray tracing parallelizes beautifully
    + add 'em all up & that's reduce
    + issue is just too many
    + what's the middle wear? (think shaders-got pixels and/or primatives, data is kind of like the scene in computer graphics), shader language is efficient way to think about how data gets pushed into the screen, vizpy + vtk, language from one to another, question is how functional? is it at the right level of abstraction? how much does the designer of 3rd party packages need to know about the backends to use these features? cognitively shouldn't have to know too much... 