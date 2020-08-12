#### Code Snippet 1 ####

import cv2
import numpy as np
import datetime
def swap(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a, b
def basic_alg_xstretch(x0, y0, x1, y1, imgparx):
    if x1 < x0:
        x0, x1 = swap(x0, x1)
        y0, y1 = swap(y0, y1)
    diffx = x1 - x0
    diffy = y1 - y0
    loopstart = datetime.datetime.now()
    for i in range(0,diffx):
        x = x0 + i
        y = int(diffy/diffx*i+y0)
        imgparx[x,y] = 1
    loopend = datetime.datetime.now()
    looptime = loopend - loopstart
    return imgparx, looptime.microseconds

def basic_alg_ystrech(x0, y0, x1, y1, imgpary):
    if y1 < y0:
        x0, x1 = swap(x0, x1)
        y0, y1 = swap(y0, y1)
    diffx = x1 - x0
    diffy = y1 - y0
    loopstart = datetime.datetime.now()
    for i in range(0, diffy):
        y = y0 + i
        x = int(diffx / diffy * i + x0)
        imgpary[x, y] = 1
    loopend = datetime.datetime.now()
    looptime = loopend - loopstart
    return imgpary, looptime.microseconds

def basic_alg_xparallel(x0, y0, x1, y1, imgx):
    if x1 < x0:
        x0, x1 = swap(x0, x1)
    diffx = x1 - x0
    loopstart = datetime.datetime.now()
    for i in range(0,diffx):
        x = x0 + i
        imgx[x,y0] = 1
    loopend = datetime.datetime.now()
    looptime = loopend - loopstart
    return imgx, looptime.microseconds


def basic_alg_yparallel(x0, y0, x1, y1, imgy):
    if y1 < y0:
        y0, y1 = swap(y0, y1)
    diffy = y1 - y0
    loopstart = datetime.datetime.now()
    for i in range(0, diffy):
        y = y0 + i
        imgy[x0, y] = 1
    loopend = datetime.datetime.now()
    looptime = loopend - loopstart
    return imgy, looptime.microseconds


def basic_alg(x0, y0, x1, y1, imgtemp):
    diffx = abs(x1 - x0)
    diffy = abs(y1 - y0)
    if diffx == 0:
        imret, timeret = basic_alg_yparallel(x0, y0, x1, y1, imgtemp)
    elif diffy == 0:
        imret, timeret = basic_alg_xparallel(x0, y0, x1, y1, imgtemp)
    elif diffx >= diffy:
        imret, timeret = basic_alg_xstretch(x0, y0, x1, y1, imgtemp)
    elif diffx < diffy:
        imret, timeret = basic_alg_ystrech(x0, y0, x1, y1, imgtemp)
    return imret, timeret

def plotLineLow(x0,y0, x1,y1, imglow):
  dx, dy, yi = x1 - x0 , y1 - y0, 1
  if dy < 0:
    yi, dy = -1, -dy
  D, y = 2*dy - dx, y0
  loopstart = datetime.datetime.now()
  for x in range(x0,x1):
    imglow[x,y] = 1
    if D > 0:
       y, D = y + yi, D - 2*dx
    D = D + 2*dy
  loopend = datetime.datetime.now()
  looptime = loopend - loopstart

  return imglow, looptime.microseconds

def plotLineHigh(x0,y0, x1,y1, imhigh):
  dx,dy,xi = x1 - x0,y1 - y0,1
  if dx < 0:
    xi, dx = -1 , -dx
  D, x = 2*dx - dy, x0

  loopstart = datetime.datetime.now()
  for y in range(y0 , y1):
    imhigh[x,y] = 1
    if D > 0:
       x, D = x + xi , D - 2*dy
    D = D + 2*dx
  loopend = datetime.datetime.now()
  looptime = loopend - loopstart
  return imhigh, looptime.microseconds

def brz(x0,y0, x1,y1, imgall):
  if abs(y1 - y0) < abs(x1 - x0):
    if x0 > x1 :
      imret, timeret = plotLineLow(x1, y1, x0, y0, imgall)
    else :
      imret, timeret = plotLineLow(x0, y0, x1, y1, imgall)
  else :
    if y0 > y1:
      imret, timeret = plotLineHigh(x1, y1, x0, y0, imgall)
    else :
      imret, timeret = plotLineHigh(x0, y0, x1, y1, imgall)
  return imret, timeret


