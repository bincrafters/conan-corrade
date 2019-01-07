[![Download](https://api.bintray.com/packages/magnum-graphics/public-conan/corrade%3Amagnum/images/download.svg) ](https://bintray.com/magnum-graphics/public-conan/corrade%3Amagnum/_latestVersion)
[![Build Status Travis](https://travis-ci.com/bincrafters/conan-corrade.svg?branch=stable%2F2018.10)](https://travis-ci.com/bincrafters/conan-corrade)
[![Build Status AppVeyor](https://ci.appveyor.com/api/projects/status/github/bincrafters/conan-corrade?branch=stable%2F2018.10&svg=true)](https://ci.appveyor.com/project/bincrafters/conan-corrade)

## Conan package recipe for [*corrade*](https://magnum.graphics/corrade)

Corrade is a multiplatform utility library written in C++11/C++14. It's used as a base for the Magnum graphics engine, among other things.

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/magnum-graphics/public-conan/corrade%3Amagnum).


## Issues

If you wish to report an issue or make a request for a package, please do so here:

[Issues Tracker](https://github.com/bincrafters/community/issues)


## For Users

### Basic setup

    $ conan install corrade/2018.10@magnum/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    corrade/2018.10@magnum/stable

    [generators]
    cmake

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.


## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create . magnum/stable


### Available Options
| Option        | Default | Possible Values  |
| ------------- |:----------------- |:------------:|
| shared      | False |  [True, False] |
| fPIC      | True |  [True, False] |
| build_deprecated      | False |  [True, False] |
| build_tests      | False |  [True, False] |
| with_interconnect      | True |  [True, False] |
| with_pluginmanager      | True |  [True, False] |
| with_testsuite      | True |  [True, False] |


## Add Remote

    $ conan remote add magnum "https://api.bintray.com/conan/magnum-graphics/public-conan"


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package corrade.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](https://github.com/bincrafters/conan-corrade/blob/stable/2018.10/LICENSE.md)
