# -*- coding: utf-8 -*-
import pytest
from typing import List, Text
from fibo import alg1, alg2, alg3

@pytest.mark.timeout(60)
@pytest.mark.skip()
def test_alg1(inputs: List[Text], outputs: List[Text]):
    assert alg1(int(inputs[0])) == int(outputs[0])

@pytest.mark.timeout(60)
@pytest.mark.skip()
def test_alg2(inputs: List[Text], outputs: List[Text]):
    assert alg2(int(inputs[0])) == int(outputs[0])

@pytest.mark.timeout(60)
@pytest.mark.skip()
def test_alg3(inputs: List[Text], outputs: List[Text]):
    assert alg3(int(inputs[0])) == int(outputs[0])