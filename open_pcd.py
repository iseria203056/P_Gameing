import open3d as o3d
import numpy as np

threshold = 0.3
init = np.asarray([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

dst = o3d.io.read_point_cloud("dst.pcd")
src = o3d.io.read_point_cloud("src.pcd")
o = np.zeros((1,3))
origin = o3d.geometry.PointCloud()
print(o)
origin.points = o3d.utility.Vector3dVector(o)

reg_15 = o3d.registration.registration_icp(
        src, dst, threshold, init,
        o3d.registration.TransformationEstimationPointToPoint(),
        o3d.registration.ICPConvergenceCriteria(max_iteration = 50))

src.transform(reg_15.transformation)


dst.paint_uniform_color([1, 0, 0])
src.paint_uniform_color([0, 1, 0])



o3d.visualization.draw_geometries([dst, origin])

