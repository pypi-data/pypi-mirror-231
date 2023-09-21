from setuptools import setup


def read_requirements_txt():
    lines = open('requirements.txt', 'r').readlines()
    return [l.strip() for l in lines]


setup(
    name='glue_ray_etl',
    version='0.2.1',
    packages=['glue_ray_etl', 'glue_ray_etl.io', 'glue_ray_etl.multi',
              'glue_ray_etl.spark', 'glue_ray_etl.spark.run'],
    url='https://github.com/archiba/glue-ray-etl',
    license='',
    author='archiba',
    author_email='',
    description='',
    include_package_data=True,
    install_requires=read_requirements_txt()
)
