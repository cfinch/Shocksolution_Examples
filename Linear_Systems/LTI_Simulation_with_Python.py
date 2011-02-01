#!/usr/bin/env python
from numpy import *
from matplotlib import pyplot as plt
from scipy import signal

def h(t, tau):
    """Impulse response of first-order LTI system."""
    h = exp(-t/tau)
    h[t<0] = 0.0
    return h

tau = 5.0*60    # 5 minutes
t_max = 60*30.0  # 30 minute experiment
dt = 10.0

sys = signal.lti(1,[1,1.0/tau])     # First-order LTI system

h_times = arange(0, t_max, dt)
x_times = arange(-t_max, t_max, dt)

step_response = sys.step(T=h_times)[1]
plt.plot(h_times, step_response/step_response.max())    # normalize to max value of 1
plt.axhline(0.63, color='red')
plt.axvline(tau, color='red')
plt.xlabel('t')
plt.title('Step response')

plt.show()

step = zeros(len(x_times))
step[len(step)/2:] = 1.0
plt.plot(x_times, step, color='black')

y = convolve(h(h_times, tau), step, mode='valid')
plt.plot(h_times, y[:-1]/y.max(), color='green', marker='o')

# Deconvolve to recover original signal
h_array = h(h_times, tau)

# Pad y(t) to be longer than h(t)
# This should not be necessary for real data where the experimental run time is much
# longer than impulse response of the sensor.
y = concatenate([zeros(len(h_times)), y, ones(len(h_times))])

x_reconstructed = signal.deconvolve(y, h_array)

x_len = len(y) - len(h_times) + 1
x_reconstructed_times = arange(-dt*x_len/2, dt*(x_len/2-1), dt)

plt.plot(x_reconstructed_times, x_reconstructed[0][:-1], color='blue', ls='', marker='s')

# Plot impulse response
#plt.figure()
#plt.plot(h_times, sys.impulse(T=h_times)[1])
#plt.xlabel('t')
#plt.title('Impulse response')
#
#plt.plot(h_times, h(h_times,tau), color='green', marker='o', ls='')

plt.show()
