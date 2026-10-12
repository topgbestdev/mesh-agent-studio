from pathlib import Path
import subprocess


class BlenderAdapter:
    def __init__(self, blender_executable: str = "blender"):
        self.blender_executable = blender_executable

    def run_python_script(self, script_path: str | Path, *args: str) -> None:
        command = [self.blender_executable, "--background", "--factory-startup", "--python", str(script_path), *args]
        subprocess.run(command, check=True)

    def import_mesh(self, mesh_path: str | Path) -> None:
        """Import a mesh into Blender. This is a placeholder for a future realistic automation setup."""
        print(f"Would import mesh: {mesh_path}")

    def export_mesh(self, output_path: str | Path, fmt: str = "glb") -> None:
        """Export a mesh from Blender. Placeholder for a real Blender script."""
        print(f"Would export mesh to: {output_path} as {fmt}")
