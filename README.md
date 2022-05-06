# Principal Component Analysis

## Files
**pca.py** contains the code to run PCA for your dataset <br/>
**pca_derivation.jpg** contains the detailed mathematical derivation of the solution space basis constrained optimization

## About 
PCA performs orthogonal transformation on the feature space by projecting the points onto an alternate orthogonal dimension space. These are called Principal Components. The Principal Components are obtained in a way that maximizes the variance of the data points in the PC feature space.

## Principal Components
The Principal Components are basically the Eigen Vectors of the Mean centered Covariance Matrix of the original dataset. The corresponding Eigen Values represent the variance explained in the new PC space. 

## Dimensionality Reduction
Dimensionality Reduction is performed by projecting the data points onto the Principal Component Feature space. The % variance preserved in the new transformed co-ordinate system is given by the cumulative sum normalized of the eigen values in the PC space (after sorting the Eigen values in descending order) 

## Obtaining the solutions of PCA
The PCA solutions (which are basically the unit vectors) are obtained by solving the Constrained Optimization equation that maximizes the variance over the 1st Principal Component subject to the constraint of unit vectors. This is solved using the Lagrange multipliers method which shows that the obtained unit vectors are basically the eigen vectors of the Covariance Matrix of the dataset. 
