from setuptools import setup, find_packages

setup(
    name="k8s-assistant",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "anthropic",
        "openai",
        "mcp", # Ensure this package is available
    ],
    entry_points={
        'console_scripts': [
            'k8s-assistant=k8s_assistant.main:cli_entry_point',  # Main entry point for the CLI
        ],
    },
    python_requires='>=3.12',
    author="Harsh D",
    description="A natural language interface for Kubernetes troubleshooting",
    keywords="kubernetes, CLI, troubleshooting, assistant",
    include_package_data=True,
    package_data={
        'k8s_assistant': [
            'server.py',
            'tools/*.py',
            'llms/*.py',
        ],
    },
    zip_safe=False
)