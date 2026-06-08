def solution_analytique(a,b,p1,p2,p3,p4):

    #renvoie la valeur exacte de l'intégrale du polynome entre a et b

    primitive_b=p1*b+(p2/2)*(b**2)+(p3/3)*(b**3)+(p4/4)*(b**4)
    primitive_a=p1*a+(p2/2)*(a**2)+(p3/3)*(a**3)+(p4/4)*(a**4)

    #intégrale exacte est F(b)-F(a)
    aire_exacte=primitive_b-primitive_a

    return aire_exacte

