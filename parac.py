#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys	
from math import sqrt 
from numpy import std,sqrt,mean,corrcoef,power,array
# This program encodes Charles C. Peters 1946 paper "A New Descriptive Statistic: The Parabolic Correlation
# Coefficient"

# X and Y must be numpy arrays. In practice I use one dimension arrays, but I have
# experimented successfuly with higher dimensional arrays with not much change in code.
def paracor (X,Y, foutt):
	if len(X) != len (Y):
		print ('The X and Y arrays are not of the same length.')
		sys.exit()
	# The first five of these eight terms are required to compute
	# ordinary least squares regression (OLSR), straight line regression.
	# The last three are the additional terms needed to compute
	# the parabolic correlation statistics. See page 64.
	sX=sum(X)
	sY=sum(Y)
	sXX=sum(X*X)
	sYY=sum(Y*Y)
	sXY=sum(X*Y)
	sXsqY= sum(X*X)*sum(Y)
	sXcu=sum(X*X*X)
	sXfo=sum(X*X*X*X)
	
	# Standard deviations.
	stdX = std(X)
	stdY= std(Y)
	N= len(X)
	
	# Equation (1) on the first page shows the standard form
	# for a parabola: y = a + bx +cx**2. The constants a, b, and c
	# are computed with the equations given on page 59.
	ctop=(sXsqY-N*sXsqY)*(N*sXX-sX**2)+(N*sXY-sX*sY)*(N*sXcu-sXX*sX)
	cbot=((N*sXcu-sXX*sX)**2)+(((sXX**2)**2)-N*sXfo)*(N*sXX-sX**2)
	c = ctop/cbot
	b = ((N*sXY-sX*sY) -(c*(N*sXcu-sXX*sX)))/(N*sXX-sX**2)
	a =(sY-c*sXX-b*sX)/N
	
	# The index of curvature is computed with
	# equation (10a) on page 63. It is a single statistic
	# for the whole parabola. This is a useful atatistic with
	# a window moving on a time series.
	ratio_top = N*sXX - power(sX,2)
	ratio_bot = N * sqrt(N*sYY-power(sY,2))
	ic= c * (ratio_top/ratio_bot)
	print ('Print correlation matrix so user sees what happens\n',corrcoef(X,Y))
	to=corrcoef(X,Y)[0,1]
	t1=(c*(N*sXcu-N * mean(X)*sXX))/((N**2)*stdX*stdY)
	isx =[]
	for curx in list(X):
		t2= (2*c*curx*(N**2)*(stdX**2))/((N**2)*stdX*stdY)
		isx+=[(to-t1+t2)]
	for g in isx:
		foutt.write(str(g)+'\n')

	Mx=mean(X)
	x= X-Mx
	My=mean(Y)
	y= Y-My
	if (N*stdX**4) != 0: B2 = sum(x*x*x*x)/(N*(stdX**4))
	else: B2 = 0
	if ((N**2)*(stdX**6)) !=0: B1 = (sum(x*x*x)**2)/((N**2)*(stdX**6))
	else: B1=1

	if list(X).count(X[0])==len(X) and list(Y).count(Y[0])==len(Y): to =0
	else:	to=corrcoef(X,Y)[0,1]
	if ((N**2)*stdX*stdY)==0:t1=0
	else:t1=(c*(N*sXcu-N* mean(X)*sXX))/((N**2)*stdX*stdY)
	if stdY == 0: ic=0
	else:
		ratio_top = N*sXX - power(sX,2)
		ratio_bot = N * sqrt(N*sYY-power(sY,2))
		ic= c * (ratio_top/ratio_bot)

	curx = X[len(X)-1]
	if ((N**2)*stdX*stdY)==0:t2=0
	else:t2= (2*c*curx*(N**2)*(stdX**2))/((N**2)*stdX*stdY)
	isx=to-t1+t2
	if (2*N*stdX**2) == 0: critX=0
	else:critX=(sXcu-mean(X)*sXX)/(2*N*stdX**2)
 	# This is an alternative method to compute crit.
	# xxx= sum(x*x*x))
	# cRad = sqrt((xxx**2)/((N**2)*(stdX**6)))
	# critb = mean(X)+.5*stdX*cRad 
	if str(isx)=='nan' or str(isx) == 'inf' : isx =0
	if str(curx)=='nan' or str(curx) == 'inf' : curx =0
	if str(ic)=='nan' or str(ic) == 'inf' : ic =0
	if B2-B1-1 > 0:
		icmax = 1/sqrt(B2-B1-1)
	else: icmax=ic
	if str(icmax)=='nan' or str(icmax) == 'inf' or str(icmax)[0]=='(' : icmax =ic
	if ic >2: ic =2
	if ic <-2: ic = -2
	if icmax >2: icmax =2
	if icmax <-2: icmax = -2
	ixcc=isx*curx
	if ixcc <-12:ixcc =-12
	if ixcc >12: ixcc=12
	if Mx:cri=(Mx-critX)/Mx
	else: cri=0
	if cri<-2:cri=-2
	if cri>2:cri=2
	if isx >12: isx=12
	if isx < -12: isx=-12
	return a,b,c,isx,ixcc,ic,cri,icmax

def get_parabola(X,a,b,c):
	Y = []
	for x in X:
		Y += [a+b*x+c*power(x,2)]
	return Y

if __name__ == '__main__':
	# The x and y data is the Pearson correlation of the financial series TICK-NYSE 
	# to first: NYSE compostite (x), second: DIA (y), the etf tracking the Dow 30 stocks. 
	# The data uses a window of seven 5 second intervals. The data only uses the first 
	# two fields of the nyac.txt.
	fin = open('nyac.txt')
	fil = fin.readlines()
	x=[]
	y=[]
	for li in fil:
		lisp = li.split(',')
		x+=[float(lisp[0])]
		y+=[float(lisp[1])]
	# File to write the index of slope statistic across x domain.
	foutt = open('isx.txt', 'w')
	a,b,c,isx,ixcc,ic,cri,icmax = paracor(array(x),array(y), foutt)
	print ('a, b, and c constants describing the parabola; ',a,b,c)
	print ('Index of curvature (ic) ', str(ic))
	print ('A negative ic means the parabola in convex, else concave.')
	print ('Maximum possible index of curvature (icmax) ', icmax)
	YY = get_parabola(x, a,b,c)
	fout = open('prab.txt', 'w')
	for i in range(len(x)):
		fout.write(str(x[i])+','+str(y[i])+','+str(YY[i])+'\n')
