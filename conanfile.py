from conans import ConanFile, AutoToolsBuildEnvironment, tools


class LibarciveConan(ConanFile):
    name = "libarchive"
    version = "3.3.3"
    license = "https://raw.githubusercontent.com/libarchive/libarchive/master/COPYING"
    author = "Alexis Lopez Zubieta <contact@azubieta.net>"
    url = "https://github.com/appimage-conan-community/conan-libarchive"
    description = "Libarchive for use in AppImage"
    topics = ("libarchive", "iso", "tar")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fpic": [True, False]}
    default_options = {"shared": False, "fpic": True}

    def source(self):
        tools.download("https://libarchive.org/downloads/libarchive-3.3.3.tar.gz",
                       "libarchive-3.3.3.tar.gz")
        tools.untargz("libarchive-3.3.3.tar.gz")

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.fpic = True
        env_build_vars = autotools.vars
        configure_args = ["--disable-bsdtar", "--disable-bsdcat", "--disable-bsdcpio", "--with-zlib",
                          "--without-bz2lib", "--without-iconv", "--without-lz4", "--without-lzma", "--without-lzo2",
                          "--without-nettle", "--without-openssl", "--without-xml2", "--without-expat"]

        if self.options["shared"]:
            configure_args += ["--enable-shared", "--disable-static"]
        else:
            configure_args += ["--disable-shared", "--enable-static"]

        if self.options["fpic"]:
            configure_args += ["--with-pic"]

        autotools.configure(configure_dir="libarchive-3.3.3", vars=env_build_vars,
                            args=configure_args)

        autotools.make(vars=env_build_vars)
        autotools.install(vars=env_build_vars)

    def package_info(self):
        self.cpp_info.libs = ["archive"]
        self.cpp_info.builddirs = ["lib/pkgconfig/"]
