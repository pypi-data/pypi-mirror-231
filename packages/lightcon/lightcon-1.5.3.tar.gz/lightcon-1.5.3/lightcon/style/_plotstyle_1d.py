import matplotlib.pyplot as plt
import scilightcon.plot

def apply_style():
    scilightcon.plot.apply_style()

def reset():
    scilightcon.plot.reset_style()

def add_watermarks():
    """Adds watermarks to all subplots of the current figure"""
    scilightcon.plot.add_watermarks(plt.gcf())

def add_watermark(ax, target='axis', loc='lower left'):
    """Add watermark to current axis or figure

    Args:
        ax (:obj:`str`): Axis object (not relevant if target=='figure')
        target (:obj:`str`): Draw axis for the whole 'figure' (default) or 'axis'
        loc (:obj:`str`): Location of the watermark ('upper right'|'upper left'|'lower left'|'lower right'|'center left'|'center right'|'lower center'|'upper center'|'center').
            Default value is 'center' when target=='figure' and 'lower left' for target=='axis'
    """
    file_name = str(Path(__file__).parent) + '\\lclogo.png'
    img = Image.open(file_name)
    
    if target == 'axis':
        scilightcon.plot.add_watermark(ax)
        
    if target == 'figure':
        scilightcon.plot.add_watermark(plt.gcf())