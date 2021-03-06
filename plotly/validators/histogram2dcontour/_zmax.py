import _plotly_utils.basevalidators


class ZmaxValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='zmax', parent_name='histogram2dcontour', **kwargs
    ):
        super(ZmaxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            implied_edits={'zauto': False},
            role='info',
            **kwargs
        )
