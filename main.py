import os
from itertools import cycle
from shutil import copy


class ImageError(Exception):
    pass


def main():
    background_path = input("Enter the path to your osu! folder: ").replace('"', '') + "/Data/bg"
    images = os.listdir("./images")
    background_changer = OsuBackgroundChanger(background_path, images)
    background_changer.run()


class OsuBackgroundChanger:
    def __init__(self, background_path, images):
        self.background_path = background_path
        self.images = images

    def run(self):
        try:
            self.pre_check()
        except Exception as e:
            print(e)
            return
        self.change_background()

    def pre_check(self):
        if len(self.images) == 0:
            raise ImageError("No images found in the images folder")
        for image in self.images:
            if image.endswith(".jpg") and image.endswith(".jpeg"):
                raise ImageError("Only jpg images are supported")
        return

    def change_background(self):
        osu_images = os.listdir(self.background_path)
        cycled_images = cycle(iter(self.images))
        for image in osu_images:
            src = "./images/" + next(cycled_images)
            dst = self.background_path + "/" + image
            copy(src, dst)
            print(f"Copied {src} to {dst}")


if __name__ == "__main__":
    main()
