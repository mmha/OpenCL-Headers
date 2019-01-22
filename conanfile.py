from conans import ConanFile

class OpenCLHeaders(ConanFile):
    name = "opencl-headers"
    version = "20190117"
    exports_sources = "CL/*"
    no_copy_source = True

    def package(self):
        self.copy("*.h", dst="include/CL", src="CL")