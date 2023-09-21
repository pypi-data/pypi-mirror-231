from stio.microscopy import MicroscopeSmallImage, SlideType
# import javabridge
# import bioformats
# import numpy as np
# import pycziutils
# from pylibCZIrw import czi as pyczi
# from tqdm.contrib import itertools as it


class ZeissMicroscopeFile(MicroscopeSmallImage):
    def __init__(self, path):
        super(ZeissMicroscopeFile, self).__init__()
        self.device.manufacturer = SlideType.Zeiss.value
        self.images_path = path
        self.sizez = None
        self.sizet = None
        self.sizec = None

#     # 读取显微镜拼接大图
#     def read_stitched_image(self):
#         imagereader = bioformats.ImageReader(self.images_path)
#         image = imagereader.read(rescale=False, wants_max_intensity=True)
#         self.stitched_image = np.transpose(image[0], (2, 0, 1))
#         return self.stitched_image
#
#     # 读取原始FOV小图，返回所有维度按先行后列得FOV列表
#     def read_fov_image(self):
#         reader = pycziutils.get_tiled_reader(self.images_path)
#         tiled_czi_ome_xml = pycziutils.get_tiled_omexml_metadata(self.images_path)
#         tiled_properties_dataframe = pycziutils.parse_planes(tiled_czi_ome_xml)
#         images = []
#         for i, row in tiled_properties_dataframe.iterrows():
#             image = reader.read(series=row["image"], )
#             image = np.transpose(image, (2, 0, 1))
#             images.append(image)
#         self.scan.fov_images = images
#         return images
#
#     def read_meta_data(self):
#         xml = bioformats.get_omexml_metadata(self.images_path)
#         self.scan.overlap = xml.split("Overlap")[1].split("Value")[1].replace(">[", "").\
#             replace("</", "").replace("]", "")
#         xml = bioformats.omexml.OMEXML(xml)
#         # height
#         self.scan.mosaic_height = xml.image().Pixels.SizeX
#         # width
#         self.scan.mosaic_width = xml.image().Pixels.SizeY
#         # stack_count
#         self.sizez = xml.image().Pixels.SizeZ
#         # timepoint_count
#         self.sizet = xml.image().Pixels.SizeT
#         # channel_count
#         self.sizec = xml.image().Pixels.SizeC
#         # 图像位深
#         self.scan.fov_dtype = xml.image().Pixels.PixelType
#         # 拍摄时间
#         self.scan.scan_time = xml.image().AcquisitionDate
#
#     # 写入图像,会自动写入metadata,array.shape示例(16, 512, 512, 3)
#     def write_image(self, array):
#         self.scan.mosaic_height = array.shape[-1]
#         self.sizez = array.shape[0]
#         with pyczi.create_czi(self.images_path, exist_ok=True) as czidoc_w:
#             for z, ch in it.product(range(self.sizez), range(self.scan.mosaic_height)):
#                 # get the 2d array for the current plane and add axis to get (Y, X, 1) as shape
#                 array2d = array[z, ..., ch][..., np.newaxis]
#                 # write the plane with shape (Y, X, 1) to the new CZI file
#                 czidoc_w.write(data=array2d, plane={"Z": z, "C": ch})
#
#
# def main():
#     # 启动java虚拟机
#     javabridge.start_vm(class_path=bioformats.JARS)
#     mmf = ZeissMicroscopeFile(r"D:\DOWN\zeiss\20210427-T242-Z2-L-M024-01222.czi")
#     # mmf.read_meta_data()
#     # print(mmf.scan.mosaic_height)
#     # print(mmf.scan.mosaic_width)
#     # print(mmf.sizez)
#     # print(mmf.sizet)
#     # print(mmf.sizec)
#     # print(mmf.scan.scan_time)
#     # print(mmf.scan.fov_dtype)
#     # print(mmf.bit_depth())
#     # large = mmf.read_fov_image()
#     # fov_images = mmf.read_stitched_image()
#     a = np.zeros((16, 1024, 512, 3), dtype=np.uint8)
#     mmf.write_image(a)
#     # 关闭java虚拟机
#     javabridge.kill_vm()
#
#
# if __name__ == '__main__':
#     main()
