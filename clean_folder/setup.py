from setuptools import setup


setup(name='sort_files_homework',
      version='0.0.1',
      description='Cleaner Files',
      url='https://github.com/Sanyavas/hwork6.git',
      author='Oleksandr Vasylyna',
      author_email='vasilinaoleksanrd@gmail.com',
      license='MIT',
      include_package_datd=True,
      entry_points={"console_scripts": [
            "clean-folder=clean_folder.clean:run"]}
      )


