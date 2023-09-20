from setuptools import setup

DIST_NAME = "pg_redis"
DIST_VERSION = "1.0.0"
__author__ = "baozilaji@gmail.com"

setup(
    name=DIST_NAME,
    version=DIST_VERSION,
    description="python game: redis",
    packages=[DIST_NAME],
    author=__author__,
    python_requires='>=3',
    install_requires=[
        'pg-environment>=0',
        'redis>=4.6.0',
    ],
)
