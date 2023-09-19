from setuptools import setup, find_packages

setup(
    name="Agent_Function_Calling",
    version="0.2.2",
    description="A tool to easily integrate custom functions with OpenAI's GPT models.",
    author="Thierry Mayrand",
    author_email="thierry.mayrand.ads@gmail.com",
    license="MIT",  # or another license you're using
    packages=find_packages(),
    install_requires=[
        "openai",
        "python-dotenv",
        "PyYAML",
    ],
    entry_points={
        'console_scripts': [
            'run_agent=clean_agent.main:run_conversation',  # Update with your package name
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",  # or "4 - Beta" or "5 - Production/Stable"
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
