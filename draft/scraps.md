Spivak - 
* simplacial sets for schemas, 
    * entity - relation for the schema
* sheaves for the data itself 
    * 
- 

Visualization library - spells out/regularizes the ways you can aesthetically encode data, preserving structure of data, scatter - magnitude between values preserved - some ways an accurate representation of the data, concerned w/ as data is changed, graph has to change accordingly, graph needs to change accordingly - owns responsibility for preserving measurement integrity when specified by encodings
    - specify what you want to preserve
        - (choose which) preserve relations in a strict math/set theory sense
    - functional is a good fit b/c it spells out these constraints 
Drawing program - user is responsible for preserving these measurements 


 Why functional?
 because what we care about is the interface, the contract between the data and the visualization. We need the minimal amount of information that fulfills our contract that we can then put on the screen. (insert react notes here). Our theoretical framework is that that visualization is a transformation from one topological space to another to a CW complex (this probably needs to be explained more), and a functional programming paradigm allows us to directly express that in code. 

 \subsection{What will be the work}
 %%this comes from the grant
 Matplotlib needs to support use cases across a vast range of science domains, enabling complex visualizations [1]. At the same time, common visualizations in a domain need to be fluid for the end-practitioners, tuned to the domain's standard data structures, and with domain-specific customization options exposed. To achieve both of these goals, we need to continue to foster a two-layer ecosystem with a shared core (Matplotlib) and many domain-specific libraries (seaborn, nipy, ...).

In the current grant cycle we have been developing a new architecture that is heavily invested in cleanly separating the three steps in a visualization pipeline: data representation, encoding the data as visual elements, and rendering those elements to screen. We believe that a better delineation of these steps will allow domain practitioners to more easily implement extensions. Following on the work done this year to design consistent data and artist abstractions, we will develop simpler and more expressive user-level APIs in core Matplotlib and in collaboration with domain-specific libraries. 



 Why topology?

 The difference between a line plot and a scatter plot is the former assumes that the data is continous, the latter that it is discrete (cite line and scatter - friendly?) In concrete implementation terms, matplotlib's imshow assumes that the data is continous and therefore does implementation, the matshow assumes it is discrete so it does not. And there are visualization types like area charts that allow even more information to be encoded bewteen the lines. When redesigning the architecture, we needed a way to articulate the differences between the different plot types and found that a topological approach allowed us to encode connectivity (discrete versus continous), dimensionality (point, line, area), and how much information the visualization encodes. 



 
 What even is data?
 Remake this graph notated w/ graph semantics:
 \begin{figure}
    \includegraphics{figures/intro/data_formatting}
    \caption{Modified from Munzner's Visualizarion Analysis and Design}
 \end{figure}

 What even is encoding?
Bertin table on 69 rewrite here clearly  
 \begin{figure}
    %% Bertin's decomposition of an image
 \end{figure}
 \begin{figure}
    \includegraphics{figures/intro/retinal_variables}
    \label{fig:retinal_variable}
    \caption{This organization of Bertin's retinal variables \cite{bertinSemiologyGraphicsDiagrams2011} that lays out the geometry(marks) and corresponding aesthetic variations (channels) with a recommendation based on data type (qualitative versus quantative) comes from Krygier and Wood's Making Maps \cite{krygierMakingMapsVisual2005}}
\end{figure}

When talking about encodings, we are referring to Bertin's codification of the properties of the graphic system \cite{bertinIIPropertiesGraphic2011} seen in fig~\ref{fig:retinal_variable} as visual variables. In this system, there are the marks, which are the point, line, and area geometric primatives on the visual plane that each represent a single instance of the data being visualized \cite{bertinIIPropertiesGraphic2011,munznerMarksChannels2014}. These marks can be varied along different visual channels  size, value, texture, color, orientation, shape, and position \cite{bertinIIPropertiesGraphic2011, munznerMarksChannels2014}. As shown in fig~\ref{fig:retinal_variable}, the marks encode topological connectivity such that they have the following graph semantics:

\begin{description} 
    \item[Points] - 0d, no edges
    \item[Lines] - 1d, every vertex has <=2 edges (1d simplex)
    \item[Area] - 2d,  every vertex has <=4 edges (2d simplex)
\end{description}

The visual channels in fig~\ref{fig:retinal_variable} are recommended based on the measurement type, quantative versus qualitativem  and Munzner generalizes the quantative channels as magnitude channels for ordered attributes (measurements drawn from an ordered set of possible values) and the qualitative channels as identity channels for categorical attributes (random set of possible values). 
topology in measurement types, and that topology informs the channels appropriate for those types:
    quantative continouse, quantative discrete, qualitative catorical ordinal, qualitative categorical
    marks - topology of measurements (people wearing dresses)
    channels - topology of space from which measurements are drawn (possible dress sizes)
    categorical - discrete points w/o anything to do 
    categorical - poset topology?

    base space - topology of observations (people wearing dresses)
    fiber topology - topology of measurements (possible dress sizes) 

functional 'cause focus on transforms - if transforms preserve linearity than whole pipeline does. Dev gets guarantee on calling composite. 

Add table of which sorts of invariance a channel will preserve....


\begin{figure}
    \includegraphics{figures/intro/munzner_datatypes}
    \label{fig:munzner_datatypes}
    \caption{Keys are unique lookup values used to find individual observations in the dataset. Keys are positional references, and can be coordinates on a map or unique values such as a primary key in a database or a (time, latitude, longitude) index in a data cube. Image modified from a diagram from Munzner's website\cite{munznerChDataAbstraction}}
\end{figure}
Munzner's key/value semantics\cite{munznerWhatDataAbstraction2014}
provide a way to identify variables that in effect act as metadata for other variables, such as how when we are interested in the temperature at a time the temperature is the lookup value. But that did not generalize well for complex heterogenous datasets. In this proposal, we refine those ideas by using topology to formally describe the connectivity between the measurements. 

\begin{verbatim}
make any stupid plot you want in robust & rigourous way
        * need rich description langauge + right choice of paradigm (functional) 
        * ability to mathemetaically formalize/conceptual framework for doing this
        * data -> artist, need to preserved the structure of the data moreso than the data 
            * how points are connected to each other
    * targeted implementation rather than protocal (numpy)
        * visualization libraries bound to the datastructures (concrete implementation)
            * encode a lot of assumptions about data in the data structure
            * MPL assume x/y plotted in order you want them in 
            * topology makes the assumptions explicit
            * explicit->math->functional  
    * spell out the layers of visualization libaries:
        * Data + computation -> visualization composites -> drawing library
        * domain specific library
        * utility library <- formalize this piece (SciPy Diagram)
    * viz - Munzner + Bertin
    * functional programming makes sense 

\subsection{visual variables}
Bertin's proposed an organization of visual variables \cite{bertinIIPropertiesGraphic2011} 


\subsection{Grammar of Graphics \& ggplot}
Specifies the end chart (graphic)
we want to specify the transformations ....
\begin{figure}
    \includegraphics{figures/intro/grammar_chart_composition.png}
    \caption{page 10 (introduction)}
\end{figure}

\begin{figure}
    \includegraphics{figures/intro/grammar_example.png}
    \caption{Wilkenson decomposed a graphic into ...} 
\end{figure}

charts - words 
    - instances of much more general objects (geometric primatives)
    - histogram =/= bar chart
graphics - statements 
expliceltly OO
    1. specification
        data - operations/computations
        trans - variable transforms (rank)
        scale - scale transforms
        coord - coordinate system
        element - marks and channels
        guide - meta elements - (axes, legends, etc)
    2. assembly - kinda what happens in artist (spec->something that can go to renderer) 
    3. display - rendering

How is our proposal different? seperation in spec between what's data, aesthetics, and render specific, and what part of the architecture owns those operations


### lit review
ggplot - strictly hierarchal components (layers), matplotlib - transforms that mostly happen indepently 
"designing and producing statistical graphics is not an art" - ties in w/ difference between drawing program and visualization library, preservation of properties of measurement type and observation type \cite{wickhamGgplot2ElegantGraphics2016a}
history of viz - collins, friendly


Wilkenson suggests that the graphics pipeline could be implemented functionally but does not push it in any direction. 

ordering: processed before plotted, 
scales before stats, marks before channels
\begin{figure}
\includegraphics[]{figures/intro/gog_pathway.png}
\caption{Diagram of Grammar of Graphics stages of visualization. Fig 2.2 from chapter 2 of The Grammar of Graphics\cite{wilkinsonGrammarGraphics2005}}
\label{fig:gog_pathway}
\end{figure}
In grammar of graphics, as shown in figure~\ref{fig:gog_pathway} data is extracted from the database one variable at a time with an associated index (primary key). The algebra stage joins the variables to become the varset, which is a flat table where the columns are the variables/attributes, each row is an observation/item, and each cell contains a measurement \cite{munznerChDataAbstraction}. Wilkenson then describes the constraints of the measurement space for each variable through scales \cite{wilkinsonGrammarGraphics2005} with implicit assumptions of the data constraints. After this step, data is transformed computationally in service of the visualization. Some of the variables are then mapped into geometric marks (symbols) and are scaled (height, width) as appropriate. These mappings are then transformed into the coordinate system of the target graph. Then the aesthethic attributes (Bertin's retinal variables, also called channels) such as color or  texture) are applied. Finally

Wilkenson's thoughts on coherancy are equivalent to invariance but less? formally stated \dots

"To call these charts meainingul, defenders must falsify specific assumptions of GoG" \cite{wilkinsonMathematicalFoundationAnalytic2010}


gog implementationss:
\begin{enumerate}
    \item SPSS nViZn
    \item tableu
    \item ggplot
    \item protoviz\d3
    \item vega (interactive GoG)
\end{enumerate}


\label{sec:hunterMatplotlib2DGraphics2007}
System of transforms:
input: data w/ structure on fiber bundle + measurement type
artist: data -> visualization
(what structure of input is preserved in output)
we can provide list of
artist : topology it preserves
point/line/face parameters: measurement type properties 

ex: 
Line2D preserves continuity
Linestyle: categorical 

%%define basic properties of measurement of types in a theoretical way or C&P from a paper

Minimum assumption a transform will make - is this a valid transform for the slot? 

Set of questions/rules to apply such that see a new artist can be defined which lets us maybe simplify optimizations.  

M, Fiber Bundle, Section, operatons on \{data, visual\}, transform data space \& visual space,  

topology gives us that m is preserved
spivak gives us that v is preserved


temperature on globe:
\begin{equation}
data = [[t1], [t2_{la1, lo2}]
fiber = {lat, lon, temp}
m = the data is 2d continous
\end{equation}
artist has implict m
aesthetic paremeters transform in fiber that preserves type operations \& relations in the fiber
lat - relative distance + ordering 

\subsubsection{Graphical Elements}
There is a set of transform functions $T$ that maps from the data space $D$ to the visual space composed of geometric marks and aesthetic channels $V$ \cite{bertinIIPropertiesGraphic2011, munznerMarksChannels}.  We propose that a visualization is 
\begin{equation}
    T: D \rightarrow V
\end{equation}

Wilkenson proposes  that visualization is  \cite{wilkinsonGrammarGraphics2005, wilkinsonMathematicalFoundationAnalytic2010}

\begin{align}
\label{eq:gog_data_range}
G &= {(x, f(x)): x \in R and f(x)=e^{-x^2}}\\
F &= [-3,3] x [0,1]
\end{align}

\begin{equation}
\label{eq:gog_aesthetic_mapping}
A: x \mapsto x_{position}, f(x) \mapsto y_{position}
\end{equation}

\begin{equation}
G_{A} = A(F \cap G) 
\end{equation}

Wilkenson formulates plotting in terms of varsets, which are sets of variables where variables are:
\begin{equation}
V:O\mapsto V    
\end{equation}
Wilkenson's data algebra is equivalent to data reshapes and join and therefore \cite{wickhamLayeredGrammarGraphics2010,wilkinsonGrammarGraphics2005}


\subsection{What is the artist}
Visualization is a two step process where the artists $A$ transforms the data into visual encodings $V$ and then the renderer $R$ transfroms the encodings $V$ to the set of pixels in $P$.
\begin{equation}
    \label{eq:artist}
    A: D \mapsto M
\end{equation}
TYPES: A(D) = M
Spivak A is analogous DT

D is the type  which means it's indexexer K(M/indexer) + V (fiber bundle)
d is a section of a bundle is the data is the values given keys on m + vars on V (c in C)
a(d) = M

$M$ is a composition of the visual channels applied as ....
Is also a CW/simplicial complex/simplacial set 

Channels are ducktyping the variable types
Marks are encoding seperability 

Marks are mapping of simplacial complex into RGB space

(find paper on complex marks)

for every key value in M, have coordinates in the fiber (space)
section: keys -> values 

Scatter Plot:
K - 0D disconnected points
\begin{multline}
A: (C1, C2, C3...)\mapsto (M....)\\
t \in A
\end{multline}

-> preserve type operation and relation

M is the disjoint collection of the output of all these transformers where the transformers preserve the relation and order. 

Line Plot:
L - 1D, can be a function on an interval [a,b]
functions in the column...f(key) -> values

invariance: The symmetry group $A$ preserves invariance when the transforms $a \in A$ are symmetric such that $operation(column) = operation(channel)$ and $operation on data -> operation (mark)$

K might have symmetry -> move back and forth in time, preserved in K
symmatery in fibers -> scaled up/down, categorical,
preserved in the visual variables

groups on K and fibers and subgroups w/ different types and temperatures (Steven's fundemental data types-measurment scales and types)

intervals can transalte, ratio can only scale
group of fibers has to do w/ measurment types
channels themselves independent of data have their own symmatery

(make table of what symmateries are preserved)
visual transformation groups

instead of inputting parameter into input, get to all the other parameters - base thing is a square, 
preserved: operation(D) <-> operation (M)
if A(g*d) = A(d)*g

normalizations of scales in mpl - devision usually leaves same picture but axis is affected - visually length got uniformally smaller but we changed ticks to compensate
Axes has rules about how transform affects it - inside graph invariance is preserved

groups:
symmteries of K
symmetries of cartesian product of columns
each visual channel has symmtery group associated w/
orbit- space of possible visualiztions by changing the constants of each aesthetic (or $f_{red} \rightarrow f_{green}$)  
visual type might be orbit of that (orbit of function in space)->single function that can be transformed in that way 

each visualization type is an orbit \& then try to set up equivalence on these...

artist will respect that w/ equivariance, knob on one side will tweak knob on another



The aesthetic transfroms $a \in A$ are a symmetry group that preserves the group structure of the measurment scales as follows: 

categorical \& shapres have the group structure and so can do a $a: c \mapsto s$
Optimal transform $a_{i}$ is one from a measurment space to a visual channel where both sides have the same group transforms-
because equivaraince requires having the same transforms on the same side. 

artists take in class of visuals + 

A - matplotlib artists 
$A: D \mapsto CW$

$\tau: fb \mapsto vv $visual variable transformers
$\{\tau_{1}, \tau_{2}...\tau_{n}\}(K)\mapsto \{CW_{1}, CW_{2}, ...CW_{n}\}$ 
$\mapsto$ is what embeds the topology k 
functions that know how to embed the k (mark)
functions that work on the fibers $\tau$

%% distance along edge to transformed physical space, s function 
%% colormap_nrom - t: d \mapsto RGBA, continouts t: d(s) \mapsto 
%% 1d has to be parameterized  t: d(s), really want t: d\ mapsto RGBA
%%  d(s) \mapsto {d....} on interval [s_{0}..s_{n}]
%% flip this to the otherside so it's an adjacency matrix
%% how do we represent invariance/equivariance  A: D \mapsto \I
%% D - columns + topology (section + topology)
%% artist is the visual idiom 
%% {D cartesian product Tau} \mapsto I
%% Artist already has everything in VV space and composing into idiom
%% functions on simplex crossed wuth transformers - everything in visual space w/ same topology
%% A: visual \mapsto idiom
%% Artist (raw data + transforms )
%% carry topology over from VV space to I space -> singular CW complex 
%% (has no inherent structure) 
%% invaraince - shuffle_sq on tick labels = shuffle_sq on data 
%% how do you preserve invariance on topology->Idiom?
%% \tau_{2} is a new \tau function taht's really tau + 2
%% taus is a group of transform functions under composition 
%% tau gos data to visual variable
%% group of functions + 
%% measurement space groups is what class of functions don't destroy your data
%% \tau: d \mapsto vv - group of mapto functions
%% set of allowable \tau is where symmtery d/v are preserved 
%% d\v isomorphisms where tau takes you from one to another
%% d\v is  isomorphisms under group of taus where tau is the permutation group
%%
%% math: structure is same as type
Steven's measurement scales have the following structure \cite{stevensTheoryScalesMeasurement1946}:
%the big point of disagreement on the scales seems to be the stats column that we don't care about
\begin{table}
    \lable{tab:measument_type}
    \begin{tabular}{l l l l}
        nominal & permutation group & one to one substitutions & $=, \neq $\\
        ordinal & isotonic group & monotonic increasing functions &  $=, \neq $, $\leq, \geq$\\
        interval & general linear group & matrix operations &  $=, \neq, \leq, \geq, +, -, $\\
        ratio & similarity group & $ \mathbb{Z}^+ $ & 
    \end{tabular}
\end{table}

%%% make a second table later of what MPL currently supports
%%% redraw as graph
%%% set of all possible taus (operations can possibly be defined on both sides)

Split is discrete/ vs continous measurment types 
It is possible to write taus to ....

A: (v...v) -> I
%% tau is when we have data/visual lineups for labeling colorbar \ legend
%% colorbar vs. legend - continous vs discrete

\begin{table}
    \label{tab:taus}
    \begin{tabular}{l*{6}{c}} 
                              & position      &  size        & shape        & texture     & color \\
    nominal                   &  1            &  1           & 1            & 1           & 1     \\ 
    ordinal                   &  1            &  1           & 1            & 1           & 1     \\
    interval                  &  1            &  1           &              &             & 1     \\   
    ratio                     &  1            &  1           &              &             & 1     \\  
    \end{tabular}
\caption{Group of $\{t_{1}....t_{n}\}$ where $tau: d \mapsto v$ preserving equivariance such that $d$ and $v$ are isomorphic. $d$ is data of type \{nominal, ordinal, interval, ratio\} and $v$ are the visual channels. \cite{bertinIIPropertiesGraphic2011,munznerMarksChannels}}
\end{table}
 

Table~\ref{tab:taus} shows under which $\tau: d maps to v$, $d$ and $v$ can be isomorphisms.


%%% draw what the function graph looks like for scatter versus linesg
Scatter Plot:
K - 0D disconnected points
\begin{multline}
A: (C1, C2, C3...)\mapsto (M....)\\
t \in A 
\end{multline}

-> preserve type operation and relation

M is the disjoint collection of the output of all these transformers where the transformers preserve the relation and order. M is a bunch of disconnected Marks

Line Plot:
L - 1D, can be a function on an interval [a,b]
functions in the column...f(key) -> values

Box chart: area + scatter 


Combining 
\begin{equation}
    \label{eg:renderer}
    R: M \mapsto P
\end{equation}
Where $P$ is the set of pixels rendered to screen ${p_{i,j} \in P}$


An artist is a function F from X to Y
that satisfyies properties P1, ... PN
Step 1: Define X
step 2: Define Y
Spefiy Pi in terms of equations.

