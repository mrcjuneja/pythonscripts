#!/usr/bin/env python
# Starting initialization for Rinkle's python implementation of slack model
import numpy 
import yaml
from phonopy import Phonopy
from phonopy.interface import vasp
from spglib import find_primitive
from phonopy.units import THzToEv, Kb, EvTokJmol, Hbar, THz, pi



##Read the gruneisen file

def read_gruneisen_yaml(filename):
    """
    Read the gruneisen.yaml and return:
    [frequencies, gruneisen parameter]
    """
    fileinfo = yaml.load(open(filename))
    phonon = fileinfo['phonon']
    for i in phonon:
	band = i['band']
	for j in band:
	frequency = j['frequency']
        gruneisen = j['gruneisen']
    return (numpy.array(frequency), numpy.array(gruneisen))

##calculate the volume
def volume_calc():
    with open ("POSCAR") as f:
        content = f.readlines()
        a1 = [x[2].split() for x in content] 
	b1 = [x[3].split() for x in content]
	c1 = [x[4].split() for x in content]
	ax, ay, az = float(a1[0]), float(a1[1]), float(a1[2])
        bx, by, bz = float(b1[0]), float(b1[1]), float(b1[2])
        cx, cy, cz = float(c1[0]), float(c1[1]), float(c1[2])	
	a = [ax, ay, az]
        b = [bx, by, bz]
        c = [cx, cy, cz]
	base = numpy.cross(b,c)
	volume = numpy.dot(base,a)
    return volume


# calculate number of atoms in the cell

def number_of_atoms_in_the_cell (primitive):
    poscar = 'POSCAR'
    cell = vasp.read_vasp(poscar)
    lattice, position, number = find_primitive(cell, symprec=1e-5)
    num = len(position)
    return num 


# Derived from phonopy code -- vasp.py -- read_vasp() -- used
# as an auxiliary part of the code to obtain the atoms, which
# are used to create a REFINED_POSCAR
def ase_type_atoms_object(lat, pos, num):



def debye_temp(filename): 
    """
    The filename should be : gruneisen.yaml
    Second moment : 
    #calculate by multiplying the frequency square and the density of state bot calculated by phonopy
    calculate by using the weighted sum of the frquency square divided by sum of weights
    """
    


def specific_heat_normal_mode(frequency, volume):
    """
    Refer Ashcroft mermin: Page-493 Eq. 25.17
    """



def mode_gruneisen(filename):
    """
    Calculate the mode gruneisen parameter from specific heat and mode-wise gruneisen parameter
    """

    



def slack_thermal_cond(debye_T, mod_grun, T):
    """
    Use the formula to get Kappa
    Refer- Eq.2.13 of the book
    High thermal conductivity - Slack model - Debye Callaway - Springer
    """

file_list = files_list_2 + files_list_3 + files_list_4


# Use matplotlib and python loops to write and plot the kappa with respect to temperature

# You may need to use operating system functions: import os and other derivatives.

# The final result should be the plot of kappa vs T 
