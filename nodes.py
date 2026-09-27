import torch
import comfy.model_management

# All dimensions are multiples of 16 for broad compatibility (SD1.5/SDXL/Flux/Wan).
# Full Body is the 9:16 transpose of Landscape; Portrait uses a 3:4 (bust/headshot) ratio.
RESOLUTIONS = {
    "Landscape 1K (1024x576)": (1024, 576),
    "Landscape 2K (1920x1088)": (1920, 1088),
    "Landscape 3K (2560x1440)": (2560, 1440),
    "Landscape 4K (3840x2160)": (3840, 2160),

    "Portrait 1K (768x1024)": (768, 1024),
    "Portrait 2K (1440x1920)": (1440, 1920),
    "Portrait 3K (1920x2560)": (1920, 2560),
    "Portrait 4K (2880x3840)": (2880, 3840),

    "Full Body 1K (576x1024)": (576, 1024),
    "Full Body 2K (1088x1920)": (1088, 1920),
    "Full Body 3K (1440x2560)": (1440, 2560),
    "Full Body 4K (2160x3840)": (2160, 3840),

    "Square 1K (1024x1024)": (1024, 1024),
    "Square 2K (2048x2048)": (2048, 2048),
    "Square 3K (3072x3072)": (3072, 3072),
    "Square 4K (4096x4096)": (4096, 4096),
}


class EmptyLatentImageResPreset:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "resolution": (list(RESOLUTIONS.keys()), {"default": "Portrait 2K (1440x1920)"}),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 4096, "tooltip": "The number of latent images in the batch."}),
            }
        }

    RETURN_TYPES = ("LATENT", "INT", "INT")
    RETURN_NAMES = ("LATENT", "width", "height")
    OUTPUT_TOOLTIPS = ("The empty latent image batch.", "Chosen width in pixels.", "Chosen height in pixels.")
    FUNCTION = "generate"
    CATEGORY = "latent"
    DESCRIPTION = "Empty Latent Image with a resolution dropdown spanning 1K-4K across Landscape, Portrait, and Full Body presets."

    def generate(self, resolution, batch_size=1):
        width, height = RESOLUTIONS[resolution]
        latent = torch.zeros(
            [batch_size, 4, height // 8, width // 8],
            device=comfy.model_management.intermediate_device(),
            dtype=comfy.model_management.intermediate_dtype(),
        )
        return ({"samples": latent, "downscale_ratio_spacial": 8}, width, height)


NODE_CLASS_MAPPINGS = {
    "EmptyLatentImageResPreset": EmptyLatentImageResPreset,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EmptyLatentImageResPreset": "Empty Latent Image (Res Presets)",
}
