from pathlib import Path
from typing import Any


class PhotogrammetryPipeline:
    def __init__(self, meshroom_executable: str = "Meshroom"):
        self.meshroom_executable = meshroom_executable

    def run_from_photos(self, image_dir: str | Path, output_dir: str | Path) -> dict[str, Any]:
        """Placeholder for a real Meshroom/COLMAP/OpenMVS workflow."""
        image_dir = Path(image_dir)
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        return {
            "status": "not_run",
            "image_dir": str(image_dir),
            "output_dir": str(output_dir),
            "message": "Integrate Meshroom / AliceVision + COLMAP + OpenMVS here.",
        }
