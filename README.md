# ComfyUI ResPreset Latent

A small ComfyUI custom node that creates an empty latent using a selectable resolution preset.

## Features

- Landscape, portrait, full-body, and square presets.
- Resolutions from 1K to 4K.
- Adjustable batch size.
- Separate width and height outputs for connecting to other nodes.

## Installation

Open a terminal in `ComfyUI/custom_nodes` and run:

```bash
git clone https://github.com/AbulH88/ComfyUI-ResPresetLatent.git
```

Restart ComfyUI after installation.

You can also download the repository and copy the `ComfyUI-ResPresetLatent` folder into `ComfyUI/custom_nodes`.

## Usage

1. Add **Empty Latent Image (Res Presets)** from the ComfyUI node menu.
2. Choose a resolution preset.
3. Set the batch size.
4. Connect the `LATENT` output to your sampler or another compatible latent input.

## Resolution presets

| Preset | Width | Height |
| --- | ---: | ---: |
| Landscape 1K (1024x576) | 1024 | 576 |
| Landscape 2K (1920x1088) | 1920 | 1088 |
| Landscape 3K (2560x1440) | 2560 | 1440 |
| Landscape 4K (3840x2160) | 3840 | 2160 |
| Portrait 1K (768x1024) | 768 | 1024 |
| Portrait 2K (1440x1920) | 1440 | 1920 |
| Portrait 3K (1920x2560) | 1920 | 2560 |
| Portrait 4K (2880x3840) | 2880 | 3840 |
| Full Body 1K (576x1024) | 576 | 1024 |
| Full Body 2K (1088x1920) | 1088 | 1920 |
| Full Body 3K (1440x2560) | 1440 | 2560 |
| Full Body 4K (2160x3840) | 2160 | 3840 |
| Square 1K (1024x1024) | 1024 | 1024 |
| Square 2K (2048x2048) | 2048 | 2048 |
| Square 3K (3072x3072) | 3072 | 3072 |
| Square 4K (4096x4096) | 4096 | 4096 |

## Inputs and outputs

Inputs:

- `resolution`: selects one of the 16 included presets.
- `batch_size`: sets how many empty latent images are created.

Outputs:

- `LATENT`: the empty latent batch.
- `width`: the selected width in pixels.
- `height`: the selected height in pixels.

## Compatibility

This node requires ComfyUI. It uses ComfyUI's model-management device and data type for the generated latent tensor. No extra Python packages are required beyond ComfyUI's existing dependencies.

## License

No license file has been added yet.
