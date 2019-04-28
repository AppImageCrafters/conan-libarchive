cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

find_package(PkgConfig)
pkg_check_modules(LIBARCHIVE REQUIRED IMPORTED_TARGET libarchive)

add_executable(example example.cpp)
target_link_libraries(example PkgConfig::LIBARCHIVE)
