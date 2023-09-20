from setuptools import setup, find_packages
# from setuptools import find_packages
# from distutils.core import setup
#print(find_packages())
setup(
    name="snb_plugin",
    version="1.2",
    author="wang xin yi",
    author_email="wangxinyi@smartnotebook.tech",
    description="smart-notebook plugin",
    url="https://snb.data-pivot.com/",
    packages=find_packages(),
    package_data={'pytransform': ['_pytransform.so']},
    # packages=['.'],
    # install_requires=["pandas==1.4.3", "sqlalchemy==1.3.24", "pandasql==0.7.3"]

    entry_points={
        'sqlalchemy.dialects': [
            'spark = snb_plugin.pyspark.sqlalchemy_hive:HiveDialect',
            "spark.https = snb_plugin.pyspark.sqlalchemy_hive:HiveHTTPSDialect",
        ],
    }
)
