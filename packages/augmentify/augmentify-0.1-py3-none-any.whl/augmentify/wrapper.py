import augmentify as aug


class A(aug.Transform):
    def __init__(self, transform, **kwargs):
        super().__init__(**kwargs)
        self.a_transform = transform

    def apply(self, array, is_seg):
        transformed_array = self.a_transform(image=array)["image"]
        return transformed_array