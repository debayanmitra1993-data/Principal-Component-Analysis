# Principal Component Analysis

## About 
PCA performs orthogonal transformation on the feature space by projecting the points onto an alternate orthogonal dimension space. These are called Principal Components. The Principal Components are obtained in a way that maximizes the variance of the data points in the PC feature space.

## Principal Components
The Principal Components are basically the Eigen Vectors of the Mean centered Covariance Matrix of the original dataset. The corresponding Eigen Values represent the variance explained in the new PC space. 

## Dimensionality Reduction
Dimensionality Reduction is performed by projecting the data points onto the Principal Component Feature space. The % variance preserved in the new transformed co-ordinate system is given by the cumulative sum normalized of the eigen values in the PC space (after sorting the Eigen values in descending order) 
