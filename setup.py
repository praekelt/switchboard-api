from setuptools import setup, find_packages


def parse_requirements(filename):
    with open(filename) as reqfile:
        lines = [l.strip() for l in reqfile.readlines()]
    # remove blank lines
    lines = [l for l in lines if l]
    # remove comments
    lines = [l for l in lines if not l.startswith('#')]
    return lines

setup(
    name="switchboard-api",
    version="0.0.1",
    url='http://github.com/praekelt/switchboard-api',
    license='BSD',
    description="Python module implementing an API for the MoH in Tanzania.",
    author='Christian Budoya',
    author_email='cbudoya@gmail.com',
    packages=find_packages(),
    install_requires=['setuptools'] + parse_requirements('requirements.pip'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
