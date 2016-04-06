cmake_minimum_required(VERSION 2.6)
project(Tutorial)

# 版本号
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)

# 定义 option
option (USE_MYMATH "使用自定义求根函数" ON)

# 配置一个头文件来传递 CMake 设置
configure_file (
    "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
    "${PROJECT_BINARY_DIR}/TutorialConfig.h"
    )

# 添加二进制树到搜索路径以搜索代码文件
include_directories("${PROJECT_BINARY_DIR}")

add_library(mymath mysqrt.cc)

# 添加 lib
if (USE_MYMATH)
    include_directories("${PROJECT_SOURCE_DIR}/mymath")
    add_subdirectory(mymath)
    set (EXTRA_LIBS ${EXTRA_LIBS} mymath)
endif (USE_MYMATH)

add_executable(Tutorial main.cc)
target_link_libraries(Tutorial ${EXTRA_LIBS})
