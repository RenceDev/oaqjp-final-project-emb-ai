from setuptools import setup, find_packages

setup(
    name='EmotionDetection',  # Name of your package
    version='0.1',
    packages=find_packages(),  # Automatically finds all packages in the project
    install_requires=[         # List dependencies (empty if there are none)
        # 'some_dependency',
    ],
    author='Your Name',
    author_email='your_email@example.com',
    description='An AI-based emotion detection application',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/emotion-detection',  # Replace with your repository URL
)
