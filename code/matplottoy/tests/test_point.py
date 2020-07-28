from types import SimpleNamespace

import pytest 
import numpy as np 
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.testing.decorators import check_figures_equal

from matplottoy.artists import point
import matplottoy.datasources.array as da
import matplottoy.datasources.dataframe as dsf

from matplottoy.tests.utils import check_axes_property


class TestPoint:
    def test_missing_required(self):
        ds = SimpleNamespace(encodings={'x':1})
        with pytest.raises(ValueError):
            point.Point(ds)

    def test_wrong_optional(self):
        ds = SimpleNamespace(encodings={'x':1, 'y':2, 'apples':3})
        with pytest.raises(ValueError):
            point.Point(ds)

class TestArray:
    @pytest.fixture(autouse=True)
    def data(self):
        values = np.tile([1.,2.,.03,5.], 
                          reps=100).reshape(100,4)
        self.arr = np.cumsum(values, axis=0)

    @check_figures_equal(extensions=['png'])
    def test_point_no_params(self, fig_test, fig_ref):
        ds = da.ArrayPoint(self.arr)
        info = ds.view().info
        xlim = (info['x']['min'], info['x']['max'])
        ylim = (info['y']['min'], info['y']['max'])

        ax_test = fig_test.subplots()
        artist_test = point.Point(ds)
        ax_test.add_artist(artist_test) 
        ax_test.set(xlim=xlim, ylim=ylim)
        ax_test.set_aspect('equal')

        ax_ref = fig_ref.subplots()
        ax_ref.scatter(self.arr[:,0], self.arr[:,1], 
                        color='C0', ec='k')
        ax_ref.set(xlim=xlim, ylim=ylim)
        ax_ref.set_aspect('equal')
        check_axes_property(ax_test, ax_ref)

    @check_figures_equal(extensions=['png'])
    def test_point_required(self, fig_test, fig_ref):
        ds = da.ArrayPoint(self.arr, 
                    encodings={'x':1, 'y':0})
        info = ds.view().info

        xlim = (info['x']['min'], info['x']['max'])
        ylim = (info['y']['min'], info['y']['max'])

        ax_test = fig_test.subplots()
        artist_test = point.Point(ds)
        ax_test.add_artist(artist_test) 
        ax_test.set(xlim=xlim, ylim=ylim)
        ax_test.set_aspect('equal')

        ax_ref = fig_ref.subplots()
        ax_ref.scatter(self.arr[:,1], self.arr[:,0], 
                        color='C0', ec='k')
        ax_ref.set(xlim=xlim, ylim=ylim)
        ax_ref.set_aspect('equal')
        check_axes_property(ax_test, ax_ref)

    @check_figures_equal(extensions=['png'])
    def test_point_optional(self, fig_test, fig_ref):
        ds = da.ArrayPoint(self.arr, 
                    encodings={'x':1, 'y':0, 's':3})
        info = ds.view().info

        xlim = (info['x']['min'], info['x']['max'])
        ylim = (info['y']['min'], info['y']['max'])

        ax_test = fig_test.subplots()
        artist_test = point.Point(ds)
        ax_test.add_artist(artist_test) 
        ax_test.set(xlim=xlim, ylim=ylim)
        ax_test.set_aspect('equal')

        ax_ref = fig_ref.subplots()
        ax_ref.scatter(self.arr[:,1], self.arr[:,0], 
                color='C0', ec='k', s=self.arr[:,3])
        ax_ref.set(xlim=xlim, ylim=ylim)
        ax_ref.set_aspect('equal')
        check_axes_property(ax_test, ax_ref)

class TestDataFrame:
    @pytest.fixture(autouse=True)
    def data(self):
        self.df = pd.DataFrame(np.cumsum(np.tile([1.,2.,.03,5.], reps=100).reshape(100,4), axis=0), 
                        columns = ['odds', 'evens','threes', 'fives'])

    @check_figures_equal(extensions=['png'])
    def test_point_no_params(self, fig_test, fig_ref):
        ds = dsf.DataFramePoint(self.df)
        info = ds.view().info
        xlim = (info['x']['min'], info['x']['max'])
        ylim = (info['y']['min'], info['y']['max'])

        ax_test = fig_test.subplots()
        artist_test = point.Point(ds)
        ax_test.add_artist(artist_test) 
        ax_test.set(xlim=xlim, ylim=ylim)
        ax_test.set_aspect('equal')

        ax_ref = fig_ref.subplots()
        ax_ref.scatter(self.df['odds'], self.df['evens'], 
                        color='C0', ec='k')
        ax_ref.set(xlim=xlim, ylim=ylim)
        ax_ref.set_aspect('equal')
        check_axes_property(ax_test, ax_ref)

    @check_figures_equal(extensions=['png'])
    def test_point_required(self, fig_test, fig_ref):
        ds = dsf.DataFramePoint(self.df, 
               encodings={'x':'odds', 'y':'fives'})
        info = ds.view().info

        xlim = (info['x']['min'], info['x']['max'])
        ylim = (info['y']['min'], info['y']['max'])

        ax_test = fig_test.subplots()
        artist_test = point.Point(ds)
        ax_test.add_artist(artist_test) 
        ax_test.set(xlim=xlim, ylim=ylim)
        ax_test.set_aspect('equal')

        ax_ref = fig_ref.subplots()
        ax_ref.scatter(self.df['odds'], self.df['fives'], 
                        color='C0', ec='k')
        ax_ref.set(xlim=xlim, ylim=ylim)
        ax_ref.set_aspect('equal')
        check_axes_property(ax_test, ax_ref)

    @check_figures_equal(extensions=['png'])
    def test_point_optional(self, fig_test, fig_ref):
        ds = dsf.DataFramePoint(self.df, 
                           encodings={'x':'fives', 'y':'evens', 's':'threes'})
        info = ds.view().info

        xlim = (info['x']['min'], info['x']['max'])
        ylim = (info['y']['min'], info['y']['max'])

        ax_test = fig_test.subplots()
        artist_test = point.Point(ds)
        ax_test.add_artist(artist_test) 
        ax_test.set(xlim=xlim, ylim=ylim)
        ax_test.set_aspect('equal')

        ax_ref = fig_ref.subplots()
        ax_ref.scatter(self.df['fives'], self.df['evens'], 
                        color='C0', ec='k', 
                        s=self.df['threes'])
        ax_ref.set(xlim=xlim, ylim=ylim)
        ax_ref.set_aspect('equal')
        check_axes_property(ax_test, ax_ref)