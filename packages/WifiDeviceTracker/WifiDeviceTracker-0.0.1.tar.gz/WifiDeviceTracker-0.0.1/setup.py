from setuptools import setup, find_packages

def find_version():
    with open('WifiDeviceTracker/__init__.py', 'r') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.strip().split('=')[1].strip().strip("'")

setup(
    name='WifiDeviceTracker',
    version=find_version(),
    author='Josh Dietz',
    author_email='joshdietz@outlook.com',
    description='Python package to detect and classify various wifi devices',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/joshdietz/wifi_device_tracker',
    packages=['WifiDeviceTracker'],
    install_requires=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
