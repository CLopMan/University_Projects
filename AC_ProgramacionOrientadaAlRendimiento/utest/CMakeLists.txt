enable_testing()

add_executable(utest
        main.cpp
        vector3d_test.cpp
        calculadora_test.cpp
        progargs_test.cpp
        tools_trazas.cpp
        tools_trazas.hpp
        etapas_simulacion_test.cpp
        malla_test.cpp
        etapas_simulacion_test.cpp)

target_link_libraries(utest
        PRIVATE
        sim
        GTest::gtest_main
        #Microsoft.GSL::GSL
)



include(GoogleTest)
gtest_discover_tests(utest)
