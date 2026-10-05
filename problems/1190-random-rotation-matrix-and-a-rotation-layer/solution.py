import numpy as np

def rotation_layer(X, angle):
    rot_mat = np.array([[np.cos(angle),-np.sin(angle)],
                        [np.sin(angle),np.cos(angle)]])
    
    for i,point in enumerate(X):
        X[i] = np.dot(rot_mat,point)
    
    return X
