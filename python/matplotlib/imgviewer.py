#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhenyu@gmail.com
# @Date:   2017-03-29 15:26:25
# @About imgviewer.py

import os
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def plot_samples(data_folders, sample_size, title=None):
    fig = plt.figure()
    if title:
        fig.suptitle(title, fontsize=16, fontweight='bold')
    for folder in data_folders:
        image_files = os.listdir(folder)
        image_sample = random.sample(image_files, sample_size)
        for image in image_sample:
            image_file = os.path.join(folder, image)
            ax = fig.add_subplot(len(data_folders), sample_size,
                    sample_size * data_folders.index(folder) + image_sample.index(image) + 1)
            image = mpimg.imread(image_file)
            ax.imshow(image)
            ax.set_axis_off()
    plt.show()

train_folders = './'
test_folders = './'

plot_samples(train_folders, 10, 'Train folder')
plot_samples(test_folders, 10, 'Test folder')
