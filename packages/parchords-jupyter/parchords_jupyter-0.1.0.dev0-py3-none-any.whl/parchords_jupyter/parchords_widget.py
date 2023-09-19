#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Alexander Rind & the SoniVis team.
# Distributed under the terms of the MIT License (see LICENSE).

"""
jupyter widget that shows a parallel coordinates plot and fires an event with filtered data whenever the plot is clicked
"""

from ipywidgets import DOMWidget, CallbackDispatcher, register
from traitlets import Unicode, Instance, List, Int, Float, observe, validate, TraitError
from ._frontend import module_name, module_version
import pandas as pd
import numpy as np


class ParChordsWidget(DOMWidget):
    """
    jupyter widget that shows a parallel coordinates plot and fires an event with filtered data whenever the plot is clicked
    """
    _model_name = Unicode('ParChordsModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('ParChordsView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    width = Int(700).tag(sync=True)
    """ width of the widget's substrate (i.e., the area between axes, where marks are plotted) """
    height = Int(400).tag(sync=True)
    """ height of the widget's substrate (i.e., the area between axes, where marks are plotted) """
    color_field = Unicode('').tag(sync=True)
    """ column name used for a categorical color encoding. While it is an empty string all marks are rendered in the same color. """
    axis_fields = List(Unicode()).tag(sync=True)
    """ column names used for a axis coordinates. It is reset whenever data is set. """
    data = Instance(klass=pd.DataFrame)
    """ pandas dataframe to be displayed """

    _marks_val = List(List(Float())).tag(sync=True)
    """ internal data with numberic column values to be used for coordinate positions as list of items/rows """
    _marks_color = List(Unicode()).tag(sync=True)
    """ internal data with mark color category as column vector. Entries do not contain the color but original values. """

    def __init__(self, data=None, **kwargs):
        super().__init__(**kwargs)
        self._axis_click_handlers = CallbackDispatcher()
        self.on_msg(self._handle_frontend_msg)

        # if isinstance(data, pd.DataFrame) == True:
        if data is None:
            self.data = pd.DataFrame()
        else:
            self.data = data

    @validate('axis_fields')
    def _valid_axis_fields(self, proposal):
        # print('## PCP ## check axis fields ')
        numeric_cols = self.data.select_dtypes(include='number').columns.values.tolist()
        # print(proposal['value'])
        # print(len(proposal['value']))
        if not (len(proposal['value']) == 0 or all(col in numeric_cols for col in proposal['value'])):
            raise TraitError('Some axis fields are not a column of the data frame.')
        return proposal['value']

    @validate('color_field')
    def _valid_color_field(self, proposal):
        if not (proposal['value'] == '' or proposal['value'] in self.data):
            raise TraitError(
                'The color field is not a column of the data frame.')
        return proposal['value']

    @observe('data')
    def _observe_data(self, change):
        # print('## PCP ## update data')

        # reset axis fields to all numeric columns
        self.axis_fields = change.new.select_dtypes(include='number').columns.values.tolist()

        # might not be necessary because done by observer
        if not len(self.axis_fields) == 0:
            self._marks_val = change.new[self.axis_fields].values.tolist()

    @observe('color_field')
    def _observe_color_field(self, change):
        # print('## PCP ## update field ' + change.name + ' to ' + change.new)
        if change.new != '':
            self._marks_color = self.data[change.new].astype(str).tolist()
        else:
            self._marks_color = []

    @observe('axis_fields')
    def _observe_fields(self, change):
        # print('## PCP ## update field ' + change.name + ' to ' + change.new)
        if len(change.new) != 0:
            self._marks_val = self.data[change.new].values.tolist()
        else:
            self._marks_val = []

    def on_axis_click(self, callback, remove=False):
        """Register a callback to execute when the lens widget is released (i.e. the touch has ended).
        The callback will be called with no arguments.
        Parameters
        ----------
        remove: bool (optional)
            Set to true to remove the callback from the list of callbacks.
        """
        self._axis_click_handlers.register_callback(callback, remove=remove)

    def axis_click(self, event: str, field: str):
        self._axis_click_handlers(self, field)

    def _handle_frontend_msg(self, _widget, payload, _buffers):
        """Handle a msg from the front-end.
        Parameters
        ----------
        payload: dict
            Content of the msg.
        """
        if payload.get('event', '') == 'axis_click':
            self.axis_click(**payload)
