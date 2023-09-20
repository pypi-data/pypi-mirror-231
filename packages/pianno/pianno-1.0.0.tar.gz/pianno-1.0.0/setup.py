from setuptools import setup, find_packages
setup(name='pianno',
      version = "1.0.0",
      author = 'yuqiu zhou',
      author_email = '20211520004@fudan.edu.cn',
      license='MIT',
      packages = find_packages(include=['pianno','data']),
      description='Pattern Image Annotation',
      include_package_data = True,
      package_data = {
          'data': ['dlPFC-151674/filtered_feature_bc_matrix.h5',
                   'dlPFC-151674/spatial/scalefactors_json.json',
                   'dlPFC-151674/spatial/tissue_hires_image.png',
                   'dlPFC-151674/spatial/tissue_lowres_image.png',
                   'dlPFC-151674/spatial/tissue_positions_list.csv']
      },
      install_requires = [
          'anndata==0.8.0',
          'matplotlib==3.5.1',
          'numpy==1.19.5',
          'opencv-python==4.5.5.64',
          'pandas==1.4.1',
          'rpy2==3.4.5',
          'scanpy==1.9.1',
          'scikit-image==0.19.2',
          'scikit-learn==1.0.2',
          'scipy==1.8.0',
          'squidpy==1.2.2',
          'tensorflow-gpu==2.6.0',
          'tensorflow-probability==0.14.0'
      ])

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('pianno', parent_package, top_path)
    return config

if __name__ == "__main__":
    from numpy.distutils.core import setup
    config = configuration(top_path='').todict()
    setup(**config)
