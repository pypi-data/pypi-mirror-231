#! /usr/bin/env python

from eclib.numutils import *
from eclib.randutils import *
from eclib.primeutils import *
from eclib.modutils import *
from collections import namedtuple
import numpy as np
from math import floor, ceil

def keygen(bit_length):
    """Key generation function

    Generate public parameters, a public key pk, and a secret key sk.
    Public parameters consists of a prime q of bit_length bit, a safe 
    prime p = 2 * q + 1, and a generator g of a plaintext space 
    M = {g^i mod p | i ∈ Zq}. A secret key is a random number s 
    uniformally sampled from Zq. A public key is h = g^s mod p.

    Parameters
    ----------
    bit_length : int
        Key length

    Returns
    -------
    params
        Public parameters
    pk : int
        Public key
    sk : int
        Secret key

    Examples
    -------
    >>> bit_length = 10
    >>> params, pk, sk = keygen(bit_length)
    >>> print(params.p, params.q, params.g)
    1523 761 3
    >>> print(pk)
    1027
    >>> print(sk)
    660

    """
    params = namedtuple('Parameters', ['p', 'q', 'g'])
    params.q, params.p = get_safe_prime(bit_length)
    params.g = get_generator(params.q, params.p)

    sk = get_rand(1, params.q)

    pk = mpow(params.g, sk, params.p)
    
    return params, pk, sk

def encrypt(params, pk, m):
    """Encryption function

    Encrypt a plaintext m using a public key pk. A ciphertext is 
    computed as c = (c1, c2) = (g^r mod p, m * h^r mod p), where r is 
    a rondom number uniformally sampled from Zq. For vectors and 
    matrices, encryption is performed for each element.

    Parameters
    ----------
    params
        Public parameters
    pk : int
        Public key
    m : int or array-like
        Plaintext

    Returns
    -------
    c : numpy.ndarray
        Ciphertext

    Examples
    -------
    >>> bit_length = 10
    >>> params, pk, sk = keygen(bit_length)
    >>> m = params.g
    >>> print(m)
    3
    >>> c = encrypt(params, pk, m)
    >>> print(c)
    [255 1147]

    """
    if isinstance(m, np.matrix) or isinstance(m, list):
        m = np.array(m)

    # scalar
    if isinstance(m, int):
        return _encrypt(params, pk, m)
    # vector
    elif isinstance(m[0], int):
        c = np.zeros(m.shape, dtype=object)
        for i in range(c.shape[0]):
            c[i] = _encrypt(params, pk, m[i])
        return c
    # matrix
    elif isinstance(m[0][0], int):
        c = np.zeros(m.shape, dtype=object)
        for i in range(c.shape[0]):
            for j in range(c.shape[1]):
                c[i][j] = _encrypt(params, pk, m[i][j])
        return c
    else:
        print('error: encryption')
        return None

def decrypt(params, sk, c):
    """Decryption function

    Decrypt a ciphertext c = (c1, c2) using a secret key sk. 
    A decrypted message is computed as m = c1^-sk * c2 mod p. 
    For vectors and matrices, decryption is performed for each element.

    Parameters
    ----------
    params
        Public parameters
    sk : int
        Secret key
    c : array-like
        Ciphertext

    Returns
    -------
    m : int or numpy.ndarray
        Plaintext

    Examples
    -------
    >>> bit_length = 10
    >>> params, pk, sk = keygen(bit_length)
    >>> m = params.g
    >>> print(m)
    3
    >>> c = encrypt(params, pk, m)
    >>> m_ = decrypt(params, sk, c)
    >>> print(m_)
    3

    """
    if isinstance(c, np.matrix) or isinstance(c, list):
        c = np.array(c)

    # scalar
    if isinstance(c[0], int):
        return _decrypt(params, sk, c)
    # vector
    elif isinstance(c[0][0], int):
        m = np.zeros(c.shape, dtype=object)
        for i in range(m.shape[0]):
            m[i] = _decrypt(params, sk, c[i])
        return m
    # matrix
    elif isinstance(c[0][0][0], int):
        m = np.zeros(c.shape, dtype=object)
        for i in range(m.shape[0]):
            for j in range(m.shape[1]):
                m[i][j] = _decrypt(params, sk, c[i][j])
        return m
    else:
        print('error: decryption')
        return None

def mult(params, c1, c2):
    """Multiplication function

    Parameters
    ----------
    params
        Public parameters
    c1 : array-like
        Ciphertext
    c2 : array-like
        Ciphertext

    Returns
    -------
    c : numpy.ndarray
        Ciphertext
    """
    if isinstance(c1, np.matrix) or isinstance(c1, list):
        c1 = np.array(c1)
    if isinstance(c2, np.matrix) or isinstance(c2, list):
        c2 = np.array(c2)

    # scalar x scalar
    if isinstance(c1[0], int) and isinstance(c2[0], int):
        return _mult(params, c1, c2)
    # scalar x vector
    elif isinstance(c1[0], int) and isinstance(c2[0][0], int):
        c = np.zeros(c2.shape, dtype=object)
        for i in range(c.shape[0]):
            c[i] = _mult(params, c1, c2[i])
        return c
    # scalar x matrix
    elif isinstance(c1[0], int) and isinstance(c2[0][0][0], int):
        c = np.zeros(c2.shape, dtype=object)
        for i in range(c.shape[0]):
            for j in range(c.shape[1]):
                c[i][j] = _mult(params, c1, c2[i][j])
        return c
    # vector x vector
    elif isinstance(c1[0][0], int) and isinstance(c2[0][0], int) and c1.shape == c2.shape:
        c = np.zeros(c1.shape, dtype=object)
        for i in range(c1.shape[0]):
            c[i] = _mult(params, c1[i], c2[i])
        return c
    # matrix x vector
    elif isinstance(c1[0][0][0], int) and isinstance(c2[0][0], int) and c1.shape[1] == c2.shape[0]:
        c = np.zeros(c1.shape, dtype=object)
        for i in range(c.shape[0]):
            for j in range(c.shape[1]):
                c[i][j] = _mult(params, c1[i][j], c2[j])
        return c
    # matrix x matrix
    elif isinstance(c1[0][0][0], int) and isinstance(c2[0][0][0], int) and c1.shape[1] == c2.shape[0]:
        c = np.zeros(c1.shape, dtype=object)
        for i in range(c.shape[0]):
            for j in range(c.shape[1]):
                c[i][j] = _mult(params, c1[i][j], c2[i][j])
        return c
    else:
        print('error: multiplication')
        return None

def encode(params, x, delta, mode='nearest'):
    """Encoding function

    Scale up a real number x dividing by a scaling factor delta, 
    and then encode it to the nearest plaintext m. For vectors and 
    matrices, encoding is performed for each element.

    Parameters
    ----------
    params
        Public parameters
    x : float or array-like
        Real number
    delta : float
        Scaling factor
    mode : str, optional
        'nearest' or 'lower' or 'upper', by default 'nearest'

    Returns
    -------
    m : int or numpy.ndarray
        Plaintext

    Examples
    -------
    >>> bit_length = 10
    >>> params, pk, sk = keygen(bit_length)
    >>> delta = 1e-2
    >>> x = 1.23
    >>> m = encode(params, x, delta)
    >>> print(m)
    122

    """
    f = np.frompyfunc(_encode, 4, 1)
    return f(params, x, delta, mode)

def decode(params, m, delta):
    """Decoding function

    Scale down a plaintext m by multiplying a scaling factor delta, 
    and then decode it to the nearest real number x. For vectors and 
    matrices, decoding is performed for each element.

    Parameters
    ----------
    params
        Public parameters
    m : int or array-like
        Plaintext
    delta : float
        Scaling factor

    Returns
    -------
    x : float or numpy.ndarray
        Real number

    Examples
    -------
    >>> bit_length = 10
    >>> params, pk, sk = keygen(bit_length)
    >>> delta = 1e-2
    >>> x = 1.23
    >>> m = encode(params, x, delta)
    >>> x_ = decode(params, m, delta)
    >>> print(x_)
    1.22

    """
    f = np.frompyfunc(_decode, 3, 1)
    return f(params, m, delta)

def enc(params, pk, x, delta, mode='nearest'):
    """Encoding and Encryptin function

    Scale up a real number x by dividing a scaling factor delta, and 
    then encode it to the nearest plaintext. After that encrypt the 
    plaintext using a public key pk. For vectors and matrices, 
    encoding is performed for each element.

    Parameters
    ----------
    params
        Public parameters
    pk : int
        Public key
    x : float
        Real number
    delta : float
        Scaling factor
    mode : str, optional
        'nearest' or 'lower' or 'upper', by default 'nearest'

    Returns
    -------
    c : numpy.ndarray
        Ciphertext

    Examples
    -------
    >>> bit_length = 10
    >>> params, pk, sk = keygen(bit_length)
    >>> delta = 1e-2
    >>> x = 1.23
    >>> c = enc(params, pk, x, delta)
    >>> print(c)
    [113 733]

    """
    return encrypt(params, pk, encode(params, x, delta, mode))

def dec(params, sk, c, delta):
    """Decryption and Decoding function

    Decrypt a ciphertext c using a secret key sk. After that scale 
    down the decrypted message by multiplying a scaling factor delta, 
    and then decode it to the nearest real number. For vectors and 
    matrices, decoding is performed for each element.

    Parameters
    ----------
    params
        Public parameters
    sk : int
        Secret key
    c : array-like
        Ciphertext
    delta : float
        Scaling factor

    Returns
    -------
    x : float or numpy.ndarray
        Real number

    Examples
    -------
    >>> bit_length = 10
    >>> params, pk, sk = keygen(bit_length)
    >>> delta = 1e-2
    >>> x = 1.23
    >>> c = enc(params, pk, x, delta)
    >>> x_ = dec(params, sk, c, delta)
    >>> print(x_)
    1.24

    """
    return decode(params, decrypt(params, sk, c), delta)

def dec_add(params, sk, c, delta):
    """Decryption, decoding, and summation function

    Parameters
    ----------
    params
        Public parameters
    sk : int
        Secret key
    c : array-like
        Ciphertext
    delta : float
        Scaling factor

    Returns
    -------
    x : float or numpy.ndarray
        Real number
    """
    if isinstance(c, np.matrix) or isinstance(c, list):
        c = np.array(c)

    # scalar
    if isinstance(c[0], int):
        return dec(params, sk, c, delta)
    # vector
    elif isinstance(c[0][0], int):
        x = dec(params, sk, c, delta)
        for i in range(1, x.shape[0]):
            x[0] += x[i]
        return x[0]
    # matrix
    elif isinstance(c[0][0][0], int):
        x = dec(params, sk, c, delta)
        for i in range(x.shape[0]):
            for j in range(1, x.shape[1]):
                x[i][0] += x[i][j]
        return x[:,0]
    else:
        print('error: decryption with addition')
        return None

def _encrypt(params, pk, m):
    r = get_rand(1, params.q)
    return np.array([mpow(params.g, r, params.p), (m * mpow(pk, r, params.p)) % params.p], dtype=object)

def _decrypt(params, sk, c):
    return (minv(mpow(c[0], sk, params.p), params.p) * c[1]) % params.p

def _mult(params, c1, c2):
    return np.array([(c1[0] * c2[0]) % params.p, (c1[1] * c2[1]) % params.p], dtype=object)

def _encode(params, x, delta, mode):
    if mode == 'nearest':
        m = floor(x / delta + 0.5)
        first_decimal_place = (x / delta * 10) % 10

        if m < 0:
            if m < -params.q:
                print('error: underflow')
                return None
            else:
                m += params.p
        elif m > params.q:
            print('error: overflow')
            return None

        if x / delta == int(x / delta) or first_decimal_place >= 5:
            for i in range(params.q):
                if m - i > 0 and is_element(m - i, params.q, params.p):
                    return m - i
                elif m + i < params.p and is_element(m + i, params.q, params.p):
                    return m + i
        else:
            for i in range(params.q):
                if m + i < params.p and is_element(m + i, params.q, params.p):
                    return m + i
                elif m - i > 0 and is_element(m - i, params.q, params.p):
                    return m - i
            
            print('error: encoding')
            return None
    
    elif mode == 'lower':
        m = ceil(x / delta)

        if m <= 0:
            if m < -params.q:
                print('error: underflow')
                return None
            else:
                m += params.p
        elif m > params.q:
            print('error: overflow')
            return None

        for i in range(m):
            if is_element(m - i, params.q, params.p):
                return m - i
        
        print('error: encoding')
        return None
    
    elif mode == 'upper':
        m = ceil(x / delta)

        if m < 0:
            if m < -params.q:
                print('error: underflow')
                return None
            else:
                m += params.p
        elif m > params.q:
            print('error: overflow')
            return None

        for i in range(params.p - m):
            if is_element(m + i, params.q, params.p):
                return m + i

        print('error: encoding')
        return None

    else:
        print('error: encoding')
        return None

def _decode(params, m, delta):
    return (m - params.p) * delta if m > params.q else m * delta
