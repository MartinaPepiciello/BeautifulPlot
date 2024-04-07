from matplotlib.colors import LinearSegmentedColormap
from matplotlib import pyplot as plt
import numpy as np


sequential = [LinearSegmentedColormap.from_list("colorado", ['darkorange', 'gold', 'lawngreen', 'lightseagreen']),
              LinearSegmentedColormap.from_list("fairytale", ['#f5b0e9', '#9cbaff', '#acf2d1']),
              LinearSegmentedColormap.from_list("mediterranean", ['#abd655', '#f1c550', '#fa701b']),
              LinearSegmentedColormap.from_list("moonshadow", ['#06cdff', '#9424ff', '#f39800']),
              LinearSegmentedColormap.from_list("unicorn", ['#ff967d', '#e56cff', '#61f7d5', '#eaff00'])
              ]

cyclic = [LinearSegmentedColormap.from_list("magicka", ['#d60080', '#5bc2c0', '#ebac42', '#d60080']),
          LinearSegmentedColormap.from_list("jungle", ['#6ecd2f', '#bf9871', '#cfdc00', '#6ecd2f']),
          LinearSegmentedColormap.from_list("pastel rainbow", ['#a4ffde', '#d8ff60', '#ffb3b8', '#e8a9ff', '#a4ffde']),
          LinearSegmentedColormap.from_list("wonder", ['#ff967d', '#e56cff', '#61f7d5', '#eaff00', '#ff967d']),
          LinearSegmentedColormap.from_list("light sunset", ['#ffada2', '#ffcc60', '#fff000', '#ffcc60', '#ffada2']),
          LinearSegmentedColormap.from_list("laguna", ['#6bf4b8', '#bff234', '#f0f300', '#bff234', '#6bf4b8'])
          ]
