#!/usr/bin/env python
from numpy import *
from matplotlib import pyplot as plt
from scipy import signal

# Setup
tau = 5.0 * 60    # 5 minutes
t_max = 60 * 30.0  # 30 minute experiment
dt = 10.0

### Using the lti class from scipy.signal ###
# Define a first-order LTI system
sys = signal.lti(1, [1, 1.0 / tau])

# Plot its step response with step method
h_times = arange(0, t_max, dt)

step_response = sys.step(T=h_times)[1]
plt.plot(h_times, step_response / step_response.max())    # normalize
plt.axhline(0.63, color='red')  # mark time constant
plt.axvline(tau, color='red')
plt.xlabel('t')
plt.ylabel('h(t)')
plt.title('Step response')

# Plot its impulse response with impulse method
plt.figure()
plt.plot(h_times, sys.impulse(T=h_times)[1], label='Using step method')
plt.xlabel('t')
plt.ylabel('h(t)')
plt.title('Impulse response')

### Defining our own 1st order LTI system ###
def h(t, tau):
    """Impulse response of first-order LTI system.
    Args:
        h   array of time values
        tau time constant
    """
    h = exp(-t / tau)
    h[t < 0] = 0.0
    return h

plt.plot(h_times, h(h_times,tau), color='green', marker='.', ls='', 
        label='Using h(t)')
plt.xlabel('t')
plt.ylabel('h(t)')
plt.title('Impulse response')
plt.legend(loc='best')

# Define a sampled step function
x_times = arange(-t_max, t_max, dt)
step = zeros(len(x_times))
step[len(step)/2:] = 1.0

plt.figure()
plt.plot(x_times, step, color='black', label='step fn')

# Convolve step function with impulse response
step_response = convolve(h(h_times, tau), step, mode='valid')
plt.plot(h_times, step_response[:-1]/step_response.max(), color='green',
        marker='.', label='step response')
plt.xlabel('t')
plt.ylabel('h(t)')
plt.title('Step response')

# Deconvolve to recover original signal
h_array = h(h_times, tau)

# Pad step_response(t) to be longer than h(t)
step_response = concatenate([zeros(len(h_times)), step_response,
    ones(len(h_times))])

x_reconstructed = signal.deconvolve(step_response, h_array)

x_len = len(step_response) - len(h_times) + 1
x_reconstructed_times = arange(-dt*x_len/2, dt*(x_len/2-1), dt)

plt.plot(x_reconstructed_times, x_reconstructed[0][:-1], color='blue', ls='',
        marker='s', label='recovered step fn')
plt.legend(loc='best')
plt.show()
