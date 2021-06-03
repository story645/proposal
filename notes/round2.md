# deliverables
* developer-aimed documentation about how to build tools using the core architecture
    * API + narrative
* provisional implementation using new architecture in Matplotlib
    * at least 3 high level plotting functions (e.g. plot, scatter, imshow, bar)
    * at least 1 computational plotting function (e.g. hist, contour)
    * that works with at least 2 types of data structures (e.g. array, list, dict, analytic function)
    * demo of at least 1 complex interactive composite plot using new api (e.g. scatter with regression and parasitic histograms)
* proof of concept 3rd party user-facing library with a biology partner that supports at least one type of structured data (for example, phylogentic tree or cryo-electron microscopy image) and one composite visualization.
* academic paper about building visualization tools on top of the core architecture

# 3 high level plotting 
* coded so whole thing can be vectorized as some sort of quasi=ufunc, output is x/y display space (D->H over S)
   * maybe something serialized that can be handed off to like datashader, q as collection of patches
   * hurricane spaghetti plot w/ 10,000 trajectories? 
   * how to handle vectorization on functional data? 
