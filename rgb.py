#!/usr/bin/python

import serial
import pygame

s = serial.Serial("/dev/ttyACM0")
while True:
	l = s.readline()
	x = l.rstrip().split(',')
	rgb = [int(val) for val in x]
	print x
	color = pygame.Color(rgb[0],rgb[1],rgb[2])
	print color
	 

