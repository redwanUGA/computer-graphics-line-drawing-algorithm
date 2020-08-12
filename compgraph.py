import cv2
import numpy as np

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
    for i in range(0,diffx):
        x = x0 + i
        y = int(diffy/diffx*i+y0)
        imgparx[x,y] = 1
    return imgparx

def basic_alg_ystrech(x0, y0, x1, y1, imgpary):
    if y1 < y0:
        x0, x1 = swap(x0, x1)
        y0, y1 = swap(y0, y1)
    diffx = x1 - x0
    diffy = y1 - y0
    for i in range(0, diffy):
        y = y0 + i
        x = int(diffx / diffy * i + x0)
        imgpary[x, y] = 1
    return imgpary

def basic_alg_xparallel(x0, y0, x1, y1, imgx):
    if x1 < x0:
        x0, x1 = swap(x0, x1)
    diffx = x1 - x0
    for i in range(0,diffx):
        x = x0 + i
        imgx[x,y0] = 1

    return imgx

def basic_alg_yparallel(x0, y0, x1, y1, imgy):
    if y1 < y0:
        y0, y1 = swap(y0, y1)
    diffy = y1 - y0
    for i in range(0, diffy):
        y = y0 + i
        imgy[x0, y] = 1
    return imgy


def basic_alg(x0, y0, x1, y1, imgtemp):
    diffx = abs(x1 - x0)
    diffy = abs(y1 - y0)
    if diffx == 0:
        basic_alg_yparallel(x0, y0, x1, y1, imgtemp)
    elif diffy == 0:
        basic_alg_xparallel(x0, y0, x1, y1, imgtemp)
    elif diffx >= diffy:
        basic_alg_xstretch(x0, y0, x1, y1, imgtemp)
    elif diffx < diffy:
        basic_alg_ystrech(x0, y0, x1, y1, imgtemp)
    return imgtemp

def plotLineLow(x0,y0, x1,y1, imglow):
  dx = x1 - x0
  dy = y1 - y0
  yi = 1
  if dy < 0:
    yi = -1
    dy = -dy
  D = 2*dy - dx
  y = y0

  for x in range(x0,x1):
    imglow[x,y] = 1
    if D > 0:
       y = y + yi
       D = D - 2*dx
    D = D + 2*dy

  return imglow

def plotLineHigh(x0,y0, x1,y1, imhigh):
  dx = x1 - x0
  dy = y1 - y0
  xi = 1
  if dx < 0:
    xi = -1
    dx = -dx
  D = 2*dx - dy
  x = x0

  for y in range(y0 , y1):
    imhigh[x,y] = 1
    if D > 0:
       x = x + xi
       D = D - 2*dy

    D = D + 2*dx
  return imhigh

def brz(x0,y0, x1,y1, imgall):
  if abs(y1 - y0) < abs(x1 - x0):
    if x0 > x1 :
      imret = plotLineLow(x1, y1, x0, y0, imgall)
    else :
      imret = plotLineLow(x0, y0, x1, y1, imgall)
  else :
    if y0 > y1:
      imret = plotLineHigh(x1, y1, x0, y0, imgall)
    else :
      imret = plotLineHigh(x0, y0, x1, y1, imgall)
  return imret


