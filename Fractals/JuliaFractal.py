# Author: reDragonCoder

# Julia fractal: a subset of julia fractal. While generating a julia fractal, we changed the values of C and with 
# Z0 = 0. But for generating a Julia fractal the value of C is kept constant throughout the execution and Z is varied. 
# For different values of C, different Julia fractals are formed.

# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Function
def julia(n_rows, n_columns, iterations, cx, cy):
    x_cor=np.linspace(-2, 2, n_rows)
    y_cor=np.linspace(-2, 2, n_columns)
    x_len=len(x_cor)
    y_len=len(y_cor)
    output=np.zeros((x_len, y_len))
    c=complex(cx, cy) 
    for i in range(x_len):
        for j in range(y_len):
            z=complex(x_cor[i], y_cor[j])
            count=0
            for k in range(iterations):
                z=(z*z)+c
                count+=1
                if(abs(z)>4):
                    break
            output[i, j]=count
            print((i/x_len)*100, "%"+" completed")
    print(output)
    plt.imshow(output.T, cmap="prism")
    plt.axis("off")
    plt.show()

# Execution
julia(1000, 1000, 120, -0.8, 0.156)