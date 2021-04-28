from urdf_parser_py.urdf import URDF
from kdl_parser import kdl_tree_from_urdf_model
from kdl_kinematics import KDLKinematics
import numpy as np
robot = URDF.from_xml_file("mm_hyu.urdf")
tree = kdl_tree_from_urdf_model(robot)
chain = tree[0].getChain("SPA_Base_Link","SPA_Link_06")
kdl_kin = KDLKinematics(robot, "SPA_Base_Link","SPA_Link_06")
q = kdl_kin.random_joint_angles()
print("random joint angle : ",q)
pose = kdl_kin.forward(q)
print("pose : ",pose)
q_ik = kdl_kin.inverse(pose, q+0.01)
print("inverse_kinematics : ",q_ik)
if q_ik is not None:
	pose_sol = kdl_kin.forward(q_ik) # should equal pose
	print("pose sol: ",pose_sol)
	print("pose: ",pose)
	print("sum of pose_error : ",np.sum(pose_sol-pose))

J = kdl_kin.jacobian(q)
print("Jacobian of q : ",J)
