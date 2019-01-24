#include <iostream>
#include <archive.h>

int main() {
    std::cout << "LibArchive version: " << archive_version_string() << std::endl;
}
