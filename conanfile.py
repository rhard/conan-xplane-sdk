from conans import ConanFile, CMake, tools
from conans.tools import download, unzip
import os


class XplanesdkConan(ConanFile):
    name = "xplane_sdk"
    version = "3.0.1"
    license = "Copyright (c) 2008, Sandy Barbour and Ben Supnik"
    url = "https://github.com/rhard/conan-xplane-sdk"
    description = "X-Plane plugin SDK"
    settings = "os"
    
    def source(self):
        zip_name = "XPSDK301.zip"
        download("http://developer.x-plane.com/wp-content/plugins/code-sample-generation/sample_templates/XPSDK301.zip", zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def package(self):
        self.copy("*")

    def package_info(self):
        self.cpp_info.includedirs.append('SDK/CHeaders/XPLM')
        self.cpp_info.includedirs.append('SDK/CHeaders/Widgets')
        if self.settings.os == "Windows":
            self.cpp_info.libdirs = ['SDK/Libraries/Win']
            self.cpp_info.libs = ["XPLM_64 XPWidgets_64"]
            self.cpp_info.defines.append("APL=0")
            self.cpp_info.defines.append("IBM=1")
            self.cpp_info.defines.append("LIN=0")
        elif self.settings.os == "Macos":
            self.cpp_info.libdirs = ['SDK/Libraries/Mac']
            self.cpp_info.exelinkflags.append("-F")
            self.cpp_info.exelinkflags.append(self.cpp_info.libdirs)
            self.cpp_info.exelinkflags.append("-framework XPLM -framework XPWidgets")
            self.cpp_info.sharedlinkflags = self.cpp_info.exelinkflags
            self.cpp_info.defines.append("APL=1")
            self.cpp_info.defines.append("IBM=0")
            self.cpp_info.defines.append("LIN=0")
        else:
            self.cpp_info.defines.append("APL=0")
            self.cpp_info.defines.append("IBM=0")
            self.cpp_info.defines.append("LIN=1")


