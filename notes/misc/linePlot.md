# Line plot thoughts.

I am trying to figure out what a line plot is mathematically before we drop down to code. When I thin of a line plot which could be either functionally specified or a sequence of points, then we have something like a function $\gamma: [0,1] \to R^2$. We don't require it be a function from $x$ to $y$. We can draw a circle in the plane with a line plot. Ok so we have the case where we might have a sequence of points like $0,1,2, \ldots $ and the continuous case $[0,1]$ as domain. The range needs to be at least $R^2$ for to have $x$ and $y$, but there will be a bunch of other parameters too, eg. color, width, line type, etc. Our range space is $X$ which could just be $R^2$ but could have as many "Bertin Channels" as needed. 

Next the two case we most care about for domains are, as just stated $[0,1]$ and $[0,1,2, \ldots]$. Lets call the domain $M$. Thus our line plot is a map $\gamma: M \to X$. It is not quite right that $M$ can nearly be discrete points. Line plots will connect the points. Thus really we have some notion of which points are neighbors. This is topology. So really, $M$ could be a graph, ie. a 1D simplicial complex, or the interval. Actually it could be a union of intervals. So in general $M$ is a 1-dim, topological space, given as a union of intervals and being a line plot means $\gamma: M \to X$ is continuous. One good thing about this is that by sending to the retinal space the ordered pair $(M,\gamma)$ we are being lazy about how $M$ needs to be sampled as it heads to rendering, allowing us to handle continuous spaces, or even allow for visual approximations of $(M,\gamma)$ to handle large data. In some sense we just send $\gamma$ over since the function needs to encode its domain and range.

The interpretation of $X$ is the names and possible values, ie the schema or type of the cartesian product of Bertin channels. This assumes that we are thinking of them as (potentially) independent channels. By this I mean one data source could vary the $x$ width and an independent but synchronised source can vary the $y$, and another independent source the color. 

So far we have not discussed the actual data or how that comes into it. Given a point $m \in M$ we need to think how will $\gamma(m) \in X$ be determined. It will be useful to think of $m$ as pointing to a row of a data table. In particular we have some mapping $f: M \to D$ where (in this case), $f(m)$ can be thought of as a row of a data table. The components of $D$, are not necessarily Bertin channels. We need a tranformation $\tau: D \to X$ which essentially picks out which components of $D$, or combination of components in $X$ will be used as values for each Bertin channel. Because there are aspects of this that may be important for the data side, and aspects for a visual side, we will consider a certain redunancy here. This map will select columns an potentially change units in a way semantically meaningful for the data. It specifies which values will be represented by the Bertain channel but not something like a colormap yet. It is helpful then to think of $X$ not as the variables specifying specific locations or color, but the input for a function that specifies the color. In this way the data side is about specifying $\gamma = \tau \circ f$. Of course we can think of $\tau$ and $f$ being parameterized functions, and those parameters allow us to specify them. These parameters, along with the structure of $M$ are the "Data Side" of the visualization. 

Next $(M,\gamma)$ are passed over to the graphics side. There there is a transformation $\nu X \to V$ which maps semantic values into visual values. 

Abstractly a line plot starts with $M$ a 1-D topological space. 

# Implementations Ideas 
What is the input data for a line plot. 
For a single line plot it is a sequence or stream.

line_plot_datasource

and a collection of methods

line_plot_datasource.metadata()
line_plot_datesource.sequence()

The metadata function
line_plot_datasource.metadata()

returns line_plot_metadata which at least has a method

line_plot_metadata.name 
    which is used for the legend
line_plot_metadata.columns 
    which is needed to know which columns have been chosen for visualization.
    this might be used for hover 
    unclear if this should be a list of strings (names)
    or objects which could have names, types, units and other metadata attributes
    the columns must must have an 'x' and 'y', ie if strings ['x','y', ... ]
    other column names (optionally) might be 'size', 'color', 'marker_shape', 'line_color', 'line_width',
    'line_type' etc.
    The line parameters would allow for continuously changing lines attributes if desirable


the line_plot_datesource.sequence() is a sequence of line_plot_observation objects.

Each line_plot_observation object has required methods (attributes?)

line_plot_observation.projection(column)
line_plot_observation.index()

the line_plot_observation.projection('x') would give the x component of the line_plot_observation


keeping with the style you wrote

lp = LinePlot(line_plot_datesource)

would still make sense.

lp.draw()

might minimally have 

def draw (self)
    map(self.datasource, draw_point)

def draw_point(point)
    
 wonder how far we could go with the idea of something like a topological M as an indexing set mapped into "rows" of a data object D as being the primary object that then gets retinal variables associated to it. If M is 1-dimensional, thats a line plot. Imshow M is 2dim as is a contour plot. For a scatter plot M is a degenerate graph with no edges (all vertices). For a simple bar graph M is a stub (a tree with a root directly attached to leaves). Same for a pie chart. For  a grouped bar graph M becomes a 2-level tree, although we could attach different Bertain variables. 

The M->D aspect is important because it encodes what is the implied continuity or grouping the data should show, but it doesn't by any means determine the visualization. For example for a density we start out with M->D which is just a sampling of rows (and we pick a column) with no topology .... M is a tree stub or equivalently just a bunch of points. But then when we aggregate in data space we aggregate those samples over the column (which is really pushing foward the measure) to get a continuous density on the column space ... or if we bin than a discrete measure on the bins.... and the bins or the column domain becomes a new "M" lets say M_2 which then in the density case becomes a line plot, or in the histogram case becomes a bar graph.

Pushing on the topology of the input data is interesting, it provides a framework to tell apart "this 2D array is an image" vs "this 2D array actually represents a stack of lines" vs "this 2D array represents a stack of bars".

In this framing, an Artist (to use the mpl language) has a list of named slots that may be filled by the data source.  Each of those slots has some rules about (required/optional, length/shape/size, topology) and the relationship between the slots.  Conversely, the data objects should declare what slots they are exposing along with the above meta-data which means we can do the type-checking to see if this databundle will go with that Artist.

