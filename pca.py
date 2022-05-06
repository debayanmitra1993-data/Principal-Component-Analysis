import numpy as np

class PCA:

  def __init__(self, dim = None):
    self.eigenvalues = []
    self.eigenvectors = []


  def fit(self,X):
    X = np.array(X)
    for dimidx in range(X.shape[1]):
      X[:,dimidx] = X[:,dimidx] - np.mean(X[:,dimidx])
    S = (1/(X.shape[0] - 1))*np.matmul(X.T,X)
    w,v = np.linalg.eig(S)
    for idx in np.argsort(w)[::-1]:
      self.eigenvalues.append(w[idx])
      self.eigenvectors.append(v[:,idx])

  def transform(self,X):
    X = np.array(X)
    for dimidx in range(X.shape[1]):
      X[:,dimidx] = X[:,dimidx] - np.mean(X[:,dimidx])
    X_ = []
    for rowidx in range(X.shape[0]):
      X_.append(np.matmul(self.eigenvectors, X[rowidx]))
    return np.array(X_)

  def get_var_explained(self,num_components):
    return round(np.sum(self.eigenvalues[:num_components])/np.sum(self.eigenvalues),4)
