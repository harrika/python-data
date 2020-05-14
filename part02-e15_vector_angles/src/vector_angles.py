#!/usr/bin/env python3

import numpy as np
import scipy.linalg
 
def vector_angles(X, Y):
    normx = scipy.linalg.norm(X, 2, axis=1)
    normy = scipy.linalg.norm(Y, 2, axis=1)
    print(f"x normalised:   {normx}")
    print(f"y normalised:  {normy}")
    
    gg = np.dot(X, Y) / (normx * normy)    
    # gg = np.inner(X, Y) / (normx * normy)    
    # gg = np.einsum('ij,ji', X, Y) / (normx * normy)    
    gg = gg.flatten()        
    rads = np.arccos(np.clip(gg, -1, 1))    
    degs = np.degrees(rads)
    print('in degrees:  ', degs) 
    return degs
 
def main():
    a = np.array([[0, 0, 1], [-1, 1, 0], [1, 1, 0]])
    b = np.array([[0, 1, 0], [1, 1, 0], [1, 1, 0]]) 
    print(vector_angles(a, b))
 
if __name__ == "__main__":
    main()