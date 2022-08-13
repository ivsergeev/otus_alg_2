# -*- coding: utf-8 -*-
import pytest
from math import isclose
from typing import List, Text
from power import alg1, alg2, alg3

@pytest.mark.timeout(60)
#@pytest.mark.skip()
def test_alg1(inputs: List[Text], outputs: List[Text]):
    assert isclose(alg1(float(inputs[0]), int(inputs[1])), float(outputs[0],), rel_tol=0.00000001)

@pytest.mark.timeout(60)
#@pytest.mark.skip()
def test_alg2(inputs: List[Text], outputs: List[Text]):
    assert isclose(alg2(float(inputs[0]), int(inputs[1])), float(outputs[0]), rel_tol=0.00000001)

@pytest.mark.timeout(60)
#@pytest.mark.skip()
def test_alg3(inputs: List[Text], outputs: List[Text]):
    assert isclose(alg2(float(inputs[0]), int(inputs[1])), float(outputs[0]), rel_tol=0.00000001)
