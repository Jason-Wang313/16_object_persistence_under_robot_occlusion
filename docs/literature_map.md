# Literature Map

## Sweep Protocol
- Landscape sweep: 1000 records in `docs/related_work_matrix.csv`.
- Serious skim: top 300 records by relevance score, using title, venue, concepts, citations, and abstract when available.
- Deep read: top 230 records were processed with the full extraction schema from metadata and abstracts.
- Hostile prior-work set: top 100 records by hostile score, emphasizing occlusion, object persistence, amodal perception, tracking, maps, and manipulation.
- Retrieval source: OpenAlex API where possible; any fallback records are explicitly marked in the matrix.

## Coverage Counts
- tracking: 256
- mapping_slam: 87
- pose_manipulation: 574
- amodal: 1
- active_perception: 175
- object_world_models: 25
- robot_self_occlusion_explicit: 140
- offline_fallback: 0

## Field Box
The field box is robot perception for persistent object state under partial observability, especially the boundary between object tracking, object-centric mapping, pose tracking during manipulation, amodal perception, active perception, and embodied world models.

## Twenty-Four Hidden Assumptions That May Be False
1. A missed detection has one generic meaning rather than a cause tied to robot geometry.
2. The robot body is treated as a nuisance mask, not as a predictable intervention on visibility.
3. Objects are either visible or absent; self-occluded persistence is rarely a first-class state.
4. Camera viewpoint changes are exogenous instead of commanded by the embodied agent.
5. Manipulation and perception are evaluated on frames where the robot is conveniently out of the way.
6. Occlusion statistics are assumed independent of the policy that moves the robot.
7. The duration of invisibility is fixed by a tracker hyperparameter rather than robot kinematics.
8. Free-space evidence is conflated with missing-pixel evidence.
9. Object deletion is usually symmetric with object creation.
10. Hidden support, containment, and contact constraints are ignored during self-occlusion.
11. The robot's own links are assumed perfectly segmented or simply removed.
12. Pose trackers assume enough visible texture or geometry remains during interaction.
13. Maps assume revisits resolve uncertainty before the object becomes task-critical.
14. Amodal methods assume training labels teach hidden extent, not action-caused observability.
15. Benchmarks often decouple perception from the robot motion that creates occlusion.
16. Multi-object trackers assume camera occluders are external scene actors.
17. World models are often rewarded for prediction, not for preserving action-relevant object slots.
18. State estimators assume the observation model is fixed across actions.
19. Robots are evaluated after occlusion ends, hiding failures during the decision interval.
20. Task planners assume the perception stack reports whether an object still exists.
21. Domain randomization is expected to cover occlusion geometry without changing the estimator.
22. Uncertainty is added after the fact rather than changing the persistence mechanism.

## Candidate Directions That Break Assumptions
- **Action-conditioned occlusion certificates:** Use the robot's own commanded geometry as evidence explaining missed detections, changing deletion and persistence rules rather than adding generic uncertainty.
- **Counterfactual clear-view absence:** Delete object state only after a robot-action model certifies that the relevant line of sight was clear enough for a detection to have occurred.
- **Self-occlusion stress tests for manipulation:** Evaluate state persistence during the decision interval when the arm hides the target, not only after the object reappears.
- **Kinematic visibility budgets:** Replace fixed tracker TTLs with visibility budgets computed from the robot's planned motion and sensor geometry.
- **Contact-aware persistence:** Use contact and support constraints to decide whether a hidden object could have moved during robot-caused invisibility.

## Top Prior-Work Neighborhood
- Rank 1: A Dexterous Hand-Arm Teleoperation System Based on Hand Pose Estimation and Active Vision (2022). Mechanism: Learned visual representation or sequence model trained from labeled experience. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 2: Mesh-based Dynamics with Occlusion Reasoning for Cloth Manipulation (2022). Mechanism: Pose registration, keypoint, correspondence, or dense alignment mechanism. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 3: Detection of Coconut Clusters Based on Occlusion Condition Using Attention-Guided Faster R-CNN for Robotic Harvesting (2022). Mechanism: Learned visual representation or sequence model trained from labeled experience. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 4: Occlusion-Based Cooperative Transport with a Swarm of Miniature Mobile Robots (2015). Mechanism: Pose registration, keypoint, correspondence, or dense alignment mechanism. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 5: Visual-Tactile Fusion for 3D Objects Reconstruction from a Single Depth View and a Single Gripper Touch for Robotics Tasks (2021). Mechanism: View selection or information-gain planning to expose hidden state. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 6: Towards Confidence-guided Shape Completion for Robotic Applications (2022). Mechanism: Learned visual representation or sequence model trained from labeled experience. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 7: Real-Time Generative Grasping with Spatio-temporal Sparse Convolution (2023). Mechanism: Task-specific perception model over partial observations. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 8: Can the robot "see" what I see? Robot gaze drives attention depending on mental state attribution (2023). Mechanism: Task-specific perception model over partial observations. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 9: An application of stereo matching algorithm based on transfer learning on robots in multiple scenes (2023). Mechanism: Pose registration, keypoint, correspondence, or dense alignment mechanism. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 10: Real-time neural network prediction for handling two-hands mutual occlusions (2019). Mechanism: Learned visual representation or sequence model trained from labeled experience. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 11: Learning Keypoints for Robotic Cloth Manipulation Using Synthetic Data (2024). Mechanism: Geometric map optimization over poses, landmarks, or object states. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 12: Mobile Manipulation Integrating Enhanced AMCL High-Precision Location and Dynamic Tracking Grasp (2020). Mechanism: Learned visual representation or sequence model trained from labeled experience. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 13: World model learning and inference (2021). Mechanism: View selection or information-gain planning to expose hidden state. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 14: Development of a sweet pepper harvesting robot (2020). Mechanism: Geometric map optimization over poses, landmarks, or object states. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 15: Autonomously Untangling Long Cables (2022). Mechanism: View selection or information-gain planning to expose hidden state. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 16: 3D-Anchored Lookahead Planning for Persistent Robotic Scene Memory via World-Model-Based MCTS (2026). Mechanism: Learned visual representation or sequence model trained from labeled experience. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 17: Communication Within Multi-FSM Based Robotic Systems (2018). Mechanism: Pose registration, keypoint, correspondence, or dense alignment mechanism. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 18: Mobile robotics platform for strawberry sensing and harvesting within precision indoor farming systems (2023). Mechanism: Learned visual representation or sequence model trained from labeled experience. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 19: Supervised Autonomy for Exploration and Mobile Manipulation in Rough Terrain with a Centaur-Like Robot (2016). Mechanism: Pose registration, keypoint, correspondence, or dense alignment mechanism. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
- Rank 20: Drone swarm strategy for the detection and tracking of occluded targets in complex environments (2023). Mechanism: Pose registration, keypoint, correspondence, or dense alignment mechanism. Leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
