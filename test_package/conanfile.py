import os

from conans import ConanFile, CMake, tools


class XplanesdkTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
    
    def test(self):
        self.output.success("Linkage is OK")
