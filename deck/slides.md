---
title: mpl maintainers talk
tags: Templates, Talk
slideOptions:
  theme: simple
description: Scipy2021 Maintainers Track Talk
---

### What's new in Matplotlib?

* slides: https://hackmd.io/@story645/scipy2021mpl
* tag: @story645, @matplotlib
* Funding thanks to CZI EOSS 1 & 3, supporting me, Thomas Casawell and Michael Grossberg
* Much support from the matplotlib dev team

---

### What does Matplotlib do? 
![Flow chart where boxes are small and arrows are big and purple. Box 1 contains images of data containers: an array, data frame, and nested list. Arrow from 1 to 2. Box 2 has images of visual encodings: a light blue circle, black line, purple to yellow gradient, and blue and orange boxes. Arrow from 2 to 3. Box 3 has graphics: histogram, line plot, image, and 3D surface. Arrow going from 3 to 1.](https://i.imgur.com/o6Kspwe.png)

---

### How does Matplotlib do it? 
![Same flow chart as above, arrows circled in blue. Circle is labeled Artist in same blue](https://i.imgur.com/7G4eCMU.png)

---

### What does the new architecture do?
![Same flow chart, no circle](https://i.imgur.com/o6Kspwe.png)

---

### How?

* Identify the different types of transformations
* Formalize the rules of these transformations
* Implement functionally to enforce seperation

---

### Topology
![Same flow chart, no circle, arrows 1 to 2 and 2 to 3 are faded out](https://i.imgur.com/bY4ZmTX.png)

----
![scatter plot of 3 dots colored purple, green, and gray, labeled JFK, ITO, and BRW respectively](https://i.imgur.com/PXZJJbB.png)

----

![above scatter on right, on left is 3 disconnected rows. Each row has a temperature and pressure value and a station name](https://i.imgur.com/X8cjQwZ.png)

----

![above scatter + rows, and arrows going from scatter points to the row with the corresponding data](https://i.imgur.com/5EaH4g4.png)

----

![same as above but the rows have been shuffled so the arrows have moved while the dots stay in the same place](https://i.imgur.com/ozA1dUe.png)

---

![3 station rows, the dots are replaced by lines connecting the dots, forming a triangle. The lines are colored with a gradient, reflected in a colorbar labeled ITO at top, JFK in middle, and BRW at bottom](https://i.imgur.com/wBPMV43.png)

---- 

![triangle image with arrows going from each corner to a corresponding row](https://i.imgur.com/UZdPL9U.png)

----

![triangle with arrows to rows. there is also an arrow from the middle of a triangle leg going to a row where each value is a ?. The ? row is between two rows of station information](https://i.imgur.com/DRoyr2W.png)

---

### Equivariance 

![artist flow chart, no circle, the arrow from 3  to 1 is faded out](https://i.imgur.com/oQ8NEqK.png)

----

![table of 5 values, line plot of precipitation, purple arrow going from table to values](https://i.imgur.com/1yLZHaG.png)

----

![same as above, plus new table underneath the first. values in second table 10th of first (mm to cm), and blue arrow from top table to bottom table ](https://i.imgur.com/YONsiLr.png)

----

![3 tables + arrows from above, plus new line plot of centimeter precip data - is much shorter cause on same scale as mm. Arrow from bottom table to bottom graph, and blue arrow from top graph to bottom graph, matching arrow from top table to bottom table. )](https://i.imgur.com/u0CDReu.png)

----

### Multivariate Data

![above rows + scatter chart. Scatter also has bar chart of x values on top, horizontal bar chart of y values on right, each scatter point corresponds to one vertical and one horizontal bar chart.](https://i.imgur.com/VOhQF78.png)

----
![rows, scatter, bars image with arrows going from ITO bars, point and legend element to ITO row](https://i.imgur.com/BPqhnno.png)

----
![rows, scatter, bars image with arrows going from JFK bars, point and legend element to JFK row](https://i.imgur.com/ERXKGy7.png)

----
![rows, scatter, bars image with arrows going from JFK bars, point and legend element to BRW row](https://i.imgur.com/BDCrQNr.png)

----
![combination of all figures with arrows from all elements in figure to corresponding rows](https://i.imgur.com/r0nUQsw.png)

---

### Nested Toplogies

![5 rows with date and precipitation columns. Dates are  at jan 16, feb 1, may 28, may 30, and july 3 2021. Arrows from the five scatter points at date back to the correspondinf rows. Plot is of date on x axis and precipitation on y axis, at JFK airport](https://i.imgur.com/96s2ljI.png)

----

![5 dot image + line plot of precipitation during same time period as the dots, arrows go from parts of the line in between dots to in between rows](https://i.imgur.com/2RkFR2b.png)

---

### Thank you!!

* contact: @story645, haizenman@gmail.com
* research: https://github.com/story645/proposal 
* discuss: https://discourse.matplotlib.org/


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




