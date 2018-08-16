from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add(settings={"arch": "x86_64"}, options={}, env_vars={}, build_requires={})
    builder.run()
