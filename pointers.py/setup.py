from setuptools import Extension, setup

with open("./README.md") as f:
    long_desc: str = f.read()

if __name__ == "__main__":
    setup(
        name="pointers_clone.py",
        version="0.0.1",
        packages=["pointers"],
        license="MIT",
        project_urls={
            "Source": "https://github.com/ZeroIntensity/pointers.py",
            "Documentation": "https://pointers.zintensity.dev/",
        },
        package_dir={"": "src"},
        ext_modules=[Extension("_pointers", ["./src/mod.c"])],
    )
