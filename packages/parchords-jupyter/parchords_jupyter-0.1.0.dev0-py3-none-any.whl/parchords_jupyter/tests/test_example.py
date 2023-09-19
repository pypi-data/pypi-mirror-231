#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Alexander Rind & the SoniVis team.
# Distributed under the terms of the MIT License (see LICENSE).

import pytest
import pandas as pd
from traitlets.traitlets import TraitError

from ..parchords_widget import ParChordsWidget


def test_example_creation_blank():
    w = ParChordsWidget()
    assert w.data.size == 0
    assert len(w._marks_val) == 0
    assert w.color_field == ''


def test_widget_create_other_datatype():
    with pytest.raises(TraitError):
        ParChordsWidget([1, 3])


df = pd.DataFrame({'var1': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
                   'var2': {0: 1, 1: 4, 2: 9, 3: 16, 4: 25}})


def test_example_creation_w_data():
    w = ParChordsWidget(df)
    assert w.data.size == df.size
    assert len(w._marks_val) == df.size


def test_example_creation_w_data():
    w = ParChordsWidget()
    w.data = df
    w.axis_fields = ['var1']
    assert w.data.size == df.size
    assert len(w._marks_val) == len(df.index)


def test_example_set_wrong_field():
    w = ParChordsWidget(df)
    with pytest.raises(TraitError):
        w.axis_fields = ['var5']
