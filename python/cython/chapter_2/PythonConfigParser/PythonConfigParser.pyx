#!/usr/bin/env python
# coding: utf-8
# @File Name: PythonConfigParser.pyx
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-11 10:11:14
# @Last Modified: 2017-11-11 11:11:11
# @Description:

from ConfigParser import SafeConfigParser
from libc.stdlib cimport malloc


cdef public struct ConfigSections:
    size_t number_of_sections
    char** sections


cdef public struct ConfigSectionKeys:
    size_t number_of_keys
    char** keys


cdef public void ParseSectionsFromConfig(const char* config_path, ConfigSections* const sections):
    parser = SafeConfigParser()
    with open(config_path) as f:
        try:
            parser.readfp(f)
            sectionsInConfig = parser.sections()
            sections.number_of_sections = len(sectionsInConfig)
            sections.sections = <char**>malloc(sections.number_of_sections)
            for i in range(sections.number_of_sections):
                sections.sections[i] = sectionsInConfig[i]
        except:
            sections.number_of_sections = 0
            sections.sections = NULL


cdef public void ParseKeysFromSectionFromConfig(const char* config_path, const char* section, ConfigSectionKeys* keys):
    parser = SafeConfigParser()
    with open(config_path) as f:
        try:
            parser.readfp(f)
            tuple_values_in_section = parser.items(section)
            keys.number_of_keys = len(tuple_values_in_section)
            keys.keys = <char**>malloc(keys.number_of_keys)
            for i in range(keys.number_of_keys):
                keys.keys[i] = tuple_values_in_section[i][0]
        except:
            keys.number_of_keys = 0
            keys.keys = NULL


cdef public char* ParseConfigKeyFromSection(const char* config_path, const char* section, const char* key):
    parser = SafeConfigParser()
    with open(config_path) as f:
        try:
            parser.readfp(f)
            return parser.get(section, key)
        except:
            return NULL
