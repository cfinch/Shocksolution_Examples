#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal

# Filter parameters
cutoff = 0.2
numtaps = 100
order = 4       # IIR

# Input signal
x = np.concatenate([np.ones(100), np.ones(100) * 10.0])  # nonzero step function

# FIR LPF
lpf = scipy.signal.firwin(numtaps, cutoff, window=('hamming'))

# Compute and plot frequency response
lpf_freq, lpf_response = scipy.signal.freqz(lpf)

plt.figure()
plt.suptitle('FIR filter frequency response')
plt.subplot(2,1,1)
plt.plot(lpf_freq, np.abs(lpf_response), marker='.')
plt.xlabel('f/f0')
plt.ylabel('Abs')

plt.subplot(2,1,2)
plt.plot(lpf_freq, np.unwrap(np.angle(lpf_response)), marker='.')
plt.xlabel('f/f0')
plt.ylabel('Angle')

# Filter signal, no initial conditions
y1 = scipy.signal.lfilter(lpf, [1.0], x)

plt.figure()
plt.title('Signal, filtered with FIR')
plt.plot(y1)
plt.xlabel('t')
plt.ylabel('y(t)')

# Filter signal, using initial conditions
zi = scipy.signal.lfiltic(lpf, [1.0], [1.0], np.ones(len(lpf)-1))
y, zf = scipy.signal.lfilter(lpf, [1.0], x, zi=zi)
plt.plot(y)

# IIR LPF
butterworth = scipy.signal.butter(order, cutoff, btype='lowpass')
butterworth_freq, butterworth_response = scipy.signal.freqz(butterworth[0], butterworth[1])

plt.figure()
plt.suptitle('IIR filter frequency response')
plt.subplot(2,1,1)
plt.plot(butterworth_freq, scipy.signal.abs(butterworth_response), marker='.', label='abs')
plt.xlabel('f/f0')
plt.ylabel('Abs')

plt.subplot(2,1,2)
plt.plot(butterworth_freq, np.unwrap(np.angle(butterworth_response)), marker='.', label='arg')
plt.xlabel('f/f0')
plt.ylabel('Angle')

# Filter signal, no initial conditions
y = scipy.signal.lfilter(butterworth[0], butterworth[1], x)

plt.figure()
plt.title('Signal, filtered with IIR filter')
plt.plot(y)

# Filter signal, using initial conditions
zi = scipy.signal.lfilter_zi(butterworth[0], butterworth[1])
y, zf = scipy.signal.lfilter(butterworth[0], butterworth[1], x, zi=zi)
plt.plot(y)

plt.show()
