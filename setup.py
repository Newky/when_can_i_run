from setuptools import setup


def parse_requirements(requirements_path):
    requirements = []
    try:
        for line in open(requirements_path):
            if '#' not in line:
                requirements.append(line)
    except IOError:
        print("Could not open requirements file {}".format(requirements_path))

    return requirements


setup(
    name='when_can_i_run',
    version='0.0.1',
    description="Script which tells you at what times you can run.",
    author="Richard Delaney",
    author_email="richdel1991@gmail.com",
    install_requires=parse_requirements('requirements.txt'),
    scripts=['bin/when_can_i_run']
)
