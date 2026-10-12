# Mesh Agent Studio

A single, open-source repo that brings together the best free tools for high-detail 3D creation and allows an AI agent workflow to orchestrate them.

The goal is simple: use AI prompts and automation to go beyond primitive boxes and straight geometry, producing organic curves, believable surfaces, detailed textures, and usable 3D models with Blender + photogrammetry + neural reconstruction.

This repo is designed as a starting point for:

- AI-guided concept generation
- Blender automation
- Photogrammetry reconstruction from photos
- Neural reconstruction / NeRF workflows
- Mesh cleanup, retopology, material setup, and export

## Core idea

The pipeline combines multiple open-source systems:

- Blender for sculpting, details, and final polish
- Meshroom / AliceVision for photogrammetry
- COLMAP for SfM / reconstruction
- OpenMVS for dense reconstruction
- Open3D for mesh processing
- Nerfstudio or Instant-NGP for neural reconstruction
- Python orchestration to connect the tools with an agent prompt layer

This is not a single monolithic app. It is a single repo that packages the best tools into a reproducible workflow.

## What this repo includes

- A complete project layout for the 3D AI pipeline
- Python orchestration scripts to run the workflow
- Blender integration examples
- Docker setup for easier reproducibility
- Example prompts for generating complex, organic, and textured 3D assets

## Recommended stack

### 1. Photogrammetry / realistic detail

- Meshroom / AliceVision
- COLMAP
- OpenMVS
- MeshLab
- Blender

### 2. Neural / high-frequency detail

- Nerfstudio
- Instant-NGP
- Open3D
- Blender

### 3. Agent orchestration

- Claude or another LLM acting as the planner
- Python automation layer
- Blender Python API automation

## Typical workflow

1. Collect reference images or concept inputs.
2. Run AI planning for style, form, and material intent.
3. Use photogrammetry or neural reconstruction to generate base geometry.
4. Feed the result into Blender for sculpting, cleanup, and retopology.
5. Use materials, textures, and UV baking for realism.
6. Export GLB, OBJ, FBX, STL, or USD.

## Repository structure

```text
.
├── README.md
├── pyproject.toml
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── .gitignore
├── LICENSE
├── src/
│   └── mesh_agent_studio/
│       ├── __init__.py
│       ├── config.py
│       ├── pipeline.py
│       ├── blender_adapter.py
│       ├── photogrammetry.py
│       ├── neural_recon.py
│       └── orchestrator.py
├── scripts/
│   ├── setup_env.sh
│   ├── run_blender_pipeline.py
│   └── run_reconstruction.py
├── examples/
│   ├── prompts.md
│   ├── blender_script.py
│   └── sample_run.json
├── docs/
│   └── architecture.md
└── notebooks/
    └── prototype.ipynb
```

## Quick start

### Install Python tools

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Or use Docker

```bash
docker compose up --build
```

### Example orchestration flow

```bash
python scripts/run_reconstruction.py --input ./data/photos --output ./output/mesh
python scripts/run_blender_pipeline.py --input ./output/mesh/base.obj --output ./output/final
```

## Example prompt ideas

These are the kinds of prompts the agent should be able to handle:

- "Generate a sculptural, organic chair with flowing curves and a matte ceramic finish."
- "Create a stylized creature form with asymmetry, layered skin folds, and high-detail horns."
- "Build a realistic rock formation with cracks, roughness variation, and a natural color palette."
- "Produce an industrial lamp with smooth organic transitions and detailed metallic texture."
- "Design a decorative vase with subtle hand-thrown imperfections and high-frequency glaze detail."

## Notes on realism and quality

High-quality 3D output usually depends on:

- good image coverage
- strong lighting
- consistent texture references
- post-processing in Blender
- a combination of geometry generation + sculpting cleanup

The goal is not to replace all of Blender. The goal is to turn Blender into a final finishing studio for AI-generated geometry.

## Environment recommendations

- GPU: strongly recommended for neural reconstruction and faster rendering
- RAM: 16GB+ recommended
- Storage: SSD recommended
- OS: Linux or Windows with WSL2 for the best open-source stack compatibility

## Why this matters

Most AI 3D workflows end up with a rigid, boxy, or overly generic result unless they are paired with a proper modeling and texturing pipeline. This repo is meant to bridge that gap by combining:

- AI planning
- reconstruction tools
- Blender sculpting and surfacing
- final export for engines, websites, and creators

## License

MIT

## Next steps

This repo is intentionally set up as a foundation. The next phase would be:

- adding a richer agent CLI
- connecting to Blender Python API wrappers
- building photogrammetry + Blender automation scripts
- integrating advanced generation models and texture pipelines

This is the first pass toward an agent-driven 3D creation studio that can generate more complex, curved, textured, and realistic asset outputs than the common basic primitives workflow.
