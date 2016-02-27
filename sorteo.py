#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Copyright (C) <2016>  <@jorgescalona>

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>

import random
l=range(1,46)
control = 1
while control != 0:
    for i in l:
        prem=random.choice(l)
        indice=l.index(prem)
        print 'El ganador es: ', prem
        l.pop(indice)
        raw_input()
    if len(l)==0:
        control=0

