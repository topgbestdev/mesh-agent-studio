#!/usr/bin/env python3

from pathlib import Path
import argparse

from mesh_agent_studio.blender_adapter import BlenderAdapter


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prepare a mesh for Blender refinement.")
    parser.add_argument("--input", type=str, required=True, help="Input mesh path")
    parser.add_argument("--output", type=str, default="./output/final.glb", help="Output export path")
    args = parser.parse_args()

    adapter = BlenderAdapter()
    adapter.import_mesh(args.input)
    adapter.export_mesh(args.output, fmt="glb")
    print(f"Prepared: {args.input} -> {args.output}")
