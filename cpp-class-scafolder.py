#!/usr/bin/env python3
import helpers
import CppHeaderParser
import sys
import os
import re

def generate_cpp(methods, className, headerFileName):
	contents = f"#include \"{headerFileName}\""

	for method in methods["private"]:
		signature = f"{method['rtnType']} {className}::{method['name']}("

		for parameter in method["parameters"]:
			signature += f"{parameter['name']} {parameter['type']}, "
		signature += "){}"
		contents += os.linesep + signature
	return contents

expectedSpecialParams = {'o','i','h'}
foundSpecial = helpers.get_marked_params(sys.argv, expectedSpecialParams)

cppHeader = CppHeaderParser.CppHeader(sys.argv[1])

test = generate_cpp(cppHeader.classes["ABCD"]["methods"],"ABCD", os.path.basename(sys.argv[1]))
print(test)



