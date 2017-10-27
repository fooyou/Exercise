cmake_minimum_required(VERSION 3.8)
project(sort)

set(CMAKE_C_STANDARD 99)
set(CMAKE_EXPORT_COMPILE_COMMANDS 1)

set(demos_NAMES
    sort
    )

foreach(demo ${demos_NAMES})
    add_executable(${demo} ${demo}.c)
endforeach(demo)

