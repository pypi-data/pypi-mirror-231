from setuptools import find_packages, setup

setup(
    name='albertai',  # the name of the package
    version='0.0.3',
    author='Professor',
    author_email='your.email@domain.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/embedchain/embedchain',  # link to your github page or website
    description='A modified version of Embedchain.',
    install_requires=["beautifulsoup4", "chromadb", "discord", "elasticsearch", "fastapi-poe", "flask", "gpt4all", "langchain", "llama-hub", "openai", "pypdf", "python-dotenv", "pytube", "requests", "sentence-transformers", "slack-sdk", "tiktoken", "torch", "twilio", "youtube-transcript-api"],  # List of dependencies
)