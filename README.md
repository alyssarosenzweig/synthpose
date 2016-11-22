# synthposes

`synthposes` generates a synthetic training set for human pose estimation according to a modified version of "Efficient Human Pose Estimation from Single Depth Images" by Shotton et al.

# Usage

Modify the environmental variables `OUTPUT_DIR` (the directory to output to) and `COUNT` (the number of samples to generate as desired) upon invoking `test.sh`.

By default, synthpose is single-threaded and is intended to be used with multiple instances in parallel for multicore machines. Note OUTPUT_DIR should be different per core for this use case, to avoid file name collisions.

# A sample

![Sample depth map](samples/render_8_depth.png)
![Sample part map](samples/render_8_parts.png)
![Sample RGB image](samples/render_8_rgb.png)

Competent texture artists wanted :-)
