"""
Tests for lib.primes.
"""

from lib.primes import Pi


def test_Pi():
    pi = Pi(10000).pi
    assert pi(1000) == 168
    assert pi(1003) == 168
    assert pi(1009) == 169
    pi = Pi(10 ** 9).pi
    assert pi(10 ** 5) == 9592
    assert pi(1000002) == 78498
    assert pi(1000004) == 78499
    assert pi(1000003) == 78499
    assert pi(10 ** 8) == 5761455
    pi = Pi(10 ** 12).pi
    assert pi(10 ** 11) == 4118054813
    assert pi(5 * 10 ** 11) == 19308136142
