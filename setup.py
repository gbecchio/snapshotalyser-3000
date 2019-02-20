from setuptools import setup


setup(
    name="snapshotalyser-3000",
    version="0.1",
    author="Grégory Becchio",
    author_email="gbecchio@yahoo.fr",
    description="SnapshotAlyser 3000 is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=["shotty"],
    url="https://github.com/gbecchio/snapshotalyser-3000",
    install_requires=[
    	"click",
    	"boto3"
    ],
    entry_points='''
    	[console_scripts]
    	shotty=shotty.shotty:cli
    ''',

)