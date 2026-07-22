from setuptools import setup, find_packages

setup(
    name="oto-debug",
    version="0.1.0",
    author="ahmtsalih",
    description="Terminal üzerinde çalışan, yapay zeka destekli otonom hata ayıklayıcı (debugger).",
    long_description="Terminalinizde çöken Python kodlarını anında analiz eden ve Gemini AI kullanarak çözüm önerilerini doğrudan terminale basan CLI aracı.",
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "typer",
        "rich",
        "google-genai"
    ],
    entry_points={
        "console_scripts": [
            "oto-debug=oto_debug.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Debuggers",
    ],
    python_requires=">=3.7",
)