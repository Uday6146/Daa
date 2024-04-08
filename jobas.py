import numpy as np
from scipy.optimize import linear_sum_assignment
cost_mat=np.array([13,18,16,18,19],
                  [9,15,24,9,12],
                  [12,9,4,4,4],
                  [6,12,10,8,13],
                  [15,17,18,12,20])
row_ind,col_ind=linear_sum_assignment(cost_matrix)
opt_ass=col-ind
tc=cost_mat[row_ind,col_ind].sum()
print(opt_ass)
print("cost:",tc)