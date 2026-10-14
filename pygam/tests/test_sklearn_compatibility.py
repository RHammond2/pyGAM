import pytest
from sklearn.utils.estimator_checks import check_estimator, parametrize_with_checks

from pygam.tests.utils.discovery import all_estimators


@pytest.mark.skip(reason="Further development work needed for full compliance")
@pytest.mark.parametrize("estimator", [el for _, el in all_estimators()])
def test_estimators_shallow(estimator):
    """
    check that the estimators are fully compatible with scikit-learn.
    """
    check_estimator(estimator())


@pytest.mark.skip(reason="Further development work needed for full compliance")
@parametrize_with_checks([est() for _, est in all_estimators()])
def test_estimators_full(estimator, check, request):
    """Check for full compliance with scikit-learn API"""
    check(estimator)
