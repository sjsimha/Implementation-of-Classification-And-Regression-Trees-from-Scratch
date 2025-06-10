import numpy as np, BagLearner as bl, LinRegLearner as lrl
class InsaneLearner(object):
    def __init__(self, verbose=False):self.learners = list(bl.BagLearner(lrl.LinRegLearner, kwargs={}, bags=20, boost=False, verbose=verbose) for i in range(20))
    def author(self):return "ssimha31" # this could be removed by this class inheriting from BagLearner, however that doesn't seem like a logical relationship
    def add_evidence(self, data_x, data_y):return list(learner.add_evidence(data_x, data_y) for learner in self.learners) # note: list method only used to enable single line for-loop
    def query(self, points):return np.mean(np.array(list(learner.query(points) for learner in self.learners)), axis=0)