# Hostile Prior Work

This set is intentionally adversarial: each entry is treated as if a reviewer might claim it already solves the paper's problem.

## 1. A Dexterous Hand-Arm Teleoperation System Based on Hand Pose Estimation and Active Vision (2022)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: object absence can wait for later map revisits; enough object surface remains visible to constrain pose; the robot can afford extra sensing actions before acting; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; map update schedule; sensing cost model; occluder semantics
- Failure modes ignored: stale object map entries during manipulation; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Long-lived object memory in a spatial representation.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 2. Model-Based 3D Hand Pose Estimation from Monocular Video (2011)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 3. Mesh-based Dynamics with Occlusion Reasoning for Cloth Manipulation (2022)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 4. Object pose estimation and tracking by fusing visual and tactile information (2012)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 5. Point Tracking Improves World Action Models (2026)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 6. Tracking People in a Mobile Robot From 2D LIDAR Scans Using Full Convolutional Neural Networks for Security in Cluttered Environments (2019)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 7. Towards Confidence-guided Shape Completion for Robotic Applications (2022)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: enough object surface remains visible to constrain pose; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 8. Failure Handling of Robotic Pick and Place Tasks With Multimodal Cues Under Partial Object Occlusion (2021)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 9. Visibility Aware Human-Object Interaction Tracking from Single RGB Camera (2023)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 10. Real-Time Generative Grasping with Spatio-temporal Sparse Convolution (2023)
- Problem claimed: Improve robot or embodied perception under incomplete observations.
- Actual mechanism introduced: Task-specific perception model over partial observations.
- Hidden assumptions: the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; occluder semantics
- Failure modes ignored: confusing clear-view absence with robot-caused invisibility
- What it makes less novel: The broad claim that robots need memory under partial observability.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 11. Monocular Robust Depth Estimation Vision System for Robotic Tasks Interventions in Metallic Targets (2019)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Detection association plus temporal propagation across frames.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 12. Real-time neural network prediction for handling two-hands mutual occlusions (2019)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the robot can afford extra sensing actions before acting; training distribution covers relevant occlusion geometry; camera occlusion generalizes to robot-body occlusion
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; sensing cost model; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 13. Detection of Coconut Clusters Based on Occlusion Condition Using Attention-Guided Faster R-CNN for Robotic Harvesting (2022)
- Problem claimed: Build a spatial memory that remains useful as the robot moves through the world.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: object absence can wait for later map revisits; enough object surface remains visible to constrain pose; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; map update schedule; occluder semantics
- Failure modes ignored: stale object map entries during manipulation; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Long-lived object memory in a spatial representation.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 14. Learning Keypoints for Robotic Cloth Manipulation Using Synthetic Data (2024)
- Problem claimed: Build a spatial memory that remains useful as the robot moves through the world.
- Actual mechanism introduced: Geometric map optimization over poses, landmarks, or object states.
- Hidden assumptions: object absence can wait for later map revisits; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; map update schedule; occluder semantics
- Failure modes ignored: stale object map entries during manipulation; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Long-lived object memory in a spatial representation.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 15. Autonomously Untangling Long Cables (2022)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: View selection or information-gain planning to expose hidden state.
- Hidden assumptions: enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 16. Occlusion-Based Cooperative Transport with a Swarm of Miniature Mobile Robots (2015)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 17. Towards Stable Self-Supervised Object Representations in Unconstrained Egocentric Video (2026)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Recursive filtering with a motion and observation model.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 18. APUT: Large Language Models as Cross-Modal Consistency Reasoning Engines for Egocentric State Estimation (2026)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the robot can afford extra sensing actions before acting; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; sensing cost model; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 19. Drone swarm strategy for the detection and tracking of occluded targets in complex environments (2023)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 20. Tracking cloth deformation: A novel dataset for closing the sim-to-real gap for robotic cloth manipulation learning (2025)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 21. Toward Safer Autonomous Vehicles: Occlusion-Aware Trajectory Planning to Minimize Risky Behavior (2023)
- Problem claimed: Improve robot or embodied perception under incomplete observations.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 22. Learning Latent Graph Dynamics for Visual Manipulation of Deformable Objects (2022)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 23. Occlusion-aware Perception and Planning for Automated Vehicles (2023)
- Problem claimed: Build a spatial memory that remains useful as the robot moves through the world.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: object absence can wait for later map revisits; enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; map update schedule; occluder semantics
- Failure modes ignored: stale object map entries during manipulation; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Long-lived object memory in a spatial representation.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 24. Visceral exposure : Melanie Gilligan, Hito Steyerl, and the biopolitics of visibility (2016)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Geometric map optimization over poses, landmarks, or object states.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 25. A Novel Distribution for Representation of 6D Pose Uncertainty (2022)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 26. Pose-Assisted Multi-Camera Collaboration for Active Object Tracking (2020)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: View selection or information-gain planning to expose hidden state.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the robot can afford extra sensing actions before acting; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; sensing cost model; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 27. Object Permanence Filter for Robust Tracking with Interactive Robots (2024)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Recursive filtering with a motion and observation model.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the robot can afford extra sensing actions before acting; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; sensing cost model; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 28. Adaptive Body Scheme Models for Robust Robotic Manipulation (2008)
- Problem claimed: Improve robot or embodied perception under incomplete observations.
- Actual mechanism introduced: Task-specific perception model over partial observations.
- Hidden assumptions: the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; occluder semantics
- Failure modes ignored: confusing clear-view absence with robot-caused invisibility
- What it makes less novel: The broad claim that robots need memory under partial observability.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 29. Predictive Autonomy for UAV Remote Sensing: A Survey of Video Prediction (2025)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: View selection or information-gain planning to expose hidden state.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; the robot can afford extra sensing actions before acting; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; sensing cost model; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 30. Learning to Identify Object Instances by Touch: Tactile Recognition via Multimodal Matching (2019)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 31. Multi-view object pose distribution tracking for pre-grasp planning on mobile robots (2022)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: View selection or information-gain planning to expose hidden state.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 32. Development of an Aerial Manipulation System Using Onboard Cameras and a Multi-Fingered Robotic Hand with Proximity Sensors (2025)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Detection association plus temporal propagation across frames.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 33. HFF6D: Hierarchical Feature Fusion Network for Robust 6D Object Pose Tracking (2022)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 34. VI-RPE: Visual-Inertial Relative Pose Estimation for Aerial Vehicles (2018)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; object absence can wait for later map revisits; enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; map update schedule; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; stale object map entries during manipulation; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 35. Recurrent Volume-Based 3-D Feature Fusion for Real-Time Multiview Object Pose Estimation (2024)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Recursive filtering with a motion and observation model.
- Hidden assumptions: enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 36. MetaGraspNetV2: All-in-One Dataset Enabling Fast and Reliable Robotic Bin Picking via Object Relationship Reasoning and Dexterous Grasping (2023)
- Problem claimed: Infer the full or hidden object extent when visible pixels are incomplete.
- Actual mechanism introduced: Amodal completion from visible evidence and learned shape priors.
- Hidden assumptions: enough object surface remains visible to constrain pose; hidden extent can be inferred from category or shape priors; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: confident hallucination of an object that was actually removed; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Inferring hidden state from visible fragments.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 37. Mobile Manipulation Integrating Enhanced AMCL High-Precision Location and Dynamic Tracking Grasp (2020)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 38. World model learning and inference (2021)
- Problem claimed: Learn latent object state useful for prediction or control.
- Actual mechanism introduced: View selection or information-gain planning to expose hidden state.
- Hidden assumptions: enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 39. Multi-robot path planning for budgeted active perception with self-organising maps (2016)
- Problem claimed: Build a spatial memory that remains useful as the robot moves through the world.
- Actual mechanism introduced: View selection or information-gain planning to expose hidden state.
- Hidden assumptions: object absence can wait for later map revisits; enough object surface remains visible to constrain pose; the robot can afford extra sensing actions before acting; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; map update schedule; sensing cost model; occluder semantics
- Failure modes ignored: stale object map entries during manipulation; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Long-lived object memory in a spatial representation.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 40. Robust Hand Motion Tracking through Data Fusion of 5DT Data Glove and Nimble VR Kinect Camera Measurements (2015)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Recursive filtering with a motion and observation model.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; the robot can afford extra sensing actions before acting; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; sensing cost model; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 41. Self-Supervised Unseen Object Instance Segmentation via Long-Term Robot Interaction (2023)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Detection association plus temporal propagation across frames.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 42. 3D-Anchored Lookahead Planning for Persistent Robotic Scene Memory via World-Model-Based MCTS (2026)
- Problem claimed: Preserve object state beyond the current sensor frame.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: the robot can afford extra sensing actions before acting; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; sensing cost model; occluder semantics
- Failure modes ignored: confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Using motion to manage occlusion.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 43. Joint Audio-Visual Tracking Using Particle Filters (2002)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Recursive filtering with a motion and observation model.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 44. Robotic Aubergine Harvesting Using Dual-Arm Manipulation (2020)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 45. Deep Learning Reactive Robotic Grasping With a Versatile Vacuum Gripper (2022)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the robot can afford extra sensing actions before acting; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; sensing cost model; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 46. Real-Time Robotic Mirrored Behavior of Facial Expressions and Head Motions Based on Lightweight Networks (2022)
- Problem claimed: Build a spatial memory that remains useful as the robot moves through the world.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; object absence can wait for later map revisits; enough object surface remains visible to constrain pose; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; map update schedule; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; stale object map entries during manipulation; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 47. BundleTrack: 6D Pose Tracking for Novel Objects without Instance or Category-Level 3D Models (2021)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; object absence can wait for later map revisits; enough object surface remains visible to constrain pose; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; map update schedule; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; stale object map entries during manipulation; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 48. Robust 3D visual tracking using particle filtering on the special Euclidean group: A combined approach of keypoint and edge features (2012)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Recursive filtering with a motion and observation model.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 49. AutoBag: Learning to Open Plastic Bags and Insert Objects (2023)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: View selection or information-gain planning to expose hidden state.
- Hidden assumptions: enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 50. Bridging 2D and 3D Object Detection: Advances in Occlusion Handling through Depth Estimation (2025)
- Problem claimed: Improve robot or embodied perception under incomplete observations.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; occluder semantics
- Failure modes ignored: confusing clear-view absence with robot-caused invisibility
- What it makes less novel: The broad claim that robots need memory under partial observability.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 51. Revolutionizing Accessibility: Smart Wheelchair Robot and Mobile Application for Mobility, Assistance, and Home Management (2023)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Detection association plus temporal propagation across frames.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 52. Tracking individual honeybees among wildflower clusters with computer vision-facilitated pollinator monitoring (2021)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; training distribution covers relevant occlusion geometry; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 53. Automated harvesting by a dual-arm fruit harvesting robot (2022)
- Problem claimed: Improve robot or embodied perception under incomplete observations.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 54. Occlusion and Deformation Handling Visual Tracking for UAV via Attention-Based Mask Generative Network (2022)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Recursive filtering with a motion and observation model.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; training distribution covers relevant occlusion geometry; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 55. Capturing forceful interaction with deformable objects using a deep learning-powered stretchable tactile array (2024)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the robot can afford extra sensing actions before acting; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; sensing cost model; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 56. Interactive segmentation, tracking, and kinematic modeling of unknown 3D articulated objects (2013)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: View selection or information-gain planning to expose hidden state.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the robot can afford extra sensing actions before acting; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; sensing cost model; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 57. Enhanced Self-Perception in Mixed Reality: Egocentric Arm Segmentation and Database With Automatic Labeling (2020)
- Problem claimed: Improve robot or embodied perception under incomplete observations.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: enough object surface remains visible to constrain pose; training distribution covers relevant occlusion geometry; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 58. NeuralFeels with neural fields: Visuotactile perception for in-hand manipulation (2024)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 59. Development and evaluation of automated localisation and reconstruction of all fruits on tomato plants in a greenhouse based on multi-view perception and 3D multi-object tracking (2023)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: View selection or information-gain planning to expose hidden state.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 60. Learning Human-Arm Reaching Motion Using a Wearable Device in Human-Robot Collaboration (2024)
- Problem claimed: Improve robot or embodied perception under incomplete observations.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: enough object surface remains visible to constrain pose; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 61. Model Predictive Control for Dynamic Cloth Manipulation: Parameter Learning and Experimental Validation (2024)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 62. Autonomous Robotic Ultrasound Approach for Fetoscope Tracking by Fusing Optical and 2D Ultrasound Data (2024)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Recursive filtering with a motion and observation model.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 63. Semantic Relational Object Tracking (2019)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 64. Learning-based cable coupling effect modeling for robotic manipulation of heavy industrial cables (2022)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the robot can afford extra sensing actions before acting; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; sensing cost model; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 65. Vision-Based Navigation and Perception for Autonomous Robots: Sensors, SLAM, Control Strategies, and Cross-Domain Applications-A Review (2025)
- Problem claimed: Build a spatial memory that remains useful as the robot moves through the world.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: object absence can wait for later map revisits; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; map update schedule; occluder semantics
- Failure modes ignored: stale object map entries during manipulation; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Long-lived object memory in a spatial representation.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 66. An RGB-D Vision-Guided Robotic Depalletizing System for Irregular Camshafts with Transformer-Based Instance Segmentation and Flexible Magnetic Gripper (2025)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 67. Visual-Tactile Fusion for 3D Objects Reconstruction from a Single Depth View and a Single Gripper Touch for Robotics Tasks (2021)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: View selection or information-gain planning to expose hidden state.
- Hidden assumptions: enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 68. Object Detection, Recognition, and Tracking Algorithms for ADASs-A Study on Recent Trends (2023)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: View selection or information-gain planning to expose hidden state.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 69. Real-Time Robotic Manipulation of Cylindrical Objects in Dynamic Scenarios Through Elliptic Shape Primitives (2018)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 70. Multi-Modal Perception Attention Network with Self-Supervised Learning for Audio-Visual Speaker Tracking (2022)
- Problem claimed: Build a spatial memory that remains useful as the robot moves through the world.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; object absence can wait for later map revisits; enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; map update schedule; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; stale object map entries during manipulation; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 71. On the Scalability of Vision-Based Drone Swarms in the Presence of Occlusions (2022)
- Problem claimed: Improve robot or embodied perception under incomplete observations.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 72. Towards an integrated study of camouflage and cognition in cephalopods (2025)
- Problem claimed: Infer the full or hidden object extent when visible pixels are incomplete.
- Actual mechanism introduced: Amodal completion from visible evidence and learned shape priors.
- Hidden assumptions: hidden extent can be inferred from category or shape priors; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; occluder semantics
- Failure modes ignored: confident hallucination of an object that was actually removed; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Inferring hidden state from visible fragments.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 73. 3D LiDAR Multi-Object Tracking with Short-Term and Long-Term Multi-Level Associations (2023)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Geometric map optimization over poses, landmarks, or object states.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the robot can afford extra sensing actions before acting; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; sensing cost model; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 74. Enhancing Robotic Perception through Synchronized Simulation and Physical Common-Sense Reasoning (2024)
- Problem claimed: Improve robot or embodied perception under incomplete observations.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; occluder semantics
- Failure modes ignored: confusing clear-view absence with robot-caused invisibility
- What it makes less novel: The broad claim that robots need memory under partial observability.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 75. Tracking Occluded Objects and Recovering Incomplete Trajectories by Reasoning About Containment Relations and Human Actions (2018)
- Problem claimed: Build a spatial memory that remains useful as the robot moves through the world.
- Actual mechanism introduced: View selection or information-gain planning to expose hidden state.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; object absence can wait for later map revisits; enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; map update schedule; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; stale object map entries during manipulation; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 76. Surround-View Fisheye Camera Perception for Automated Driving: Overview, Survey &amp; Challenges (2023)
- Problem claimed: Improve robot or embodied perception under incomplete observations.
- Actual mechanism introduced: View selection or information-gain planning to expose hidden state.
- Hidden assumptions: enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 77. Online Multiple Object Tracking Using a Novel Discriminative Module for Autonomous Driving (2021)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 78. Visuo-Haptic Rendering of the Hand during 3D Manipulation in Augmented Reality (2024)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Geometric map optimization over poses, landmarks, or object states.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 79. Object Tracking in UAV Videos by Multifeature Correlation Filters With Saliency Proposals (2023)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Recursive filtering with a motion and observation model.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 80. Can the robot "see" what I see? Robot gaze drives attention depending on mental state attribution (2023)
- Problem claimed: Improve robot or embodied perception under incomplete observations.
- Actual mechanism introduced: Task-specific perception model over partial observations.
- Hidden assumptions: the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; occluder semantics
- Failure modes ignored: confusing clear-view absence with robot-caused invisibility
- What it makes less novel: The broad claim that robots need memory under partial observability.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 81. Turning Video Models into Generalist Robot Policies (2026)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 82. Towards Vision-Based Dual Arm Robotic Fruit Harvesting (2023)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 83. DetTrack: An Algorithm for Multiple Object Tracking by Improving Occlusion Object Detection (2023)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 84. An application of stereo matching algorithm based on transfer learning on robots in multiple scenes (2023)
- Problem claimed: Build a spatial memory that remains useful as the robot moves through the world.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: object absence can wait for later map revisits; enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; map update schedule; occluder semantics
- Failure modes ignored: stale object map entries during manipulation; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Long-lived object memory in a spatial representation.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 85. Mobile Robotic Sensor Network Using Vision Tracking (2008)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 86. Visual Reconstruction and Localization-Based Robust Robotic 6-DoF Grasping in the Wild (2021)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 87. An Occlusion-Aware Tracker With Local-Global Features Modeling in UAV Videos (2024)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 88. AgriSORT: A Simple Online Real-time Tracking-by-Detection framework for robotics in precision agriculture (2024)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 89. Point2Volume: A Vision-Based Dietary Assessment Approach Using View Synthesis (2019)
- Problem claimed: Improve robot or embodied perception under incomplete observations.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: enough object surface remains visible to constrain pose; training distribution covers relevant occlusion geometry; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 90. Adaptive response maps fusion of correlation filters with anti-occlusion mechanism for visual object tracking (2022)
- Problem claimed: Build a spatial memory that remains useful as the robot moves through the world.
- Actual mechanism introduced: Recursive filtering with a motion and observation model.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; object absence can wait for later map revisits; enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; map update schedule; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; stale object map entries during manipulation; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 91. Memory-Augmented Vision-Language Agents for Persistent and Semantically Consistent Object Captioning (2026)
- Problem claimed: Build a spatial memory that remains useful as the robot moves through the world.
- Actual mechanism introduced: View selection or information-gain planning to expose hidden state.
- Hidden assumptions: object absence can wait for later map revisits; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; map update schedule; occluder semantics
- Failure modes ignored: stale object map entries during manipulation; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Long-lived object memory in a spatial representation.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 92. A Grid-Based Framework for Collective Perception in Autonomous Vehicles (2021)
- Problem claimed: Build a spatial memory that remains useful as the robot moves through the world.
- Actual mechanism introduced: Recursive filtering with a motion and observation model.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; object absence can wait for later map revisits; enough object surface remains visible to constrain pose; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; map update schedule; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; stale object map entries during manipulation; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 93. Visual Tracking: An Experimental Survey (2014)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: View selection or information-gain planning to expose hidden state.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the robot can afford extra sensing actions before acting; camera occlusion generalizes to robot-body occlusion; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; sensing cost model; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 94. Benchmarks for Cloud Robotics (2016)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 95. Development of a sweet pepper harvesting robot (2020)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Geometric map optimization over poses, landmarks, or object states.
- Hidden assumptions: enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 96. Artificial intelligence within the interplay between natural and artificial computation: Advances in data science, trends and applications (2020)
- Problem claimed: Improve robot or embodied perception under incomplete observations.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; occluder semantics
- Failure modes ignored: confusing clear-view absence with robot-caused invisibility
- What it makes less novel: The broad claim that robots need memory under partial observability.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 97. An Adaptive Dynamic Multi-Template Correlation Filter for Robust Object Tracking (2022)
- Problem claimed: Maintain object identity and state through missed or ambiguous detections.
- Actual mechanism introduced: Recursive filtering with a motion and observation model.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 98. AI-Driven Intelligent Control Strategies for Industrial Robotics: A Reinforcement Learning Approach (2025)
- Problem claimed: Improve robot or embodied perception under incomplete observations.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: enough object surface remains visible to constrain pose; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 99. Communication Within Multi-FSM Based Robotic Systems (2018)
- Problem claimed: Improve robot or embodied perception under incomplete observations.
- Actual mechanism introduced: Pose registration, keypoint, correspondence, or dense alignment mechanism.
- Hidden assumptions: enough object surface remains visible to constrain pose; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; object geometry or pose prior; occluder semantics
- Failure modes ignored: pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: Pose maintenance under partial visibility.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.

## 100. Real-Time Iris Tracking Using Deep Regression Networks for Robotic Ophthalmic Surgery (2020)
- Problem claimed: Estimate object pose robustly enough for robot manipulation.
- Actual mechanism introduced: Learned visual representation or sequence model trained from labeled experience.
- Hidden assumptions: misses are tolerable with a fixed temporal patience window; enough object surface remains visible to constrain pose; training distribution covers relevant occlusion geometry; the cause of a missing detection is not represented as robot-action evidence
- Variables treated as fixed: camera calibration; deletion patience; object geometry or pose prior; occluder semantics
- Failure modes ignored: identity deletion during long robot self-occlusion; pose drift when the gripper hides the discriminative surface; confusing clear-view absence with robot-caused invisibility
- What it makes less novel: General temporal persistence and missed-detection handling.
- What it leaves open: A mechanism that treats robot self-occlusion as an action-conditioned certificate for when a missing detection should preserve, not delete, object state.
