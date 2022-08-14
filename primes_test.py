# -*- coding: utf-8 -*-
import pytest
from typing import List, Text
from primes import alg1, alg2_1, alg2_2, alg3, alg4, alg5

@pytest.mark.timeout(60)
@pytest.mark.skip()
def test_alg1(inputs: List[Text], outputs: List[Text]):
    assert alg1(int(inputs[0])) == int(outputs[0])

@pytest.mark.timeout(60)
@pytest.mark.skip()
def test_alg2_1(inputs: List[Text], outputs: List[Text]):
    assert alg2_1(int(inputs[0])) == int(outputs[0])

@pytest.mark.timeout(60)
@pytest.mark.skip()
def test_alg2_2(inputs: List[Text], outputs: List[Text]):
    assert alg2_2(int(inputs[0])) == int(outputs[0])

@pytest.mark.timeout(60)
@pytest.mark.skip()
def test_alg3(inputs: List[Text], outputs: List[Text]):
    assert alg3(int(inputs[0])) == int(outputs[0])

@pytest.mark.timeout(60)
@pytest.mark.skip()
def test_alg4(inputs: List[Text], outputs: List[Text]):
    assert alg4(int(inputs[0])) == int(outputs[0])

#@pytest.mark.timeout(60)
#@pytest.mark.skip()
def test_alg5(inputs: List[Text], outputs: List[Text]):
    assert alg5(int(inputs[0])) == int(outputs[0])
