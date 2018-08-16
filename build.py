from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds()
    filtered_builds = []
    for settings, options, env_vars, build_requires, reference in builder.items:
        if settings["build_type"] != "Debug" and settings["arch"] != "x86" and settings["compiler.runtime"] != "MD":
             filtered_builds.append([settings, options, env_vars, build_requires])
    builder.builds = filtered_builds
    builder.run()
