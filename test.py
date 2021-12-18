import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

grafik = plt.figure()
sumbu = plt.axes(projection='3d')


# def f(x, y):
#     z = x ** 2 + y ** 2 + 25 * (np.sin(x) ** 2 + np.sin(y) ** 2)
#     return z


# x = np.linspace(-2 * np.pi, 2 * np.pi, 25)
# y = np.linspace(-2 * np.pi, 2 * np.pi, 25)
# X, Y = np.meshgrid(x, y)
# Z = f(X, Y)
# sumbu.plot_surface(X, Y, Z, cmap='viridis')


def main():
    print('Bat Algorithm')
    print('---------------------------\n')
    batAlgorithm(1200)


# Define the test function
def fungUji(x, y):
    # The test function is eggcrate function
    z = x ** 2 + y ** 2 + 25 * (np.sin(x) ** 2 + np.sin(y) ** 2)
    return z


def batAlgorithm(n=10, A=0.25, r=0.5):
    # Parameters:
    #   n = population of bats
    #   A = Loudness
    #   r = Pulse rate

    # Frequency range to determine the scale
    # Lowest frequency
    Qmin = 0
    # Highest frequency
    Qmax = 2

    # Loop parameters
    tol = 10 ** (-5)
    # number of iterations
    N_iter = 0

    # Search space dimension
    d = 2

    # Initial array of values
    # the frequency of each bat
    Q = np.zeros(n)
    # the speed of each bat in each dimension
    v = np.zeros((n, d))

    # Assignment of initial values in bat populations (solution)
    # position of each bat
    Sol = np.zeros((n, d))
    # temporary position
    S = np.zeros((n, d))
    # value of the test function of each bat
    Fitness = np.zeros(n)

    fmin = 1
    best = 0
    # The application of the Bat Algorithm
    while fmin > tol:
        # loops imposed on all bats
        for i in range(n):
            beta = np.random.rand()
            Q[i] = Qmin + (Qmax - Qmin) * beta
            v[i, :] = v[i, :] + (Sol[i, :] - best) * Q[i]
            S[i, :] = Sol[i, :] + v[i, :]

            # pulse rate effect
            alpha = 0.01
            if np.random.rand() > r:
                S[i, :] = best + alpha * np.random.randn(1, d)

            # calculate the new solution
            x = S[i, 0]
            y = S[i, 1]
            Fnew = fungUji(x, y)

            # if the new solution is better and the loudness decreases
            if Fnew <= Fitness[i] and np.random.rand() < A:
                Sol[i, :] = S[i, :]
                Fitness[i] = Fnew

            # update the smallest / best test function value
            if Fnew < fmin:
                best = S[i, :]
                fmin = Fnew

        N_iter = N_iter + n

    print('Number of iterations = ', N_iter)
    print('Best Position = ', best)
    print('Lowest test function = ', fmin)
    print('The final position of all bats = ')
    for i in range(n):
        print(' ', i + 1, Sol[i, :])


if __name__ == '__main__':
    main()
