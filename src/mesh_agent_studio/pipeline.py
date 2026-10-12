from __future__ import annotations

from pathlib import Path
from typing import Any

from .blender_adapter import BlenderAdapter
from .photogrammetry import PhotogrammetryPipeline
from .neural_recon import NeuralReconstructionPipeline


class MeshAgentPipeline:
    def __init__(self, config: Any):
        self.config = config
        self.blender = BlenderAdapter(config.blender_executable)
        self.photogrammetry = PhotogrammetryPipeline(config.meshroom_executable)
        self.neural = NeuralReconstructionPipeline(config.nerfstudio_executable)

    def run(self, image_dir: str | Path, output_dir: str | Path) -> dict[str, Any]:
        photogrammetry_result = self.photogrammetry.run_from_photos(image_dir, output_dir)
        neural_result = self.neural.run(image_dir, output_dir)

        return {
            "photogrammetry": photogrammetry_result,
            "neural": neural_result,
            "blender": {
                "executable": self.config.blender_executable,
                "ready": True,
            },
        }
