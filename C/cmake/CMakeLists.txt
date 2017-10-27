cmake_minimum_required(VERSION 2.4)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}")

if (${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    set(MACOSX TRUE)
    message(${CMAKE_SYSTEM_NAME})
endif()

find_package(GLib2)
if(GLIB2_FOUND)
    message('${GLIB2_INCLUDE_DIR}')
    message('${GLIB2_LIBRARY}')
endif()

find_package(FRIBIDI)
if(FRIBIDI_FOUND)
    message("Found FriBiDi")
    message(${FRIBIDI_INCLUDE_DIR})
    message(${FRIBIDI_LIBRARY})
endif()
