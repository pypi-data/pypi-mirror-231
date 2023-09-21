#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import h5py
import shutil
import pytest
import numpy as np

# Current, parent and file paths
CWD = os.getcwd()
CF  = os.path.realpath(__file__)
CFD = os.path.dirname(CF)
sys.path.append(os.path.join(CFD,'../'))

# Import library specific modules
from pyspod.pod.standard import Standard as pod_standard
import pyspod.pod.utils      as utils_pod
import pyspod.utils.io       as utils_io
import pyspod.utils.parallel as utils_par
import pyspod.utils.errors   as utils_errors
import pyspod.utils.postproc as post


@pytest.mark.mpi(minsize=2, maxsize=3)
def test_standard_class_compute():
    ## -------------------------------------------------------------------------
    data_file = os.path.join(CFD,'./data', 'fluidmechanics_data.mat')
    data_dict = utils_io.read_data(data_file=data_file)
    data = data_dict['p'].T
    dt = data_dict['dt'][0,0]
    t = dt * np.arange(0,data.shape[0]).T
    nt = t.shape[0]
    params = {
        # -- required parameters
        'time_step'   : dt,
        'n_space_dims': 2,
        'n_variables' : 1,
        # -- optional parameters
        'normalize_weights': False,
        'n_modes_save'     : 8,
        'dtype'            : 'double',
        'savedir'          : os.path.join(CFD, 'results')
    }
    ## -------------------------------------------------------------------------
    try:
        from mpi4py import MPI
        comm = MPI.COMM_WORLD
    except:
        comm = None
    ## fit and transform pod
    pod_class = pod_standard(params=params, comm=comm)
    pod = pod_class.fit(data_list=data)
    results_dir = pod._savedir_sim
    file_coeffs, coeffs_dir = pod.compute_coeffs_op(
        data=data, results_dir=results_dir)
    file_dynamics, coeffs_dir = pod.compute_reconstruction(
        coeffs_dir=coeffs_dir, time_idx='all')

    ## assert test
    savedir = pod._savedir
    assert(pod.dim         ==4)
    assert(pod.shape       ==(1, 20, 88, 1))
    assert(pod.nt          ==1000)
    assert(pod.nx          ==1760)
    assert(pod.nv          ==1)
    assert(pod.xdim        ==2)
    assert(pod.xshape      ==(20, 88))
    assert(pod.dt          ==0.2)
    assert(pod.n_modes_save==8)
    modes = np.load(pod._file_modes)
    coeffs = np.load(file_coeffs)
    recons = np.load(file_dynamics)
    recons_cl = np.load(file_dynamics)
    # print(coeffs.shape)
    # print(recons.shape)
    tol1 = 1e-6; tol2 = 1e-10
    if comm.rank == 0:
        ## fit
        # print(np.real(pod.eigs[0]))
        # print(pod.weights[0])
        # print(np.abs(modes[0,1,0,0]))
        # print(np.abs(modes[10,3,0,2]))
        # print(np.abs(modes[14,15,0,1]))
        # print(np.min(np.abs(modes)))
        # print(np.max(np.abs(modes)))
        assert(modes.shape==(20, 88, 1, 8))
        assert((np.real(pod.eigs[0])    <5.507017010287017  +tol1) and \
               (np.real(pod.eigs[0])    >5.507017010287017  -tol1))
        assert((pod.weights[0,0]        <1.                 +tol1) and \
               (pod.weights[0,0]        >1.                 -tol1))
        assert((np.abs(modes[0,1,0,0])  <0.00083357978228883+tol2) and \
               (np.abs(modes[0,1,0,0])  >0.00083357978228883-tol2))
        assert((np.abs(modes[10,3,0,2]) <3.9895843115101e-05+tol2) and \
               (np.abs(modes[10,3,0,2]) >3.9895843115101e-05-tol2))
        assert((np.abs(modes[14,15,0,1])<5.6967220942460e-05+tol2) and \
               (np.abs(modes[14,15,0,1])>5.6967220942460e-05-tol2))
        assert((np.min(np.abs(modes))   <3.7644953502612e-08+tol2) and \
               (np.min(np.abs(modes))   >3.7644953502612e-08-tol2))
        assert((np.max(np.abs(modes))   <0.13122305680422694+tol2) and \
               (np.max(np.abs(modes))   >0.13122305680422694-tol2))
        ## transform
        # print(np.real(np.max(coeffs)))
        # print(np.real(np.max(recons)))
        assert(coeffs.shape==(8, 1000))
        assert(recons.shape==(1000, 20, 88, 1))
        assert((np.real(np.max(coeffs))<0.244272570390476+tol2) and \
               (np.real(np.max(coeffs))>0.244272570390476-tol2))
        assert((np.real(np.max(recons))<4.495997223290585+tol2) and \
               (np.real(np.max(recons))>4.495997223290585-tol2))
        assert((np.real(np.max(recons_cl))<4.495997223290585+tol2) and \
               (np.real(np.max(recons_cl))>4.495997223290585-tol2))
        x = data[...,None]
        l1 = utils_errors.compute_l_errors(recons, x, norm_type='l1')
        l2 = utils_errors.compute_l_errors(recons, x, norm_type='l2')
        li = utils_errors.compute_l_errors(recons, x, norm_type='linf')
        l1_r = utils_errors.compute_l_errors(recons, x, norm_type='l1_rel')
        l2_r = utils_errors.compute_l_errors(recons, x, norm_type='l2_rel')
        li_r = utils_errors.compute_l_errors(recons, x, norm_type='linf_rel')
        ## errors
        # print(f'{l1 = :}')
        # print(f'{l2 = :}')
        # print(f'{li = :}')
        # print(f'{l1_r = :}')
        # print(f'{l2_r = :}')
        # print(f'{li_r = :}')
        assert((l1  <0.002285731618209+tol2) and (l1  >0.002285731618209-tol2))
        assert((l2  <2.85867239211e-06+tol2) and (l2  >2.85867239211e-06-tol2))
        assert((li  <0.095300914161469+tol2) and (li  >0.095300914161469-tol2))
        assert((l1_r<0.000512977176726+tol2) and (l1_r>0.000512977176726-tol2))
        assert((l2_r<6.41990505721e-07+tol2) and (l2_r>6.41990505721e-07-tol2))
        assert((li_r<0.021960611302988+tol2) and (li_r>0.021960611302988-tol2))
        ## clean up results
        try:
            shutil.rmtree(os.path.join(CFD,'results'))
        except OSError as e:
            pass

@pytest.mark.mpi(minsize=2, maxsize=3)
def test_standard_utils_compute():
    ## -------------------------------------------------------------------------
    data_file = os.path.join(CFD,'./data', 'fluidmechanics_data.mat')
    data_dict = utils_io.read_data(data_file=data_file)
    data = data_dict['p'].T
    dt = data_dict['dt'][0,0]
    t = dt * np.arange(0,data.shape[0]).T
    nt = t.shape[0]
    params = {
        # -- required parameters
        'time_step'   : dt,
        'n_space_dims': 2,
        'n_variables' : 1,
        # -- optional parameters
        'normalize_weights': False,
        'n_modes_save'     : 8,
        'dtype'            : 'double',
        'savedir'          : os.path.join(CFD, 'results')
    }
    ## -------------------------------------------------------------------------
    try:
        from mpi4py import MPI
        comm = MPI.COMM_WORLD
    except:
        comm = None
    ## fit and transform pod
    comm = MPI.COMM_WORLD
    pod_class = pod_standard(params=params, comm=comm)
    pod = pod_class.fit(data_list=data)
    results_dir = pod._savedir_sim
    file_coeffs, coeffs_dir = utils_pod.compute_coeffs_op(
        data=data, results_dir=results_dir, comm=comm)
    file_dynamics, coeffs_dir = utils_pod.compute_reconstruction(
        coeffs_dir=coeffs_dir, time_idx='all', comm=comm)

    ## assert test
    savedir = pod._savedir
    assert(pod.dim         ==4)
    assert(pod.shape       ==(1, 20, 88, 1))
    assert(pod.nt          ==1000)
    assert(pod.nx          ==1760)
    assert(pod.nv          ==1)
    assert(pod.xdim        ==2)
    assert(pod.xshape      ==(20, 88))
    assert(pod.dt          ==0.2)
    assert(pod.n_modes_save==8)
    modes = np.load(pod._file_modes)
    coeffs = np.load(file_coeffs)
    recons = np.load(file_dynamics)
    # print(coeffs.shape)
    # print(recons.shape)
    tol1 = 1e-6; tol2 = 1e-10
    if comm.rank == 0:
        ## fit
        # print(np.real(pod.eigs[0]))
        # print(pod.weights[0])
        # print(np.abs(modes[0,1,0,0]))
        # print(np.abs(modes[10,3,0,2]))
        # print(np.abs(modes[14,15,0,1]))
        # print(np.min(np.abs(modes)))
        # print(np.max(np.abs(modes)))
        assert(modes.shape==(20, 88, 1, 8))
        assert((np.real(pod.eigs[0])    <5.507017010287017  +tol1) and \
               (np.real(pod.eigs[0])    >5.507017010287017  -tol1))
        assert((pod.weights[0,0]        <1.                 +tol1) and \
               (pod.weights[0,0]        >1.                 -tol1))
        assert((np.abs(modes[0,1,0,0])  <0.00083357978228883+tol2) and \
               (np.abs(modes[0,1,0,0])  >0.00083357978228883-tol2))
        assert((np.abs(modes[10,3,0,2]) <3.9895843115101e-05+tol2) and \
               (np.abs(modes[10,3,0,2]) >3.9895843115101e-05-tol2))
        assert((np.abs(modes[14,15,0,1])<5.6967220942460e-05+tol2) and \
               (np.abs(modes[14,15,0,1])>5.6967220942460e-05-tol2))
        assert((np.min(np.abs(modes))   <3.7644953502612e-08+tol2) and \
               (np.min(np.abs(modes))   >3.7644953502612e-08-tol2))
        assert((np.max(np.abs(modes))   <0.13122305680422694+tol2) and \
               (np.max(np.abs(modes))   >0.13122305680422694-tol2))
        ## transform
        # print(np.real(np.max(coeffs)))
        # print(np.real(np.max(recons)))
        assert(coeffs.shape==(8, 1000))
        assert(recons.shape==(1000, 20, 88, 1))
        assert((np.real(np.max(coeffs))<0.244272570390476+tol2) and \
               (np.real(np.max(coeffs))>0.244272570390476-tol2))
        assert((np.real(np.max(recons))<4.495997223290585+tol2) and \
               (np.real(np.max(recons))>4.495997223290585-tol2))
        x = data[...,None]
        l1 = utils_errors.compute_l_errors(recons, x, norm_type='l1')
        l2 = utils_errors.compute_l_errors(recons, x, norm_type='l2')
        li = utils_errors.compute_l_errors(recons, x, norm_type='linf')
        l1_r = utils_errors.compute_l_errors(recons, x, norm_type='l1_rel')
        l2_r = utils_errors.compute_l_errors(recons, x, norm_type='l2_rel')
        li_r = utils_errors.compute_l_errors(recons, x, norm_type='linf_rel')
        ## errors
        # print(f'{l1 = :}')
        # print(f'{l2 = :}')
        # print(f'{li = :}')
        # print(f'{l1_r = :}')
        # print(f'{l2_r = :}')
        # print(f'{li_r = :}')
        assert((l1  <0.002285731618209+tol2) and (l1  >0.002285731618209-tol2))
        assert((l2  <2.85867239211e-06+tol2) and (l2  >2.85867239211e-06-tol2))
        assert((li  <0.095300914161469+tol2) and (li  >0.095300914161469-tol2))
        assert((l1_r<0.000512977176726+tol2) and (l1_r>0.000512977176726-tol2))
        assert((l2_r<6.41990505721e-07+tol2) and (l2_r>6.41990505721e-07-tol2))
        assert((li_r<0.021960611302988+tol2) and (li_r>0.021960611302988-tol2))
        ## clean up results
        try:
            shutil.rmtree(os.path.join(CFD,'results'))
        except OSError as e:
            pass

@pytest.mark.mpi(minsize=2, maxsize=3)
def test_standard_convergence():
    ## -------------------------------------------------------------------------
    data_file = os.path.join(CFD,'./data', 'fluidmechanics_data.mat')
    data_dict = utils_io.read_data(data_file=data_file)
    data = data_dict['p'].T
    dt = data_dict['dt'][0,0]
    t = dt * np.arange(0,data.shape[0]).T
    nt = t.shape[0]
    params = {
        # -- required parameters
        'time_step'   : dt,
        'n_space_dims': 2,
        'n_variables' : 1,
        # -- optional parameters
        'normalize_weights': False,
        'n_modes_save'     : 300,
        'dtype'            : 'double',
        'savedir'          : os.path.join(CFD, 'results')
    }
    ## -------------------------------------------------------------------------
    try:
        from mpi4py import MPI
        comm = MPI.COMM_WORLD
    except:
        comm = None
    ## fit and transform pod
    pod_class = pod_standard(params=params, comm=comm)
    pod = pod_class.fit(data_list=data)
    results_dir = pod._savedir_sim
    file_coeffs, coeffs_dir = utils_pod.compute_coeffs_op(
        data=data, results_dir=results_dir, comm=comm)
    file_dynamics, coeffs_dir = utils_pod.compute_reconstruction(
        coeffs_dir=coeffs_dir, time_idx='all', comm=comm)

    ## assert test
    savedir = pod._savedir
    modes = np.load(pod._file_modes)
    coeffs = np.load(file_coeffs)
    recons = np.load(file_dynamics)
    tol1 = 1e-6; tol2 = 1e-10
    if comm.rank == 0:
        x = pod.get_data(data)
        l1 = utils_errors.compute_l_errors(recons, x, norm_type='l1')
        l2 = utils_errors.compute_l_errors(recons, x, norm_type='l2')
        li = utils_errors.compute_l_errors(recons, x, norm_type='linf')
        l1_r = utils_errors.compute_l_errors(recons, x, norm_type='l1_rel')
        l2_r = utils_errors.compute_l_errors(recons, x, norm_type='l2_rel')
        li_r = utils_errors.compute_l_errors(recons, x, norm_type='linf_rel')
        ## errors
        # print(f'{l1 = :}')
        # print(f'{l2 = :}')
        # print(f'{li = :}')
        # print(f'{l1_r = :}')
        # print(f'{l2_r = :}')
        # print(f'{li_r = :}')
        post.generate_2d_subplot(
            var1=x     [10,...,0], title1='data1',
            var2=recons[10,...,0], title2='data2',
            N_round=6, path=params['savedir'],
            filename='rec.png')
        ## clean up results
        try:
            shutil.rmtree(os.path.join(CFD,'results'))
        except OSError as e:
            pass



if __name__ == "__main__":
    test_standard_class_compute()
    test_standard_utils_compute()
    test_standard_convergence()
