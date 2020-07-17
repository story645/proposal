import pytest 
import numpy as np 

import matplotlib.pyplot as plt
from matplotlib.testing.decorators import check_figures_equal

import matplottoy.artists.artists as ap
import matplottoy.datasources.array as da

class TestArray: 
    @pytest.fixture(autouse=True)
    def data(self):
        self.array =  np.tile(np.arange(13),10).reshape(10,13)
        self.datasource = da.DataSourceArray(self.array)

    @check_figures_equal(extensions=['png'])
    def test_image(self, fig_test, fig_ref):
        axt = fig_test.subplots()
        imd = ap.Image(axt, self.datasource, origin="lower")
        axt.add_image(imd)
        axt.set_aspect(1.0)
        fig_test.colorbar(imd, ax=axt)
        fig_test.canvas.draw()

        axr = fig_ref.subplots()
        im = axr.imshow(self.datasource.data, origin="lower")
        axt.set_aspect(1.0)
        fig_ref.colorbar(im, ax=axr)
        fig_ref.canvas.draw()

        assert axt.get_xlim() == axr.get_xlim()
        assert axt.get_ylim() == axr.get_ylim()
        assert axt.get_aspect() == axr.get_aspect()
        assert imd.get_extent() == im.get_extent()
        assert imd.zorder == im.zorder
        assert (axt.get_position().bounds == 
                axr.get_position().bounds)
        assert (axt.get_window_extent().bounds ==
                axr.get_window_extent().bounds)
        assert (imd.get_window_extent().bounds ==
                im.get_window_extent().bounds)


    @pytest.mark.skip()
    @check_figures_equal(extensions=['png'])
    def test_line(self, fig_test, fig_ref):
        pass
    
    @pytest.mark.skip()
    @check_figures_equal(extensions=['png'])
    def test_bar_grouped(self, fig_test, fig_ref):
        pass
    
    @pytest.mark.skip()
    @check_figures_equal(extensions='png')
    def test_bar_stacked(self, fig_test, fig_ref):
        pass
    
    