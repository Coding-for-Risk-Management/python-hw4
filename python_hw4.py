import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# qSLR1
def MyLM(formula, data):
    fit = None  # populate the smf.ols function using the formula and fit it
    return fit


# qSLR2
def PlotSLRCI():
    # Plot the data
    # Plot the lower confidence interval
    # Plot the upper confidence interval
    return None


# qTMat1
def TMAT1(vec1, vec2):
    pass


# qTMat2
def Forecast_nPeriod(vec, tmat, n):
    # Use a loop to multiply tmat by itself n times
    # Placeholder for the student work:
    # Start with the identity matrix as neutral element for multiplication
    out = np.eye(tmat.shape[0])
    for _ in range(n):
        out = np.dot(out, tmat)  # Matrix multiplication

    # Multiply the resulting matrix by the initial vector to get the state distribution n periods ahead
    # Placeholder for the student work:
    out = np.dot(vec, out)

    return out


# qTmat2Bonus
def Forecast_nPeriod_Recursive(vec, mat, n):
    # Use a function that calls itself n times
    # The final result is the n period ahead forecast
    pass


# qBondDuration
def getBondDuration(y, face, couponRate, m, ppy=1):
    # your work here
    duration = None  # Placeholder
    return duration


# qGetReturnsLag
def getReturns(pricevec, lag=1):
    # Calculate the returns based on the given lag
    # YOUR WORK HERE
    returns = None  # Placeholder
    return returns


# qVAR
def PercentVaR(r, alpha):
    # This function returns the left tail value and displays a histogram
    # alpha = risk level
    # r = a vector of stock returns
    # out = positively stated value of r at the 1-alpha percentile

    plt.hist(r, bins=50)
    plt.show()

    # Get the lower tail value and return its absolute value
    # Placeholder for student work:
    out = None  # Placeholder for student work
    return out


# qES
def ES(losses, alpha=None, VaR=None):
    # losses = positively stated loss values
    # alpha = risk level e.g. 99%
    # VaR = either a dollar value or a percent

    # Calculate Expected Shortfall based on the given parameters
    if VaR is not None:
        # Use the provided VaR to calculate Expected Shortfall
        # Placeholder for student work: calculate the average of all losses greater than VaR
        out = None  # Placeholder for student work
    else:
        # Calculate VaR at the given alpha percentile if VaR is not provided
        VaR = np.percentile(losses, 100 * (1 - alpha))
        # Then calculate Expected Shortfall as the average of losses exceeding this VaR
        out = losses[losses > VaR].mean()

    return out
