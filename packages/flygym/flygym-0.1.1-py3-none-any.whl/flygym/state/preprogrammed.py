from flygym.util.data import data_path
from flygym.state import KinematicPose

stretched_pose = KinematicPose.from_yaml(data_path / "pose/pose_stretch.yaml")
zero_pose = KinematicPose.from_yaml(data_path / "pose/pose_zero.yaml")
walking_pose = KinematicPose.from_yaml(data_path / "pose/pose_default.yaml")
