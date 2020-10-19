# scatter (assume data is subselected)
* 10 columns of data
    * 100 rows
    * k - 0D simplex all disconnect
        * f - no argument ()
        * constant function
* $\sigma(k)$ returns tuple of 10 values
* return of sigma k bound to transforms (including NullTransform)
* transformed k is then composed into visual idiom into simplex

# line
* k - 1D, function(1 paramters) (defined on interval - always 0-1 distance between two vertices)
    * by definition on an edge:
        * left edge 0
        * right edge 1
    * temp/pressure spreadsheet would be represented as set of functions between each node
* composed(transforms(functions)) into cw simplex representing visual idiom

# image
* two triangles, f(x,y) that generates a value for each x,y to populate the image, 
* 0-1 domain and range
* compose(transform(f(x,y))) -> cw complex that represents the visual idom

# boxplot
* 0d, discrete, f constant
* \sigma(k) returns the statistics of the box plot
* artist(transforms(stats)) -> glyph 
    * artist dictates the transform
* artist(transforms(outliers)) -> scatter
