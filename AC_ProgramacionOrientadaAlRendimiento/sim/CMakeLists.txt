set(CMAKE_CXX_STANDARD 20)
add_library(sim
        particle.hpp
        vector_3d.hpp
        malla.hpp
        malla.cpp
        calculadora.hpp
        calculadora.cpp
        simulacion.hpp
        simulacion.cpp
        progargs.cpp
        progargs.hpp
)

target_include_directories(sim PUBLIC ..)
#target_link_libraries(sim PRIVATE Microsoft.GSL::GSL)