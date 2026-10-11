import pytest
import numpy as np
import sys
import os

# Add parent directory to path to import PWP
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import PWP

def test_absorb():
    # Test absorb function
    beta1 = 0.6
    beta2 = 20.0
    zlen = 10
    dz = 1.0
    absrb = PWP.absorb(beta1, beta2, zlen, dz)
    
    # Check length
    assert len(absrb) == zlen
    
    # Check sum of absorption - should be close to 1 for deep water, but here we just check it's <= 1 and positive
    assert np.all(absrb >= 0)
    assert np.sum(absrb) <= 1.0
    
def test_remove_si():
    # Test remove_si function (static instability)
    t = np.array([20.0, 19.0, 19.5, 18.0])
    s = np.array([35.0, 35.0, 35.0, 35.0])
    # d should increase with depth. Instability at index 1->2 (1025.0 -> 1024.5)
    d = np.array([1024.0, 1025.0, 1024.5, 1026.0])
    u = np.array([0.1, 0.1, 0.1, 0.1])
    v = np.array([0.1, 0.1, 0.1, 0.1])
    
    t_out, s_out, d_out, u_out, v_out = PWP.remove_si(t, s, d, u, v)
    
    # Density should be strictly non-decreasing after removing static instability
    assert np.all(np.diff(d_out) >= 0)
    
    # Check that the mixing conserved the mean properties of the mixed part
    # Indices 0, 1, 2 should be mixed because 1 and 2 were unstable, causing mixing up to surface
    assert np.isclose(d_out[0], d_out[1])
    assert np.isclose(d_out[1], d_out[2])

def test_mix5():
    t = np.array([20.0, 19.0, 18.0, 17.0])
    s = np.array([35.0, 35.0, 35.0, 35.0])
    d = np.array([1024.0, 1025.0, 1026.0, 1027.0])
    u = np.array([0.4, 0.3, 0.2, 0.1])
    v = np.array([0.4, 0.3, 0.2, 0.1])
    
    j = 3 # mix indices 0, 1, 2
    t_out, s_out, d_out, u_out, v_out = PWP.mix5(t, s, d, u, v, j)
    
    assert np.allclose(t_out[:j], np.mean(t[:j]))
    assert np.allclose(s_out[:j], np.mean(s[:j]))
    assert np.allclose(d_out[:j], np.mean(d[:j]))
    assert np.allclose(u_out[:j], np.mean(u[:j]))
    assert np.allclose(v_out[:j], np.mean(v[:j]))

def test_rot():
    u = np.array([1.0, 0.0])
    v = np.array([0.0, 1.0])
    ang = np.pi / 2 # 90 degrees
    
    u_out, v_out = PWP.rot(u, v, ang)
    
    expected_u_out = np.array([0.0, -1.0])
    expected_v_out = np.array([1.0, 0.0])
    
    assert np.allclose(u_out, expected_u_out)
    assert np.allclose(v_out, expected_v_out)

def test_bulk_mix():
    t = np.array([20.0, 19.0, 18.0, 17.0])
    s = np.array([35.0, 35.0, 35.0, 35.0])
    d = np.array([1024.0, 1025.0, 1026.0, 1027.0])
    u = np.array([1.0, 0.0, 0.0, 0.0])
    v = np.array([0.0, 0.0, 0.0, 0.0])
    g = 9.81
    rb = 0.65
    nz = 4
    z = np.array([0.0, 10.0, 20.0, 30.0])
    mld_idx = 1
    
    t_out, s_out, d_out, u_out, v_out = PWP.bulk_mix(t, s, d, u, v, g, rb, nz, z, mld_idx)
    assert len(t_out) == nz

def test_grad_mix():
    t = np.array([20.0, 19.0, 18.0, 17.0])
    s = np.array([35.0, 35.0, 35.0, 35.0])
    d = np.array([1024.0, 1025.0, 1026.0, 1027.0])
    u = np.array([1.0, 0.0, 0.0, 0.0])
    v = np.array([0.0, 0.0, 0.0, 0.0])
    dz = 10.0
    g = 9.81
    rg = 0.25
    nz = 4
    
    t_out, s_out, d_out, u_out, v_out = PWP.grad_mix(t, s, d, u, v, dz, g, rg, nz)
    assert len(t_out) == nz
