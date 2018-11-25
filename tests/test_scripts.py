#!/usr/bin/env python
import pytest
import subprocess


def test_latitude():
    pytest.importorskip('matplotlib')
    subprocess.check_call(['IRIlatitudeProfile', '-148'])


def test_time():
    pytest.importorskip('matplotlib')
    subprocess.check_call(['IRItimeProfile', '65', '-148'])


def test_alt():
    pytest.importorskip('matplotlib')
    subprocess.check_call(['IRIaltitudeProfile', '65', '-148'])


if __name__ == '__main__':
    pytest.main(['-xv', __file__])
