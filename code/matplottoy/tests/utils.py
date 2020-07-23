"""
Commonly used test helpers
"""
def check_axes_property(ax_test, ax_ref):

    assert ax_test.get_xlim() == ax_ref.get_xlim()
    assert ax_test.get_ylim() == ax_ref.get_ylim()
    assert ax_test.get_aspect() == ax_ref.get_aspect()

    assert (ax_test.get_position().bounds == 
            ax_ref.get_position().bounds)
    assert (ax_test.get_window_extent().bounds ==
            ax_ref.get_window_extent().bounds)