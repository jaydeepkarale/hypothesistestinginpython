from hypothesis import given, settings
from hypothesis import given, example
import hypothesis.strategies as strategy
from src.crossbrowser_selenium import CrossBrowserSetup
import pytest

@pytest.mark.hypothesis
@settings(deadline=None)
@given(strategy.just("Firefox"))
#@given(strategy.just("Chrome"))
def test_add(browsertype_1):
    cbt = CrossBrowserSetup()
    assert True == cbt.add(browsertype_1)
