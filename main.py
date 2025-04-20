# filepath: /blender-rigging-toolkit/blender-rigging-toolkit/src/main.py

import argparse
from rigging.creature_rig import CreatureRig
from rigging.mecha_rig import MechaRig
from rigging.abstract_rig import AbstractRig

def main():
    parser = argparse.ArgumentParser(description="Blender Rigging Toolkit")
    parser.add_argument('model_type', choices=['creature', 'mecha', 'abstract'], help='Type of model to rig')
    parser.add_argument('--options', nargs='*', help='Additional options for rig generation')

    args = parser.parse_args()

    if args.model_type == 'creature':
        rig = CreatureRig()
        rig.create_bones()
        rig.set_skin_weights()
        rig.apply_constraints()
    elif args.model_type == 'mecha':
        rig = MechaRig()
        rig.create_joints()
        rig.set_ik_constraints()
        rig.configure_movement()
    elif args.model_type == 'abstract':
        rig = AbstractRig()
        rig.create_shapes()
        rig.define_movement_patterns()
        rig.apply_modifiers()

if __name__ == "__main__":
    main()