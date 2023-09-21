#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import h5py
import pytest
import shutil
import numpy as np

# Current, parent and file paths
CWD = os.getcwd()
CF  = os.path.realpath(__file__)
CFD = os.path.dirname(CF)
sys.path.append(os.path.join(CFD,'../'))

# Import library specific modules
from pyspod.spod.standard  import Standard  as spod_standard
from pyspod.spod.streaming import Streaming as spod_streaming
import pyspod.spod.utils     as utils_spod
import pyspod.utils.weights  as utils_weights
import pyspod.utils.errors   as utils_errors
import pyspod.utils.io       as utils_io
import pyspod.utils.postproc as post


@pytest.mark.mpi(minsize=2, maxsize=3)
def test_standard_fullspectrum():
    ## -------------------------------------------------------------------
    try:
        from mpi4py import MPI
        comm = MPI.COMM_WORLD
    except:
        comm = None
    data_file = os.path.join(CFD,'./data', 'fluidmechanics_data.mat')
    data_dict = utils_io.read_data(data_file=data_file)
    data = data_dict['p'].T
    dt = data_dict['dt'][0,0]
    nt = data.shape[0]
    config_file = os.path.join(CFD, 'data', 'input_spod.yaml')
    params = utils_io.read_config(config_file)
    params['time_step'] = dt
    params['fullspectrum'] = True
    ## -------------------------------------------------------------------
    spod_class = spod_standard(params=params, comm=comm)
    spod = spod_class.fit(data_list=data)
    T_ = 12.5;     tol = 1e-10
    f_, f_idx = spod.find_nearest_freq(freq_req=1/T_, freq=spod.freq)
    if comm.rank == 0:
        modes_at_freq = spod.get_modes_at_freq(freq_idx=f_idx)
        print(np.abs(modes_at_freq[0,1,0,0]))
        assert((np.abs(modes_at_freq[0,1,0,0])  <0.00046343628114412+tol) and \
               (np.abs(modes_at_freq[0,1,0,0])  >0.00046343628114412-tol))
        assert((np.abs(modes_at_freq[10,3,0,2]) <0.00015920889387988+tol) and \
               (np.abs(modes_at_freq[10,3,0,2]) >0.00015920889387988-tol))
        assert((np.abs(modes_at_freq[14,15,0,1])<0.00022129956393462+tol) and \
               (np.abs(modes_at_freq[14,15,0,1])>0.00022129956393462-tol))
        assert((np.min(np.abs(modes_at_freq))   <1.1110799348607e-05+tol) and \
               (np.min(np.abs(modes_at_freq))   >1.1110799348607e-05-tol))
        assert((np.max(np.abs(modes_at_freq))   <0.10797565399041009+tol) and \
               (np.max(np.abs(modes_at_freq))   >0.10797565399041009-tol))
        try:
            shutil.rmtree(os.path.join(CWD, params['savedir']))
        except OSError as e:
            pass

@pytest.mark.mpi(minsize=2, maxsize=3)
def test_standard_reuse_blocks():
    ## -------------------------------------------------------------------
    try:
        from mpi4py import MPI
        comm = MPI.COMM_WORLD
    except:
        comm = None
    data_file = os.path.join(CFD,'./data', 'fluidmechanics_data.mat')
    data_dict = utils_io.read_data(data_file=data_file)
    data = data_dict['p'].T
    dt = data_dict['dt'][0,0]
    nt = data.shape[0]
    config_file = os.path.join(CFD, 'data', 'input_spod.yaml')
    params = utils_io.read_config(config_file)
    params['time_step'] = dt
    params['savefft'] = True
    params['reuse_blocks'] = False
    params['fullspectrum'] = True
    ## -------------------------------------------------------------------
    spod_class = spod_standard(params=params, comm=comm)
    spod = spod_class.fit(data_list=data)
    T_ = 12.5;     tol = 1e-10
    f_, f_idx = spod.find_nearest_freq(freq_req=1/T_, freq=spod.freq)
    if comm.rank == 0:
        modes_at_freq = spod.get_modes_at_freq(freq_idx=f_idx)
        assert((np.abs(modes_at_freq[0,1,0,0])  <0.00046343628114412+tol) and \
               (np.abs(modes_at_freq[0,1,0,0])  >0.00046343628114412-tol))
        assert((np.abs(modes_at_freq[10,3,0,2]) <0.00015920889387988+tol) and \
               (np.abs(modes_at_freq[10,3,0,2]) >0.00015920889387988-tol))
        assert((np.abs(modes_at_freq[14,15,0,1])<0.00022129956393462+tol) and \
               (np.abs(modes_at_freq[14,15,0,1])>0.00022129956393462-tol))
        assert((np.min(np.abs(modes_at_freq))   <1.1110799348607e-05+tol) and \
               (np.min(np.abs(modes_at_freq))   >1.1110799348607e-05-tol))
        assert((np.max(np.abs(modes_at_freq))   <0.10797565399041009+tol) and \
               (np.max(np.abs(modes_at_freq))   >0.10797565399041009-tol))
    ## now reuse blocks
    params['reuse_blocks'] = True
    spod_class = spod_standard(params=params,  comm=comm)
    spod = spod_class.fit(data_list=data)
    T_ = 12.5;     tol = 1e-10
    f_, f_idx = spod.find_nearest_freq(freq_req=1/T_, freq=spod.freq)
    if comm.rank == 0:
        modes_at_freq = spod.get_modes_at_freq(freq_idx=f_idx)
        assert((np.abs(modes_at_freq[0,1,0,0])  <0.00046343628114412+tol) and \
               (np.abs(modes_at_freq[0,1,0,0])  >0.00046343628114412-tol))
        assert((np.abs(modes_at_freq[10,3,0,2]) <0.00015920889387988+tol) and \
               (np.abs(modes_at_freq[10,3,0,2]) >0.00015920889387988-tol))
        assert((np.abs(modes_at_freq[14,15,0,1])<0.00022129956393462+tol) and \
               (np.abs(modes_at_freq[14,15,0,1])>0.00022129956393462-tol))
        assert((np.min(np.abs(modes_at_freq))   <1.1110799348607e-05+tol) and \
               (np.min(np.abs(modes_at_freq))   >1.1110799348607e-05-tol))
        assert((np.max(np.abs(modes_at_freq))   <0.10797565399041009+tol) and \
               (np.max(np.abs(modes_at_freq))   >0.10797565399041009-tol))
        try:
            shutil.rmtree(os.path.join(CWD, params['savedir']))
        except OSError as e:
            pass

@pytest.mark.mpi(minsize=2, maxsize=3)
def test_standard_svd():
    ## -------------------------------------------------------------------
    try:
        from mpi4py import MPI
        comm = MPI.COMM_WORLD
    except:
        comm = None
    data_file = os.path.join(CFD,'./data', 'fluidmechanics_data.mat')
    data_dict = utils_io.read_data(data_file=data_file)
    data = data_dict['p'].T
    dt = data_dict['dt'][0,0]
    nt = data.shape[0]
    config_file = os.path.join(CFD, 'data', 'input_spod.yaml')
    params = utils_io.read_config(config_file)
    params['time_step'   ] = dt
    params['mean_type'   ] = 'blockwise'
    params['n_modes_save'] = 40
    params['overlap'     ] = 50
    params['fullspectrum'] = True
    ## -------------------------------------------------------------------
    SPOD_analysis = spod_standard(params=params,  comm=comm)
    spod = SPOD_analysis.fit(data_list=data)
    results_dir = spod.savedir_sim
    file_coeffs, coeffs_dir = utils_spod.compute_coeffs_op(
        data=data, results_dir=results_dir, svd=True, comm=comm)
    file_dynamics, coeffs_dir = utils_spod.compute_reconstruction(
        coeffs_dir=coeffs_dir, time_idx='all', comm=comm)
    T_ = 12.5;     tol = 1e-8
    f_, f_idx = spod.find_nearest_freq(freq_req=1/T_, freq=spod.freq)
    if comm.rank == 0:
        modes_at_freq = spod.get_modes_at_freq(freq_idx=f_idx)
        coeffs = np.load(file_coeffs)
        recons = np.load(file_dynamics)
        ## fit
        assert((np.min(np.abs(modes_at_freq))<3.685998997e-06+tol) and \
               (np.min(np.abs(modes_at_freq))>3.685998997e-06-tol))
        assert((np.max(np.abs(modes_at_freq))<0.1674285987544+tol) and \
               (np.max(np.abs(modes_at_freq))>0.1674285987544-tol))
        ## transform
        assert((np.real(np.max(coeffs))<0.086430605471409+tol) and \
               (np.real(np.max(coeffs))>0.086430605471409-tol))
        assert((np.real(np.max(recons))<4.498864853598955+tol) and \
               (np.real(np.max(recons))>4.498864853598955-tol))
        x = data[...,None]
        l1 = utils_errors.compute_l_errors(recons, x, norm_type='l1')
        l2 = utils_errors.compute_l_errors(recons, x, norm_type='l2')
        li = utils_errors.compute_l_errors(recons, x, norm_type='linf')
        l1_r = utils_errors.compute_l_errors(recons, x, norm_type='l1_rel')
        l2_r = utils_errors.compute_l_errors(recons, x, norm_type='l2_rel')
        li_r = utils_errors.compute_l_errors(recons, x, norm_type='linf_rel')
        ## errors
        assert((l1  <2.48238393194e-06+tol) and (l1  >2.48238393194e-06-tol))
        assert((l2  <1.68617429317e-08+tol) and (l2  >1.68617429317e-08-tol))
        assert((li  <0.002026691589296+tol) and (li  >0.002026691589296-tol))
        assert((l1_r<5.56566193217e-07+tol) and (l1_r>5.56566193217e-07-tol))
        assert((l2_r<3.78105921025e-09+tol) and (l2_r>3.78105921025e-09-tol))
        assert((li_r<0.000454925304459+tol) and (li_r>0.000454925304459-tol))
        try:
            shutil.rmtree(os.path.join(CWD, params['savedir']))
        except OSError as e:
            pass

@pytest.mark.mpi(minsize=2, maxsize=3)
def test_standard_inv():
    ## -------------------------------------------------------------------
    try:
        from mpi4py import MPI
        comm = MPI.COMM_WORLD
    except:
        comm = None
    data_file = os.path.join(CFD,'./data', 'fluidmechanics_data.mat')
    data_dict = utils_io.read_data(data_file=data_file)
    data = data_dict['p'].T
    dt = data_dict['dt'][0,0]
    nt = data.shape[0]
    config_file = os.path.join(CFD, 'data', 'input_spod.yaml')
    params = utils_io.read_config(config_file)
    params['time_step'   ] = dt
    params['mean_type'   ] = 'longtime'
    params['n_modes_save'] = 40
    params['overlap'     ] = 50
    params['fullspectrum'] = True
    ## -------------------------------------------------------------------
    SPOD_analysis = spod_standard(params=params, comm=comm)
    spod = SPOD_analysis.fit(data_list=data)
    results_dir = spod.savedir_sim
    file_coeffs, coeffs_dir = utils_spod.compute_coeffs_op(
        data=data, results_dir=results_dir,
        svd=False, comm=comm)
    file_dynamics, coeffs_dir = utils_spod.compute_reconstruction(
        coeffs_dir=coeffs_dir, time_idx='all', comm=comm)
    T_ = 12.5;     tol = 1e-10
    f_, f_idx = spod.find_nearest_freq(freq_req=1/T_, freq=spod.freq)
    if comm.rank == 0:
        modes_at_freq = spod.get_modes_at_freq(freq_idx=f_idx)
        coeffs = np.load(file_coeffs)
        recons = np.load(file_dynamics)
        ## fit
        assert((np.min(np.abs(modes_at_freq))<8.971537836e-07+tol) and \
               (np.min(np.abs(modes_at_freq))>8.971537836e-07-tol))
        assert((np.max(np.abs(modes_at_freq))<0.1874697574930+tol) and \
               (np.max(np.abs(modes_at_freq))>0.1874697574930-tol))
        ## transform
        assert((np.real(np.max(coeffs))<0.13950582200756+tol) and \
               (np.real(np.max(coeffs))>0.13950582200756-tol))
        assert((np.real(np.max(recons))<4.49886478858618+tol) and \
               (np.real(np.max(recons))>4.49886478858618-tol))
        x = data[...,None]
        l1 = utils_errors.compute_l_errors(recons, x, norm_type='l1')
        l2 = utils_errors.compute_l_errors(recons, x, norm_type='l2')
        li = utils_errors.compute_l_errors(recons, x, norm_type='linf')
        l1_r = utils_errors.compute_l_errors(recons, x, norm_type='l1_rel')
        l2_r = utils_errors.compute_l_errors(recons, x, norm_type='l2_rel')
        li_r = utils_errors.compute_l_errors(recons, x, norm_type='linf_rel')
        ## errors
        assert((l1  <4.77703783599e-07+tol) and (l1  >4.77703783599e-07-tol))
        assert((l2  <5.83926118831e-09+tol) and (l2  >5.83926118831e-09-tol))
        assert((li  <0.000614800089066+tol) and (li  >0.000614800089066-tol))
        assert((l1_r<1.07101850791e-07+tol) and (l1_r>1.07101850791e-07-tol))
        assert((l2_r<1.30918399202e-09+tol) and (l2_r>1.30918399202e-09-tol))
        assert((li_r<0.000137704603970+tol) and (li_r>0.000137704603970-tol))
        try:
            shutil.rmtree(os.path.join(CWD, params['savedir']))
        except OSError as e:
            pass

@pytest.mark.mpi(minsize=2, maxsize=3)
def test_standard_freq2_class_compute():
    try:
        from mpi4py import MPI
        comm = MPI.COMM_WORLD
    except:
        comm = None

    data_file = os.path.join(CFD, './data/', 'era_interim_data.nc')
    ds = utils_io.read_data(data_file=data_file)

    nt = len(np.array(ds['time']))
    x1 = np.array(ds['longitude']) - 180
    x2 = np.array(ds['latitude'])
    data = ds['tp']

    ## params
    config_file = os.path.join(CFD, 'data', 'input_tutorial2.yaml')
    params = utils_io.read_config(config_file)

    weights = utils_weights.geo_trapz_2D(
        x1_dim=x2.shape[0], x2_dim=x1.shape[0],
        n_vars=params['n_variables'])
    ## -------------------------------------------------------------------

    ## one-stage reader with the old freq writer
    params['savefreq_disk']  = True
    params['savefreq_disk2'] = False
    standard = spod_standard(params=params, weights=weights, comm=comm)
    spod = standard.fit(data_list=data)
    T_ = 960
    f_, f_idx = spod.find_nearest_freq(freq_req=1/T_, freq=spod.freq)
    if comm.rank == 0:
        modes_at_freq1 = spod.get_modes_at_freq(freq_idx=f_idx)
        try:
            shutil.rmtree(os.path.join(CWD, params['savedir']))
        except OSError as e:
            pass

    ## two-stage reader with flattened data reader and the new freq/mode writer
    params['savefreq_disk'] = False
    params['savefreq_disk2'] = True
    standard = spod_standard(params=params, weights=weights, comm=comm)
    spod = standard.fit(data_list=[data_file],variables=['tp'])
    T_ = 960
    f_, f_idx = spod.find_nearest_freq(freq_req=1/T_, freq=spod.freq)
    if comm.rank == 0:
        modes_at_freq2 = spod.get_modes_at_freq(freq_idx=f_idx)
        try:
            shutil.rmtree(os.path.join(CWD, params['savedir']))
        except OSError as e:
            pass

        assert np.allclose(modes_at_freq1, modes_at_freq2, atol=0.0001, rtol=0)

@pytest.mark.mpi(minsize=2, maxsize=3)
def test_standard_freq_class_compute():
    ## -------------------------------------------------------------------
    try:
        from mpi4py import MPI
        comm = MPI.COMM_WORLD
    except:
        comm = None
    data_file = os.path.join(CFD,'./data', 'fluidmechanics_data.mat')
    data_dict = utils_io.read_data(data_file=data_file)
    data = data_dict['p'].T
    dt = data_dict['dt'][0,0]
    nt = data.shape[0]
    config_file = os.path.join(CFD, 'data', 'input_spod.yaml')
    params = utils_io.read_config(config_file)
    params['time_step'   ] = dt
    params['mean_type'   ] = 'longtime'
    params['n_modes_save'] = 40
    params['overlap'     ] = 50
    params['fullspectrum'] = True
    ## -------------------------------------------------------------------
    SPOD_analysis = spod_standard(params=params,  comm=comm)
    spod = SPOD_analysis.fit(data_list=data)
    results_dir = spod.savedir_sim
    file_coeffs, coeffs_dir = spod.compute_coeffs_op(
        data=data, results_dir=results_dir, tol=1e-10,
        svd=False, T_lb=0.5, T_ub=1.1)
    file_dynamics, coeffs_dir = spod.compute_reconstruction(
        coeffs_dir=coeffs_dir, time_idx='all')
    T_ = 12.5;     tol1 = 1e-3;  tol2 = 1e-8
    f_, f_idx = spod.find_nearest_freq(freq_req=1/T_, freq=spod.freq)
    if comm.rank == 0:
        modes_at_freq = spod.get_modes_at_freq(freq_idx=f_idx)
        coeffs = np.load(file_coeffs)
        recons = np.load(file_dynamics)
        ## fit
        assert((np.min(np.abs(modes_at_freq))<8.971537836e-07+tol2) and \
               (np.min(np.abs(modes_at_freq))>8.971537836e-07-tol2))
        assert((np.max(np.abs(modes_at_freq))<0.1874697574930+tol2) and \
               (np.max(np.abs(modes_at_freq))>0.1874697574930-tol2))
        ## transform
        # print(f'{np.real(np.min(coeffs)) = :}')
        # print(f'{np.real(np.max(coeffs)) = :}')
        # print(f'{np.real(np.min(recons)) = :}')
        # print(f'{np.real(np.max(recons)) = :}')
        assert((np.real(np.min(coeffs))<-101.6470600168104+tol1) and \
               (np.real(np.min(coeffs))>-101.6470600168104-tol1))
        assert((np.real(np.max(coeffs))< 117.3492244840017+tol1) and \
               (np.real(np.max(coeffs))> 117.3492244840017-tol1))
        assert((np.real(np.min(recons))< 4.340606772197322+tol1) and \
               (np.real(np.min(recons))> 4.340606772197322-tol1))
        assert((np.real(np.max(recons))< 4.498677772159833+tol1) and \
               (np.real(np.max(recons))> 4.498677772159833-tol1))
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
        assert((l1  <0.00104122273134+tol2) and (l1  >0.00104122273134-tol2))
        assert((l2  <1.1276085475e-06+tol2) and (l2  >1.1276085475e-06-tol2))
        assert((li  <0.01784020507579+tol2) and (li  >0.01784020507579-tol2))
        assert((l1_r<0.00023355591009+tol2) and (l1_r>0.00023355591009-tol2))
        assert((l2_r<2.5299012083e-07+tol2) and (l2_r>2.5299012083e-07-tol2))
        assert((li_r<0.00403310279450+tol2) and (li_r>0.00403310279450-tol2))
        try:
            shutil.rmtree(os.path.join(CWD, params['savedir']))
        except OSError as e:
            pass

@pytest.mark.mpi(minsize=2, maxsize=3)
def test_standard_freq_utils_compute():
    ## -------------------------------------------------------------------
    try:
        from mpi4py import MPI
        comm = MPI.COMM_WORLD
    except:
        comm = None
    data_file = os.path.join(CFD,'./data', 'fluidmechanics_data.mat')
    data_dict = utils_io.read_data(data_file=data_file)
    data = data_dict['p'].T
    dt = data_dict['dt'][0,0]
    nt = data.shape[0]
    config_file = os.path.join(CFD, 'data', 'input_spod.yaml')
    params = utils_io.read_config(config_file)
    params['time_step'   ] = dt
    params['mean_type'   ] = 'longtime'
    params['n_modes_save'] = 40
    params['overlap'     ] = 50
    params['fullspectrum'] = True
    ## -------------------------------------------------------------------
    SPOD_analysis = spod_standard(params=params,  comm=comm)
    spod = SPOD_analysis.fit(data_list=data)
    results_dir = spod.savedir_sim
    file_coeffs, coeffs_dir = utils_spod.compute_coeffs_op(
        data=data, results_dir=results_dir, tol=1e-10,
        svd=False, T_lb=0.5, T_ub=1.1, comm=comm)
    file_dynamics, coeffs_dir = utils_spod.compute_reconstruction(
        coeffs_dir=coeffs_dir, time_idx='all', comm=comm)
    flag1, o1 = utils_spod.check_orthogonality(
        results_dir=results_dir, mode_idx1=[1], mode_idx2=[0],
        freq_idx=[5], dtype='double', comm=comm)
    flag2, o2 = utils_spod.check_orthogonality(
        results_dir=results_dir, mode_idx1=[1], mode_idx2=[0],
        freq_idx=[5], dtype='single', comm=comm)
    flag3, o3 = utils_spod.check_orthogonality(
        results_dir=results_dir, mode_idx1=[1], mode_idx2=[1],
        freq_idx=[5], dtype='single', comm=comm)
    T_ = 12.5;     tol1 = 1e-3;  tol2 = 1e-8
    f_, f_idx = spod.find_nearest_freq(freq_req=1/T_, freq=spod.freq)
    if comm.rank == 0:
        modes_at_freq = spod.get_modes_at_freq(freq_idx=f_idx)
        coeffs = np.load(file_coeffs)
        recons = np.load(file_dynamics)
        ## fit
        # print(f'{flag1 = :}')
        # print(f'{np.abs(o1) = :}')
        # print(f'{flag2 = :}')
        # print(f'{np.abs(o2) = :}')
        # print(f'{flag3 = :}')
        # print(f'{np.abs(o3) = :}')
        assert((np.min(np.abs(modes_at_freq))<8.971537836e-07+tol2) and \
               (np.min(np.abs(modes_at_freq))>8.971537836e-07-tol2))
        assert((np.max(np.abs(modes_at_freq))<0.1874697574930+tol2) and \
               (np.max(np.abs(modes_at_freq))>0.1874697574930-tol2))
        assert(flag1==True); assert(np.abs(o1)<1e-15)
        assert(flag2==True); assert((np.abs(o2)<1e-7 )and(np.abs(o2)>1e-9 ))
        assert(flag3==True); assert((np.abs(o3)<1.001 )and(np.abs(o3)>0.999 ))
        ## transform
        # print(f'{np.real(np.min(coeffs)) = :}')
        # print(f'{np.real(np.max(coeffs)) = :}')
        # print(f'{np.real(np.min(recons)) = :}')
        # print(f'{np.real(np.max(recons)) = :}')
        assert((np.real(np.min(coeffs))<-101.6470600168104+tol1) and \
               (np.real(np.min(coeffs))>-101.6470600168104-tol1))
        assert((np.real(np.max(coeffs))< 117.3492244840017+tol1) and \
               (np.real(np.max(coeffs))> 117.3492244840017-tol1))
        assert((np.real(np.min(recons))< 4.340606772197322+tol1) and \
               (np.real(np.min(recons))> 4.340606772197322-tol1))
        assert((np.real(np.max(recons))< 4.498677772159833+tol1) and \
               (np.real(np.max(recons))> 4.498677772159833-tol1))
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
        assert((l1  <0.00104122273134+tol2) and (l1  >0.00104122273134-tol2))
        assert((l2  <1.1276085475e-06+tol2) and (l2  >1.1276085475e-06-tol2))
        assert((li  <0.01784020507579+tol2) and (li  >0.01784020507579-tol2))
        assert((l1_r<0.00023355591009+tol2) and (l1_r>0.00023355591009-tol2))
        assert((l2_r<2.5299012083e-07+tol2) and (l2_r>2.5299012083e-07-tol2))
        assert((li_r<0.00403310279450+tol2) and (li_r>0.00403310279450-tol2))
        try:
            shutil.rmtree(os.path.join(CWD, params['savedir']))
        except OSError as e:
            pass

@pytest.mark.mpi(minsize=2, maxsize=3)
def test_standard_normalize():
    ## -------------------------------------------------------------------
    try:
        from mpi4py import MPI
        comm = MPI.COMM_WORLD
    except:
        comm = None
    data_file = os.path.join(CFD,'./data', 'fluidmechanics_data.mat')
    data_dict = utils_io.read_data(data_file=data_file)
    data = data_dict['p'].T
    dt = data_dict['dt'][0,0]
    nt = data.shape[0]
    config_file = os.path.join(CFD, 'data', 'input_spod.yaml')
    params = utils_io.read_config(config_file)
    params['time_step'   ] = dt
    params['mean_type'   ] = 'longtime'
    params['n_modes_save'] = 40
    params['overlap'     ] = 50
    params['fullspectrum'] = True
    params['normalize_weights'] = True
    params['normalize_data'   ] = True
    ## -------------------------------------------------------------------
    SPOD_analysis = spod_standard(params=params,  comm=comm)
    spod = SPOD_analysis.fit(data_list=data)
    results_dir = spod.savedir_sim
    file_coeffs, coeffs_dir = utils_spod.compute_coeffs_op(
        data=data, results_dir=results_dir,
        tol=1e-10, svd=False, T_lb=0.5, T_ub=1.1, comm=comm)
    file_dynamics, coeffs_dir = utils_spod.compute_reconstruction(
        coeffs_dir=coeffs_dir, time_idx='all', comm=comm)
    T_ = 12.5;     tol1 = 1e-3;  tol2 = 1e-8
    f_, f_idx = spod.find_nearest_freq(freq_req=1/T_, freq=spod.freq)
    if comm.rank == 0:
        modes_at_freq = spod.get_modes_at_freq(freq_idx=f_idx)
        coeffs = np.load(file_coeffs)
        recons = np.load(file_dynamics)
        # print(f'{np.real(np.min(recons)) = :}')
        # print(f'{np.real(np.min(coeffs)) = :}')
        # print(f'{np.real(np.max(recons)) = :}')
        # print(f'{np.real(np.max(coeffs)) = :}')
        ## fit
        assert((np.min(np.abs(modes_at_freq))<1.600183827320e-09+tol2) and \
               (np.min(np.abs(modes_at_freq))>1.600183827320e-09-tol2))
        assert((np.max(np.abs(modes_at_freq))<0.0071528728753325+tol2) and \
               (np.max(np.abs(modes_at_freq))>0.0071528728753325-tol2))
        ## transform
        assert((np.real(np.max(coeffs))<2156.676391925318+tol1) and \
               (np.real(np.max(coeffs))>2156.676391925318-tol1))
        assert((np.real(np.max(recons))<4.474232181561473+tol2) and \
               (np.real(np.max(recons))>4.474232181561473-tol2))
        x = data[...,None]
        l1 = utils_errors.compute_l_errors(recons, x, norm_type='l1')
        l2 = utils_errors.compute_l_errors(recons, x, norm_type='l2')
        li = utils_errors.compute_l_errors(recons, x, norm_type='linf')
        l1_r = utils_errors.compute_l_errors(recons, x, norm_type='l1_rel')
        l2_r = utils_errors.compute_l_errors(recons, x, norm_type='l2_rel')
        li_r = utils_errors.compute_l_errors(recons, x, norm_type='linf_rel')
        ## errors
        assert((l1  <0.003262458870240+tol2) and (l1  >0.003262458870240-tol2))
        assert((l2  <3.85087739991e-06+tol2) and (l2  >3.85087739991e-06-tol2))
        assert((li  <0.111822437047942+tol2) and (li  >0.111822437047942-tol2))
        assert((l1_r<0.000732038850593+tol2) and (l1_r>0.000732038850593-tol2))
        assert((l2_r<8.64671493204e-07+tol2) and (l2_r>8.64671493204e-07-tol2))
        assert((li_r<0.025767738920132+tol2) and (li_r>0.025767738920132-tol2))
        try:
            shutil.rmtree(os.path.join(CWD, params['savedir']))
        except OSError as e:
            pass

@pytest.mark.mpi(minsize=2, maxsize=3)
def test_streaming_fullspectrum():
    ## -------------------------------------------------------------------
    try:
        from mpi4py import MPI
        comm = MPI.COMM_WORLD
    except:
        comm = None
    data_file = os.path.join(CFD,'./data', 'fluidmechanics_data.mat')
    data_dict = utils_io.read_data(data_file=data_file)
    data = data_dict['p'].T
    dt = data_dict['dt'][0,0]
    nt = data.shape[0]
    config_file = os.path.join(CFD, 'data', 'input_spod.yaml')
    params = utils_io.read_config(config_file)
    params['time_step'] = dt
    params['fullspectrum'] = True
    ## -------------------------------------------------------------------
    spod_class = spod_streaming(params=params,  comm=comm)
    spod = spod_class.fit(data_list=data)
    T_ = 12.5;     tol = 1e-10
    f_, f_idx = spod.find_nearest_freq(freq_req=1/T_, freq=spod.freq)
    if comm.rank == 0:
        modes_at_freq = spod.get_modes_at_freq(freq_idx=f_idx)
        # print(f'{np.abs(modes_at_freq[0,1,0,0]) = :}')
        # print(f'{np.abs(modes_at_freq[10,3,0,2]) = :}')
        # print(f'{np.abs(modes_at_freq[14,15,0,1]) = :}')
        # print(f'{np.abs(modes_at_freq[14,15,0,1]) = :}')
        # print(f'{np.min(np.abs(modes_at_freq)) = :}')
        # print(f'{np.max(np.abs(modes_at_freq)) = :}')
        assert((np.abs(modes_at_freq[0,1,0,0])  <0.00034252270314601+tol) and \
               (np.abs(modes_at_freq[0,1,0,0])  >0.00034252270314601-tol))
        assert((np.abs(modes_at_freq[10,3,0,2]) <0.00017883224454813+tol) and \
               (np.abs(modes_at_freq[10,3,0,2]) >0.00017883224454813-tol))
        assert((np.abs(modes_at_freq[14,15,0,1])<0.00020809153783069+tol) and \
               (np.abs(modes_at_freq[14,15,0,1])>0.00020809153783069-tol))
        assert((np.min(np.abs(modes_at_freq))   <4.5039283294598e-06+tol) and \
               (np.min(np.abs(modes_at_freq))   >4.5039283294598e-06-tol))
        assert((np.max(np.abs(modes_at_freq))   <0.11068809881000957+tol) and \
               (np.max(np.abs(modes_at_freq))   >0.11068809881000957-tol))
        try:
            shutil.rmtree(os.path.join(CWD, params['savedir']))
        except OSError as e:
            pass

@pytest.mark.mpi(minsize=2, maxsize=3)
def test_streaming_freq():
    ## -------------------------------------------------------------------
    try:
        from mpi4py import MPI
        comm = MPI.COMM_WORLD
    except:
        comm = None
    data_file = os.path.join(CFD,'./data', 'fluidmechanics_data.mat')
    data_dict = utils_io.read_data(data_file=data_file)
    data = data_dict['p'].T
    dt = data_dict['dt'][0,0]
    nt = data.shape[0]
    config_file = os.path.join(CFD, 'data', 'input_spod.yaml')
    params = utils_io.read_config(config_file)
    params['time_step'   ] = dt
    params['mean_type'   ] = 'longtime'
    params['n_modes_save'] = 40
    params['overlap'     ] = 50
    params['fullspectrum'] = True
    ## -------------------------------------------------------------------
    SPOD_analysis = spod_streaming(params=params,  comm=comm)
    spod = SPOD_analysis.fit(data_list=data)
    results_dir = spod.savedir_sim
    file_coeffs, coeffs_dir = utils_spod.compute_coeffs_op(
        data=data, results_dir=results_dir,
        tol=1e-10, svd=False, T_lb=0.5, T_ub=1.1, comm=comm)
    file_dynamics, coeffs_dir = utils_spod.compute_reconstruction(
        coeffs_dir=coeffs_dir, time_idx='all', comm=comm)
    flag1, o1 = utils_spod.check_orthogonality(
        results_dir=results_dir, mode_idx1=[1], mode_idx2=[0],
        freq_idx=[5], dtype='double', comm=comm)
    flag2, o2 = utils_spod.check_orthogonality(
        results_dir=results_dir, mode_idx1=[1], mode_idx2=[0],
        freq_idx=[5], dtype='single', comm=comm)
    flag3, o3 = utils_spod.check_orthogonality(
        results_dir=results_dir, mode_idx1=[1], mode_idx2=[1],
        freq_idx=[5], dtype='single', comm=comm)
    T_ = 12.5;     tol1 = 1e-3;  tol2 = 1e-8
    f_, f_idx = spod.find_nearest_freq(freq_req=1/T_, freq=spod.freq)
    if comm.rank == 0:
        modes_at_freq = spod.get_modes_at_freq(freq_idx=f_idx)
        coeffs = np.load(file_coeffs)
        recons = np.load(file_dynamics)
        # print(f'{np.min(np.abs(modes_at_freq)) = :}')
        # print(f'{np.max(np.abs(modes_at_freq)) = :}')
        # print(f'{flag1 = :}')
        # print(f'{np.abs(o1) = :}')
        # print(f'{flag2 = :}')
        # print(f'{np.abs(o2) = :}')
        # print(f'{flag3 = :}')
        # print(f'{np.abs(o3) = :}')
        ## fit
        assert((np.min(np.abs(modes_at_freq))<0+tol2) and \
               (np.min(np.abs(modes_at_freq))>0-tol2))
        assert((np.max(np.abs(modes_at_freq))<0.17575077060057+tol2) and \
               (np.max(np.abs(modes_at_freq))>0.17575077060057-tol2))
        assert(flag1==True); assert(np.abs(o1)<1e-15)
        assert(flag2==True); assert((np.abs(o2)<1e-7 )and(np.abs(o2)>1e-9 ))
        assert(flag3==True); assert((np.abs(o3)<1.001 )and(np.abs(o3)>0.999 ))
        ## transform
        # print(f'{np.real(np.min(recons)) = :}')
        # print(f'{np.real(np.min(coeffs)) = :}')
        # print(f'{np.real(np.max(recons)) = :}')
        # print(f'{np.real(np.max(coeffs)) = :}')
        assert((np.real(np.min(coeffs))<-95.19671159637073+tol1) and \
               (np.real(np.min(coeffs))>-95.19671159637073-tol1))
        assert((np.real(np.max(coeffs))< 92.4498133690795+tol1) and \
               (np.real(np.max(coeffs))> 92.4498133690795-tol1))
        assert((np.real(np.min(recons))< 4.340179150964369+tol1) and \
               (np.real(np.min(recons))> 4.340179150964369-tol1))
        assert((np.real(np.max(recons))< 4.498808236142374+tol1) and \
               (np.real(np.max(recons))> 4.498808236142374-tol1))
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
        assert((l1  <0.00107942380613+tol2) and (l1  >0.00107942380613-tol2))
        assert((l2  <1.1519824371e-06+tol2) and (l2  >1.1519824371e-06-tol2))
        assert((li  <0.01834080799354+tol2) and (li  >0.01834080799354-tol2))
        assert((l1_r<0.00024212332147+tol2) and (l1_r>0.00024212332147-tol2))
        assert((l2_r<2.5845390761e-07+tol2) and (l2_r>2.5845390761e-07-tol2))
        assert((li_r<0.00413503874851+tol2) and (li_r>0.00413503874851-tol2))
        try:
            shutil.rmtree(os.path.join(CWD, params['savedir']))
        except OSError as e:
            pass

@pytest.mark.mpi(minsize=2, maxsize=3)
def test_parallel_postproc():
    ## -------------------------------------------------------------------
    try:
        from mpi4py import MPI
        comm = MPI.COMM_WORLD
    except:
        comm = None
    data_file = os.path.join(CFD,'./data', 'fluidmechanics_data.mat')
    data_dict = utils_io.read_data(data_file=data_file)
    data = data_dict['p'].T
    dt = data_dict['dt'][0,0]
    nt = data.shape[0]
    x1 = data_dict['r'].T; x1 = x1[:,0]
    x2 = data_dict['x'].T; x2 = x2[0,:]
    config_file = os.path.join(CFD, 'data', 'input_spod.yaml')
    params = utils_io.read_config(config_file)
    params['time_step'   ] = dt
    params['mean_type'   ] = 'blockwise'
    params['n_modes_save'] = 3
    params['overlap'     ] = 50
    params['fullspectrum'] = True
    ## -------------------------------------------------------------------
    spod_class = spod_standard(params=params,  comm=comm)
    spod = spod_class.fit(data_list=data)
    T_ = 12.5;     tol = 1e-10
    f_, f_idx = spod.find_nearest_freq(freq_req=1/T_, freq=spod.freq)
    if comm.rank == 0:
        modes_at_freq = spod.get_modes_at_freq(freq_idx=f_idx)
        spod.plot_eigs             (filename='eigs.png')
        spod.plot_eigs_vs_frequency(filename='eigs.png')
        spod.plot_eigs_vs_period   (filename='eigs.png')
        spod.plot_2d_modes_at_frequency(freq_req=f_,
                                        freq=spod.freq,
                                        x1=x1, x2=x2,
                                        filename='modes.png')
        spod.plot_2d_modes_at_frequency(freq_req=f_,
                                        freq=spod.freq,
                                        x1=x1, x2=x2,
                                        imaginary=True,
                                        filename='modes.png')
        # spod.plot_2d_mode_slice_vs_time(freq_req=f_,
        #                                 freq=spod.freq,
        #                                 filename='modes.png')
        spod.plot_mode_tracers(freq_req=f_, freq=spod.freq,
                                coords_list=[(10,10), (14,14)],
                                filename='tracers.png')
        data = spod.get_data(data)
        post.plot_2d_data(data, time_idx=[0,10],
            path=params['savedir'], filename='data.png')
        post.plot_data_tracers(data, coords_list=[(10,10), (14,14)],
            path=params['savedir'], filename='data_tracers.png')
        spod.plot_2d_data(data, time_idx=[0,10], filename='data.png')
        spod.plot_data_tracers(data, coords_list=[(10,10), (14,14)],
                                filename='data_tracers.png')
        # spod.generate_2d_data_video(filename='data_movie.mp4')
        # print(f'{np.min(np.abs(modes_at_freq)) = :}')
        # print(f'{np.max(np.abs(modes_at_freq)) = :}')
        assert((np.abs(modes_at_freq[0,1,0,0])  <0.00046343628114412+tol) and \
               (np.abs(modes_at_freq[0,1,0,0])  >0.00046343628114412-tol))
        assert((np.abs(modes_at_freq[10,3,0,2]) <0.00015920889387988+tol) and \
               (np.abs(modes_at_freq[10,3,0,2]) >0.00015920889387988-tol))
        assert((np.abs(modes_at_freq[14,15,0,1])<0.00022129956393462+tol) and \
               (np.abs(modes_at_freq[14,15,0,1])>0.00022129956393462-tol))
        assert((np.min(np.abs(modes_at_freq))   <1.1110799348607e-05+tol) and \
               (np.min(np.abs(modes_at_freq))   >1.1110799348607e-05-tol))
        assert((np.max(np.abs(modes_at_freq))   <0.10797565399041009+tol) and \
               (np.max(np.abs(modes_at_freq))   >0.10797565399041009-tol))
        try:
            shutil.rmtree(os.path.join(CWD, params['savedir']))
        except OSError as e:
            pass



if __name__ == "__main__":
    test_standard_fullspectrum()
    test_standard_reuse_blocks()
    test_standard_svd()
    test_standard_inv()
    test_standard_freq_class_compute()
    test_standard_freq2_class_compute()
    test_standard_freq_utils_compute()
    test_standard_normalize()
    test_streaming_fullspectrum()
    test_streaming_freq()
    test_parallel_postproc()
