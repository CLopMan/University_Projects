# General
cmake_minimum_required(VERSION 3.25)
project(fluid LANGUAGES CXX)


# Estandar
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Opciones de compilacion
add_compile_options(-Wall -Wextra -Werror -pedantic -pedantic-errors)
set(CMAKE_CXX_FLAGS_RELEASE "-march=native -O3 -Ofast -DNDEBUG")
set(-DCMAKE_CXX_FLAGS=fsanitize=address -fno-omit-frame-pointer)

include(FetchContent)

#Enable google test
FETCHCONTENT_DECLARE(
        googletest
        GIT_REPOSITORY https://github.com/google/googletest.git
        GIT_TAG v1.14.0
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FETCHCONTENT_MAKEAVAILABLE(googletest)

set(CMAKE_CXX_CLANG_TIDY clang-tidy -header-filter=.*)

# incluir todos los directorios de código
include_directories(PUBLIC .)

# Subdirectorios
add_subdirectory(sim)
add_subdirectory(fluid)

enable_testing()
add_subdirectory(utest)
add_subdirectory(ftest)