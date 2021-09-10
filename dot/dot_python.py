import numpy as np
from numpy.lib.twodim_base import mask_indices


# [n,p]*[p,m]=[n,m]
def naive_dot(a: np.ndarray, b: np.ndarray):
    if a.shape[1] != b.shape[0]:
        raise ValueError('shape no matched')

    n, p, m = a.shape[0], a.shape[1], a.shape[1]
    c = np.zeros((n, m), dtype=np.float32)
    for i in range(n):
        for j in range(m):
            s = 0
            for k in range(p):
                s += a[i, k] * b[k, j]
            c[i, j] = s
    return c
if __name__=='__main__':
    a=np.random.randn(100,200).astype(np.float32)
    b=np.random.randn(200,500).astype(np.float32)
    ret=naive_dot(a,b)
    print(f'ret:{ret}')
