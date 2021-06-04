![parabolic_corr](https://user-images.githubusercontent.com/24655619/120843704-6baad700-c53c-11eb-8015-2ae14b6de4c0.png)
# parabolic-regression
How to fit a parabola to data

Parabolic regression fits the best fit two dimensional parabola through data. The computational overhead to do this is minimal, and the fitted curve often gives a better model than a straight line. As an example, look at the attached four panels. The second panel is the data. The top panel is 'Ordinary Least Squares Regression', using a straight line. The third panel is the best fit parabola. In the data panel, look at the points in the upper right corner. Then look how those points project up to the line in the top panel. Then look how they are projected down onto the parabola. Notice how that parabolic representation portrays better the shape of the distribution of the data. But notice also that the actual values predicted by the straight line are closer to the values predicted by the parabola. Part of this simply results from the elaboration of "the shortest distance between two points is a straight line" to accommodate many points. The parabola, a conic, is guaranteed to skew. But often the shape of the distribution has useful information.

The python file parac.py computes parabolic correlation, described in the 1946 paper by Charles Peters, the only paper that I know that describes it. 

The fourth panel shows slope of the fitted parabola, which in this case is a straight line y = -0.7285x + 0.36664, using standard form y = mx + b. Note that b, the y-intercept, in this case 0.3664 is marked with an orange line (the origin at zero is in the center, not leftmost).  There are two blue lines on this panel. The one on the left at x =-0.0328 is a critical x value where the slope of the tangent to the parabola at that point is
equal to the slope of best fit staight line in the top panel, which is the Pearsonian Correlation, 0.3945. Peters discusses this point on page 62 (he mentions that it would be also be plausible to evaluate at the mean, but says that such a statistic would lack a connection to the widely known
coefficeint of correlation. The blue line on the right  at x =.5033 marks an inflection point on the parabola, where the slope is zero.



