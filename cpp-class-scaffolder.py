#!/usr/bin/env python3
import helpers
import CppHeaderParser
import sys
import os
import re

def generate_cpp(methods, className, headerFileName):
	contents = f"#include \"{headerFileName}\""

	for method in methods["public"] + methods["private"] + methods["protected"]:
		signature = f"{method['rtnType']} {className}::{method['name']}("
		
		i = 0
		while i < (len(method["parameters"]) - 1):
			parameter =  method["parameters"][i]
			signature += f"{parameter['type']} {parameter['name']}, "
			i += 1

		parameter = method["parameters"][i]
		signature += f"{parameter['type']} {parameter['name']}"

		signature += "){}"

		contents += os.linesep + signature
	return contents

headerPath = sys.argv[1]
outputPath = sys.argv[2]
cppHeader = CppHeaderParser.CppHeader(headerPath)

for cppClass in cppHeader.classes:
	output = open(f"{outputPath}/{cppClass}.cpp", "w")
	output.write(generate_cpp(cppHeader.classes[cppClass]["methods"], cppClass, os.path.basename(sys.argv[1])))




