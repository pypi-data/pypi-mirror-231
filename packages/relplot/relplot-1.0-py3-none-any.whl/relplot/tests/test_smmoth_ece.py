import pytest
import numpy as np


from sklearn.linear_model import LogisticRegressionCV
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

from ..metrics import smECE_slow, smECE_fast, smooth_ece, smooth_ece_interpolated
from ..kernels import smooth_round_to_grid

EPS = 0.001

@pytest.fixture(params=[1,2,3,4,5,6])
def logistic_fy(request):
    np.random.seed(request.param)
    x, y = make_classification(n_samples = 50000, n_features=5, n_informative=3, n_redundant=2)
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=1000)
    model = LogisticRegressionCV()
    model.fit(x_train, y_train)
    f_train = model.predict_proba(x_train)[:,1]
    f_test = model.predict_proba(x_test)[:,1]
    return [(f_train, y_train), (f_test, y_test)]

@pytest.fixture
def small_fy():
    f0 = np.array([0.15845153, 0.18352692, 0.32189059, 0.48730361])
    f1 = np.array([0.30953839, 0.5, 0.74037771, 0.77163793])
    f_small = np.concatenate((f0, f1))
    y_small = np.array([0] * len(f0) + [1] * len(f1))
    return (f_small, y_small)

@pytest.fixture
def sigma():
    return 0.2

def ensure_equal(f, y):
    assert np.abs(smECE_slow(f, y) -  smECE_fast(f, y)) < EPS

def test_small(small_fy):
    (f_small, y_small) = small_fy
    ensure_equal(f_small, y_small)

def test_logistic_scipy(logistic_fy):
    for f,y in logistic_fy:
        ensure_equal(f,y)

def test_smooth_ece_small(small_fy, sigma):
    (f, y) = small_fy
    num_eval_points = 2000
    r_values = smooth_round_to_grid(f, f - y, eval_points=num_eval_points) / len(f)
    value = smooth_ece_interpolated(r_values, sigma)
    assert np.abs(value - smooth_ece(f,y, sigma)) < 0.001

def test_smooth_ece_logistic(logistic_fy, sigma):
    num_eval_points = 2000
    for f,y in logistic_fy:
        r_values = smooth_round_to_grid(f, f - y, eval_points=num_eval_points) / len(f)
        value = smooth_ece_interpolated(r_values, sigma)
        assert np.abs(value - smooth_ece(f,y,sigma)) < 0.001
