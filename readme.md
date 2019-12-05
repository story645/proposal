# Dissertation Proposal
notes, API sketches, drafts, etc. leading towards dissertation proposal:

## Sections
1. lit view of visualization library architectures
	1. vtk
	3. d3
	4. ggplot
	4. vega, vegalite, altair
	5. Bokeh, Holoviews <- data oriented
2. functional specification in haskell
3. prototype implementation for mpl v4 
	* https://github.com/matplotlib/CZI_2019-07_mpl
	* https://paper.dropbox.com/doc/Matplotlib-4.0--AlgrOup2~s4LE~gK2Ps_Orn9AQ-WTYwd0NQaSHTjtLUZwkNx
	* https://paper.dropbox.com/doc/CZI--AljtJwJnd6WwhqaTNPKhYkzYAQ-NMUblZDFOsSGB8woQFQUj
	* https://gist.github.com/tacaswell/95177903175dbc28be5353b4a0e5118f
	
## prototype:
* haskell->js/something serialized (.fig) -> mpl 
* read method on mpl:
	1. instatiate & compose objects based on the file
