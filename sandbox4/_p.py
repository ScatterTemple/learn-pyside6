__all__ = ['_dummy']
class _Dummy:
    def __init__(self):
        self.pid = 1
        self.prj = r'c:\some\file.prj'
        self.pid = 'some-model'

    def get_prm_names(self):
        return ['p1', 'p2', 'p3']

    def get_prm_expressions(self):
        return [1, 'p1+p2', '3.1415926563']

    def get_output_names(self):
        return ['out1', 'out2', 'out3', 'out4']

_dummy = _Dummy()
