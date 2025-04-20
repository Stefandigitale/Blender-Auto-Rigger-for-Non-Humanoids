# Blender-Auto-Rigger-for-Non-Humanoids
Python-powered automatic rigging system for creatures, mechas, and abstract 3D models in Blender – because not everything moves like a human.

Rigging non-humanoid 3D models (dragons, robots, eldritch horrors) is tedious and poorly supported by existing tools. This project:
✅ Automates rigging for complex geometries using Python + geometric algorithms
✅ Saves hours of manual bone placement
✅ Supports motion transfer between mismatched creatures
✅ Works inside Blender as a script/add-on

draft key points which i want to reach
🛠️ Features
1. Auto-Rigging Core
Detects natural "joint" positions using mesh curvature analysis (scipy.spatial)

Generates optimized bone hierarchies with inverse kinematics (IK)

Handles multi-limbed, winged, and asymmetrical topologies

3. Dataset Tools
Generate synthetic training data for ML-assisted joint prediction

Pre-process existing rigs to improve auto-rigging
