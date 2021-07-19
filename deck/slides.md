---
title: mpl maintainers talk
tags: matplotlib, talk
slideOptions:
  theme: simple
description: Scipy2021 Maintainers Track Talk
---

![Matplotlib logo with matplotlib spelled out](https://i.imgur.com/YozjaNz.png)

* https://hackmd.io/@story645/scipy2021mpl
* tag: @story645, @matplotlib

---

# Thanks
* CZI EOSS 1 & 3 for supporting Thomas Caswell, Michael Grossberg, and me
* Thomas Caswell & Michael Grossberg
* Sam & Melissa 
* YT for making the best presentations to steal ideas from
* the Matplotlib team :hearts: 

---

## Rearchitecture Goals
* Identify the different types of transformations
* Formalize the rules of these transformations
* Implement in a way that respects seperation

<!--why? makes it easier to code against, implement, maintain, correctly write these abstractions, improves consistency in complex cases-->

---

### What is Matplotlib's job? 
<!--provide components for converting data to graphics-->
![Flow chart where boxes are small and arrows are big and purple. Box 1 contains images of data containers: an array, data frame, and nested list. Arrow from 1 to 2. Box 2 has images of visual encodings: a light blue circle, black line, purple to yellow gradient, and blue and orange boxes. Arrow from 2 to 3. Box 3 has graphics: histogram, line plot, image, and 3D surface. Arrow going from 3 to 1.](https://i.imgur.com/o6Kspwe.png)

---

### How does Matplotlib do it? 
<!-- the artist object-->
![Same flow chart as above, arrows circled in blue. Circle is labeled Artist in same blue](https://i.imgur.com/jXWWOxE.png)


----

<!-- stress it takes in an object, it forwards to an object, list of objects -->

![screenshot of matplotlib PathCollection ocs https://matplotlib.org/stable/api/collections_api.html?highlight=pathcollection#matplotlib.collections.PathCollection](https://i.imgur.com/wOCv9m7.png)

---

### What is the proposed API?

<!-- is about functions, drop ins, decoupled flexibility -->

![three columns: first has a table with a temperature value 17.7, precipitation value 27.9, and station name JFK. The second column has a matching table of a vertical line, vertical horizontal, and the bottom box is purple. There are 3 purple arrows, one going from temp to the vertical line, one from prcp to horizontal line, and one from station to the purple box. The third panel shows a horizontal and vertical line and at the intersection is a purple dot. There is a purple arrow from the 2nd panel to the dot, and from the dot to the table in the first panel](https://i.imgur.com/0a2qonD.png)

---

### Graphic -> Data: Topology

<!-- make the point here that it's about breaking out of the structure, is for a general model -->

![Same flow chart, no circle, arrows 1 to 2 and 2 to 3 are faded out](https://i.imgur.com/bY4ZmTX.png)

----

<!--- dig down into scatter to explain what we mean by topology --->

![scatter plot of 3 dots colored purple, green, and gray, labeled JFK, ITO, and BRW respectively](https://i.imgur.com/PXZJJbB.png)

----

<!---implicit assumption scatter is backed by discrete points-->

![above scatter on right, on left is 3 disconnected rows. Each row has a temperature and pressure value and a station name](https://i.imgur.com/79YGhol.png)

----

<!-- made explicit via arrows rather than hard coding any assumption-->
![above scatter + rows, and arrows going from scatter points to the row with the corresponding data](https://i.imgur.com/FOaWlf9.png)

----

<!--- can verify w/ shuffle -->
![same as above but the rows have been shuffled so the arrows have moved while the dots stay in the same place](https://i.imgur.com/rTCSzyh.png)

----

<!-- what happens when we connect?-->
![3 station rows, the dots are replaced by lines connecting the dots, forming a triangle. The lines are colored with a gradient, reflected in a colorbar labeled ITO at top, JFK in middle, and BRW at bottom](https://i.imgur.com/LzBUK5t.png)

----

<!--- still have map back to data-->

![triangle image with arrows going from each corner to a corresponding row](https://i.imgur.com/qUL5rAR.png)

----

<!--- but introduce map that doesn't exist --->
![triangle with arrows to rows. there is also an arrow from the middle of a triangle leg going to a row where each value is a ?. The ? row is between two rows of station information](https://i.imgur.com/i0M0N24.png)

<!--wrap w/ how this allows us to express graphic to data relationships w/o relying on one notion of continuity-->

---

### Data -> Graphic: Equivariance 

<!--visualization is structure preserving maps, by structure we mean things like measurment type-->
![artist flow chart, no circle, the arrow from 3  to 1 is faded out](https://i.imgur.com/oQ8NEqK.png)

----

<!--precip is ratio, distance between Jan 1 and Jan 2 and Jan 2 and Jan 3 is proportionally same in data and viz-->
![table of 5 values, line plot of precipitation, purple arrow going from table to values](https://i.imgur.com/1yLZHaG.png)

----

<!-- scaling the data induces scaling in the viz-->
![3 tables + arrows from above, plus new line plot of centimeter precip data - is much shorter cause on same scale as mm. Arrow from bottom table to bottom graph, and blue arrow from top graph to bottom graph, matching arrow from top table to bottom table. )](https://i.imgur.com/u0CDReu.png)

---

### Why? Multivariate Multidimensional Data
<!--space + label or change to histogram, add in all points but keep 3 points, top and right to precip -->
![3 rows of station data. Scatter chart temp vs. precip for all station data from Hanuary to july. on top of chart is  a time series plot of precip, to the right is rotated timeseries plot of temperature.](https://i.imgur.com/7pmNJOf.png)

----

<!--- bookeeeping problem-->

![4 arrows going from corresponding point in scatter, legend, and line charts to ITO row](https://i.imgur.com/GeOUzOW.png)

----

<!--- topology & generalized data model--->

![4 arrows going from corresponding point in scatter, legend, and line charts to JFK row](https://i.imgur.com/EQ5UR9F.png)

----

<!--- equivariance and consistent updates-->
![4 arrows going from corresponding point in scatter, legend, and line charts to BRW row](https://i.imgur.com/msMF3Wv.png)

----

![combination of all figures with arrows from points, lines, and legend to corresponding rows, 12 in all](https://i.imgur.com/bNLx5jH.png)

---

### Takeaways
<!--reframe goals, + overall status-->
* decoupling the data, visual encoding, and plot assembly steps
* provides easier to code against interface
* improves reliability, consistency, maintability
* conceptual prototype: https://github.com/story645/proposal 

---

### Thank you!!

* contact: @story645, haizenman@gmail.com
* discuss: https://discourse.matplotlib.org/
* gitter: https://gitter.im/matplotlib/matplotlib

---

## Appendix

---

### Functional API model
```python
def fiberbundle(section): 
        index = section.section.index
        def projection(column_name):
            def values(): #
                if column_name is None:
                    return pd.Series(index=index, dtype=float)
                return section.section[column_name][index]
            return values 
        return projection
    return subset_k #s
```

----

```python
@dataclass
class Section:
    F =  {'fruit': np.dtype('O'), 
               'calories': np.dtype('int64'), 
               'juice': np.dtype('bool')}
    K =  pd.core.indexes.range.RangeIndex

    section: pd.DataFrame

    def __post_init__(self):
        #check the fiber matches
        assert self.section.dtypes.to_dict() == self.F
        assert isinstance(self.section.index, self.K)
````

----

```python
data = {'fruit': ['apple', 'orange', 'lemon', 'lime'], 
       'calories':[95, 67, 17, 20], 
       'juice':[True, True, False, False]}
df = pd.DataFrame(data)

fruit.fiberbundle(fruit.Section(df))(None)('juice')()
```

---

```python
nus = {'position': lambda x : x, 
       'length' : position.Nominal({'apple': 0, 'orange': 2, 'lemon': 4, 'lime': 6}),
       'floor': lambda _: 0,
       'width': lambda _ : .8,
       'facecolor' : color.Nominal({True: 'orange', False: 'blue'}), 
       'edgecolor' : lambda _ : 'k', 
       'linewidth' :  lambda _ : 2,
       'linestyle' : lambda _ : (None, None)}
```

---

```python
class BarArtist(martist.Artist):
    #view is fruit.fiberbundle
    def __init__(self, view, orientation, aes, position, length, floor, width, facecolors, edgecolors, linewidths, linestyles):
        # some function unpacking/ set parametrs
    
    def assemble(pos, ..., fc):
        xval = pos
        paths = [[(x, y), (x, y+yo), (x+xo, y+yo), (x+xo, y), (x, y)] 
                for (x, xo, y, yo) in zip(xval, xoff, yval, yoff)]
        return paths, ..., fc
    
    def draw(self, renderer, *args, **kwargs):
        #conversion works something like 
        pos = position(view(self.data)(None)(aes['position']))
        # ....
        fc = facecolors(view(self.data)(None)(aes['facecolors']))

        # all the visual conversion gets pushed to child artists
        self.assemble(pos, ..., fc)
```

---

### Topological Equivariant Artist Model

----
<!--sorry didn't have time for alt text yet, these are diagrams of the math. Please bug me for more info if interested-->

![](https://i.imgur.com/A9HSlTK.png)

----

![](https://i.imgur.com/B0UOZAk.png)

----

![](https://i.imgur.com/5xx5IFu.png)

----

![](https://i.imgur.com/R7xTsFA.png)

----

![](https://i.imgur.com/aYyAr3t.png)

----

![](https://i.imgur.com/w5emg7E.png)

----

![](https://i.imgur.com/njNi3OH.png)

----

![](https://i.imgur.com/RPtec2k.png)

----

![](https://i.imgur.com/FlSNRvg.png)

