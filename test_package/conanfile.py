import os

from conans import ConanFile, CMake, tools


class LibarciveTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    build_requires = ["cmake_installer/3.13.0@conan/stable"]
    generators = ("pkg_config")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            self.run(".%sexample" % os.sep)
