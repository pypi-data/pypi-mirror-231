from __future__ import print_function, absolute_import, division
# Fix
# MPI_IN_PLACE and MKL
import sys, os
from ctypes import util, CDLL, RTLD_LOCAL, RTLD_GLOBAL
if 'mpi4py' in sys.modules :
    if hasattr(util, '_findLib_ld') and hasattr(util, '_get_soname') :
        mpilib = util._get_soname(util._findLib_ld('mpi'))
    else :
        mpilib = None
    mpilib = mpilib or util.find_library('mpi') or util.find_library('mpifort')
    try:
        CDLL(mpilib, RTLD_LOCAL | RTLD_GLOBAL)
    except Exception :
        pass
try:
    if hasattr(util, '_findLib_ld'):
        mkllib = os.path.basename(util._findLib_ld('mkl_rt'))
    else :
        mkllib = util.find_library('mkl_rt')
    CDLL(mkllib, RTLD_LOCAL | RTLD_GLOBAL)
except Exception :
    pass

# control the output
import types
from .core import Logger, env
class QEpyLib :
    def __init__(self, **kwargs):
        import _qepy as qepylib
        sys.modules['_qepy'] = self
        self.qepylib =qepylib

    def __getattr__(self, attr):
        attr_value = getattr(self.qepylib, attr)
        if '__array__' not in attr :
            attr_value = Logger.stdout2file(attr_value, fileobj=env['STDOUT'])
        return attr_value
qepylib = QEpyLib()
# End fix
import _qepy
import f90wrap.runtime
import logging
import qepy.constants
import qepy.wvfct
import qepy.force_mod
import qepy.ifconstants
import qepy.vlocal
import qepy.fs
import qepy.wavefunctions
import qepy.rap_point_group
import qepy.oldxml_xml_io_base
import qepy.mp_bands
import qepy.rap_point_group_so
import qepy.ener
import qepy.scatter_mod
import qepy.read_input
import qepy.mp_bands_tddfpt
import qepy.relax
import qepy.pwcom
import qepy.scf
import qepy.oldxml_qexml_module
import qepy.qepy_common
import qepy.cellmd
import qepy.qepy_sys
import qepy.check_stop
import qepy.uspp_param
import qepy.command_line_options
import qepy.pw_restart_new
import qepy.funct
import qepy.gvect
import qepy.pp_module
import qepy.lsda_mod
import qepy.control_flags
import qepy.alpha2f_vals
import qepy.mp_diag
import qepy.wannier
import qepy.mp_pools
import qepy.us
import qepy.rap_point_group_is
import qepy.mp_orthopools
import qepy.mp_global
import qepy.gvecs
import qepy.grid_module
import qepy.fixed_occ
import qepy.fermi_proj_routines
import qepy.io_global
import qepy.uspp
import qepy.qes_read_module
import qepy.mp_world
import qepy.environment
import qepy.oldxml_pw_restart
import qepy.basis
import qepy.io_base_export
import qepy.spin_orb
import qepy.qepy_mod
import qepy.fft_types
import qepy.alpha2f_routines
import qepy.int_global_variables
import qepy.oldxml_io_rho_xml
import qepy.cell_base
import qepy.klist
import qepy.ions_base
import qepy.qexsd_module
import qepy.extrapolation

def impose_deviatoric_strain(at_old, at):
    """
    impose_deviatoric_strain(at_old, at)
    
    
    Defined at deviatoric.fpp lines 14-35
    
    Parameters
    ----------
    at_old : float array
    at : float array
    
    ---------------------------------------------------------------------
         Impose a pure deviatoric(volume-conserving) deformation
         Needed to enforce volume conservation in variable-cell MD/optimization
    """
    _qepy.f90wrap_impose_deviatoric_strain(at_old=at_old, at=at)

def impose_deviatoric_strain_2d(at_old, at):
    """
    impose_deviatoric_strain_2d(at_old, at)
    
    
    Defined at deviatoric.fpp lines 39-62
    
    Parameters
    ----------
    at_old : float array
    at : float array
    
    ---------------------------------------------------------------------
         Modif. of impose_deviatoric_strain but for
         Area conserving deformation(2DSHAPE) added by Richard Charles Andrew
         Physics Department, University if Pretoria,
         South Africa, august 2012
    """
    _qepy.f90wrap_impose_deviatoric_strain_2d(at_old=at_old, at=at)

def impose_deviatoric_stress(sigma):
    """
    impose_deviatoric_stress(sigma)
    
    
    Defined at deviatoric.fpp lines 66-80
    
    Parameters
    ----------
    sigma : float array
    
    ---------------------------------------------------------------------
         Impose a pure deviatoric stress
    """
    _qepy.f90wrap_impose_deviatoric_stress(sigma=sigma)

def impose_deviatoric_stress_2d(sigma):
    """
    impose_deviatoric_stress_2d(sigma)
    
    
    Defined at deviatoric.fpp lines 84-99
    
    Parameters
    ----------
    sigma : float array
    
    ---------------------------------------------------------------------
         Modif. of impose_deviatoric_stress but for
         Area conserving deformation(2DSHAPE) added by Richard Charles Andrew
         Physics Department, University if Pretoria,
         South Africa, august 2012
    """
    _qepy.f90wrap_impose_deviatoric_stress_2d(sigma=sigma)

def punch(what):
    """
    punch(what)
    
    
    Defined at punch.fpp lines 13-135
    
    Parameters
    ----------
    what : str
    
    ----------------------------------------------------------------------------
     This routine is called at the end of the run to save on a file
     the information needed for further processing(phonon etc.).
     * what = 'all' : write xml data file, charge density, wavefunctions
    (for final data);
     * what = 'config' : write xml data file and charge density; also,
                         for nks=1, wavefunctions in plain binary format
    (see why in comments below). For intermediate
                         or incomplete results;
     * what = 'config-nowf' : write xml data file iand charge density only
     * what = 'config-init' : write xml data file only excluding final results
    (for dry run, can be called at early stages).
    """
    _qepy.f90wrap_punch(what=what)

def close_files(lflag):
    """
    close_files(lflag)
    
    
    Defined at close_files.fpp lines 13-86
    
    Parameters
    ----------
    lflag : bool
    
    ----------------------------------------------------------------------------
     Close all files and synchronize processes for a new scf calculation.
    """
    _qepy.f90wrap_close_files(lflag=lflag)

def stress(sigma):
    """
    stress(sigma)
    
    
    Defined at stress.fpp lines 14-261
    
    Parameters
    ----------
    sigma : float array
    
    ----------------------------------------------------------------------
     Computes the total stress.
    """
    _qepy.f90wrap_stress(sigma=sigma)

def electrons():
    """
    electrons()
    
    
    Defined at electrons.fpp lines 18-344
    
    
    ----------------------------------------------------------------------------
     General self-consistency loop, also for hybrid functionals
     For non-hybrid functionals it just calls "electron_scf"
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%%%%%  Iterate hybrid functional  %%%%%%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """
    _qepy.f90wrap_electrons()

def electrons_scf(printout, exxen):
    """
    electrons_scf(printout, exxen)
    
    
    Defined at electrons.fpp lines 348-1362
    
    Parameters
    ----------
    printout : int
    exxen : float
    
    ----------------------------------------------------------------------------
     This routine is a driver of the self-consistent cycle.
     It uses the routine c_bands for computing the bands at fixed
     Hamiltonian, the routine sum_band to compute the charge density,
     the routine v_of_rho to compute the new potential and the routine
     mix_rho to mix input and output charge densities.
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%%%%%          iterate
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """
    _qepy.f90wrap_electrons_scf(printout=printout, exxen=exxen)

def exxenergyace():
    """
    exxenergyace = exxenergyace()
    
    
    Defined at electrons.fpp lines 1366-1411
    
    
    Returns
    -------
    exxenergyace : float
    
    --------------------------------------------------------------------------
     Compute exchange energy using ACE
    """
    exxenergyace = _qepy.f90wrap_exxenergyace()
    return exxenergyace

def scale_h():
    """
    scale_h()
    
    
    Defined at scale_h.fpp lines 14-105
    
    
    -----------------------------------------------------------------------
     When variable cell calculation are performed this routine scales the
     quantities needed in the calculation of the hamiltonian using the
     new and old cell parameters.
    """
    _qepy.f90wrap_scale_h()

def pw2casino(istep):
    """
    pw2casino(istep)
    
    
    Defined at pw2casino.fpp lines 16-90
    
    Parameters
    ----------
    istep : int
    
    ----------------------------------------------------------------------------
    """
    _qepy.f90wrap_pw2casino(istep=istep)

def forces():
    """
    forces()
    
    
    Defined at forces.fpp lines 18-417
    
    
    ----------------------------------------------------------------------------
     This routine is a driver routine which computes the forces
     acting on the atoms. The complete expression of the forces
     contains four parts which are computed by different routines:
      a)  force_lc,     local contribution to the forces
      b)  force_cc,     contribution due to NLCC
      c)  force_ew,     contribution due to the electrostatic ewald term
      d)  force_us,     contribution due to the non-local potential
      e)  force_corr,   correction term for incomplete self-consistency
      f)  force_hub,    contribution due to the Hubbard term
      g)  force_london, semi-empirical correction for dispersion forces
      h)  force_d3,     Grimme-D3(DFT-D3) correction to dispersion forces
    """
    _qepy.f90wrap_forces()

def move_ions(idone, ions_status):
    """
    move_ions(idone, ions_status)
    
    
    Defined at move_ions.fpp lines 13-362
    
    Parameters
    ----------
    idone : int
    ions_status : int
    
    ----------------------------------------------------------------------------
     Perform a ionic step, according to the requested scheme:
     * lbfgs: bfgs minimizations
     * lmd: molecular dynamics( all kinds )
     Additional variables affecting the calculation:
     * lmovecell: Variable-cell calculation
     * calc: type of MD
     * lconstrain: constrained MD
     * "idone" is the counter on ionic moves, "nstep" their total number
     * "istep" contains the number of all steps including previous runs.
     Coefficients for potential and wavefunctions extrapolation are
     no longer computed here but in update_pot.
    """
    _qepy.f90wrap_move_ions(idone=idone, ions_status=ions_status)

def add_qexsd_step(i_step):
    """
    add_qexsd_step(i_step)
    
    
    Defined at add_qexsd_step.fpp lines 17-103
    
    Parameters
    ----------
    i_step : int
    
    -----------------------------------------------------------------
    ------------------------------------------------------------------------
           START_GLOBAL_VARIABLES( INTENT(IN) )
    --------------------------------------------------------------------------
    """
    _qepy.f90wrap_add_qexsd_step(i_step=i_step)

def hinit1():
    """
    hinit1()
    
    
    Defined at hinit1.fpp lines 13-86
    
    
    ----------------------------------------------------------------------------
     Atomic configuration dependent hamiltonian initialization,
     potential, wavefunctions for Hubbard U.
     Important note: it does not recompute structure factors and core charge,
     they must be computed before this routine is called.
    """
    _qepy.f90wrap_hinit1()

def run_pwscf():
    """
    exit_status = run_pwscf()
    
    
    Defined at run_pwscf.fpp lines 13-289
    
    
    Returns
    -------
    exit_status : int
    
    ----------------------------------------------------------------------------
     Author: Paolo Giannozzi
     License: GNU
     Summary: Run an instance of the Plane Wave Self-Consistent Field code
     Run an instance of the Plane Wave Self-Consistent Field code
     MPI initialization and input data reading is performed in the
     calling code - returns in exit_status the exit code for pw.x,
     returned in the shell. Values are:
     * 0: completed successfully
     * 1: an error has occurred(value returned by the errore() routine)
     * 2-127: convergence error
        * 2: scf convergence error
        * 3: ion convergence error
     * 128-255: code exited due to specific trigger
        * 255: exit due to user request, or signal trapped,
              or time > max_seconds
    (note: in the future, check_stop_now could also return a value
         to specify the reason of exiting, and the value could be used
         to return a different value for different reasons)
     @Note
     10/01/17 Samuel Ponce: Add Ford documentation
     @endnote
    """
    exit_status = _qepy.f90wrap_run_pwscf()
    return exit_status

def reset_gvectors():
    """
    reset_gvectors()
    
    
    Defined at run_pwscf.fpp lines 294-334
    
    
    -------------------------------------------------------------
     Prepare a new scf calculation with newly recomputed grids,
     restarting from scratch, not from available data of previous
     steps(dimensions and file lengths will be different in general)
     Useful as a check of variable-cell optimization:
     once convergence is achieved, compare the final energy with the
     energy computed with G-vectors and plane waves for the final cell
    """
    _qepy.f90wrap_reset_gvectors()

def reset_exx():
    """
    reset_exx()
    
    
    Defined at run_pwscf.fpp lines 339-363
    
    
    -------------------------------------------------------------
    """
    _qepy.f90wrap_reset_exx()

def reset_magn():
    """
    reset_magn()
    
    
    Defined at run_pwscf.fpp lines 368-394
    
    
    ----------------------------------------------------------------
     LSDA optimization: a final configuration with zero
     absolute magnetization has been found and we check
     if it is really the minimum energy structure by
     performing a new scf iteration without any "electronic" history.
    """
    _qepy.f90wrap_reset_magn()

def reset_starting_magnetization():
    """
    reset_starting_magnetization()
    
    
    Defined at run_pwscf.fpp lines 399-483
    
    
    -------------------------------------------------------------------
     On input, the scf charge density is needed.
     On output, new values for starting_magnetization, angle1, angle2
     estimated from atomic magnetic moments - to be used in last step.
    """
    _qepy.f90wrap_reset_starting_magnetization()

def stop_run(exit_status):
    """
    stop_run(exit_status)
    
    
    Defined at stop_run.fpp lines 13-59
    
    Parameters
    ----------
    exit_status : int
    
    ----------------------------------------------------------------------------
     Close all files and synchronize processes before stopping:
     * exit_status = 0: successfull execution, remove temporary files;
     * exit_status =-1: code stopped by user request;
     * exit_status = 1: convergence not achieved.
     Do not remove temporary files needed for restart.
    """
    _qepy.f90wrap_stop_run(exit_status=exit_status)

def do_stop(exit_status):
    """
    do_stop(exit_status)
    
    
    Defined at stop_run.fpp lines 63-93
    
    Parameters
    ----------
    exit_status : int
    
    ---------------------------------------
     Stop the run.
    """
    _qepy.f90wrap_do_stop(exit_status=exit_status)

def closefile():
    """
    closefile()
    
    
    Defined at stop_run.fpp lines 97-108
    
    
    ----------------------------------------------------------------------------
     Close all files and synchronize processes before stopping.
     Called by "sigcatch" when it receives a signal.
    """
    _qepy.f90wrap_closefile()

def sum_band():
    """
    sum_band()
    
    
    Defined at sum_band.fpp lines 14-818
    
    
    ----------------------------------------------------------------------------
     ... Calculates the symmetrized charge density and related quantities
     ... Also computes the occupations and the sum of occupied eigenvalues.
    """
    _qepy.f90wrap_sum_band()

def sum_bec(ik, current_spin, ibnd_start, ibnd_end, this_bgrp_nbnd):
    """
    sum_bec(ik, current_spin, ibnd_start, ibnd_end, this_bgrp_nbnd)
    
    
    Defined at sum_band.fpp lines 821-1053
    
    Parameters
    ----------
    ik : int
    current_spin : int
    ibnd_start : int
    ibnd_end : int
    this_bgrp_nbnd : int
    
    ----------------------------------------------------------------------------
     This routine computes the sum over bands
         \sum_i <\psi_i|\beta_l>w_i<\beta_m|\psi_i>
     for point "ik" and, for LSDA, spin "current_spin"
     Calls calbec to compute "becp"=<beta_m|psi_i>
     Output is accumulated(unsymmetrized) into "becsum", module "uspp"
     Routine used in sum_band(if okvan) and in compute_becsum, called by hinit1(if \
         okpaw)
    """
    _qepy.f90wrap_sum_bec(ik=ik, current_spin=current_spin, ibnd_start=ibnd_start, \
        ibnd_end=ibnd_end, this_bgrp_nbnd=this_bgrp_nbnd)

def add_becsum_nc(na, np, becsum_nc, becsum):
    """
    add_becsum_nc(na, np, becsum_nc, becsum)
    
    
    Defined at sum_band.fpp lines 1057-1102
    
    Parameters
    ----------
    na : int
    np : int
    becsum_nc : complex array
    becsum : float array
    
    ----------------------------------------------------------------------------
     This routine multiplies becsum_nc by the identity and the Pauli matrices,
     saves it in becsum for the calculation of augmentation charge and
     magnetization.
    """
    _qepy.f90wrap_add_becsum_nc(na=na, np=np, becsum_nc=becsum_nc, becsum=becsum)

def add_becsum_so(na, np, becsum_nc, becsum):
    """
    add_becsum_so(na, np, becsum_nc, becsum)
    
    
    Defined at sum_band.fpp lines 1106-1169
    
    Parameters
    ----------
    na : int
    np : int
    becsum_nc : complex array
    becsum : float array
    
    ----------------------------------------------------------------------------
     This routine multiplies becsum_nc by the identity and the Pauli matrices,
     rotates it as appropriate for the spin-orbit case, saves it in becsum
     for the calculation of augmentation charge and magnetization.
    """
    _qepy.f90wrap_add_becsum_so(na=na, np=np, becsum_nc=becsum_nc, becsum=becsum)

def non_scf():
    """
    non_scf()
    
    
    Defined at non_scf.fpp lines 14-114
    
    
    -----------------------------------------------------------------------
     Diagonalization of the KS hamiltonian in the non-scf case.
    """
    _qepy.f90wrap_non_scf()

def v_of_rho(self, rho_core, rhog_core, etotefield, v):
    """
    ehart, etxc, vtxc, eth, charge = v_of_rho(self, rho_core, rhog_core, etotefield, \
        v)
    
    
    Defined at v_of_rho.fpp lines 14-109
    
    Parameters
    ----------
    rho : Scf_Type
    rho_core : float array
    rhog_core : complex array
    etotefield : float
    v : Scf_Type
    
    Returns
    -------
    ehart : float
    etxc : float
    vtxc : float
    eth : float
    charge : float
    
    ----------------------------------------------------------------------------
     This routine computes the Hartree and Exchange and Correlation
     potential and energies which corresponds to a given charge density
     The XC potential is computed in real space, while the
     Hartree potential is computed in reciprocal space.
    """
    ehart, etxc, vtxc, eth, charge = _qepy.f90wrap_v_of_rho(rho=self._handle, \
        rho_core=rho_core, rhog_core=rhog_core, etotefield=etotefield, v=v._handle)
    return ehart, etxc, vtxc, eth, charge

def v_xc_meta(self, rho_core, rhog_core, etxc, vtxc, v, kedtaur):
    """
    v_xc_meta(self, rho_core, rhog_core, etxc, vtxc, v, kedtaur)
    
    
    Defined at v_of_rho.fpp lines 114-302
    
    Parameters
    ----------
    rho : Scf_Type
    rho_core : float array
    rhog_core : complex array
    etxc : float
    vtxc : float
    v : float array
    kedtaur : float array
    
    ----------------------------------------------------------------------------
     Exchange-Correlation potential(meta) Vxc(r) from n(r)
    """
    _qepy.f90wrap_v_xc_meta(rho=self._handle, rho_core=rho_core, \
        rhog_core=rhog_core, etxc=etxc, vtxc=vtxc, v=v, kedtaur=kedtaur)

def v_xc(self, rho_core, rhog_core, v):
    """
    etxc, vtxc = v_xc(self, rho_core, rhog_core, v)
    
    
    Defined at v_of_rho.fpp lines 306-471
    
    Parameters
    ----------
    rho : Scf_Type
    rho_core : float array
    rhog_core : complex array
    v : float array
    
    Returns
    -------
    etxc : float
    vtxc : float
    
    ----------------------------------------------------------------------------
     Exchange-Correlation potential Vxc(r) from n(r)
    """
    etxc, vtxc = _qepy.f90wrap_v_xc(rho=self._handle, rho_core=rho_core, \
        rhog_core=rhog_core, v=v)
    return etxc, vtxc

def v_h(rhog, v):
    """
    ehart, charge = v_h(rhog, v)
    
    
    Defined at v_of_rho.fpp lines 475-622
    
    Parameters
    ----------
    rhog : complex array
    v : float array
    
    Returns
    -------
    ehart : float
    charge : float
    
    ----------------------------------------------------------------------------
     Hartree potential VH(r) from n(G)
    """
    ehart, charge = _qepy.f90wrap_v_h(rhog=rhog, v=v)
    return ehart, charge

def v_hubbard(ns, v_hub):
    """
    eth = v_hubbard(ns, v_hub)
    
    
    Defined at v_of_rho.fpp lines 626-795
    
    Parameters
    ----------
    ns : float array
    v_hub : float array
    
    Returns
    -------
    eth : float
    
    ---------------------------------------------------------------------
     Computes Hubbard potential and Hubbard energy
    """
    eth = _qepy.f90wrap_v_hubbard(ns=ns, v_hub=v_hub)
    return eth

def v_hubbard_nc(ns, v_hub, eth):
    """
    v_hubbard_nc(ns, v_hub, eth)
    
    
    Defined at v_of_rho.fpp lines 798-957
    
    Parameters
    ----------
    ns : complex array
    v_hub : complex array
    eth : float
    
    -------------------------------------
     Noncollinear version of v_hubbard.
    """
    _qepy.f90wrap_v_hubbard_nc(ns=ns, v_hub=v_hub, eth=eth)

def v_h_of_rho_r(rhor, v):
    """
    ehart, charge = v_h_of_rho_r(rhor, v)
    
    
    Defined at v_of_rho.fpp lines 961-1005
    
    Parameters
    ----------
    rhor : float array
    v : float array
    
    Returns
    -------
    ehart : float
    charge : float
    
    ----------------------------------------------------------------------------
     Hartree potential VH(r) from a density in R space n(r)
    """
    ehart, charge = _qepy.f90wrap_v_h_of_rho_r(rhor=rhor, v=v)
    return ehart, charge

def gradv_h_of_rho_r(rho, gradv):
    """
    gradv_h_of_rho_r(rho, gradv)
    
    
    Defined at v_of_rho.fpp lines 1008-1097
    
    Parameters
    ----------
    rho : float array
    gradv : float array
    
    ----------------------------------------------------------------------------
     Gradient of Hartree potential in R space from a total
    (spinless) density in R space n(r)
    """
    _qepy.f90wrap_gradv_h_of_rho_r(rho=rho, gradv=gradv)

def laxlib_free_ortho_group():
    """
    laxlib_free_ortho_group()
    
    
    Defined at la_helper.fpp lines 6-12
    
    
    ----------------------------------------------------------------------------
    """
    _qepy.f90wrap_laxlib_free_ortho_group()

def set_mpi_comm_4_solvers(parent_comm, intra_bgrp_comm_, inter_bgrp_comm_):
    """
    set_mpi_comm_4_solvers(parent_comm, intra_bgrp_comm_, inter_bgrp_comm_)
    
    
    Defined at set_mpi_comm_4_solvers.fpp lines 13-37
    
    Parameters
    ----------
    parent_comm : int
    intra_bgrp_comm_ : int
    inter_bgrp_comm_ : int
    
    ----------------------------------------------------------------------------
    """
    _qepy.f90wrap_set_mpi_comm_4_solvers(parent_comm=parent_comm, \
        intra_bgrp_comm_=intra_bgrp_comm_, inter_bgrp_comm_=inter_bgrp_comm_)

def do_elf(elf):
    """
    do_elf(elf)
    
    
    Defined at elf.fpp lines 13-175
    
    Parameters
    ----------
    elf : float array
    
    -----------------------------------------------------------------------
      calculation of the electron localization function;
         elf = 1/(1+d**2)
      where
         d = ( t(r) - t_von_Weizacker(r) ) / t_Thomas-Fermi(r)
      and
         t(r) = (hbar**2/2m) * \sum_{k,i} |grad psi_{k,i}|**2
    (kinetic energy density)
         t_von_Weizaecker(r) = (hbar**2/2m) * 0.25 * |grad rho(r)|**2/rho
    (non-interacting boson)
         t_Thomas-Fermi(r) = (hbar**2/2m) * 3/5 * (3*pi**2)**(2/3) * rho**(5/3)
    (free electron gas)
      see also http://en.wikipedia.org/wiki/Electron_localization_function
    """
    _qepy.f90wrap_do_elf(elf=elf)

def do_rdg(rdg):
    """
    do_rdg(rdg)
    
    
    Defined at elf.fpp lines 178-209
    
    Parameters
    ----------
    rdg : float array
    
    -----------------------------------------------------------------------
      reduced density gradient
         rdg(r) = (1/2) (1/(3*pi**2))**(1/3) * |\nabla rho(r)|/rho(r)**(4/3)
    """
    _qepy.f90wrap_do_rdg(rdg=rdg)

def do_sl2rho(sl2rho):
    """
    do_sl2rho(sl2rho)
    
    
    Defined at elf.fpp lines 212-263
    
    Parameters
    ----------
    sl2rho : float array
    
    -----------------------------------------------------------------------
      Computes sign(l2)*rho(r), where l2 is the second largest eigenvalue
      of the electron-density Hessian matrix
    """
    _qepy.f90wrap_do_sl2rho(sl2rho=sl2rho)

def local_dos(iflag, lsign, kpoint, kband, spin_component, emin, emax, dos):
    """
    local_dos(iflag, lsign, kpoint, kband, spin_component, emin, emax, dos)
    
    
    Defined at local_dos.fpp lines 15-418
    
    Parameters
    ----------
    iflag : int
    lsign : bool
    kpoint : int
    kband : int
    spin_component : int
    emin : float
    emax : float
    dos : float array
    
    --------------------------------------------------------------------
         iflag=0: calculates |psi|^2 for band "kband" at point "kpoint"
         iflag=1: calculates the local density of state at e_fermi
    (only for metals)
         iflag=2: calculates the local density of  electronic entropy
    (only for metals with fermi spreading)
         iflag=3: calculates the integral of local dos from "emin" to "emax"
    (emin, emax in Ry)
         lsign:   if true and k=gamma and iflag=0, write |psi|^2 * sign(psi)
         spin_component: for iflag=3 and LSDA calculations only
                         0 for up+down dos,  1 for up dos, 2 for down dos
    """
    _qepy.f90wrap_local_dos(iflag=iflag, lsign=lsign, kpoint=kpoint, kband=kband, \
        spin_component=spin_component, emin=emin, emax=emax, dos=dos)

def local_dos_mag(spin_component, kpoint, kband, raux):
    """
    local_dos_mag(spin_component, kpoint, kband, raux)
    
    
    Defined at local_dos_mag.fpp lines 14-275
    
    Parameters
    ----------
    spin_component : int
    kpoint : int
    kband : int
    raux : float array
    
    ----------------------------------------------------------------------------
     ... compute the contribution of band "kband" at k-point "kpoint"
     ... to the noncolinear magnetization for the given "spin_component"
    """
    _qepy.f90wrap_local_dos_mag(spin_component=spin_component, kpoint=kpoint, \
        kband=kband, raux=raux)

def oldxml_wfcinit(starting=None):
    """
    oldxml_wfcinit([starting])
    
    
    Defined at oldxml_wfcinit.fpp lines 14-178
    
    Parameters
    ----------
    starting : str
    
    ----------------------------------------------------------------------------
     ... This routine computes an estimate of the starting wavefunctions
     ... from superposition of atomic wavefunctions and/or random wavefunctions.
     ... It also open needed files or memory buffers
    """
    _qepy.f90wrap_oldxml_wfcinit(starting=starting)

def oldxml_potinit(starting=None):
    """
    oldxml_potinit([starting])
    
    
    Defined at oldxml_potinit.fpp lines 14-257
    
    Parameters
    ----------
    starting : str
    
    ----------------------------------------------------------------------------
     ... This routine initializes the self consistent potential in the array
     ... vr. There are three possible cases:
     ... a) the code is restarting from a broken run:
     ...    read rho from data stored during the previous run
     ... b) the code is performing a non-scf calculation following a scf one:
     ...    read rho from the file produced by the scf calculation
     ... c) the code starts a new calculation:
     ...    calculate rho as a sum of atomic charges
     ... In all cases the scf potential is recalculated and saved in vr
    """
    _qepy.f90wrap_oldxml_potinit(starting=starting)

def oldxml_nc_magnetization_from_lsda(nnr, nspin, rho):
    """
    oldxml_nc_magnetization_from_lsda(nnr, nspin, rho)
    
    
    Defined at oldxml_potinit.fpp lines 261-298
    
    Parameters
    ----------
    nnr : int
    nspin : int
    rho : float array
    
    -------------
    """
    _qepy.f90wrap_oldxml_nc_magnetization_from_lsda(nnr=nnr, nspin=nspin, rho=rho)

def oldxml_read_file():
    """
    oldxml_read_file()
    
    
    Defined at oldxml_read_file.fpp lines 18-187
    
    
    ----------------------------------------------------------------------------
     Wrapper routine, for compatibility
    """
    _qepy.f90wrap_oldxml_read_file()

def oldxml_read_xml_file():
    """
    oldxml_read_xml_file()
    
    
    Defined at oldxml_read_file.fpp lines 190-192
    
    
    """
    _qepy.f90wrap_oldxml_read_xml_file()

def oldxml_read_xml_file_nobs():
    """
    oldxml_read_xml_file_nobs()
    
    
    Defined at oldxml_read_file.fpp lines 194-196
    
    
    """
    _qepy.f90wrap_oldxml_read_xml_file_nobs()

def oldxml_read_xml_file_internal(withbs):
    """
    oldxml_read_xml_file_internal(withbs)
    
    
    Defined at oldxml_read_file.fpp lines 199-502
    
    Parameters
    ----------
    withbs : bool
    
    ----------------------------------------------------------------------------
     ... This routine allocates space for all quantities already computed
     ... in the pwscf program and reads them from the data file.
     ... All quantities that are initialized in subroutine "setup" when
     ... starting from scratch should be initialized here when restarting
    """
    _qepy.f90wrap_oldxml_read_xml_file_internal(withbs=withbs)

def qepy_setlocal():
    """
    qepy_setlocal()
    
    
    Defined at qepy_setlocal.fpp lines 18-138
    
    
    ----------------------------------------------------------------------
     This routine computes the local potential in real space vltot(ir).
    """
    _qepy.f90wrap_qepy_setlocal()

def qepy_v_of_rho_all(self, rho_core, rhog_core, etotefield, v):
    """
    ehart, etxc, vtxc, eth, charge = qepy_v_of_rho_all(self, rho_core, rhog_core, \
        etotefield, v)
    
    
    Defined at qepy_v_of_rho.fpp lines 14-98
    
    Parameters
    ----------
    rho : Scf_Type
    rho_core : float array
    rhog_core : complex array
    etotefield : float
    v : Scf_Type
    
    Returns
    -------
    ehart : float
    etxc : float
    vtxc : float
    eth : float
    charge : float
    
    ----------------------------------------------------------------------------
     This routine computes the Hartree and Exchange and Correlation
     potential and energies which corresponds to a given charge density
     The XC potential is computed in real space, while the
     Hartree potential is computed in reciprocal space.
    """
    ehart, etxc, vtxc, eth, charge = \
        _qepy.f90wrap_qepy_v_of_rho_all(rho=self._handle, rho_core=rho_core, \
        rhog_core=rhog_core, etotefield=etotefield, v=v._handle)
    return ehart, etxc, vtxc, eth, charge

def qepy_v_of_rho(self, rho_core, rhog_core, etotefield, v):
    """
    ehart, etxc, vtxc, eth, charge = qepy_v_of_rho(self, rho_core, rhog_core, \
        etotefield, v)
    
    
    Defined at qepy_v_of_rho.fpp lines 102-207
    
    Parameters
    ----------
    rho : Scf_Type
    rho_core : float array
    rhog_core : complex array
    etotefield : float
    v : Scf_Type
    
    Returns
    -------
    ehart : float
    etxc : float
    vtxc : float
    eth : float
    charge : float
    
    ----------------------------------------------------------------------------
     This routine computes the Hartree and Exchange and Correlation
     potential and energies which corresponds to a given charge density
     The XC potential is computed in real space, while the
     Hartree potential is computed in reciprocal space.
    """
    ehart, etxc, vtxc, eth, charge = _qepy.f90wrap_qepy_v_of_rho(rho=self._handle, \
        rho_core=rho_core, rhog_core=rhog_core, etotefield=etotefield, v=v._handle)
    return ehart, etxc, vtxc, eth, charge

def qepy_calc_energies():
    """
    qepy_calc_energies()
    
    
    Defined at qepy_pw2casino_write.fpp lines 298-754
    
    
    """
    _qepy.f90wrap_qepy_calc_energies()

def qepy_init_run():
    """
    qepy_init_run()
    
    
    Defined at qepy_init_run.fpp lines 13-147
    
    
    ----------------------------------------------------------------------------
    """
    _qepy.f90wrap_qepy_init_run()

def qepy_pwscf(infile, my_world_comm=None, oldxml=None, embed=None):
    """
    qepy_pwscf(infile[, my_world_comm, oldxml, embed])
    
    
    Defined at qepy_pwscf.fpp lines 13-140
    
    Parameters
    ----------
    infile : str
    my_world_comm : int
    oldxml : bool
    embed : Embed_Base
    
    """
    _qepy.f90wrap_qepy_pwscf(infile=infile, my_world_comm=my_world_comm, \
        oldxml=oldxml, embed=None if embed is None else embed._handle)

def qepy_pwscf_finalise():
    """
    qepy_pwscf_finalise()
    
    
    Defined at qepy_pwscf.fpp lines 143-148
    
    
    """
    _qepy.f90wrap_qepy_pwscf_finalise()

def qepy_initial(self=None, embed=None):
    """
    qepy_initial([self, embed])
    
    
    Defined at qepy_pwscf.fpp lines 150-191
    
    Parameters
    ----------
    input : Input_Base
    embed : Embed_Base
    
    """
    _qepy.f90wrap_qepy_initial(input=None if self is None else self._handle, \
        embed=None if embed is None else embed._handle)

def qepy_finalise_end(self=None):
    """
    qepy_finalise_end([self])
    
    
    Defined at qepy_pwscf.fpp lines 193-205
    
    Parameters
    ----------
    input : Input_Base
    
    """
    _qepy.f90wrap_qepy_finalise_end(input=None if self is None else self._handle)

def qepy_run_pwscf():
    """
    exit_status = qepy_run_pwscf()
    
    
    Defined at qepy_run_pwscf.fpp lines 13-307
    
    
    Returns
    -------
    exit_status : int
    
    ----------------------------------------------------------------------------
     Author: Paolo Giannozzi
     License: GNU
     Summary: Run an instance of the Plane Wave Self-Consistent Field code
     Run an instance of the Plane Wave Self-Consistent Field code
     MPI initialization and input data reading is performed in the
     calling code - returns in exit_status the exit code for pw.x,
     returned in the shell. Values are:
     * 0: completed successfully
     * 1: an error has occurred(value returned by the errore() routine)
     * 2-127: convergence error
        * 2: scf convergence error
        * 3: ion convergence error
     * 128-255: code exited due to specific trigger
        * 255: exit due to user request, or signal trapped,
              or time > max_seconds
    (note: in the future, check_stop_now could also return a value
         to specify the reason of exiting, and the value could be used
         to return a different value for different reasons)
     @Note
     10/01/17 Samuel Ponce: Add Ford documentation
     @endnote
    """
    exit_status = _qepy.f90wrap_qepy_run_pwscf()
    return exit_status

def qepy_electrons():
    """
    qepy_electrons()
    
    
    Defined at qepy_electrons.fpp lines 18-352
    
    
    ----------------------------------------------------------------------------
     General self-consistency loop, also for hybrid functionals
     For non-hybrid functionals it just calls "electron_scf"
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%%%%%  Iterate hybrid functional  %%%%%%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """
    _qepy.f90wrap_qepy_electrons()

def qepy_electrons_scf(printout, exxen):
    """
    qepy_electrons_scf(printout, exxen)
    
    
    Defined at qepy_electrons.fpp lines 356-1525
    
    Parameters
    ----------
    printout : int
    exxen : float
    
    ----------------------------------------------------------------------------
     This routine is a driver of the self-consistent cycle.
     It uses the routine c_bands for computing the bands at fixed
     Hamiltonian, the routine sum_band to compute the charge density,
     the routine v_of_rho to compute the new potential and the routine
     mix_rho to mix input and output charge densities.
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%%%%%          iterate
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """
    _qepy.f90wrap_qepy_electrons_scf(printout=printout, exxen=exxen)

def qepy_delta_e(vr):
    """
    qepy_delta_e = qepy_delta_e(vr)
    
    
    Defined at qepy_electrons.fpp lines 1577-1649
    
    Parameters
    ----------
    vr : float array
    
    Returns
    -------
    qepy_delta_e : float
    
    -----------------------------------------------------------------------
     This function computes \(\textrm{delta_e}\), where:
     $$\begin{alignat*}{2} \text{delta}\_\text{e} &= - \
         \int\text{rho}\%\text{of}\_\text{r(r)}\cdot
                                                               \text{v}\%\text{of}\_\text{r(r)} && \
                              &= - \int \text{rho}\%\text{kin}\_\text{r(r)}\cdot \text{v}\%\text{kin}\_
                                                               \text{r(r)} && \text{[for Meta-GGA]} \
                              &= - \sum \text{rho}\%\text{ns}\cdot \text{v}\%\text{ns} &&
                                                                                   \text{[for LDA+U]}\
                              &= - \sum \text{becsum}\cdot \text{D1}\_\text{Hxc} && \text{[for PAW]}
                                                                                      \end{alignat*} $$
     ... delta_e =  - \int rho%of_r(r)  v%of_r(r)
                    - \int rho%kin_r(r) v%kin_r(r) [for Meta-GGA]
                    - \sum rho%ns       v%ns       [for LDA+U]
                    - \sum becsum       D1_Hxc     [for PAW]
    """
    qepy_delta_e = _qepy.f90wrap_qepy_delta_e(vr=vr)
    return qepy_delta_e

def qepy_electrons_nscf(printout, exxen):
    """
    qepy_electrons_nscf(printout, exxen)
    
    
    Defined at qepy_electrons_nscf.fpp lines 13-320
    
    Parameters
    ----------
    printout : int
    exxen : float
    
    ----------------------------------------------------------------------------
     This routine is a driver of the self-consistent cycle.
     It uses the routine c_bands for computing the bands at fixed
     Hamiltonian, the routine sum_band to compute the charge density,
     the routine v_of_rho to compute the new potential and the routine
     mix_rho to mix input and output charge densities.
    """
    _qepy.f90wrap_qepy_electrons_nscf(printout=printout, exxen=exxen)

def qepy_hinit1():
    """
    qepy_hinit1()
    
    
    Defined at qepy_hinit1.fpp lines 13-86
    
    
    ----------------------------------------------------------------------------
     Atomic configuration dependent hamiltonian initialization,
     potential, wavefunctions for Hubbard U.
     Important note: it does not recompute structure factors and core charge,
     they must be computed before this routine is called.
    """
    _qepy.f90wrap_qepy_hinit1()

def qepy_forces(icalc=None):
    """
    qepy_forces([icalc])
    
    
    Defined at qepy_forces.fpp lines 18-453
    
    Parameters
    ----------
    icalc : int
    
    ----------------------------------------------------------------------------
     This routine is a driver routine which computes the forces
     acting on the atoms. The complete expression of the forces
     contains four parts which are computed by different routines:
      a)  force_lc,     local contribution to the forces
      b)  force_cc,     contribution due to NLCC
      c)  force_ew,     contribution due to the electrostatic ewald term
      d)  force_us,     contribution due to the non-local potential
      e)  force_corr,   correction term for incomplete self-consistency
      f)  force_hub,    contribution due to the Hubbard term
      g)  force_london, semi-empirical correction for dispersion forces
      h)  force_d3,     Grimme-D3(DFT-D3) correction to dispersion forces
    """
    _qepy.f90wrap_qepy_forces(icalc=icalc)

def qepy_stop_run(exit_status, print_flag=None, what=None, finalize=None):
    """
    qepy_stop_run(exit_status[, print_flag, what, finalize])
    
    
    Defined at qepy_stop_run.fpp lines 13-116
    
    Parameters
    ----------
    exit_status : int
    print_flag : int
    what : str
    finalize : bool
    
    ----------------------------------------------------------------------------
     Close all files and synchronize processes before stopping:
     * exit_status = 0: successfull execution, remove temporary files;
     * exit_status =-1: code stopped by user request;
     * exit_status = 1: convergence not achieved.
     Do not remove temporary files needed for restart.
    qepy -->
     Also add some from pwscf and run_pwscf
     Merge and modify the mp_global.mp_global_end
    qepy <--
    """
    _qepy.f90wrap_qepy_stop_run(exit_status=exit_status, print_flag=print_flag, \
        what=what, finalize=finalize)

def qepy_stress(sigma, icalc=None):
    """
    qepy_stress(sigma[, icalc])
    
    
    Defined at qepy_stress.fpp lines 14-276
    
    Parameters
    ----------
    sigma : float array
    icalc : int
    
    ----------------------------------------------------------------------
     Computes the total stress.
    """
    _qepy.f90wrap_qepy_stress(sigma=sigma, icalc=icalc)

def fftsort(n, ia):
    """
    fftsort(n, ia)
    
    
    Defined at scatter_mod.fpp lines 369-445
    
    Parameters
    ----------
    n : int
    ia : int array
    
    ---------------------------------------------------------------------
     sort an integer array ia(1:n) into ascending order using heapsort algorithm.
     n is input, ia is replaced on output by its sorted rearrangement.
     create an index table(ind) by making an exchange in the index array
     whenever an exchange is made on the sorted data array(ia).
     in case of equal values in the data array(ia) the values in the
     index array(ind) are used to order the entries.
     if on input ind(1)  = 0 then indices are initialized in the routine,
     if on input ind(1)
    = 0 then indices are assumed to have been
                    initialized before entering the routine and these
                    indices are carried around during the sorting process
     no work space needed
     free us from machine-dependent sorting-routines
     adapted from Numerical Recipes pg. 329(new edition)
    """
    _qepy.f90wrap_fftsort(n=n, ia=ia)

def potinit():
    """
    potinit()
    
    
    Defined at potinit.fpp lines 14-247
    
    
    ----------------------------------------------------------------------------
     ... This routine initializes the self consistent potential in the array
     ... vr. There are three possible cases:
     ... a) the code is restarting from a broken run:
     ...    read rho from data stored during the previous run
     ... b) the code is performing a non-scf calculation following a scf one:
     ...    read rho from the file produced by the scf calculation
     ... c) the code starts a new calculation:
     ...    calculate rho as a sum of atomic charges
     ... In all cases the scf potential is recalculated and saved in vr
    """
    _qepy.f90wrap_potinit()

def nc_magnetization_from_lsda(ngm, nspin, rho):
    """
    nc_magnetization_from_lsda(ngm, nspin, rho)
    
    
    Defined at potinit.fpp lines 251-281
    
    Parameters
    ----------
    ngm : int
    nspin : int
    rho : complex array
    
    -------------
    """
    _qepy.f90wrap_nc_magnetization_from_lsda(ngm=ngm, nspin=nspin, rho=rho)

def wfcinit():
    """
    wfcinit()
    
    
    Defined at wfcinit.fpp lines 14-180
    
    
    ----------------------------------------------------------------------------
     ... This routine computes an estimate of the starting wavefunctions
     ... from superposition of atomic wavefunctions and/or random wavefunctions.
     ... It also open needed files or memory buffers
    """
    _qepy.f90wrap_wfcinit()

def init_wfc(ik):
    """
    init_wfc(ik)
    
    
    Defined at wfcinit.fpp lines 184-340
    
    Parameters
    ----------
    ik : int
    
    ----------------------------------------------------------------------------
     ... This routine computes starting wavefunctions for k-point ik
    """
    _qepy.f90wrap_init_wfc(ik=ik)

def read_file():
    """
    read_file()
    
    
    Defined at read_file_new.fpp lines 13-61
    
    
    ----------------------------------------------------------------------------
     Wrapper routine, for backwards compatibility
    """
    _qepy.f90wrap_read_file()

def read_file_new(needwf):
    """
    read_file_new(needwf)
    
    
    Defined at read_file_new.fpp lines 65-123
    
    Parameters
    ----------
    needwf : bool
    
    ----------------------------------------------------------------------------
     Reads xml data file produced by pw.x or cp.x, performs initializations
     related to the contents of the xml file
     If needwf=.t. performs wavefunction-related initialization as well
     Does not read wfcs but returns in "wfc_is_collected" info on the wfc file
    """
    _qepy.f90wrap_read_file_new(needwf=needwf)

def post_xml_init():
    """
    post_xml_init()
    
    
    Defined at read_file_new.fpp lines 126-348
    
    
    ----------------------------------------------------------------------------
     ... Various initializations needed to start a calculation:
     ... pseudopotentials, G vectors, FFT arrays, rho, potential
    """
    _qepy.f90wrap_post_xml_init()

def plugin_arguments():
    """
    plugin_arguments()
    
    
    Defined at plugin_arguments.fpp lines 13-66
    
    
    -----------------------------------------------------------------------------
     check for presence of command-line option "-plugin_name" or "--plugin_name"
     where "plugin_name" has to be set here. If such option is found, variable
     "use_plugin_name" is set and usage of "plugin_name" is thus enabled.
     Currently implemented: "plumed", "pw2casino" (both case-sensitive)
    """
    _qepy.f90wrap_plugin_arguments()

def plugin_arguments_bcast(root, comm):
    """
    plugin_arguments_bcast(root, comm)
    
    
    Defined at plugin_arguments.fpp lines 70-95
    
    Parameters
    ----------
    root : int
    comm : int
    
    ----------------------------------------------------------------------------
     broadcast plugin arguments
    """
    _qepy.f90wrap_plugin_arguments_bcast(root=root, comm=comm)

def input_images_getarg():
    """
    input_images = input_images_getarg()
    
    
    Defined at path_io_tools.fpp lines 11-48
    
    
    Returns
    -------
    input_images : int
    
    -----------------------------------------------------------------------------
     check for command-line option "-input_images N" or "--input_images N",
     return N(0 if not found)
    """
    input_images = _qepy.f90wrap_input_images_getarg()
    return input_images

def close_io_units(myunit):
    """
    close_io_units(myunit)
    
    
    Defined at path_io_tools.fpp lines 51-65
    
    Parameters
    ----------
    myunit : int
    
    -----------------------------------------------------------------------------
    """
    _qepy.f90wrap_close_io_units(myunit=myunit)

def open_io_units(myunit, file_name, lappend):
    """
    open_io_units(myunit, file_name, lappend)
    
    
    Defined at path_io_tools.fpp lines 69-86
    
    Parameters
    ----------
    myunit : int
    file_name : str
    lappend : bool
    
    -----------------------------------------------------------------------------
    """
    _qepy.f90wrap_open_io_units(myunit=myunit, file_name=file_name, lappend=lappend)

def input_from_file():
    """
    input_from_file()
    
    
    Defined at inpfile.fpp lines 13-67
    
    
    """
    _qepy.f90wrap_input_from_file()

def get_file():
    """
    input_file = get_file()
    
    
    Defined at inpfile.fpp lines 71-108
    
    
    Returns
    -------
    input_file : str
    
    """
    input_file = _qepy.f90wrap_get_file()
    return input_file

def alpha2f():
    """
    alpha2f()
    
    
    Defined at alpha2f.fpp lines 378-418
    
    
    ------------------------------------------------------------------------------
     This routine reads lambda*.dat and compute a^2F, phonon DOS, lambda,
     & omega_ln
    """
    _qepy.f90wrap_alpha2f()

def average():
    """
    average()
    
    
    Defined at average.fpp lines 13-373
    
    
    -----------------------------------------------------------------------
          Compute planar and macroscopic averages of a quantity(e.g. charge)
          in real space on a 3D FFT mesh. The quantity is read from a file
          produced by "pp.x", or from multiple files as follows:
              Q(i,j,k) = \sum_n w_n q_n(i,j,k)
          where q_n is the quantity for file n, w_n is a user-supplied weight
          The planar average is defined as
             p(k) = \sum_{i=1}^{N_1} \sum_{j=1}^{N_2} Q(i,j,k) / (N_1 N_2)
          along direction 3, and the like for directions 1 and 2;
          N_1, N_2, N_3 are the three dimensions of the 3D FFT.
          Note that if Q is a charge density whose integral is Z_v:
             Z_v = \int p(z) dV = \sum_k p(k) \Omega/N_3
          where \Omega is the size of the unit cell(or supercell)
          The planar average is then interpolated on the specified number
          of points supplied in input and written to file "avg.dat"
          The macroscopic average is defined as
             m(z) = \int_z^{z+a} p(z) dz
          where a is the size of the window(supplied in input)
          Input variables
          nfile        the number of files contaning the desired quantities
                       All files must refer to the same physical system
     for each file:
          filename     the name of the n-th file
          weight       the weight w_n of the quantity read from n-th file
          .
          .
     end
          npt          the number of points for the final interpolation of
                       the planar and macroscopic averages, as written to file
                       If npt <= N_idir(see below) no interpolation is done,
                       the N_idir FFT points in direction idir are printed.
          idir         1,2 or 3. Planar average is done in the plane orthogonal
                       to direction "idir", as defined for the crystal cell
          awin         the size of the window for macroscopic average(a.u.)
     Format of output file avg.dat:
        x   p(x)   m(x)
     where
        x = coordinate(a.u) along direction idir
            x runs from 0 to the length of primitive vector idir
      p(x)= planar average, as defined above
      m(x)= macroscopic average, as defined above
    """
    _qepy.f90wrap_average()

def do_bands():
    """
    do_bands()
    
    
    Defined at bands.fpp lines 14-646
    
    
    -----------------------------------------------------------------------
     See files INPUT_BANDS.* in Doc/ directory for usage
    """
    _qepy.f90wrap_do_bands()

def benchmark_libxc():
    """
    benchmark_libxc()
    
    
    Defined at benchmark_libxc.fpp lines 13-35
    
    
    --------------------------------------------------------------------------------
     This program compares the output results(energies and potentials) from the libxc
     routines with the ones from q-e xc internal library.
     Available options:
     * LDA ;
     * derivative of LDA(dmxc) ;
     * GGA ;
     * derivative of GGA(dgcxc) ;
     * metaGGA.
    ------------------------------------------------------------------------------------
      To be run on a single processor
    ------------------------------------------------------------------------------------
    """
    _qepy.f90wrap_benchmark_libxc()

def cell2ibrav():
    """
    cell2ibrav()
    
    
    Defined at cell2ibrav.fpp lines 13-59
    
    
    ----------------------------------------------------------------------
    """
    _qepy.f90wrap_cell2ibrav()

def pwcond():
    """
    pwcond()
    
    
    Defined at condmain.fpp lines 19-24
    
    
    """
    _qepy.f90wrap_pwcond()

def do_dos():
    """
    do_dos()
    
    
    Defined at dos.fpp lines 14-239
    
    
    --------------------------------------------------------------------
     Calculates the Density of States(DOS),
     separated into up and down components for LSDA
     See files INPUT_DOS.* in Doc/ directory for usage
     IMPORTANT: since v.5 namelist name is &dos and no longer &inputpp
    """
    _qepy.f90wrap_do_dos()

def dynmat():
    """
    dynmat()
    
    
    Defined at dynmat.fpp lines 13-244
    
    
    --------------------------------------------------------------------
      This program
      - reads a dynamical matrix file produced by the phonon code
      - adds the nonanalytical part(if Z* and epsilon are read from file),
        applies the chosen Acoustic Sum Rule(if q=0)
      - diagonalise the dynamical matrix
      - calculates IR and Raman cross sections(if Z* and Raman tensors
        are read from file, respectively)
      - writes the results to files, both for inspection and for plotting
      Input data(namelist "input")
      fildyn  character input file containing the dynamical matrix
    (default: fildyn='matdyn')
      q(3)      real    calculate LO modes(add nonanalytic terms) along
                        the direction q(cartesian axis, default: q=(0,0,0) )
      amass(nt) real    mass for atom type nt, amu
    (default: amass is read from file fildyn)
      asr   character   indicates the type of Acoustic Sum Rule imposed
                         - 'no': no Acoustic Sum Rules imposed(default)
                         - 'simple':  previous implementation of the asr used
    (3 translational asr imposed by correction of
                         the diagonal elements of the dynamical matrix)
                         - 'crystal': 3 translational asr imposed by optimized
                         correction of the dyn. matrix(projection).
                         - 'one-dim': 3 translational asr + 1 rotational asr
                         imposed by optimized correction of the dyn. mat. (the
                         rotation axis is the direction of periodicity; it
                         will work only if this axis considered is one of
                         the cartesian axis).
                         - 'zero-dim': 3 translational asr + 3 rotational asr
                         imposed by optimized correction of the dyn. mat.
                         Note that in certain cases, not all the rotational asr
                         can be applied(e.g. if there are only 2 atoms in a
                         molecule or if all the atoms are aligned, etc.).
                         In these cases the supplementary asr are cancelled
                         during the orthonormalization procedure(see below).
                         Finally, in all cases except 'no' a simple correction
                         on the effective charges is performed(same as in the
                         previous implementation).
      axis    integer    indicates the rotation axis for a 1D system
    (1=Ox, 2=Oy, 3=Oz ; default =3)
      lperm   logical    .true. to calculate Gamma-point mode contributions to
                         dielectric permittivity tensor
    (default: lperm=.false.)
      lplasma logical    .true. to calculate Gamma-point mode effective plasma
                         frequencies, automatically triggers lperm = .true.
    (default: lplasma=.false.)
      filout character output file containing phonon frequencies and normalized
                        phonon displacements(i.e. eigenvectors divided by the
                        square root of the mass and then normalized; they are
                        not orthogonal)
    (default: filout='dynmat.out')
      fileig character output file containing phonon frequencies and eigenvectors
                        of the dynamical matrix(they are orthogonal)
    (default: fileig=' ')
      filmol  character as above, in a format suitable for 'molden'
    (default: filmol='dynmat.mold')
      filxsf  character as above, in axsf format suitable for xcrysden
    (default: filxsf='dynmat.axsf')
      loto_2d logical set to .true. to activate two-dimensional treatment of LO-TO \
          splitting.
    """
    _qepy.f90wrap_dynmat()

def epa():
    """
    epa()
    
    
    Defined at epa.fpp lines 17-506
    
    
    """
    _qepy.f90wrap_epa()

def epsilon():
    """
    epsilon()
    
    
    Defined at epsilon.fpp lines 126-298
    
    
    ------------------------------
     Compute the complex macroscopic dielectric function,
     at the RPA level, neglecting local field effects.
     Eps is computed both on the real or immaginary axis
     Authors:
         2006 Andrea Benassi, Andrea Ferretti, Carlo Cavazzoni: basic \
             implementation(partly taken from pw2gw.f90)
         2007 Andrea Benassi: intraband contribution, nspin=2
         2016    Tae-Yun Kim, Cheol-Hwan Park:                       bugs fixed
         2016 Tae-Yun Kim, Cheol-Hwan Park, Andrea Ferretti: non-collinear magnetism \
             implemented
                                                                     code significantly restructured
    """
    _qepy.f90wrap_epsilon()

def eps_calc(intersmear, intrasmear, nbndmin, nbndmax, shift, metalcalc, nspin):
    """
    eps_calc(intersmear, intrasmear, nbndmin, nbndmax, shift, metalcalc, nspin)
    
    
    Defined at epsilon.fpp lines 301-499
    
    Parameters
    ----------
    intersmear : float
    intrasmear : float
    nbndmin : int
    nbndmax : int
    shift : float
    metalcalc : bool
    nspin : int
    
    -----------------------------------------------------------------------------
    """
    _qepy.f90wrap_eps_calc(intersmear=intersmear, intrasmear=intrasmear, \
        nbndmin=nbndmin, nbndmax=nbndmax, shift=shift, metalcalc=metalcalc, \
        nspin=nspin)

def jdos_calc(smeartype, intersmear, nbndmin, nbndmax, shift, nspin):
    """
    jdos_calc(smeartype, intersmear, nbndmin, nbndmax, shift, nspin)
    
    
    Defined at epsilon.fpp lines 502-763
    
    Parameters
    ----------
    smeartype : str
    intersmear : float
    nbndmin : int
    nbndmax : int
    shift : float
    nspin : int
    
    --------------------------------------------------------------------------------------
    """
    _qepy.f90wrap_jdos_calc(smeartype=smeartype, intersmear=intersmear, \
        nbndmin=nbndmin, nbndmax=nbndmax, shift=shift, nspin=nspin)

def offdiag_calc(intersmear, intrasmear, nbndmin, nbndmax, shift, metalcalc, \
    nspin):
    """
    offdiag_calc(intersmear, intrasmear, nbndmin, nbndmax, shift, metalcalc, nspin)
    
    
    Defined at epsilon.fpp lines 766-955
    
    Parameters
    ----------
    intersmear : float
    intrasmear : float
    nbndmin : int
    nbndmax : int
    shift : float
    metalcalc : bool
    nspin : int
    
    -----------------------------------------------------------------------------
    """
    _qepy.f90wrap_offdiag_calc(intersmear=intersmear, intrasmear=intrasmear, \
        nbndmin=nbndmin, nbndmax=nbndmax, shift=shift, metalcalc=metalcalc, \
        nspin=nspin)

def dipole_calc(ik, dipole_aux, metalcalc, nbndmin, nbndmax):
    """
    dipole_calc(ik, dipole_aux, metalcalc, nbndmin, nbndmax)
    
    
    Defined at epsilon.fpp lines 958-1053
    
    Parameters
    ----------
    ik : int
    dipole_aux : complex array
    metalcalc : bool
    nbndmin : int
    nbndmax : int
    
    ------------------------------------------------------------------
    """
    _qepy.f90wrap_dipole_calc(ik=ik, dipole_aux=dipole_aux, metalcalc=metalcalc, \
        nbndmin=nbndmin, nbndmax=nbndmax)

def eps_writetofile(namein, desc, nw, wgrid, ncol, var):
    """
    eps_writetofile(namein, desc, nw, wgrid, ncol, var)
    
    
    Defined at epsilon.fpp lines 1056-1085
    
    Parameters
    ----------
    namein : str
    desc : str
    nw : int
    wgrid : float array
    ncol : int
    var : float array
    
    ------------------------------------------------------------------
    """
    _qepy.f90wrap_eps_writetofile(namein=namein, desc=desc, nw=nw, wgrid=wgrid, \
        ncol=ncol, var=var)

def ev():
    """
    ev()
    
    
    Defined at ev.fpp lines 19-416
    
    
    -----------------------------------------------------------------------
    """
    _qepy.f90wrap_ev()

def birch(x, k0, dk0, d2k0):
    """
    birch = birch(x, k0, dk0, d2k0)
    
    
    Defined at ev.fpp lines 418-434
    
    Parameters
    ----------
    x : float
    k0 : float
    dk0 : float
    d2k0 : float
    
    Returns
    -------
    birch : float
    
    """
    birch = _qepy.f90wrap_birch(x=x, k0=k0, dk0=dk0, d2k0=d2k0)
    return birch

def keane(x, k0, dk0, d2k0):
    """
    keane = keane(x, k0, dk0, d2k0)
    
    
    Defined at ev.fpp lines 437-444
    
    Parameters
    ----------
    x : float
    k0 : float
    dk0 : float
    d2k0 : float
    
    Returns
    -------
    keane : float
    
    """
    keane = _qepy.f90wrap_keane(x=x, k0=k0, dk0=dk0, d2k0=d2k0)
    return keane

def write_evdata_xml(npt, fac, v0, etot, efit, istat, par, npar, emin, chisq, \
    filout):
    """
    ierr = write_evdata_xml(npt, fac, v0, etot, efit, istat, par, npar, emin, chisq, \
        filout)
    
    
    Defined at ev.fpp lines 448-550
    
    Parameters
    ----------
    npt : int
    fac : float
    v0 : float array
    etot : float array
    efit : float array
    istat : int
    par : float array
    npar : int
    emin : float
    chisq : float
    filout : str
    
    Returns
    -------
    ierr : int
    
    -----------------------------------------------------------------------
    """
    ierr = _qepy.f90wrap_write_evdata_xml(npt=npt, fac=fac, v0=v0, etot=etot, \
        efit=efit, istat=istat, par=par, npar=npar, emin=emin, chisq=chisq, \
        filout=filout)
    return ierr

def fd():
    """
    fd()
    
    
    Defined at fd.fpp lines 11-476
    
    
    """
    _qepy.f90wrap_fd()

def fd_raman():
    """
    fd_raman()
    
    
    Defined at fd_ef.fpp lines 6-484
    
    
    -----------------------------------------------------------------------
    """
    _qepy.f90wrap_fd_raman()

def fd_ifc():
    """
    fd_ifc()
    
    
    Defined at fd_ifc.fpp lines 11-852
    
    
    """
    _qepy.f90wrap_fd_ifc()

def fermi_proj():
    """
    fermi_proj()
    
    
    Defined at fermi_proj.fpp lines 199-311
    
    
    ----------------------------------------------------------------------------
     Usage :
     $ proj_fermi.x -in {input file}
     Then it generates proj.frmsf(for nspin = 1, 4) or
     proj1.frmsf and proj2.frmsf(for nspin = 2)
     Input file format(projwfc.x + tail):
     &PROJWFC
     prefix = "..."
     outdir = "..."
     ...
     /
     {Number of target WFCs}
     {Index of WFC1} {Index of WFC2} {Index of WFC3} ...
    """
    _qepy.f90wrap_fermi_proj()

def fermi_velocity():
    """
    fermi_velocity()
    
    
    Defined at fermi_velocity.fpp lines 20-155
    
    
    --------------------------------------------------------------------------
    """
    _qepy.f90wrap_fermi_velocity()

def fermisurface():
    """
    fermisurface()
    
    
    Defined at fermisurface.fpp lines 359-382
    
    
    --------------------------------------------------------------------
    """
    _qepy.f90wrap_fermisurface()

def fqha():
    """
    fqha()
    
    
    Defined at fqha.fpp lines 15-90
    
    
    """
    _qepy.f90wrap_fqha()

def gww():
    """
    gww()
    
    
    Defined at gww.fpp lines 14-246
    
    
    """
    _qepy.f90wrap_gww()

def gww_fit():
    """
    gww_fit()
    
    
    Defined at gww_fit.fpp lines 13-159
    
    
    """
    _qepy.f90wrap_gww_fit()

def hp_main():
    """
    hp_main()
    
    
    Defined at hp_main.fpp lines 13-253
    
    
    -----------------------------------------------------------------------
     This is the main driver of the HP code.
    """
    _qepy.f90wrap_hp_main()

def ibrav2cell():
    """
    ibrav2cell()
    
    
    Defined at ibrav2cell.fpp lines 13-81
    
    
    ----------------------------------------------------------------------
    """
    _qepy.f90wrap_ibrav2cell()

def initial_state():
    """
    initial_state()
    
    
    Defined at initial_state.fpp lines 13-89
    
    
    -----------------------------------------------------------------------
      compute initial-state contribution to core level shift
     input: namelist "&inputpp", with variables
       prefix      prefix of input files saved by program pwscf
       outdir      temporary directory where files resides
    """
    _qepy.f90wrap_initial_state()

def special_points():
    """
    special_points()
    
    
    Defined at kpoints.fpp lines 14-263
    
    
    -----======================--------------------------------------------
         calculates special points for any structure,
         the default definition for the mesh is a shift of 1/(2n_i)
         where the length of b_i is equal to 1
    _______________________________________________________________________
    """
    _qepy.f90wrap_special_points()

def elph():
    """
    elph()
    
    
    Defined at lambda.fpp lines 19-176
    
    
    """
    _qepy.f90wrap_elph()

def ld1():
    """
    ld1()
    
    
    Defined at ld1.fpp lines 13-81
    
    
    ---------------------------------------------------------------
         atomic self-consistent local-density program
         atomic rydberg units are used : e^2=2, m=1/2, hbar=1
         psi(r) = rR(r), where R(r) is the radial part of the wfct
         rho(r) = psi(r)^2 => rho(r) = (true charge density)*(4\pi r^2)
                           The same applies to the core charge
    ---------------------------------------------------------------
    """
    _qepy.f90wrap_ld1()

def lr_dav_main():
    """
    lr_dav_main()
    
    
    Defined at lr_dav_main.fpp lines 13-144
    
    
    ---------------------------------------------------------------------
     Xiaochuan Ge, SISSA, 2013
    ---------------------------------------------------------------------
     ... overall driver routine for applying davidson algorithm
     ... to the matrix of equations coming from tddft
    ---------------------------------------------------------------------
    """
    _qepy.f90wrap_lr_dav_main()

def lr_eels_main():
    """
    lr_eels_main()
    
    
    Defined at lr_eels_main.fpp lines 13-266
    
    
    ---------------------------------------------------------------------
     This is the main driver of the turboEELS code for Electron Energy Loss \
         Spectroscopy.
     It applys the Lanczos algorithm to the matrix of equations coming from TDDFPT.
     Iurii Timrov(Ecole Polytechnique, SISSA, and EPFL) 2010-2018
    """
    _qepy.f90wrap_lr_eels_main()

def lr_main():
    """
    lr_main()
    
    
    Defined at lr_main.fpp lines 13-329
    
    
    ---------------------------------------------------------------------
     This is the main driver of the TDDFPT code
     for Absorption Spectroscopy.
     It applys the Lanczos algorithm to the matrix
     of equations coming from TDDFPT.
     Brent Walker, ICTP, 2004
     Dario Rocca, SISSA, 2006
     Osman Baris Malcioglu, SISSA, 2008
     Simone Binnie, SISSA, 2011
     Xiaochuan Ge, SISSA, 2013
     Iurii Timrov, SISSA, 2015
    """
    _qepy.f90wrap_lr_main()

def matdyn():
    """
    matdyn()
    
    
    Defined at matdyn.fpp lines 30-2534
    
    
    -----------------------------------------------------------------------
      this program calculates the phonon frequencies for a list of generic
      q vectors starting from the interatomic force constants generated
      from the dynamical matrices as written by DFPT phonon code through
      the companion program q2r
      matdyn can generate a supercell of the original cell for mass
      approximation calculation. If supercell data are not specified
      in input, the unit cell, lattice vectors, atom types and positions
      are read from the force constant file
      Input cards: namelist &input
         flfrc     file produced by q2r containing force constants(needed)
                   It is the same as in the input of q2r.x(+ the .xml extension
                   if the dynamical matrices produced by ph.x were in xml
                   format). No default value: must be specified.
          asr(character) indicates the type of Acoustic Sum Rule imposed
                   - 'no': no Acoustic Sum Rules imposed(default)
                   - 'simple':  previous implementation of the asr used
    (3 translational asr imposed by correction of
                      the diagonal elements of the force constants matrix)
                   - 'crystal': 3 translational asr imposed by optimized
                      correction of the force constants(projection).
                   - 'one-dim': 3 translational asr + 1 rotational asr
                      imposed by optimized correction of the force constants
    (the rotation axis is the direction of periodicity;
                       it will work only if this axis considered is one of
                       the cartesian axis).
                   - 'zero-dim': 3 translational asr + 3 rotational asr
                      imposed by optimized correction of the force constants
                   Note that in certain cases, not all the rotational asr
                   can be applied(e.g. if there are only 2 atoms in a
                   molecule or if all the atoms are aligned, etc.).
                   In these cases the supplementary asr are cancelled
                   during the orthonormalization procedure(see below).
         dos       if .true. calculate phonon Density of States(DOS)
                   using tetrahedra and a uniform q-point grid(see below)
                   NB: may not work properly in noncubic materials
                   if .false. calculate phonon bands from the list of q-points
                   supplied in input(default)
         nk1,nk2,nk3  uniform q-point grid for DOS calculation(includes q=0)
    (must be specified if dos=.true., ignored otherwise)
         deltaE    energy step, in cm^(-1), for DOS calculation: from min
                   to max phonon energy(default: 1 cm^(-1) if ndos, see
                   below, is not specified)
         ndos      number of energy steps for DOS calculations
    (default: calculated from deltaE if not specified)
         fldos     output file for dos(default: 'matdyn.dos')
                   the dos is in states/cm(-1) plotted vs omega in cm(-1)
                   and is normalised to 3*nat, i.e. the number of phonons
         flfrq     output file for frequencies(default: 'matdyn.freq')
         flvec     output file for normalized phonon displacements
    (default: 'matdyn.modes'). The normalized phonon displacements
                   are the eigenvectors divided by the square root of the mass,
                   then normalized. As such they are not orthogonal.
         fleig     output file for phonon eigenvectors(default: 'matdyn.eig')
                   The phonon eigenvectors are the eigenvectors of the dynamical
                   matrix. They are orthogonal.
         fldyn output file for dynamical matrix(default: ' ' i.e. not written)
         at        supercell lattice vectors - must form a superlattice of the
                   original lattice(default: use original cell)
         l1,l2,l3  supercell lattice vectors are original cell vectors times
                   l1, l2, l3 respectively(default: 1, ignored if at specified)
         ntyp      number of atom types in the supercell(default: ntyp of the
                   original cell)
         amass     masses of atoms in the supercell(a.m.u.), one per atom type
    (default: use masses read from file flfrc)
         readtau   read  atomic positions of the supercell from input
    (used to specify different masses) (default: .false.)
         fltau     write atomic positions of the supercell to file "fltau"
    (default: fltau=' ', do not write)
         la2F      if .true. interpolates also the el-ph coefficients.
         q_in_band_form if .true. the q points are given in band form:
                   Only the first and last point of one or more lines
                   are given. See below. (default: .false.).
         q_in_cryst_coord if .true. input q points are in crystalline
                  coordinates(default: .false.)
         eigen_similarity: use similarity of the displacements to order
                           frequencies(default: .false.)
                    NB: You cannot use this option with the symmetry
                    analysis of the modes.
         fd(logical) if .t. the ifc come from the finite displacement calculation
         na_ifc(logical) add non analitic contributions to the interatomic force
                    constants if finite displacement method is used(as in Wang et al.
                    Phys. Rev. B 85, 224303(2012)) [to be used in conjunction with fd.x]
         nosym      if .true., no symmetry and no time reversal are imposed
         loto_2d set to .true. to activate two-dimensional treatment of LO-TO splitting.
      if(readtau) atom types and positions in the supercell follow:
    (tau(i,na),i=1,3), ityp(na)
      IF(q_in_band_form.and..not.dos) THEN
         nq
     number of q points
    (q(i,n),i=1,3), nptq   nptq is the number of points between this point
                                and the next. These points are automatically
                                generated. the q points are given in Cartesian
                                coordinates, 2pi/a units(a=lattice parameters)
      ELSE, if(.not.dos) :
         nq         number of q-points
    (q(i,n), i=1,3)    nq q-points in cartesian coordinates, 2pi/a units
      If q = 0, the direction qhat(q=>0) for the non-analytic part
      is extracted from the sequence of q-points as follows:
         qhat = q(n) - q(n-1)  or   qhat = q(n) - q(n+1)
      depending on which one is available and nonzero.
      For low-symmetry crystals, specify twice q = 0 in the list
      if you want to have q = 0 results for two different directions
    """
    _qepy.f90wrap_matdyn()

def molecularpdos():
    """
    molecularpdos()
    
    
    Defined at molecularpdos.fpp lines 13-515
    
    
    -----------------------------------------------------------------------
     Takes the projections onto orthogonalized atomic wavefunctions
     as computed by projwfc.x(see outdir/prefix.save/atomic_proj.xml)
     to build an LCAO-like representation of the eigenvalues of a system
     "full" and "part" of it(each should provide its own atomic_proj.xml file).
     Then the eigenvectors of the full system are projected onto the ones of the
     part.
     An explanation of the keywords and the implementation is provided in
     Scientific Reports | 6:24603 | DOI: 10.1038/srep24603(2016) (Supp. Info)
     Typical application: decompose the PDOS of an adsorbed molecule into
     its molecular orbital, as determined by a gas-phase calculation.
     The user has to specify which atomic functions(range beg:end) to use in
     both the full system and the part(the same atomic set should be used).
     MOPDOS(E,ibnd_part) = \sum_k w_k [ \sum_{ibnd_full}
                                        <psi_{ibnd_part,k}|psi_{ibnd_full,k}>
                                        * \delta(E-\epsilon_{ibnd_full,k}) *
                                        <psi_{ibnd_full,k}|psi_{ibnd_part,k}> ]
     where <psi_{ibnd_part,k}|psi_{ibnd_full,k}> are computed by using the LCAO
     representations:
     |psi_{ibnd_full,k}> =
            \sum_iatmwfc projs_full(iatmwfc,ibnd_full,k) |phi_{iatmwfc}>
     |psi_{ibnd_part,k}> =
            \sum_iatmwfc projs_part(iatmwfc,ibnd_part,k) |phi_{iatmwfc}>
     <psi_{ibnd_part,k}|psi_{ibnd_full,k}> =: projs_mo(ibnd_part,ibnd_full,k)
          = \sum_iatmwfc CONJG(projs_part(iatmwfc,ibnd_part,k))
                             * projs_full(iatmwfc,ibnd_full,k)
     If kresolveddos=.true. from input, the summation over k is not performed
     and individual k-resolved contributions are given in output.
    """
    _qepy.f90wrap_molecularpdos()

def neb():
    """
    neb()
    
    
    Defined at neb.fpp lines 13-123
    
    
    ----------------------------------------------------------------------------
     ... Nudged Elastic Band / Strings Method algorithm
    """
    _qepy.f90wrap_neb()

def open_grid():
    """
    open_grid()
    
    
    Defined at open_grid.fpp lines 6-232
    
    
    ------------------------------------------------------------------------
    """
    _qepy.f90wrap_open_grid()

def images_interpolator():
    """
    images_interpolator()
    
    
    Defined at path_interpolation.fpp lines 35-365
    
    
    """
    _qepy.f90wrap_images_interpolator()

def phonon():
    """
    phonon()
    
    
    Defined at phonon.fpp lines 13-112
    
    
    -----------------------------------------------------------------------
     ... This is the main driver of the phonon code.
     ... It reads all the quantities calculated by pwscf, it
     ... checks if some recover file is present and determines
     ... which calculation needs to be done. Finally, it calls do_phonon
     ... that does the loop over the q points.
     ... Presently implemented:
     ... dynamical matrix(q/=0)   NC [4], US [4], PAW [4]
     ... dynamical matrix(q=0)    NC [5], US [5], PAW [4]
     ... dielectric constant       NC [5], US [5], PAW [3]
     ... born effective charges    NC [5], US [5], PAW [3]
     ... polarizability(iu)       NC [2], US [2]
     ... electron-phonon           NC [3], US [3]
     ... electro-optic             NC [1]
     ... raman tensor              NC [1]
     NC = norm conserving pseudopotentials
     US = ultrasoft pseudopotentials
     PAW = projector augmented-wave
     [1] LDA,
     [2] [1] + GGA,
     [3] [2] + LSDA/sGGA,
     [4] [3] + Spin-orbit/nonmagnetic, non-local vdW functionals, DFT-D2
     [5] [4] + Spin-orbit/magnetic(experimental when available)
     Not implemented in ph.x:
     [6] [5] + constraints on the magnetization
     [7] Tkatchenko-Scheffler, DFT-D3
     [8] Hybrid and meta-GGA functionals
     [9] External Electric field
     [10] nonperiodic boundary conditions.
    """
    _qepy.f90wrap_phonon()

def plan_avg():
    """
    plan_avg()
    
    
    Defined at plan_avg.fpp lines 14-283
    
    
    -----------------------------------------------------------------------
     calculate planar averages of each wavefunction
    """
    _qepy.f90wrap_plan_avg()

def plotband():
    """
    plotband()
    
    
    Defined at plotband.fpp lines 12-774
    
    
    """
    _qepy.f90wrap_plotband()

def plotproj():
    """
    plotproj()
    
    
    Defined at plotproj.fpp lines 12-150
    
    
    """
    _qepy.f90wrap_plotproj()

def plotrho():
    """
    plotrho()
    
    
    Defined at plotrho.fpp lines 14-984
    
    
    -----------------------------------------------------------------------
       2D contour plot - logarithmically or linearly spaced levels
                       - Postscript printable output
       if " cplot" is called:
                       - contour lines plus gray levels
                       - negative values are shaded
       if "psplot" is called:
                       - contour lines of various kinds(solid, dashed, etc)
    """
    _qepy.f90wrap_plotrho()

def pmw():
    """
    pmw()
    
    
    Defined at poormanwannier.fpp lines 14-390
    
    
    -----------------------------------------------------------------------
     projects wavefunctions onto atomic wavefunctions,
     input: namelist "&inputpp", with variables
       prefix      prefix of input files saved by program pwscf
       outdir      temporary directory where files resides
    """
    _qepy.f90wrap_pmw()

def pp():
    """
    pp()
    
    
    Defined at postproc.fpp lines 227-264
    
    
    -----------------------------------------------------------------------
        Program for data analysis and plotting. The two basic steps are:
        1) read the output file produced by pw.x, extract and calculate
           the desired quantity(rho, V, ...)
        2) write the desired quantity to file in a suitable format for
           various types of plotting and various plotting programs
        The two steps can be performed independently. Intermediate data
        can be saved to file in step 1 and read from file in step 2.
        DESCRIPTION of the INPUT : see file Doc/INPUT_PP.*
    """
    _qepy.f90wrap_pp()

def do_ppacf():
    """
    do_ppacf()
    
    
    Defined at ppacf.fpp lines 13-1155
    
    
    -----------------------------------------------------------------------
     This routine computes the coupling constant dependency of exchange
     correlation potential \( E_{\text{xc},\lambda}, \lambda \in \[0:1\]
     and the spatial distribution of exchange correlation energy
     density and kinetic correlation energy density according to:
     Y. Jiao, E. Schr\"oder, and P. Hyldgaard, Phys. Rev. B 97, 085115(2018).
     For an illustration of how to use this routine to set hybrid
     mixing parameter, please refer to:
     Y. Jiao, E. Schr\"oder, P. Hyldgaard, J. Chem. Phys. 148, 194115(2018).
    """
    _qepy.f90wrap_do_ppacf()

def do_projwfc():
    """
    do_projwfc()
    
    
    Defined at projwfc.fpp lines 13-243
    
    
    -----------------------------------------------------------------------
     projects wavefunctions onto orthogonalized atomic wavefunctions,
     calculates Lowdin charges, spilling parameter, projected DOS
     or computes the LDOS in a volume given in input as function of energy
     See files INPUT_PROJWFC.* in Doc/ directory for usage
     IMPORTANT: since v.5 namelist name is &projwfc and no longer &inputpp
    """
    _qepy.f90wrap_do_projwfc()

def get_et_from_gww(nbnd, et):
    """
    get_et_from_gww(nbnd, et)
    
    
    Defined at projwfc.fpp lines 245-279
    
    Parameters
    ----------
    nbnd : int
    et : float array
    
    """
    _qepy.f90wrap_get_et_from_gww(nbnd=nbnd, et=et)

def write_lowdin(filproj, nat, lmax_wfc, nspin, charges, charges_lm=None):
    """
    write_lowdin(filproj, nat, lmax_wfc, nspin, charges[, charges_lm])
    
    
    Defined at projwfc.fpp lines 282-391
    
    Parameters
    ----------
    filproj : str
    nat : int
    lmax_wfc : int
    nspin : int
    charges : float array
    charges_lm : float array
    
    """
    _qepy.f90wrap_write_lowdin(filproj=filproj, nat=nat, lmax_wfc=lmax_wfc, \
        nspin=nspin, charges=charges, charges_lm=charges_lm)

def sym_proj_g(rproj0, proj_out):
    """
    sym_proj_g(rproj0, proj_out)
    
    
    Defined at projwfc.fpp lines 395-466
    
    Parameters
    ----------
    rproj0 : float array
    proj_out : float array
    
    -----------------------------------------------------------------------
    """
    _qepy.f90wrap_sym_proj_g(rproj0=rproj0, proj_out=proj_out)

def sym_proj_k(proj0, proj_out):
    """
    sym_proj_k(proj0, proj_out)
    
    
    Defined at projwfc.fpp lines 470-541
    
    Parameters
    ----------
    proj0 : complex array
    proj_out : float array
    
    -----------------------------------------------------------------------
    """
    _qepy.f90wrap_sym_proj_k(proj0=proj0, proj_out=proj_out)

def sym_proj_so(domag, proj0, proj_out):
    """
    sym_proj_so(domag, proj0, proj_out)
    
    
    Defined at projwfc.fpp lines 545-647
    
    Parameters
    ----------
    domag : bool
    proj0 : complex array
    proj_out : float array
    
    -----------------------------------------------------------------------
    """
    _qepy.f90wrap_sym_proj_so(domag=domag, proj0=proj0, proj_out=proj_out)

def sym_proj_nc(proj0, proj_out):
    """
    sym_proj_nc(proj0, proj_out)
    
    
    Defined at projwfc.fpp lines 650-735
    
    Parameters
    ----------
    proj0 : complex array
    proj_out : float array
    
    """
    _qepy.f90wrap_sym_proj_nc(proj0=proj0, proj_out=proj_out)

def write_proj(lmax_wfc, filproj, proj):
    """
    write_proj(lmax_wfc, filproj, proj)
    
    
    Defined at projwfc.fpp lines 738-897
    
    Parameters
    ----------
    lmax_wfc : int
    filproj : str
    proj : float array
    
    -----------------------------------------------------------------------
    """
    _qepy.f90wrap_write_proj(lmax_wfc=lmax_wfc, filproj=filproj, proj=proj)

def force_theorem(ef_0, filproj):
    """
    force_theorem(ef_0, filproj)
    
    
    Defined at projwfc.fpp lines 900-996
    
    Parameters
    ----------
    ef_0 : float
    filproj : str
    
    """
    _qepy.f90wrap_force_theorem(ef_0=ef_0, filproj=filproj)

def projwave_paw(filproj):
    """
    projwave_paw(filproj)
    
    
    Defined at projwfc.fpp lines 1000-1095
    
    Parameters
    ----------
    filproj : str
    
    -----------------------------------------------------------------------
    """
    _qepy.f90wrap_projwave_paw(filproj=filproj)

def compute_mj(j, l, m):
    """
    compute_mj = compute_mj(j, l, m)
    
    
    Defined at projwfc.fpp lines 1099-1113
    
    Parameters
    ----------
    j : float
    l : int
    m : int
    
    Returns
    -------
    compute_mj : float
    
    -----------------------------------------------------------------------
    """
    compute_mj = _qepy.f90wrap_compute_mj(j=j, l=l, m=m)
    return compute_mj

def write_proj_iotk(filename, lbinary, projs, lwrite_ovp, ovps):
    """
    write_proj_iotk(filename, lbinary, projs, lwrite_ovp, ovps)
    
    
    Defined at projwfc.fpp lines 1117-1274
    
    Parameters
    ----------
    filename : str
    lbinary : bool
    projs : complex array
    lwrite_ovp : bool
    ovps : complex array
    
    -----------------------------------------------------------------------
    """
    _qepy.f90wrap_write_proj_iotk(filename=filename, lbinary=lbinary, projs=projs, \
        lwrite_ovp=lwrite_ovp, ovps=ovps)

def write_proj_file(filproj, proj):
    """
    write_proj_file(filproj, proj)
    
    
    Defined at projwfc.fpp lines 1278-1348
    
    Parameters
    ----------
    filproj : str
    proj : float array
    
    -----------------------------------------------------------------------
    """
    _qepy.f90wrap_write_proj_file(filproj=filproj, proj=proj)

def projwave(filproj, lsym, lwrite_ovp, lbinary):
    """
    projwave(filproj, lsym, lwrite_ovp, lbinary)
    
    
    Defined at projwfc.fpp lines 1354-1941
    
    Parameters
    ----------
    filproj : str
    lsym : bool
    lwrite_ovp : bool
    lbinary : bool
    
    -----------------------------------------------------------------------
    """
    _qepy.f90wrap_projwave(filproj=filproj, lsym=lsym, lwrite_ovp=lwrite_ovp, \
        lbinary=lbinary)

def pw2bgw():
    """
    pw2bgw()
    
    
    Defined at pw2bgw.fpp lines 100-2516
    
    
    """
    _qepy.f90wrap_pw2bgw()

def pw2critic():
    """
    pw2critic()
    
    
    Defined at pw2critic.fpp lines 37-148
    
    
    """
    _qepy.f90wrap_pw2critic()

def pw2gw():
    """
    pw2gw()
    
    
    Defined at pw2gw.fpp lines 26-1144
    
    
    -----------------------------------------------------------------------
     This subroutine writes files containing plane wave coefficients
     and other stuff needed by GW codes
    """
    _qepy.f90wrap_pw2gw()

def pw2wannier90():
    """
    pw2wannier90()
    
    
    Defined at pw2wannier90.fpp lines 96-4828
    
    
    ------------------------------------------------------------------------
    """
    _qepy.f90wrap_pw2wannier90()

def gwl_punch():
    """
    gwl_punch()
    
    
    Defined at pw4gww.fpp lines 28-689
    
    
    -----------------------------------------------------------------------
     read in PWSCF data in XML format using IOTK lib
     then prepare matrices for GWL calculation
     input:  namelist "&inputpp", with variables
       prefix       prefix of input files saved by program pwscf
       outdir       temporary directory where files resides
       pp_file      output file. If it is omitted, a directory
                    "prefix.export/" is created in outdir and
                    some output files are put there. Anyway all the data
                    are accessible through the "prefix.export/index.xml" file which
                    contains implicit pointers to all the other files in the
                    export directory. If reading is done by the IOTK library
                    all data appear to be in index.xml even if physically it
                    is not.
       uspp_spsi    using US PP if set .TRUE. writes S | psi >
                    and | psi > separately in the output file
       single_file  one-file output is produced
       ascii        ....
       pseudo_dir   pseudopotential directory
       psfile(:)    name of the pp file for each species
    """
    _qepy.f90wrap_gwl_punch()

def pwscf():
    """
    pwscf()
    
    
    Defined at pwscf.fpp lines 13-124
    
    
    """
    _qepy.f90wrap_pwscf()

def q2qstar():
    """
    q2qstar()
    
    
    Defined at q2qstar.fpp lines 24-242
    
    
    ----------------------------------------------------------------------------
    """
    _qepy.f90wrap_q2qstar()

def q2r():
    """
    q2r()
    
    
    Defined at q2r.fpp lines 13-116
    
    
    ----------------------------------------------------------------------------
      q2r.x:
         reads force constant matrices C(q) produced by the phonon code
         for a grid of q-points, calculates the corresponding set of
         interatomic force constants(IFC), C(R)
      Input data: Namelist "input"
         fildyn     :  input file name(character, must be specified)
                       "fildyn"0 contains information on the q-point grid
                       "fildyn"1-N contain force constants C_n = C(q_n)
                       for n=1,...N, where N is the number of q-points
                       in the irreducible brillouin zone
                       Normally this should be the same as specified
                       on input to the phonon code
                       In the non collinear/spin-orbit case the files
                       produced by ph.x are in .xml format. In this case
                       fildyn is the same as in the phonon code + the .xml
                       extension.
         flfrc      :  output file containing the IFC in real space
    (character, must be specified)
         zasr       :  Indicates type of Acoustic Sum Rules used for the Born
                       effective charges(character):
                       - 'no': no Acoustic Sum Rules imposed(default)
                       - 'simple':  previous implementation of the asr used
    (3 translational asr imposed by correction of
                         the diagonal elements of the force-constants matrix)
                       - 'crystal': 3 translational asr imposed by optimized
                          correction of the IFC(projection).
                       - 'one-dim': 3 translational asr + 1 rotational asr
                         imposed by optimized correction of the IFC(the
                         rotation axis is the direction of periodicity; it
                         will work only if this axis considered is one of
                         the cartesian axis).
                       - 'zero-dim': 3 translational asr + 3 rotational asr
                         imposed by optimized correction of the IFC.
                       Note that in certain cases, not all the rotational asr
                       can be applied(e.g. if there are only 2 atoms in a
                       molecule or if all the atoms are aligned, etc.).
                       In these cases the supplementary asr are cancelled
                       during the orthonormalization procedure(see below).
         loto_2d : set to .true. to activate two-dimensional treatment of LO-TO \
             splitting.
      If a file "fildyn"0 is not found, the code will ignore variable "fildyn"
      and will try to read from the following cards the missing information
      on the q-point grid and file names:
         nr1,nr2,nr3:  dimensions of the FFT grid formed by the q-point grid
         nfile      :  number of files containing C(q_n), n=1,nfile
      followed by nfile cards:
         filin      :  name of file containing C(q_n)
      The name and order of files is not important as long as q=0 is the first
    """
    _qepy.f90wrap_q2r()

def q2trans():
    """
    q2trans()
    
    
    Defined at q2trans.fpp lines 13-1745
    
    
    ----------------------------------------------------------------------------
      q2r.x:
         reads force constant matrices C(q) produced by the phonon code
         for a grid of q-points, calculates the corresponding set of
         interatomic force constants(IFC), C(R)
      Input data: Namelist "input"
         fildyn     :  input file name(character, must be specified)
                       "fildyn"0 contains information on the q-point grid
                       "fildyn"1-N contain force constants C_n = C(q_n)
                       for n=1,...N, where N is the number of q-points
                       in the irreducible brillouin zone
                       Normally this should be the same as specified
                       on input to the phonon code
                       In the non collinear/spin-orbit case the files
                       produced by ph.x are in .xml format. In this case
                       fildyn is the same as in the phonon code + the .xml
                       extension.
         flfrc      :  output file containing the IFC in real space
    (character, must be specified)
         zasr       :  Indicates type of Acoustic Sum Rules used for the Born
                       effective charges(character):
                       - 'no': no Acoustic Sum Rules imposed(default)
                       - 'simple':  previous implementation of the asr used
    (3 translational asr imposed by correction of
                         the diagonal elements of the force-constants matrix)
                       - 'crystal': 3 translational asr imposed by optimized
                          correction of the IFC(projection).
                       - 'one-dim': 3 translational asr + 1 rotational asr
                         imposed by optimized correction of the IFC(the
                         rotation axis is the direction of periodicity; it
                         will work only if this axis considered is one of
                         the cartesian axis).
                       - 'zero-dim': 3 translational asr + 3 rotational asr
                         imposed by optimized correction of the IFC.
                       Note that in certain cases, not all the rotational asr
                       can be applied(e.g. if there are only 2 atoms in a
                       molecule or if all the atoms are aligned, etc.).
                       In these cases the supplementary asr are cancelled
                       during the orthonormalization procedure(see below).
      If a file "fildyn"0 is not found, the code will ignore variable "fildyn"
      and will try to read from the following cards the missing information
      on the q-point grid and file names:
         nr1,nr2,nr3:  dimensions of the FFT grid formed by the q-point grid
         nfile      :  number of files containing C(q_n), n=1,nfile
      followed by nfile cards:
         filin      :  name of file containing C(q_n)
      The name and order of files is not important as long as q=0 is the first
    """
    _qepy.f90wrap_q2trans()

def q2trans_fd():
    """
    q2trans_fd()
    
    
    Defined at q2trans_fd.fpp lines 13-490
    
    
    ----------------------------------------------------------------------------
         reads force constant matrices C(q) produced by the cwFD phonon code
         for a grid of q-points, calculates the corresponding set of
         interatomic force constants(IFC), C(R)
      Input data: Namelist "input"
         fildyn     :  input file name(character, must be specified)
                       "fildyn"0 contains information on the q-point grid
                       "fildyn"1-N contain force constants C_n = C(q_n)
                       for n=1,...N, where N is the number of q-points
                       in the irreducible brillouin zone
                       Normally this should be the same as specified
                       on input to the phonon code
                       In the non collinear/spin-orbit case the files
                       produced by ph.x are in .xml format. In this case
                       fildyn is the same as in the phonon code + the .xml
                       extension.
         flfrc      :  output file containing the IFC in real space
    (character, must be specified)
         zasr       :  Indicates type of Acoustic Sum Rules used for the Born
                       effective charges(character):
                       - 'no': no Acoustic Sum Rules imposed(default)
                       - 'simple':  previous implementation of the asr used
    (3 translational asr imposed by correction of
                         the diagonal elements of the force-constants matrix)
                       - 'crystal': 3 translational asr imposed by optimized
                          correction of the IFC(projection).
                       - 'one-dim': 3 translational asr + 1 rotational asr
                         imposed by optimized correction of the IFC(the
                         rotation axis is the direction of periodicity; it
                         will work only if this axis considered is one of
                         the cartesian axis).
                       - 'zero-dim': 3 translational asr + 3 rotational asr
                         imposed by optimized correction of the IFC.
                       Note that in certain cases, not all the rotational asr
                       can be applied(e.g. if there are only 2 atoms in a
                       molecule or if all the atoms are aligned, etc.).
                       In these cases the supplementary asr are cancelled
                       during the orthonormalization procedure(see below).
      If a file "fildyn"0 is not found, the code will ignore variable "fildyn"
      and will try to read from the following cards the missing information
      on the q-point grid and file names:
         nr1,nr2,nr3:  dimensions of the FFT grid formed by the q-point grid
         nfile      :  number of files containing C(q_n), n=1,nfile
      followed by nfile cards:
         filin      :  name of file containing C(q_n)
      The name and order of files is not important as long as q=0 is the first
    """
    _qepy.f90wrap_q2trans_fd()

def simple():
    """
    simple()
    
    
    Defined at simple.fpp lines 6-147
    
    
    -----------------------------------------------------------------------
     input:  namelist "&inputsimple", with variables
       prefix       prefix of input files saved by program pwscf
       outdir       temporary directory where files resides
    """
    _qepy.f90wrap_simple()

def simple_bse():
    """
    simple_bse()
    
    
    Defined at simple_bse.fpp lines 5-21
    
    
    """
    _qepy.f90wrap_simple_bse()

def simple_ip():
    """
    simple_ip()
    
    
    Defined at simple_ip.fpp lines 5-59
    
    
    """
    _qepy.f90wrap_simple_ip()

def sumpdos():
    """
    sumpdos()
    
    
    Defined at sumpdos.fpp lines 13-305
    
    
    """
    _qepy.f90wrap_sumpdos()

def lr_calculate_spectrum():
    """
    lr_calculate_spectrum()
    
    
    Defined at tddfpt_calculate_spectrum.fpp lines 13-1429
    
    
    ---------------------------------------------------------------------
     Calculates the spectrum by solving tridiagonal problem for each value
     of the frequency omega
     Modified by Osman Baris Malcioglu(2008)
     Modified by Xiaochuan Ge(2013)
     Modified by Iurii Timrov(2015)
    """
    _qepy.f90wrap_lr_calculate_spectrum()

def wannier_ham():
    """
    wannier_ham()
    
    
    Defined at wannier_ham.fpp lines 12-308
    
    
    -----------------------------------------------------------------------
     This program generates Hamiltonian matrix on Wannier-functions basis
    """
    _qepy.f90wrap_wannier_ham()

def wannier_plot():
    """
    wannier_plot()
    
    
    Defined at wannier_plot.fpp lines 12-227
    
    
    -----------------------------------------------------------------------
     This program plots charge density of selected wannier function in
     IBM Data Explorer format
    """
    _qepy.f90wrap_wannier_plot()

def wfck2r():
    """
    wfck2r()
    
    
    Defined at wfck2r.fpp lines 39-211
    
    
    -----------------------------------------------------------------------
    """
    _qepy.f90wrap_wfck2r()

# import atexit

# def pwscf_finalise():
#     qepy_pwscf_finalise()


# atexit.register(pwscf_finalise)

import pkgutil
import operator
def qepy_clean_saved():
    mods = [name for _, name, _ in pkgutil.iter_modules(qepy.__path__)]
    for mod in mods :
        if hasattr(qepy, mod):
            for item in ['_arrays', '_objs'] :
                if hasattr(operator.attrgetter(mod)(qepy), item):
                    attr = mod + '.' + item
                    operator.attrgetter(attr)(qepy).clear()


qepy_clean_saved()
__author__ = "Pavanello Research Group"
__contact__ = "m.pavanello@rutgers.edu"
__version__ = "6.5.0"
__license__ = "GPL"
__date__ = "2023-09-20"

try:
    from importlib.metadata import version # python >= 3.8
except Exception :
    try:
        from importlib_metadata import version
    except Exception :
        pass

try:
    __version__ = version("qepy")
except Exception :
    pass

from qepy.driver import Driver
