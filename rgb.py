#!/usr/bin/python

#MAD HELP FROM AUSTIN BIG BEAR SCHOBER

import serial
import pygame
import sys

from pygame.locals import *

pygame.init()

s = serial.Serial("/dev/ttyACM0")
DISPLAYSURF = pygame.display.set_mode((400,300))
while True:
	l = s.readline()
	x = l.rstrip().split(',')
	rgb = [int(val) for val in x]

	print rgb
	DISPLAYSURF.fill((rgb[0],rgb[1],rgb[2]))
	pygame.display.update()
	 




