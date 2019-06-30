#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import colors

class Colormap(colors.ListedColormap):
    def __init__(self, c, name='from_list', n=None):
        '''Initialization'''
        self._colors = c
        self._name = name
        self._N = n

        # call parent __init__
        super(Colormap, self).__init__(self._colors, name=self._name, N=self._N)

    def __getitem__(self, item):
        return Colormap(self._colors[item], name='sliced_' + self._name)

    def show(self):
        import matplotlib.pyplot as plt
        a = np.outer(np.ones(10), np.arange(0, 1, 0.001))
        plt.figure(figsize=(2.5, 0.5))
        plt.subplots_adjust(top=0.95, bottom=0.05, left=0.01, right=0.99)
        plt.subplot(111)
        plt.axis('off')
        plt.imshow(a, aspect='auto', cmap=self, origin='lower')
        plt.text(0.5, 0.5, self._name,
                 verticalalignment='center', horizontalalignment='center',
                 fontsize=12, transform=plt.gca().transAxes)
        plt.show()
cmp = ['#A8A8A8', '#812089', '#A817B0', '#F098EF', '#010090',
     '#6868C8', '#C8C8E0', '#1FA021', '#70D06F', '#B0F1B1',
     '#DFE000', '#E89008', '#C78121', '#C0712F', '#D00000',
     '#A00000', '#383838', '#A8A8A8']
a=Colormap(cmp)
a.show()