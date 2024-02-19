# R-sqaured Matrix
def r_squared(actual, predicted):
    mean_actual = sum(actual) / len(actual)
    ss_total = sum((x - mean_actual) ** 2 for x in actual)
    ss_residual = sum((x - y) ** 2 for x, y in zip(actual, predicted))
    return 1 - (ss_residual / ss_total)

# Mean Squared Error (MSE) Matrix
def mean_squared_error(actual, predicted):
    return sum((x - y) ** 2 for x, y in zip(actual, predicted)) / len(actual)

# Root Mean Squared Error (RMSE) Matrix
def root_mean_squared_error(actual, predicted):
    mse = mean_squared_error(actual, predicted)
    return mse ** 0.5

# Mean Absolute Error (MAE) Matrix
def mean_absolute_error(actual, predicted):
    return sum(abs(x - y) for x, y in zip(actual, predicted)) / len(actual)

# Mean Absolute Relative Error (MARE) Matrix
def mean_absolute_relative_error(actual, predicted):
    return sum(abs((x - y) / x) for x, y in zip(actual, predicted)) / len(actual)

# Mean Square Relative Error (MSRE) Matrix
def mean_square_relative_error(actual, predicted):
    return sum(((x - y) / x) ** 2 for x, y in zip(actual, predicted)) / len(actual)

# Root Mean Squared Relative Error (RMSRE) Matrix
def root_mean_squared_relative_error(actual, predicted):
    msre = mean_square_relative_error(actual, predicted)
    return msre ** 0.5

# Relative Root Mean Square Error (RRMSE) Matrix
def relative_root_mean_square_error(actual, predicted):
    rmse = root_mean_squared_error(actual, predicted)
    mean_actual = sum(actual) / len(actual)
    return (rmse / mean_actual) * 100

# Mean Bias Error (MBE) Matrix
def mean_bias_error(actual, predicted):
    return sum(x - y for x, y in zip(actual, predicted)) / len(actual)

# Maximum Absolute Relative Error Function
def max_absolute_relative_error(actual, predicted):
    return max(abs((x - y) / x) for x, y in zip(actual, predicted))

# Standard Deviation (SD) Matrix
def standard_deviation(values):
    mean_val = sum(values) / len(values)
    return (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5

# T-Statistic Matrix
def t_statistic(actual, predicted):
    mbe = mean_bias_error(actual, predicted)
    rmse = root_mean_squared_error(actual, predicted)
    return ((len(actual) - 1) * mbe ** 2) / (rmse ** 2 - mbe ** 2)


# Uncertainty at 95% (U95) Matrix
def uncertainty_at_95(actual, predicted):
    sd = standard_deviation(actual)
    rmse = root_mean_squared_error(actual, predicted)
    return 1.96 * (sd ** 2 + rmse ** 2) ** 0.5
