import matplotlib.pyplot as plt
import numpy as np

# code parameters
n_plot = 100

# model parameters
y0 = .001
m0 = .25
a_opt = 4.*m0
a_sub = 2.*a_opt

@np.vectorize
def y(t,a):
    """fraction of population that has been infected by time t"""
    return y0*np.exp(a*t)/(y0*np.exp(a*t)+(1.-y0))

def y_prime(t,a):
    """derivative of y with respect to t"""
    return a*y(t,a)*(1.-y(t,a))

def peak_time(a):
    """time at which y_prime attains its maximum of a/4 (when y=1/2)"""
    return np.log((1.-y0)/y0)/a 

t_plot = np.linspace(0.,2.*peak_time(a_opt),n_plot) 

plt.plot(t_plot,m0+0.*t_plot,'-k')
plt.plot(t_plot,y_prime(t_plot,a_sub))
plt.plot(t_plot,y_prime(t_plot,a_opt))
plt.xticks([peak_time(a_sub),peak_time(a_opt)],['$T(a)$','$T(a_{m})$'])
plt.yticks([m0,a_sub/4.],['$m$','$a/4$'])
plt.xlabel("time: $t$")
plt.ylabel("frequency of infections: $y'(t)$")
plt.xlim([min(t_plot),max(t_plot)])
plt.legend(['medical capacity $m$','contact rate $a$','optimal contact rate $a_{m}=4m$'])
plt.grid()
plt.show()
