from geometry.hit import Hit
from cam.ortopraphic_camera import OrthographicCamera 
from geometry.sphere import Sphere
from geometry.group import Group
from utils.io_utils import read_scene_from_json, save_image
import numpy as np

def raycast(scene, resolution, near, far, output_name):
    width, height = resolution
    color_image = np.zeros((height, width, 3), dtype=np.float32)
    depth_image = np.zeros((height, width), dtype=np.float32)

    ortho_camera_data = scene.get("orthocamera", {})
    ortho_camera = OrthographicCamera(ortho_camera_data["center"], ortho_camera_data["direction"],
                                      ortho_camera_data["up"], ortho_camera_data["size"])

    background_color = np.array(scene.get("background", {}).get("color", [0, 0, 0]))

    group_data = scene.get("group", [])
    objects = [Sphere(**data["sphere"]) for data in group_data]

    scene_group = Group(objects)

    for y in range(height):
        for x in range(width):
            normalized_x = x / (width - 1)
            normalized_y = 1 - y / (height - 1)  # Invert y to match the coordinate system

            ray = ortho_camera.generate_ray(normalized_x, normalized_y)
            hit = Hit()

            scene_group.intersect(ray, hit, near)

            color = background_color
            if hit.color:
                color = hit.color

            color_image[y, x] = color
            depth_image[y, x] = (far - hit.t) / (far - near)

    # Normalize depth values to [0, 255]
    depth_image = (depth_image * 255).astype(np.uint8)

    save_image(color_image, f"{output_name}_color.jpg")
    save_image(depth_image, f"{output_name}_depth.jpg")

if __name__ == "__main__":
    
    scene_data = read_scene_from_json("caster/scene1.json")
    resolution = (800, 600)
    near_depth = 2
    far_depth = 5


    scene_data2 = read_scene_from_json("caster/scene2.json")
    resolution2 = (800, 600)
    near_depth2 = 2
    far_depth2 = 5



    raycast(scene_data, resolution, near_depth, far_depth, "scene1")
    raycast(scene_data2, resolution2, near_depth2, far_depth2, "scene2")
