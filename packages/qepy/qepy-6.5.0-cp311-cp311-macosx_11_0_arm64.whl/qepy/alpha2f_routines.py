"""
Module alpha2f_routines


Defined at alpha2f.fpp lines 37-374

"""
from __future__ import print_function, absolute_import, division
import _qepy
import f90wrap.runtime
import logging

_arrays = {}
_objs = {}

def read_polarization():
    """
    read_polarization()
    
    
    Defined at alpha2f.fpp lines 47-144
    
    
    -----------------------------------------------------------------------
     This routine read the polarization vectors
     from [prefix].dyn* & lambda*.dat
    """
    _qepy.f90wrap_read_polarization()

def read_lam():
    """
    read_lam()
    
    
    Defined at alpha2f.fpp lines 148-205
    
    
    ------------------------------------------------------------------
     This routine reads lambad_{q nu} & omega_{q nu} from lambda*.dat
    """
    _qepy.f90wrap_read_lam()

def compute_a2f():
    """
    compute_a2f()
    
    
    Defined at alpha2f.fpp lines 209-301
    
    
    -----------------------------------------------------------------
     This routine writes a2F and phonon DOS to file(a2F.dat).
    """
    _qepy.f90wrap_compute_a2f()

def compute_lambda():
    """
    compute_lambda()
    
    
    Defined at alpha2f.fpp lines 305-372
    
    
    ---------------------------------------------------------------
     This routine computes omega_ln & lambda
    """
    _qepy.f90wrap_compute_lambda()


_array_initialisers = []
_dt_array_initialisers = []

try:
    for func in _array_initialisers:
        func()
except ValueError:
    logging.debug('unallocated array(s) detected on import of module \
        "alpha2f_routines".')

for func in _dt_array_initialisers:
    func()
