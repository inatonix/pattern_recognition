import numpy as np
import matplotlib.tri as tri
import matplotlib.pyplot as plt

if __name__ == '__main__':
    corners = np.array([[0,0],[1,0],[0.5, 0.75**0.5]])
    triangle = tri.Triangulation(corners[:,0],corners[:,1])
    refiner = tri.UniformTriRefiner(triangle)

    trimesh = refiner.refine_triangulation(subdiv=4)
    plt.figure(figsize=(8,4))

    for (i, mesh) in enumerate((triangle, trimesh)):
        plt.subplot(1, 2, i+ 1)
        plt.triplot(mesh)
        plt.axis('off')
        plt.axis('equal')

    plt.show()