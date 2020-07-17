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
        print(self.datasource.data.shape)
        print(self.array.shape)
        axt = fig_test.subplots()
        imd = ap.Image(axt, self.datasource, origin="lower")
        axt.add_image(imd)
    
        fig_test.colorbar(imd, ax=axt)

        axr = fig_ref.subplots()
        im = axr.imshow(self.array, origin="lower")
        fig_test.colorbar(im, ax=axr)
        pass

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
    
    