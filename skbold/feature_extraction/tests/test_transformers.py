from __future__ import absolute_import, division, print_function

import os.path as op
from ...core import MvpWithin
from ... import testdata_path
from skbold.feature_extraction import *


testfeats = [op.join(testdata_path, 'run1.feat'),
             op.join(testdata_path, 'run2.feat')]


mvp_within = MvpWithin(source=testfeats, read_labels=True,
                       remove_contrast=[], invert_selection=False,
                       ref_space='epi', beta2tstat=True, remove_zeros=False,
                       mask=None)

mvp_within.create()


def test_array_permuter():

    transf = ArrayPermuter()
    transf.fit(mvp_within.X, mvp_within.y)
    transf.transform(mvp_within.X)


def test_cluster_threshold():

    transf = ClusterThreshold(mvp=mvp_within, min_score=2)
    transf.fit(mvp_within.X, mvp_within.y)
    transf.transform(mvp_within.X)


def test_pattern_averager():

    transf = PatternAverager()
    transf.fit(mvp_within.X, mvp_within.y)
    transf.transform(mvp_within.X)


def test_pca_filter():

    transf = PCAfilter()
    transf.fit(mvp_within.X, mvp_within.y)
    transf.transform(mvp_within.X)
