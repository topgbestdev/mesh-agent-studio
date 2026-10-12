#!/usr/bin/env python3

from pathlib import Path
import argparse

from mesh_agent_studio.config import DEFAULT_CONFIG
from mesh_agent_studio.pipeline import MeshAgentPipeline


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the unified 3D reconstruction pipeline.")
    parser.add_argument("--input", type=str, required=True, help="Input image directory or dataset")
    parser.add_argument("--output", type=str, default="./output", help="Output directory")
    args = parser.parse_args()

    pipeline = MeshAgentPipeline(DEFAULT_CONFIG)
    result = pipeline.run(Path(args.input), Path(args.output))
    print(result)
