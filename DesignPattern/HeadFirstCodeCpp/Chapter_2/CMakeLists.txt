cmake_minimum_required(VERSION 2.6)
project(WeatherStation)
include_directories("${PROJECT_BINARY_DIR}")
add_executable(WeatherStation
   main.cpp 
   currentcondationsdisplay.cpp 
   weatherdata.cpp)
