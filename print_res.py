#!/usr/bin/env python3.3
## print.py for  in /home/tetard/EPITECH_Y2/maths/202unsold
## 
## Made by benjamin girard
## Login   <tetard@epitech.net>
## 
## Started on  Mon Feb 27 17:46:43 2017 benjamin girard
## Last update Mon Feb 27 18:14:03 2017 benjamin girard
##

from calc import sum_proba, expected_val, variance

def print_distrib_res(proba_res):
    res = []
    print("z\t20\t30\t40\t50\t60\t70\t80\t90\t100\ttotal")
    print("p(Z=z)\t", end='')
    for nb in range(20, 110, 10):
        res.append(sum_proba(proba_res, nb))
        print("%0.3f\t" % res[-1], end='')
    print("1")
    return res

def print_sum_res(proba_res):
    z_res = {"x": [], "y": []}
    print("----------------------------------------")
    print("\tX=10\tX=20\tX=30\tX=40\tX=50\tY law")
    for y, x_dict in proba_res.items():
        print("Y={y}\t".format(y=y), end='')
        for key, x in x_dict.items():
            print("{x}\t".format(x="%0.3f" % x), end='')
        z_res["y"].append(sum(x_dict.values()))
        print("{law}".format(law="%0.3f" % sum(x_dict.values())))
    print("X law\t", end='')
    z_res["x"].append(sum([proba_res[10][10], proba_res[20][10], proba_res[30][10],
                                proba_res[40][10], proba_res[50][10]]))
    z_res["x"].append(sum([proba_res[10][20], proba_res[20][20], proba_res[30][20],
                                proba_res[40][20], proba_res[50][20]]))
    z_res["x"].append(sum([proba_res[10][30], proba_res[20][30], proba_res[30][30],
                                proba_res[40][30], proba_res[50][30]]))
    z_res["x"].append(sum([proba_res[10][40], proba_res[20][40], proba_res[30][40],
                                proba_res[40][40], proba_res[50][40]]))
    z_res["x"].append(sum([proba_res[10][50], proba_res[20][50], proba_res[30][50],
                                proba_res[40][50], proba_res[50][50]]))
    for i in range(0, 5):
        print("{law}\t".format(law="%0.3f" % z_res["x"][i]), end='')
    print("1")
    print("----------------------------------------")
    return z_res

def print_exp_var(proba_res, z_res):
    print("----------------------------------------")
    print("expected value of X:\t%0.1f" % expected_val(z_res['x'], 10))
    print("variance of X:\t\t%0.1f" % variance(z_res['x'], 10))
    print("expected value of Y:\t%0.1f" % expected_val(z_res['y'], 10))
    print("variance of Y:\t\t%0.1f" % variance(z_res['y'], 10))
    print("expected value of Z:\t%0.1f" % expected_val(z_res['z'], 20))
    print("variance of Z:\t\t%0.1f" % variance(z_res['z'], 20))

    print("----------------------------------------")
