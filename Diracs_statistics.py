import numpy as np
#a given b
a = "student really knows the material"
b = "student answers question correctly"

p_a = .6
p_b_given_a = 1-0.15
#0.85
p_b_given_not_a = 0.20
p_b = (p_b_given_a*p_a)+(p_b_given_not_a*(1-p_a))
p_a_given_b = (p_b_given_a*p_a)/p_b
print p_a_given_b