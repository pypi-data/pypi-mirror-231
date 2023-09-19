# Generates and installs simple Cython modules with specified settings. If you are overwhelmed by the compiler directives and the creation of the setup.py file, this is right for you. 

## Tested against Windows 10 / Python 3.11 / Anaconda

### pip install cythonautoinstall


This function takes Cython code along with various setup parameters and generates a
Cython module, compiles it, and installs it as a Python package. It handles the
generation of the Cython code, the creation of a setup script, compilation, and
installation. Made for people who write simple scripts and are overwhelmed 
by the compiler directives and the creation of the setup.py file


```python
Parameters:
	cython_code (str): The Cython code to be compiled into a module.
	foldername (str): The name of the folder where the package will be installed.
	setup_name (str): The name of the module to be generated.
	setup_sources (tuple or list): A tuple or list of source file paths.
	setup_include_dirs (tuple or list): A tuple or list of include directory paths.
	setup_py_limited_api (bool, optional): Whether to use Python limited API. Default is False.
	setup_define_macros (tuple or list, optional): Define macros for the compilation. Default is ().
	setup_undef_macros (tuple or list, optional): Undefine macros for the compilation. Default is ().
	setup_library_dirs (tuple or list, optional): Library directories. Default is ().
	setup_libraries (tuple or list, optional): Libraries to link against. Default is ().
	setup_runtime_library_dirs (tuple or list, optional): Runtime library directories. Default is ().
	setup_extra_objects (tuple or list, optional): Extra objects to link with. Default is ().
	setup_extra_compile_args (tuple or list, optional): Extra compilation arguments. Default is ().
	setup_extra_link_args (tuple or list, optional): Extra link arguments. Default is ().
	setup_export_symbols (tuple or list, optional): Exported symbols. Default is ().
	setup_swig_opts (tuple or list, optional): SWIG options. Default is ().
	setup_depends (tuple or list, optional): Dependency files. Default is ().
	setup_language (str, optional): Language for compilation. Default is None.
	setup_optional (tuple or list, optional): Optional components. Default is None.
	extra_directives (str, optional): Additional Cython compiler directives. Default is "".
	distutils_extra_compile_args (str, optional): Additional distutils compilation arguments. Default is "".
	distutils_extra_link_args (str, optional): Additional distutils link arguments. Default is "".
	distutils_language (str, optional): Language for distutils compilation. Default is "".
	distutils_define_macros (str, optional): Define macros for distutils compilation. Default is "NPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION".
	cython_binding (bool, optional): Whether to generate Cython bindings. Default is True.
	cython_boundscheck (bool, optional): Enable bounds checking. Default is True.
	cython_wraparound (bool, optional): Enable wraparound checking. Default is True.
	cython_initializedcheck (bool, optional): Enable initialized variable checking. Default is False.
	cython_nonecheck (bool, optional): Enable None checking. Default is False.
	cython_overflowcheck (bool, optional): Enable overflow checking. Default is False.
	cython_overflowcheck_fold (bool, optional): Enable folding of overflow checks. Default is True.
	cython_embedsignature (bool, optional): Embed function signatures. Default is False.
	cython_embedsignature_format (str, optional): Format for embedded signatures. Default is "c".
	cython_cdivision (bool, optional): Enable C division. Default is False.
	cython_cdivision_warnings (bool, optional): Enable C division warnings. Default is False.
	cython_cpow (bool, optional): Enable C pow function. Default is False.
	cython_c_api_binop_methods (bool, optional): Enable C API binary operator methods. Default is False.
	cython_profile (bool, optional): Enable profiling. Default is False.
	cython_linetrace (bool, optional): Enable line tracing. Default is False.
	cython_infer_types (bool, optional): Enable type inference. Default is False.
	cython_language_level (int, optional): Cython language level. Default is 3.
	cython_c_string_type (str, optional): C string type. Default is "bytes".
	cython_c_string_encoding (str, optional): C string encoding. Default is "default".
	cython_type_version_tag (bool, optional): Enable type version tag. Default is True.
	cython_unraisable_tracebacks (bool, optional): Enable unraisable tracebacks. Default is False.
	cython_iterable_coroutine (bool, optional): Enable iterable coroutine support. Default is True.
	cython_annotation_typing (bool, optional): Enable annotation typing. Default is True.
	cython_emit_code_comments (bool, optional): Enable code comments in the generated code. Default is False.
	cython_cpp_locals (bool, optional): Enable C++ local variable support. Default is False.

Returns:
	str: The path to the generated package's __init__.py file.

Note:
	Read https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#compiler-directives

Example:

import numpy as np

cython_code = '''
from cython.parallel cimport prange
cimport cython
import numpy as np
cimport numpy as np
import cython
from collections import defaultdict

cpdef searchforcolor(unsigned char[:] pic, unsigned char[:] colors, int width, int totallengthpic, int totallengthcolor):
	cdef my_dict = defaultdict(list)
	cdef int i, j
	cdef unsigned char r,g,b
	for i in prange(0, totallengthcolor, 3,nogil=True):
		r = colors[i]
		g = colors[i + 1]
		b = colors[i + 2]
		for j in range(0, totallengthpic, 3):
			if (r == pic[j]) and (g == pic[j+1]) and (b == pic[j+2]):
				with gil:
					my_dict[(r,g,b)].append(j )

	for key in my_dict.keys():
		my_dict[key] = np.dstack(np.divmod(np.array(my_dict[key]) // 3, width))[0]
	return my_dict
'''

fx = generate_auto_install(
	cython_code,
	foldername="locatepixelcolcompiledpy",
	setup_py_limited_api=False,
	setup_name="locatepixelcolorcompiled",
	setup_sources=("locatepixelcolorcompiled.pyx",),
	setup_include_dirs=(np.get_include(),),
	setup_define_macros=(),
	setup_undef_macros=(),
	setup_library_dirs=(),
	setup_libraries=(),
	setup_runtime_library_dirs=(),
	setup_extra_objects=(),
	setup_extra_compile_args=(),
	setup_extra_link_args=(),
	setup_export_symbols=(),
	setup_swig_opts=(),
	setup_depends=(),
	setup_language=None,
	setup_optional=None,
	extra_directives="",
	distutils_extra_compile_args="/openmp",
	distutils_extra_link_args="/openmp",
	distutils_language="c",
	distutils_define_macros="NPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION",
	cython_binding=False,
	cython_boundscheck=False,
	cython_wraparound=False,
	cython_initializedcheck=False,
	cython_nonecheck=False,
	cython_overflowcheck=True,
	cython_overflowcheck_fold=False,
	cython_embedsignature=False,
	cython_embedsignature_format="c",
	cython_cdivision=True,
	cython_cdivision_warnings=False,
	cython_cpow=True,
	cython_c_api_binop_methods=True,
	cython_profile=False,
	cython_linetrace=False,
	cython_infer_types=False,
	cython_language_level=3,
	cython_c_string_type="bytes",
	cython_c_string_encoding="default",
	cython_type_version_tag=True,
	cython_unraisable_tracebacks=False,
	cython_iterable_coroutine=True,
	cython_annotation_typing=True,
	cython_emit_code_comments=False,
	cython_cpp_locals=True,
)
print(fx)

# create a Python file
r'''
import numpy as np
import cv2
import locatepixelcolcompiledpy

def search_colors(pic,colors):
	if not isinstance(colors, np.ndarray):
		colors = np.array(colors, dtype=np.uint8)
	pipi = pic.ravel()
	cololo = colors.ravel()
	totallengthcolor = cololo.shape[0] - 1
	totallenghtpic = pipi.shape[0]-1
	width = pic.shape[1]
	resus0 = locatepixelcolcompiledpy.locatepixelcolorcompiled.searchforcolor(pipi, cololo,width,totallenghtpic,totallengthcolor)
	return resus0


# 4525 x 6623 x 3 picture https://www.pexels.com/pt-br/foto/foto-da-raposa-sentada-no-chao-2295744/
picx = r"C:\Users\hansc\Downloads\pexels-alex-andrews-2295744.jpg"
pic = cv2.imread(picx)
colors0 = np.array([[255, 255, 255]],dtype=np.uint8)
resus0 = search_colors(pic=pic, colors=colors0)
colors1=np.array([(66,  71,  69),(62,  67,  65),(144, 155, 153),(52,  57,  55),(127, 138, 136),(53,  58,  56),(51,  56,  54),(32,  27,  18),(24,  17,   8),],dtype=np.uint8)
resus1 =  search_colors(pic=pic, colors=colors1)
'''
This is how a generated file looks like (it can be edited after the generation):


	import os
	import subprocess
	import sys

	def _dummyimport():
		import Cython
	try:
		from . import locatepixelcolorcompiled
	except Exception as e:

		cstring = '''# distutils: language=c
	# distutils: extra_compile_args=/openmp
	# distutils: extra_link_args=/openmp
	# distutils: define_macros=NPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION
	# cython: binding=False
	# cython: boundscheck=False
	# cython: wraparound=False
	# cython: initializedcheck=False
	# cython: nonecheck=False
	# cython: overflowcheck=True
	# cython: overflowcheck.fold=False
	# cython: embedsignature=False
	# cython: embedsignature.format=c
	# cython: cdivision=True
	# cython: cdivision_warnings=False
	# cython: cpow=True
	# cython: c_api_binop_methods=True
	# cython: profile=False
	# cython: linetrace=False
	# cython: infer_types=False
	# cython: language_level=3
	# cython: c_string_type=bytes
	# cython: c_string_encoding=default
	# cython: type_version_tag=True
	# cython: unraisable_tracebacks=False
	# cython: iterable_coroutine=True
	# cython: annotation_typing=True
	# cython: emit_code_comments=False
	# cython: cpp_locals=True


	from cython.parallel cimport prange
	cimport cython
	import numpy as np
	cimport numpy as np
	import cython
	from collections import defaultdict

	cpdef searchforcolor(unsigned char[:] pic, unsigned char[:] colors, int width, int totallengthpic, int totallengthcolor):
		cdef my_dict = defaultdict(list)
		cdef int i, j
		cdef unsigned char r,g,b
		for i in prange(0, totallengthcolor, 3,nogil=True):
			r = colors[i]
			g = colors[i + 1]
			b = colors[i + 2]
			for j in range(0, totallengthpic, 3):
				if (r == pic[j]) and (g == pic[j+1]) and (b == pic[j+2]):
					with gil:
						my_dict[(r,g,b)].append(j )

		for key in my_dict.keys():
			my_dict[key] = np.dstack(np.divmod(np.array(my_dict[key]) // 3, width))[0]
		return my_dict'''
		pyxfile = f"locatepixelcolorcompiled.pyx"
		pyxfilesetup = f"locatepixelcolorcompiled_setup.py"

		dirname = os.path.abspath(os.path.dirname(__file__))
		pyxfile_complete_path = os.path.join(dirname, pyxfile)
		pyxfile_setup_complete_path = os.path.join(dirname, pyxfilesetup)

		if os.path.exists(pyxfile_complete_path):
			os.remove(pyxfile_complete_path)
		if os.path.exists(pyxfile_setup_complete_path):
			os.remove(pyxfile_setup_complete_path)
		with open(pyxfile_complete_path, mode="w", encoding="utf-8") as f:
			f.write(cstring)

		compilefile = '''
		from setuptools import Extension, setup
		from Cython.Build import cythonize
		ext_modules = Extension(**{'py_limited_api': False, 'name': 'locatepixelcolorcompiled', 'sources': ['locatepixelcolorcompiled.pyx'], 'include_dirs': ['C:\\Users\\hansc\\.conda\\envs\\dfdir\\Lib\\site-packages\\numpy\\core\\include'], 'define_macros': [], 'undef_macros': [], 'library_dirs': [], 'libraries': [], 'runtime_library_dirs': [], 'extra_objects': [], 'extra_compile_args': [], 'extra_link_args': [], 'export_symbols': [], 'swig_opts': [], 'depends': [], 'language': None, 'optional': None})

		setup(
			name='locatepixelcolorcompiled',
			ext_modules=cythonize(ext_modules),
		)
				'''
		with open(pyxfile_setup_complete_path, mode="w", encoding="utf-8") as f:
			f.write('\n'.join([x.lstrip().replace(os.sep, "/") for x in compilefile.splitlines()]))
		subprocess.run(
			[sys.executable, pyxfile_setup_complete_path, "build_ext", "--inplace"],
			cwd=dirname,
			shell=True,
			env=os.environ.copy(),
		)
		from . import locatepixelcolorcompiled


```