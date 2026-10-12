# Architecture overview

This project acts as a unified orchestration layer around several open-source 3D stacks.

## Layer 1: Input and planning

- AI-assisted prompt generation
- style selection
- concept constraints

## Layer 2: Reconstruction

- image-based photogrammetry
- neural reconstruction
- mesh generation

## Layer 3: Blender refinement

- cleanup
- sculpting
- retopology
- UVs / textures
- final export

## Layer 4: Asset pipeline

- GLB export
- web embedding
- game assets
- product visualization

## Why this repo is useful

It makes it easy to assemble free tools into a single project rather than trying to manually stitch independent workflows together.
