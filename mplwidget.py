from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplWidget(FigureCanvasQTAgg):

    def __init__(self, parent=None):
        # self.setParent(parent) optional
        fig = Figure(figsize=(10, 10))
        super(MplWidget, self).__init__(fig)
