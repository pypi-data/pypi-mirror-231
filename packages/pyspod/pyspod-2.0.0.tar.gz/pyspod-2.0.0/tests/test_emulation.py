#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import h5py
import yaml
import shutil
import numpy as np

# Current, parent and file paths
CWD = os.getcwd()
CF  = os.path.realpath(__file__)
CFD = os.path.dirname(CF)
sys.path.append(os.path.join(CFD,'../'))

# Import library specific modules
from pyspod.pod.standard  import Standard as pod_standard
from pyspod.spod.standard import Standard as spod_standard
from pyspod.emulation.neural_nets import Neural_Nets as emulation_nn
import pyspod.pod.utils      as utils_pod
import pyspod.spod.utils     as utils_spod
import pyspod.pod.utils      as utils_pod
import pyspod.utils.io       as utils_io
import pyspod.utils.postproc as post



def test_lstm_pod():
    ## -------------------------------------------------------------------------
    data_file = os.path.join(CFD,'./data', 'fluidmechanics_data.mat')
    data_dict = utils_io.read_data(data_file=data_file)
    data = data_dict['p'].T
    dt = data_dict['dt'][0,0]
    t = dt * np.arange(0,data.shape[0]).T
    nt = t.shape[0]
    train_ratio = 0.8
    test_ratio = (1 - train_ratio)
    params_pod = {
        # -- required parameters
        'time_step'   : dt,
        'n_space_dims': 2,
        'n_variables' : 1,
        # -- optional parameters
        'overlap'          : 50,
        'normalize_weights': True,
        'scale_data'       : True,
        'n_modes_save'     : 8,
        'dtype'            : 'double',
        'savedir'          : os.path.join(CFD, 'results')
    }
    params_emulation = {
        'network'   : 'lstm',
        'scaler'    : 'localmax',
        'data_type' : 'real',
        'epochs'    : 10,
        'batch_size': 32,
        'n_seq_in'  : 60,
        'n_seq_out' : 1,
        'n_neurons' : 1,
        'dropout'   : 0.15,
        'savedir'   : os.path.join(CFD, 'results')
    }
    ## -------------------------------------------------------------------------

    ##  training and testing database definition
    nt_train = int(train_ratio * nt)
    d_train = data[:nt_train,:,:]
    nt_test = nt - nt_train
    d_test  = data[nt_train:,:,:]

    ## fit and transform pod
    pod_class = pod_standard(params=params_pod)
    pod = pod_class.fit(data_list=d_train)
    phi = np.load(os.path.join(pod._savedir_sim, 'modes.npy'))
    # coeffs_train, phi, tm, file_coeffs, max_axis = utils_pod.compute_coeffs_op(
    #     data=d_train, results_dir=pod._savedir_sim)
    results_dir = pod._savedir_sim
    c_train_file, dir_train = utils_pod.compute_coeffs_op(
        d_train, results_dir, savedir='train')
    c_test_file, dir_test = utils_pod.compute_coeffs_op(
        d_test, results_dir, savedir='test')

    ## compute test coefficients
    # d_r_test = np.reshape(d_test[:,:,:], [nt_test,pod.nv*pod.nx])
    # for i in range(nt_test):
        # d_r_test[i,:] = np.squeeze(d_r_test[i,:]) - np.squeeze(tm)
    # coeffs_test = np.transpose(phi) @ d_r_test.T

    ## initialization of variables and structures
    n_modes = params_pod['n_modes_save']
    coeffs_train = np.load(c_train_file)
    coeffs_test = np.load(c_test_file)
    dim1_train = coeffs_train.shape[1]
    dim0_test  = coeffs_test .shape[0]
    dim1_test  = coeffs_test .shape[1]
    data_train = np.zeros([n_modes  , dim1_train], dtype=float)
    data_test  = np.zeros([n_modes  , dim1_test] , dtype=float)
    coeffs     = np.zeros([dim0_test, dim1_test] , dtype=float)
    coeffs_tmp = np.zeros([n_modes  , dim1_test] , dtype=float)

    ## select lstm
    params_emulation['network'] = 'lstm'

    ## initialization Emulation class and run
    emulation = emulation_nn(params_emulation)
    emulation.model_initialize(data=data_train)

    ## normalize data
    c_train = coeffs_train[:,:]
    c_test = coeffs_test[:,:]
    scaler1 = emulation.scaler(data=c_train)
    scaler2 = emulation.scaler(data=c_train)
    data_train[:,:] = emulation.scale_data(c_train, vec=scaler1)
    data_test [:,:] = emulation.scale_data(c_test , vec=scaler1)

    ## train model
    emulation.model_train(data_train=data_train, data_valid=data_test)
    coeffs_tmp = emulation.model_inference(data_in=data_test)

    ## denormalize data
    coeffs[:,:] = emulation.descale_data(coeffs_tmp, scaler1)

    ## plot training history
    train_loss = emulation.train_history.history['loss']
    valid_loss = emulation.train_history.history['val_loss']
    post.plot_training_histories(
        train_loss, valid_loss,
        path=params_pod['savedir'],
        filename='history.png')

    # reconstruct solutions
    f_p, _ = utils_pod.compute_reconstruction(
        coeffs=c_test, coeffs_dir=dir_train, time_idx='all',
        savedir=dir_test, filename='recons_projection')
    f_e, _ = utils_pod.compute_reconstruction(
        coeffs=coeffs, coeffs_dir=dir_train, time_idx='all',
        savedir=dir_test, filename='recons_emulation')
    p_rec = np.load(f_p)
    e_rec = np.load(f_e)

    ## assert test
    tol = 1e-6
    savedir = pod._savedir
    assert(pod.dim         ==4)
    assert(pod.shape       ==(1, 20, 88, 1))
    assert(pod.nt          ==800)
    assert(pod.nx          ==1760)
    assert(pod.nv          ==1)
    assert(pod.xdim        ==2)
    assert(pod.xshape      ==(20, 88))
    assert(pod.dt          ==0.2)
    assert(pod.n_modes_save==8)
    assert((np.real(pod.eigs[0])   <90699.72245430+tol) and \
           (np.real(pod.eigs[0])   >90699.72245430-tol))
    assert((pod.weights[0,0]       <19934.84235881+tol) and \
           (pod.weights[0,0]       >19934.84235881-tol))
    assert((np.abs(e_rec[0,1,0])   <4.467810376724+tol) and \
           (np.abs(e_rec[0,1,0])   >4.467810376724-tol))
    assert((np.abs(e_rec[100,1,0]) <4.467810376724+tol) and \
           (np.abs(e_rec[100,1,0]) >4.467810376724-tol))
    assert((np.abs(e_rec[150,1,0]) <4.467810376761+tol) and \
           (np.abs(e_rec[150,1,0]) >4.467810376761-tol))
    assert((np.abs(e_rec[100,10,5])<4.463844748293+tol) and \
           (np.abs(e_rec[100,10,5])>4.463844748293-tol))
    assert((np.abs(e_rec[50,7,20]) <4.459104904890+tol) and \
           (np.abs(e_rec[50,7,20]) >4.459104904890-tol))
    assert((np.abs(e_rec[60,8,9])  <4.463696917777+tol) and \
           (np.abs(e_rec[60,8,9])  >4.463696917777-tol))
    # clean up results
    try:
        shutil.rmtree(os.path.join(CFD,'results'))
    except OSError as e:
        pass


def test_lstm_spod():
    ## -------------------------------------------------------------------------
    data_file = os.path.join(CFD,'./data', 'fluidmechanics_data.mat')
    data_dict = utils_io.read_data(data_file=data_file)
    data = data_dict['p'].T
    dt = data_dict['dt'][0,0]
    t = dt * np.arange(0,data.shape[0]).T
    nt = t.shape[0]
    train_ratio = 0.95
    test_ratio = (1 - train_ratio)
    block_dimension = 64 * dt
    params_spod = {
        # -- required parameters
        'time_step'   : dt,
        'n_space_dims': 2,
        'n_variables' : 1,
        'n_dft'       : np.ceil(block_dimension / dt),
        # -- optional parameters
        'overlap'          : 50,
        'mean_type'        : 'blockwise',
        'normalize_weights': False,
        'normalize_data'   : False,
        'n_modes_save'     : 3,
        'conf_level'       : 0.95,
        'savedir'          : os.path.join(CFD, 'results'),
        'reuse_blocks'     : False,
        'fullspectrum'     : True,
        'dtype'            : 'double'
    }
    params_emulation = {
        'network'   : 'lstm',
        'scaler'    : 'localmax',
        'data_type' : 'complex',
        'epochs'    : 3,
        'batch_size': 32,
        'n_seq_in'  : 30,
        'n_seq_out' : 1,
        'n_neurons' : 1,
        'dropout'   : 0.15,
        'savedir'   : os.path.join(CFD, 'results')
    }
    ## -------------------------------------------------------------------------

    ##  training and testing database definition
    nt_train = int(train_ratio * nt)
    d_train  = data[:nt_train,:,:]
    nt_test  = nt - nt_train
    d_test   = data[nt_train:,:,:]

    ## fit and transform spod
    spod_class = spod_standard(params=params_spod)
    spod = spod_class.fit(data_list=d_train)
    results_dir = spod.savedir_sim
    c_train_file, dir_train = utils_spod.compute_coeffs_op(
        d_train, results_dir, savedir='train')
    c_test_file, dir_test = utils_spod.compute_coeffs_op(
        d_test, results_dir, savedir='test')

    ## initialization of variables and structures
    coeffs_train = np.load(c_train_file)
    coeffs_test  = np.load(c_test_file )
    f_train = os.path.join(dir_train, 'params_coeffs.yaml')
    f_test  = os.path.join(dir_test , 'params_coeffs.yaml')
    with open(f_train) as f: params_train = yaml.load(f, Loader=yaml.FullLoader)
    with open(f_test ) as f: params_test  = yaml.load(f, Loader=yaml.FullLoader)
    n_freq = params_train['n_freq_r']
    n_modes    = params_spod['n_modes_save']
    n_feature  = coeffs_train.shape[0]
    dim1_train = coeffs_train.shape[1]
    dim0_test  = coeffs_test .shape[0]
    dim1_test  = coeffs_test .shape[1]
    data_train = np.zeros([n_freq,dim1_train]  , dtype=complex)
    data_test  = np.zeros([n_freq,dim1_test ]  , dtype=complex)
    coeffs_tmp = np.zeros([n_freq,dim1_test ]  , dtype=complex)
    coeffs     = np.zeros([dim0_test,dim1_test], dtype=complex)

    ## select lstm
    params_emulation['network'] = 'lstm'

    ## initialization Emulation class and run
    emulation = emulation_nn(params_emulation)
    emulation.model_initialize(data=data_train)

    for idx in range(n_modes):
        idx_x = list(range(idx,n_feature,n_modes))
        ## normalize data
        c_train = coeffs_train[idx_x,:]
        c_test  = coeffs_test [idx_x,:]
        scaler1 = emulation.scaler(data=c_train)
        scaler2 = emulation.scaler(data=c_train)
        data_train[:,:] = emulation.scale_data(c_train, vec=scaler1)
        data_test [:,:] = emulation.scale_data(c_test , vec=scaler1)

        ## train model
        emulation.model_train(
            data_train=data_train, data_valid=data_test, idx=idx)
        coeffs_tmp = emulation.model_inference(data_in=data_test, idx=idx)

        ## denormalize data
        coeffs[idx_x,:] = emulation.descale_data(coeffs_tmp, scaler1)

    ## plot training history
    train_loss = emulation.train_history.history['loss']
    valid_loss = emulation.train_history.history['val_loss']
    post.plot_training_histories(
        train_loss, valid_loss,
        path=params_spod['savedir'],
        filename='history.png')

    ## reconstruct solutions
    f_p, _ = utils_spod.compute_reconstruction(
        coeffs_dir=dir_train, coeffs=coeffs_test, time_idx='all',
        savedir=dir_test, filename='recons_projection')
    f_e, _ = utils_spod.compute_reconstruction(
        coeffs_dir=dir_train, coeffs=coeffs, time_idx='all',
        savedir=dir_test, filename='recons_emulation')
    d_test = d_test[...,None]
    p_rec = np.load(f_p)
    e_rec = np.load(f_e)

    ## test visualization
    post.generate_2d_subplot(
        var1=d_test[10,...,0], title1='data',
        var2=p_rec [10,...,0], title2='projection',
        var3=e_rec [10,...,0], title3='lstm emulation',
        N_round=6, path=params_spod['savedir'], filename='emulation.png')
    post.plot_compare_time_series(
        series1=coeffs_test[0,:], series2=coeffs[0,:],
        label1='test', label2='lstm', legendLocation='upper left',
        path=params_spod['savedir'], filename='timeseries_comparison.png')
    _ = post.compute_energy_spectrum(coeffs_test[0,:])

    ## assert test solutions
    tol = 1e-6
    # print(f'{np.abs(p_rec[0,0,0,0]) = :}')
    # print(f'{np.abs(p_rec[10,0,0,0]) = :}')
    # print(f'{np.abs(p_rec[15,5,12,0]) = :}')
    # print(f'{np.abs(e_rec[0,0,0,0]) = :}')
    # print(f'{np.abs(e_rec[10,0,0,0]) = :}')
    # print(f'{np.abs(e_rec[15,5,12,0]) = :}')
    assert((np.abs(p_rec[0,0,0,0])  <4.467528967599+tol) and \
           (np.abs(p_rec[0,0,0,0])  >4.467528967599-tol))
    assert((np.abs(p_rec[10,0,0,0]) <4.465600418067+tol) and \
           (np.abs(p_rec[10,0,0,0]) >4.465600418067-tol))
    assert((np.abs(p_rec[15,5,12,0])<4.457098452307+tol) and \
           (np.abs(p_rec[15,5,12,0])>4.457098452307-tol))
    assert((np.abs(e_rec[0,0,0,0])  <4.467528967599+tol) and \
           (np.abs(e_rec[0,0,0,0])  >4.467528967599-tol))
    assert((np.abs(e_rec[10,0,0,0]) <4.465600418067+tol) and \
           (np.abs(e_rec[10,0,0,0]) >4.465600418067-tol))
    assert((np.abs(e_rec[15,5,12,0])<4.457098452307+tol) and \
           (np.abs(e_rec[15,5,12,0])>4.457098452307-tol))
    # # clean up results
    # try:
    #     shutil.rmtree(os.path.join(CFD,'results'))
    # except OSError as e:
    #     pass


def test_cnn_spod():
    ## -------------------------------------------------------------------------
    data_file = os.path.join(CFD,'./data', 'fluidmechanics_data.mat')
    data_dict = utils_io.read_data(data_file=data_file)
    data = data_dict['p'].T
    dt = data_dict['dt'][0,0]
    t = dt * np.arange(0,data.shape[0]).T
    nt = t.shape[0]
    train_ratio = 0.95
    test_ratio = (1 - train_ratio)
    block_dimension = 64 * dt
    params_spod = {
        # -- required parameters
        'time_step'   : dt,
        'n_space_dims': 2,
        'n_variables' : 1,
        'n_dft'       : np.ceil(block_dimension / dt),
        # -- optional parameters
        'overlap'          : 50,
        'mean_type'        : 'blockwise',
        'normalize_weights': False,
        'normalize_data'   : False,
        'n_modes_save'     : 3,
        'conf_level'       : 0.95,
        'savedir'          : os.path.join(CFD, 'results'),
        'reuse_blocks'     : False,
        'fullspectrum'     : True,
        'dtype'            : 'double'
    }
    params_emulation = {
        'network'   : 'lstm',
        'scaler'    : 'localmax',
        'data_type' : 'complex',
        'epochs'    : 3,
        'batch_size': 32,
        'n_seq_in'  : 30,
        'n_seq_out' : 1,
        'n_neurons' : 1,
        'dropout'   : 0.15,
        'savedir'   : os.path.join(CFD, 'results')
    }
    ## -------------------------------------------------------------------------

    ##  training and testing database definition
    nt_train = int(train_ratio * nt)
    d_train  = data[:nt_train,:,:]
    nt_test  = nt - nt_train
    d_test   = data[nt_train:,:,:]

    ## fit and transform spod
    spod_class = spod_standard(params=params_spod)
    spod = spod_class.fit(data_list=d_train)
    results_dir = spod.savedir_sim
    c_train_file, dir_train = utils_spod.compute_coeffs_op(
        d_train, results_dir, savedir='train')
    c_test_file, dir_test = utils_spod.compute_coeffs_op(
        d_test, results_dir, savedir='test')

    ## initialization of variables and structures
    coeffs_train = np.load(c_train_file)
    coeffs_test  = np.load(c_test_file )
    f_train = os.path.join(dir_train, 'params_coeffs.yaml')
    f_test  = os.path.join(dir_test , 'params_coeffs.yaml')
    with open(f_train) as f: params_train = yaml.load(f, Loader=yaml.FullLoader)
    with open(f_test ) as f: params_test  = yaml.load(f, Loader=yaml.FullLoader)
    n_freq = params_train['n_freq_r']
    n_modes    = params_spod['n_modes_save']
    dim0_test  = coeffs_test .shape[0]
    dim1_train = coeffs_train.shape[1]
    dim1_test  = coeffs_test .shape[1]
    n_feature  = coeffs_train.shape[0]
    data_train = np.zeros([n_freq,dim1_train]  , dtype=complex)
    data_test  = np.zeros([n_freq,dim1_test ]  , dtype=complex)
    coeffs_tmp = np.zeros([n_freq,dim1_test ]  , dtype=complex)
    coeffs     = np.zeros([dim0_test,dim1_test], dtype=complex)

    ## select cnn
    params_emulation['network'] = 'cnn'

    ## initialization Emulation class and run
    emulation = emulation_nn(params_emulation)
    emulation.model_initialize(data=data_train)

    # clean up results
    try:
        shutil.rmtree(os.path.join(CFD,'results'))
    except OSError as e:
        pass



if __name__ == "__main__":
    test_lstm_pod ()
    test_lstm_spod()
    test_cnn_spod ()
