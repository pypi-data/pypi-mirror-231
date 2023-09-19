import numpy as np
import skimage
from skimage import transform as ski_transform
from scipy import spatial
from scipy import ndimage as ndi
from typing import Union, Sequence, Dict
import random
from augmentify import utils
from augmentify.utils import slicer
from augmentify.constants import IMAGE, SEG, NUMPY, TENSOR
from augmentify import variables
import torch


# TODO: ATM a different transform/augment paras are chosen for every aug.IMAGE and aug.SEG. FIXED in abstract transform, need to adapt in real transforms
# TODO: Has problems with channel and batch dim.
# TODO: Related to above: Apply transform only to selected axes
# TODO: Always expect data to have a channel dim. Problematic with memory-mapped data. If it does not have a channel dim then adding one would load the data.
# TODO: Convert type stuff / expected type stuff. <- Will load memory-mapped data. Bad!
# TODO: What is the structure to implement 1D, 2D, 3D and nD transforms in a single transform
# TODO: CUDA accelaration
# TODO: Wrapper for other augmentation / preprocessing libraries (Torchvision, albumations, TorchIO)
# TODO: Write tests
# TODO: Guarantee datatypes for method inputs
# TODO: Add AffineTransform
# TODO: Add RandNoise, RandBlur (gaussian, median, ...),
# TODO: Extend RandCrop to random crop size with min-max size not just random position
# TODO: Add documentation
# TODO: Getter to return generated transfrom parameters from a (used) transform
# TODO: Apply with given transform parameters
# TODO: Transform history
# TODO: Inverse transform that undoes all transforms based on a history
# TODO: Save/load transform pipeline to yaml/json
# TODO: OneOf / MultipleOf + with a function that changes the probability and intensity

class Transform:
    def __init__(self, p=1, ignore_img=False, ignore_seg=False):
        self.p = p
        self.ignore_img = ignore_img
        self.ignore_seg = ignore_seg
        self.expected_type = NUMPY
        self.apply_separate = True

        # variables = variables.globals()
        self.num_dims = variables.NUM_DIMS
        self.has_channel_dim = variables.HAS_CHANNEL_DIM
        self.has_batch_dim = variables.HAS_BATCH_DIM

    def __call__(self, subject, is_seg=False, **kwargs):
        if self.p is not None and self.p < random.random():
            return subject

        # converted_subject = self.convert_type(subject)  #TODO: This will load the entire zarr array
        converted_subject = subject


        paras = self.gen_paras(self.get_first_array(converted_subject))

        if not self.apply_separate:
            transformed_subject = self.apply(converted_subject, paras, False, **kwargs)
        elif isinstance(converted_subject, dict):
            transformed_subject = {}
            if IMAGE in converted_subject:
                if not self.ignore_img:
                    if isinstance(converted_subject[IMAGE], list):
                        transformed_arrays = []
                        for i in range(len(converted_subject[IMAGE])):
                            transformed_arrays.append(self.apply(converted_subject[IMAGE][i], paras, False, **kwargs))
                    else:
                        transformed_arrays = self.apply(converted_subject[IMAGE], paras, False)
                    transformed_subject[IMAGE] = transformed_arrays
                else:
                    transformed_subject[IMAGE] = converted_subject[IMAGE]
            if SEG in converted_subject:
                if not self.ignore_seg:
                    if isinstance(converted_subject[SEG], list):
                        transformed_arrays = []
                        for i in range(len(converted_subject[aug.SEG])):
                            transformed_arrays.append(self.apply(converted_subject[SEG][i], paras, True, **kwargs))
                    else:
                        transformed_arrays = self.apply(converted_subject[SEG], paras, True, **kwargs)
                    transformed_subject[SEG] = transformed_arrays
                else:
                    transformed_subject[SEG] = converted_subject[SEG]
        elif (not is_seg and not self.ignore_img) or (is_seg and not self.ignore_seg):
            transformed_subject = self.apply(converted_subject, paras, is_seg, **kwargs)
        else:
            transformed_subject = converted_subject
        return transformed_subject

    def convert_type(self, subject):
        if isinstance(subject, dict):
            converted_subject = {key: self.convert_type(subject[key]) for key in subject}
        elif isinstance(subject, list):
            converted_subject = [self.convert_type(array) for array in subject]
        else:
            converted_subject = self.expected_type(subject)
        return converted_subject

    def get_first_array(self, subject):
        if isinstance(subject, dict):
            if IMAGE in subject:
                if isinstance(subject[IMAGE], list):
                    return subject[IMAGE][0]
                else:
                    return subject[IMAGE]
            else:
                if isinstance(subject[SEG], list):
                    return subject[SEG][0]
                else:
                    return subject[SEG]
        else:
            return subject

    def gen_paras(self, array):
        return {}

    def apply(self, array, paras, is_seg, **kwargs):
        return array


class Compose(Transform):
    def __init__(self, transforms: Sequence[Transform], **kwargs):
        super().__init__(p=None, **kwargs)
        self.transforms = transforms

    def __call__(self, subject, is_seg=False, **kwargs):
        transformed_subject = subject
        for transform in self.transforms:
            transformed_subject = transform(transformed_subject, is_seg)
        return transformed_subject


class ToTensor(Transform):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def apply(self, array, paras, is_seg, **kwargs):
        transformed_array = torch.tensor(array)
        return transformed_array


class ToFloat(Transform):
    def __init__(self, double=False, **kwargs):
        super().__init__(**kwargs)
        self.precision = np.float32
        if double:
            self.precision = np.float64

    def apply(self, array, paras, is_seg, **kwargs):
        transformed_array = array.astype(self.precision)
        return transformed_array


class AddBatchDim(Transform):  # TODO: Does not work in combination with AddChannelDim and not with mixed data
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def apply(self, array, paras, is_seg, **kwargs):
        if self.has_channel_dim and self.num_dims is None:
            channel_dim = 1
        else:
            channel_dim = 0

        if self.num_dims is not None:
            if len(array.shape) == self.num_dims + channel_dim + 1:
                transformed_array = array
            elif len(array.shape) < self.num_dims + channel_dim + 1:
                transformed_array = array[np.newaxis, ...]
            else:
                raise RuntimeError("Cannot infer if array has already a batch dimension.")
        elif self.has_batch_dim:
            transformed_array = array
        elif not self.has_batch_dim:
            transformed_array = array[np.newaxis, ...]
        else:
            raise RuntimeError("Either HAS_BATCH_DIM or NUM_DIMS must be specified.")
        return transformed_array


class AddChannelDim(Transform):  # TODO: Does not work in combination with AddBatchDim and not with mixed data
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def apply(self, array, paras, is_seg, **kwargs):
        if self.has_batch_dim and self.num_dims is None:
            batch_dim = 1
        else:
            batch_dim = 0

        if self.num_dims is not None:
            if len(array.shape) == self.num_dims + batch_dim + 1:
                transformed_array = array
            elif len(array.shape) < self.num_dims + batch_dim + 1:
                transformed_array = array[np.newaxis, ...]
            else:
                raise RuntimeError("Cannot infer if array has already a batch dimension.")
        elif self.has_channel_dim:
            transformed_array = array
        elif not self.has_channel_dim:
            transformed_array = array[np.newaxis, ...]
        else:
            raise RuntimeError("Either HAS_CHANNEL_DIM or NUM_DIMS must be specified.")
        return transformed_array


class Resize(Transform):
    def __init__(self, target_shape, image_interpolation=1, seg_interpolation=0, **kwargs):
        """
        Resize image to match a certain size.
        :param target_shape:
        :param image_interpolation: int, optional
        The order of interpolation. The order has to be in the range 0-5:
        - 0: Nearest-neighbor
        - 1: Bi-linear (default)
        - 2: Bi-quadratic
        - 3: Bi-cubic
        - 4: Bi-quartic
        - 5: Bi-quintic
        :param seg_interpolation: int, optional
        The order of interpolation. The order has to be in the range 0-5:
        - 0: Nearest-neighbor (default)
        - 1: Bi-linear
        - 2: Bi-quadratic
        - 3: Bi-cubic
        - 4: Bi-quartic
        - 5: Bi-quintic
        """
        super().__init__(**kwargs)
        self.target_shape = target_shape
        self.image_interpolation = image_interpolation
        self.seg_interpolation = seg_interpolation

    def apply(self, array, paras, is_seg, **kwargs):
        if not is_seg:
            order = self.image_interpolation
            anti_aliasing = False
        else:
            order = self.seg_interpolation
            anti_aliasing = False
        non_spatial_dims = len(array.shape) - len(self.target_shape)
        target_shape = (*array.shape[:non_spatial_dims], *self.target_shape)
        transformed_array = ski_transform.resize(array, output_shape=target_shape, order=order, anti_aliasing=anti_aliasing, mode='edge')
        return transformed_array

    def get_slices(self, image, patch_indices, non_spatial_dims):
        slices = [None] * non_spatial_dims
        slices.extend([index_pair.tolist() for index_pair in patch_indices])
        return slices


class CropOrPad(Transform):  # Non-spatial-dim ready
    def __init__(self, target_shape, padding_mode='constant', **kwargs):
        super().__init__(**kwargs)
        self.target_shape = np.asarray(target_shape)
        self.padding_mode = padding_mode

    def apply(self, array, paras, is_seg, **kwargs):
        non_spatial_dims = len(array.shape) - len(self.target_shape)
        quotient, remainder = np.divmod(self.target_shape - array.shape[non_spatial_dims:], 2)
        crop_or_pad_widths = [[0, 0] for _ in range(non_spatial_dims)]
        crop_or_pad_widths.extend(np.stack([quotient, quotient+remainder], axis=0).flatten(order='F').reshape(-1, 2))
        crop_or_pad_widths = np.asarray(crop_or_pad_widths)

        pad_widths = np.clip(crop_or_pad_widths, a_min=0, a_max=None)
        transformed_array = array
        if np.max(pad_widths) > 0:
            transformed_array = np.pad(array, pad_widths, mode=self.padding_mode)

        crop_widths = np.clip(crop_or_pad_widths, a_min=None, a_max=0)
        crop_widths = np.abs(crop_widths)
        if np.max(crop_widths) > 0:
            crop_widths[:, 1] = transformed_array.shape - crop_widths[:, 1]
            transformed_array = transformed_array[slicer(transformed_array, crop_widths)]

        return transformed_array


class OneHot(Transform):
    def __init__(self, num_classes, **kwargs):
        super().__init__(ignore_img=True, **kwargs)
        self.num_classes = num_classes

    def apply(self, array, paras, is_seg, **kwargs):
        transformed_array = np.zeros((self.num_classes, *array.shape), dtype=array.dtype)
        for i in range(self.num_classes):
            transformed_array[i][array == i] = 1
        return transformed_array


class Zscore(Transform):
    def __init__(self, mean, std, max_pixel_value=None, **kwargs):
        super().__init__(ignore_seg=True, **kwargs)
        self.mean = mean
        self.std = std
        if max_pixel_value is not None:
            self.max_pixel_value = max_pixel_value
        else:
            self.max_pixel_value = 1.0

    def apply(self, array, paras, is_seg, **kwargs):
        transformed_array = array
        for axis in range(len(self.mean)):
            transformed_array[axis] = (transformed_array[axis] - self.mean[axis] * self.max_pixel_value) / (self.std[axis] * self.max_pixel_value)
        return transformed_array


class RandRotate3D(Transform):
    def __init__(self, degrees=(0, 360), axis=(0, 1, 2), multiple_axis=True, image_interpolation=1, seg_interpolation=0, mode='constant', cval=0.0, prefilter=True, **kwargs):  # TODO: Enable angles to be individual for each axis
        """
        Original doc: https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.affine_transform.html
        TODO: Check how to do the cool doc reference they are using
        :param degrees:
        :param axis:
        :param multiple_axis:
        :param image_interpolation:
        :param seg_interpolation:
        :param mode:
        :param cval:
        :param prefilter:
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.degrees = degrees
        self.axis = axis
        self.multiple_axis = multiple_axis
        self.image_interpolation = image_interpolation
        self.seg_interpolation = seg_interpolation
        self.mode = mode
        self.cval = cval
        self.prefilter = prefilter

    def apply(self, array, paras, is_seg, **kwargs):
        if self.multiple_axis:
            rand_axes = random.sample(self.axis, random.randint(1, len(self.axis)))
        else:
            rand_axes = [random.choice(self.axis)]

        rand_degrees = [0] * len(array.shape)
        for rand_axis in rand_axes:
            rand_degrees[rand_axis] = random.randint(*self.degrees)

        # Move center to (0, 0, 0)
        T0 = np.diag(np.ones(4), 0)
        T0[:3, 3] = (-1 * np.asarray(array.shape) // 2).T

        # Rotate
        rotation = spatial.transform.Rotation.from_euler('xyz', rand_degrees, degrees=True)
        R = np.diag(np.ones(4), 0)
        R[:3, :3] = rotation.as_matrix()

        # Move back to center
        T1 = np.diag(np.ones(4), 0)
        T1[:3, 3] = (np.asarray(array.shape) // 2).T

        affine_transform = T1 @ R @ T0  # TODO: Use np.dot instead

        inv_affine_transform = np.linalg.inv(affine_transform)

        if not is_seg:
            order = self.image_interpolation
        else:
            order = self.seg_interpolation

        transformed_array = ndi.affine_transform(array, inv_affine_transform, order=order, mode=self.mode, cval=self.cval, prefilter=self.prefilter)

        return transformed_array


class RandScale3D(Transform):
    def __init__(self, scales=(0.7, 1.3), isotropic=True, image_interpolation=1, seg_interpolation=0, mode='constant', cval=0.0, prefilter=True, **kwargs):
        """
        Original doc: https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.affine_transform.html
        TODO: Check how to do the cool doc reference they are using
        :param scales:
        :param isotropic:
        :param image_interpolation:
        :param seg_interpolation:
        :param mode:
        :param cval:
        :param prefilter:
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.scales = scales
        self.isotropic = isotropic
        self.image_interpolation = image_interpolation
        self.seg_interpolation = seg_interpolation
        self.mode = mode
        self.cval = cval
        self.prefilter = prefilter

    def apply(self, array, paras, is_seg, **kwargs):
        if not self.isotropic:
            rand_scales = [random.uniform(*self.scales) for _ in range(3)]
        else:
            rand_scales = [random.uniform(*self.scales)] * 3

        # Move center to (0, 0, 0)
        T0 = np.diag(np.ones(4), 0)
        T0[:3, 3] = (-1 * np.asarray(array.shape) // 2).T

        # Scale
        R = np.diag(np.ones(4), 0)
        R[0, 0] = rand_scales[0]
        R[1, 1] = rand_scales[1]
        R[2, 2] = rand_scales[2]

        # Move back to center
        T1 = np.diag(np.ones(4), 0)
        T1[:3, 3] = (np.asarray(array.shape) // 2).T

        affine_transform = T1 @ R @ T0

        inv_affine_transform = np.linalg.inv(affine_transform)

        if not is_seg:
            order = self.image_interpolation
        else:
            order = self.seg_interpolation

        transformed_array = ndi.affine_transform(array, inv_affine_transform, order=order, mode=self.mode, cval=self.cval, prefilter=self.prefilter)

        return transformed_array


class RandFlip3D(Transform):
    def __init__(self, axis=(0, 1, 2), **kwargs):
        super().__init__(**kwargs)
        self.axis = axis

    def apply(self, array, paras, is_seg, **kwargs):
        rand_axis = random.sample(self.axis, random.randint(1, len(self.axis)))
        transformed_array = np.flip(array, rand_axis)
        return transformed_array


class RandCrop(Transform):
    def __init__(self, target_shape, **kwargs):
        super().__init__(**kwargs)
        self.target_shape = np.asarray(target_shape)

    def gen_paras(self, array):
        non_spatial_dims = len(array.shape) - len(self.target_shape)
        indices = self.random_position(array.shape, self.target_shape, non_spatial_dims)
        indices = np.stack((indices, indices + self.target_shape), axis=1)
        indices = self.get_slices(array, indices, non_spatial_dims)
        paras = {"indices": indices}
        return paras

    def apply(self, array, paras, is_seg, **kwargs):
        indices = paras["indices"]
        transformed_array = array[slicer(array, indices)]
        return transformed_array

    def random_position(self, source_shape, target_shape, non_spatial_dims):
        indices = [random.randint(0, source_shape[non_spatial_dims + axis] - target_shape[axis]) for axis in range(len(target_shape))]
        return indices

    def get_slices(self, image, patch_indices, non_spatial_dims):
        slices = [None] * non_spatial_dims
        slices.extend([index_pair.tolist() for index_pair in patch_indices])
        return slices


class RandGamma(Transform):
    def __init__(self, log_gamma=(-0.3, 0.3), **kwargs):
        super().__init__(ignore_seg=True, **kwargs)
        self.log_gamma = log_gamma

    def apply(self, array, paras, is_seg, **kwargs):
        rand_gamma = np.exp(random.uniform(*self.log_gamma))  # TODO: ATM a different gamma is chosen for every aug.IMAGE and aug.SEG
        transformed_array = np.power(array, rand_gamma)
        return transformed_array


# Default3D = Compose([RandRotate3D()])
# DefaultMedical3D = Compose([RandRotate3D()])


if __name__ == '__main__':
    import augmentify as aug

    image1 = np.zeros((10, 10, 10))
    image2 = np.zeros((10, 10, 10))
    seg = np.zeros((10, 10, 10))
    subject = {IMAGE: [image1, image2], SEG: seg}

    # transform = Resize((20, 20, 20), p=0.5)
    # print("Source subject shape: ", subject[aug.IMAGE][0].shape)
    # resized_subject = transform(subject)
    # print("Target subject shape: ", resized_subject[aug.IMAGE][0].shape)
    #
    # transform = Compose([Resize((20, 20, 20)), Resize((40, 40, 40))])
    # print("Source subject shape: ", subject[aug.IMAGE][0].shape)
    # resized_subject = transform(subject)
    # print("Target subject shape: ", resized_subject[aug.IMAGE][0].shape)

    transform = CropOrPad((15, 5, 15))
    print("Source subject shape: ", subject[aug.IMAGE][0].shape)
    resized_subject = transform(subject)
    print("Target subject shape: ", resized_subject[aug.IMAGE][0].shape)


    def create_zero_centered_coordinate_mesh(shape):
        tmp = tuple([np.arange(i) for i in shape])
        coords = np.array(np.meshgrid(*tmp, indexing='ij')).astype(float)
        for d in range(len(shape)):
            coords[d] -= ((np.array(shape).astype(float) - 1) / 2.)[d]
        return coords


    # print(create_zero_centered_coordinate_mesh(image1.shape).transpose(1, 2, 3, 0))

    tmp = tuple([np.arange(i) for i in image1.shape])
    coords = np.array(np.meshgrid(*tmp, indexing='ij')).astype(float)
    print(coords.transpose(1, 2, 3, 0))

    # import SimpleITK as sitk
    # array = sitk.GetArrayFromImage(sitk.ReadImage(r"D:\Datasets\DKFZ\AFK_M1f_cropped.nii.gz"))
    # sitk.WriteImage(sitk.GetImageFromArray(transformed_array), r"D:\Datasets\DKFZ\AFK_M1f_cropped_tmp.nii.gz")