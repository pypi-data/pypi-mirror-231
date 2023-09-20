import os
import subprocess
import sys
import numpy as np


def _dummyimport():
    import Cython


try:
    from . import locatepixelcolorcompiled
except Exception as e:
    cstring = """# distutils: language=c
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
	return my_dict"""
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
    numpyincludefolder = np.get_include()
    compilefile = (
        """
	from setuptools import Extension, setup
	from Cython.Build import cythonize
	ext_modules = Extension(**{'py_limited_api': False, 'name': 'locatepixelcolorcompiled', 'sources': ['locatepixelcolorcompiled.pyx'], 'include_dirs': [\'"""
        + numpyincludefolder
        + """\'], 'define_macros': [], 'undef_macros': [], 'library_dirs': [], 'libraries': [], 'runtime_library_dirs': [], 'extra_objects': [], 'extra_compile_args': [], 'extra_link_args': [], 'export_symbols': [], 'swig_opts': [], 'depends': [], 'language': None, 'optional': None})

	setup(
		name='locatepixelcolorcompiled',
		ext_modules=cythonize(ext_modules),
	)
			"""
    )
    with open(pyxfile_setup_complete_path, mode="w", encoding="utf-8") as f:
        f.write(
            "\n".join(
                [x.lstrip().replace(os.sep, "/") for x in compilefile.splitlines()]
            )
        )
    subprocess.run(
        [sys.executable, pyxfile_setup_complete_path, "build_ext", "--inplace"],
        cwd=dirname,
        shell=True,
        env=os.environ.copy(),
    )
    from . import locatepixelcolorcompiled


def search_colors(pic, colors):
    if not isinstance(colors, np.ndarray):
        colors = np.array(colors, dtype=np.uint8)
    pipi = pic.ravel()
    cololo = colors.ravel()
    totallengthcolor = cololo.shape[0] - 1
    totallenghtpic = pipi.shape[0] - 1
    width = pic.shape[1]
    resus0 = locatepixelcolorcompiled.searchforcolor(
        pipi, cololo, width, totallenghtpic, totallengthcolor
    )
    return resus0
