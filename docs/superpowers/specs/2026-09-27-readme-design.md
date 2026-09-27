# README Design

## Goal

Create a concise README that lets a ComfyUI user understand and install the custom node without reading its Python source.

## Audience

ComfyUI users who want preset latent resolutions for image-generation workflows.

## Structure

The README will contain:

1. The project name and a one-sentence description.
2. A short feature list.
3. Installation instructions using Git and manual folder copying.
4. Basic usage steps and the node's search/display name.
5. A table of every bundled resolution preset.
6. Input and output descriptions.
7. Compatibility and dependency notes.
8. A brief license note stating that no license has yet been added.

## Constraints

- Keep the language simple and concise.
- Document only behavior confirmed by `nodes.py`.
- Do not claim support beyond the node's implemented latent format and ComfyUI dependency.
- Do not add screenshots or troubleshooting sections in this first version.

## Verification

- Confirm every documented preset matches `RESOLUTIONS` in `nodes.py`.
- Confirm the internal and display names match the node mappings.
- Confirm Markdown has no placeholders or broken relative references.
