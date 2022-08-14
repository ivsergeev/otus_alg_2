# -*- coding: utf-8 -*-
import pytest
from typing import List, Text
from fibo import alg1, alg2, alg3, alg4

MAX_TIMEOUT = 300

@pytest.mark.timeout(MAX_TIMEOUT)
@pytest.mark.skip()
def test_alg1(inputs: List[Text], outputs: List[Text]):
    assert alg1(int(inputs[0])) == int(outputs[0])

@pytest.mark.timeout(MAX_TIMEOUT)
@pytest.mark.skip()
def test_alg2(inputs: List[Text], outputs: List[Text]):
    assert alg2(int(inputs[0])) == int(outputs[0])

@pytest.mark.timeout(MAX_TIMEOUT)
@pytest.mark.skip()
def test_alg3(inputs: List[Text], outputs: List[Text]):
    assert alg3(int(inputs[0])) == int(outputs[0])

#@pytest.mark.timeout(MAX_TIMEOUT)
#@pytest.mark.skip()
def test_alg4(inputs: List[Text], outputs: List[Text]):
    assert alg4(int(inputs[0])) == int(outputs[0])
