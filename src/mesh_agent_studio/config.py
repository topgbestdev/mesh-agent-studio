from dataclasses import dataclass, field
from pathlib import Path
from typing import List


@dataclass
class ProjectConfig:
    project_root: Path = Path(__file__).resolve().parents[2]
    data_dir: Path = field(default_factory=lambda: Path(__file__).resolve().parents[2] / "data")
    output_dir: Path = field(default_factory=lambda: Path(__file__).resolve().parents[2] / "output")
    blender_executable: str = "blender"
    meshroom_executable: str = "Meshroom"
    colmap_executable: str = "colmap"
    openmvs_executable: str = "ReconstructMesh"
    nerfstudio_executable: str = "ns-process"
    desired_style: str = "organic, curved, realistic, highly detailed, textured"
    prompt_templates: List[str] = field(
        default_factory=lambda: [
            "Create an organic form with soft volume transitions and detailed surface variation.",
            "Generate a realistic high-detail asset with sculptural curves and natural material variations.",
            "Model a functional object with refined topology, smooth transitions, and material richness.",
        ]
    )


DEFAULT_CONFIG = ProjectConfig()
