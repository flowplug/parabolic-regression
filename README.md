# parabolic-regression
How to fit a parabola to data

Parabolic regression fits the best fit two dimensional parabola through data. The computational overhead to do this is minimal, and the fitted curve often gives a better model than a straight line. As an example, look at the attached three panels. The middle panel is the data. The top panel is 'Ordinary Least Squares Regression', using a straight line. The bottom panel is Parabolic Regression. In the data panel, look at the points in the upper right corner. Then look how those points project up to the line in the top panel. Then look how they are projected down onto the parabola. Notice how that parabolic representation portrays better the shape of the distribution of the data. But notice also that the actual values predicted by the straight line are closer to the values predicted by the parabola.
  parac.py computes parabolic correlation, described in the 1946 paper by Charles Peters, the only paper that I know that describes it
![parabolic](https://user-images.githubusercontent.com/24655619/120386180-4e84c700-c2f6-11eb-8b07-b1203633dde6.png)

