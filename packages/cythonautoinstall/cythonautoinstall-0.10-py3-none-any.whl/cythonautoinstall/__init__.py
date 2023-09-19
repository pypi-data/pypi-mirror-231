import os
import Cython


def create_compiler_directives(
    extra_directives="",
    distutils_extra_compile_args="",
    distutils_extra_link_args="",
    distutils_language="c",
    distutils_define_macros="NPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION",
    cython_binding=True,
    cython_boundscheck=True,
    cython_wraparound=True,
    cython_initializedcheck=False,
    cython_nonecheck=False,
    cython_overflowcheck=False,
    cython_overflowcheck_fold=True,
    cython_embedsignature=False,
    cython_embedsignature_format="c",
    cython_cdivision=False,
    cython_cdivision_warnings=False,
    cython_cpow=False,
    cython_c_api_binop_methods=False,
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
    cython_cpp_locals=False,
):
    compilerdirectives = rf"""
    {extra_directives}
    # distutils: language={distutils_language}
    # distutils: extra_compile_args={distutils_extra_compile_args}
    # distutils: extra_link_args={distutils_extra_link_args}
    # distutils: define_macros={distutils_define_macros}
    # cython: binding={cython_binding}
    # cython: boundscheck={cython_boundscheck}
    # cython: wraparound={cython_wraparound}
    # cython: initializedcheck={cython_initializedcheck}
    # cython: nonecheck={cython_nonecheck}
    # cython: overflowcheck={cython_overflowcheck}
    # cython: overflowcheck.fold={cython_overflowcheck_fold}
    # cython: embedsignature={cython_embedsignature}
    # cython: embedsignature.format={cython_embedsignature_format}
    # cython: cdivision={cython_cdivision}
    # cython: cdivision_warnings={cython_cdivision_warnings}
    # cython: cpow={cython_cpow}
    # cython: c_api_binop_methods={cython_c_api_binop_methods}
    # cython: profile={cython_profile}
    # cython: linetrace={cython_linetrace}
    # cython: infer_types={cython_infer_types}
    # cython: language_level={cython_language_level}
    # cython: c_string_type={cython_c_string_type}
    # cython: c_string_encoding={cython_c_string_encoding}
    # cython: type_version_tag={cython_type_version_tag}
    # cython: unraisable_tracebacks={cython_unraisable_tracebacks}
    # cython: iterable_coroutine={cython_iterable_coroutine}
    # cython: annotation_typing={cython_annotation_typing}
    # cython: emit_code_comments={cython_emit_code_comments}
    # cython: cpp_locals={cython_cpp_locals}
    """
    return "\n".join(
        [
            g
            for x in compilerdirectives.splitlines()
            if not (g := x.strip()).endswith("=") and g.startswith("#")
        ]
    )


def prepare_setup_dict(
    setup_py_limited_api=False,
    setup_name="",
    setup_sources=(),
    setup_include_dirs=(),
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
):
    addtodict = {}
    addtodict["py_limited_api"] = (
        list(setup_py_limited_api)
        if isinstance(setup_py_limited_api, tuple)
        else setup_py_limited_api
    )
    addtodict["name"] = (
        list(setup_name) if isinstance(setup_name, tuple) else setup_name
    )
    addtodict["sources"] = (
        list(setup_sources) if isinstance(setup_sources, tuple) else setup_sources
    )
    addtodict["include_dirs"] = (
        list(setup_include_dirs)
        if isinstance(setup_include_dirs, tuple)
        else setup_include_dirs
    )
    addtodict["define_macros"] = (
        list(setup_define_macros)
        if isinstance(setup_define_macros, tuple)
        else setup_define_macros
    )
    addtodict["undef_macros"] = (
        list(setup_undef_macros)
        if isinstance(setup_undef_macros, tuple)
        else setup_undef_macros
    )
    addtodict["library_dirs"] = (
        list(setup_library_dirs)
        if isinstance(setup_library_dirs, tuple)
        else setup_library_dirs
    )
    addtodict["libraries"] = (
        list(setup_libraries) if isinstance(setup_libraries, tuple) else setup_libraries
    )
    addtodict["runtime_library_dirs"] = (
        list(setup_runtime_library_dirs)
        if isinstance(setup_runtime_library_dirs, tuple)
        else setup_runtime_library_dirs
    )
    addtodict["extra_objects"] = (
        list(setup_extra_objects)
        if isinstance(setup_extra_objects, tuple)
        else setup_extra_objects
    )
    addtodict["extra_compile_args"] = (
        list(setup_extra_compile_args)
        if isinstance(setup_extra_compile_args, tuple)
        else setup_extra_compile_args
    )
    addtodict["extra_link_args"] = (
        list(setup_extra_link_args)
        if isinstance(setup_extra_link_args, tuple)
        else setup_extra_link_args
    )
    addtodict["export_symbols"] = (
        list(setup_export_symbols)
        if isinstance(setup_export_symbols, tuple)
        else setup_export_symbols
    )
    addtodict["swig_opts"] = (
        list(setup_swig_opts) if isinstance(setup_swig_opts, tuple) else setup_swig_opts
    )
    addtodict["depends"] = (
        list(setup_depends) if isinstance(setup_depends, tuple) else setup_depends
    )
    addtodict["language"] = (
        list(setup_language) if isinstance(setup_language, tuple) else setup_language
    )
    addtodict["optional"] = (
        list(setup_optional) if isinstance(setup_optional, tuple) else setup_optional
    )
    return addtodict


def generate_auto_install(
    cython_code,
    foldername,
    setup_name,
    setup_sources,
    setup_include_dirs,
    setup_py_limited_api=False,
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
    distutils_extra_compile_args="",
    distutils_extra_link_args="",
    distutils_language="",
    distutils_define_macros="NPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION",
    cython_binding=True,
    cython_boundscheck=True,
    cython_wraparound=True,
    cython_initializedcheck=False,
    cython_nonecheck=False,
    cython_overflowcheck=False,
    cython_overflowcheck_fold=True,
    cython_embedsignature=False,
    cython_embedsignature_format="c",
    cython_cdivision=False,
    cython_cdivision_warnings=False,
    cython_cpow=False,
    cython_c_api_binop_methods=False,
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
    cython_cpp_locals=False,
):
    r"""
    Generate and install a Cython module with the specified settings.

    This function takes Cython code along with various setup parameters and generates a
    Cython module, compiles it, and installs it as a Python package. It handles the
    generation of the Cython code, the creation of a setup script, compilation, and
    installation.

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



    """

    compdir = create_compiler_directives(
        extra_directives=extra_directives,
        distutils_extra_compile_args=distutils_extra_compile_args,
        distutils_extra_link_args=distutils_extra_link_args,
        distutils_language=distutils_language,
        distutils_define_macros=distutils_define_macros,
        cython_binding=cython_binding,
        cython_boundscheck=cython_boundscheck,
        cython_wraparound=cython_wraparound,
        cython_initializedcheck=cython_initializedcheck,
        cython_nonecheck=cython_nonecheck,
        cython_overflowcheck=cython_overflowcheck,
        cython_overflowcheck_fold=cython_overflowcheck_fold,
        cython_embedsignature=cython_embedsignature,
        cython_embedsignature_format=cython_embedsignature_format,
        cython_cdivision=cython_cdivision,
        cython_cdivision_warnings=cython_cdivision_warnings,
        cython_cpow=cython_cpow,
        cython_c_api_binop_methods=cython_c_api_binop_methods,
        cython_profile=cython_profile,
        cython_linetrace=cython_linetrace,
        cython_infer_types=cython_infer_types,
        cython_language_level=cython_language_level,
        cython_c_string_type=cython_c_string_type,
        cython_c_string_encoding=cython_c_string_encoding,
        cython_type_version_tag=cython_type_version_tag,
        cython_unraisable_tracebacks=cython_unraisable_tracebacks,
        cython_iterable_coroutine=cython_iterable_coroutine,
        cython_annotation_typing=cython_annotation_typing,
        cython_emit_code_comments=cython_emit_code_comments,
        cython_cpp_locals=cython_cpp_locals,
    )
    cstring = (compdir + "\n\n" + cython_code).strip()
    ext_module = prepare_setup_dict(
        setup_py_limited_api=setup_py_limited_api,
        setup_name=setup_name,
        setup_sources=setup_sources,
        setup_include_dirs=setup_include_dirs,
        setup_define_macros=setup_define_macros,
        setup_undef_macros=setup_undef_macros,
        setup_library_dirs=setup_library_dirs,
        setup_libraries=setup_libraries,
        setup_runtime_library_dirs=setup_runtime_library_dirs,
        setup_extra_objects=setup_extra_objects,
        setup_extra_compile_args=setup_extra_compile_args,
        setup_extra_link_args=setup_extra_link_args,
        setup_export_symbols=setup_export_symbols,
        setup_swig_opts=setup_swig_opts,
        setup_depends=setup_depends,
        setup_language=setup_language,
        setup_optional=setup_optional,
    )

    module_name = setup_name
    filewrite = rf'''
import os
import subprocess
import sys

def _dummyimport():
    import Cython
try:
    from . import {module_name}
except Exception as e:

    cstring = """{cstring}"""
    pyxfile = f"{module_name}.pyx"
    pyxfilesetup = f"{module_name}_setup.py"

    dirname = os.path.abspath(os.path.dirname(__file__))
    pyxfile_complete_path = os.path.join(dirname, pyxfile)
    pyxfile_setup_complete_path = os.path.join(dirname, pyxfilesetup)

    if os.path.exists(pyxfile_complete_path):
        os.remove(pyxfile_complete_path)
    if os.path.exists(pyxfile_setup_complete_path):
        os.remove(pyxfile_setup_complete_path)
    with open(pyxfile_complete_path, mode="w", encoding="utf-8") as f:
        f.write(cstring)

    compilefile = """
    from setuptools import Extension, setup
    from Cython.Build import cythonize
    ext_modules = Extension(**{repr(ext_module)})

    setup(
        name='{module_name}',
        ext_modules=cythonize(ext_modules),
    )
            """
    with open(pyxfile_setup_complete_path, mode="w", encoding="utf-8") as f:
        f.write('\n'.join([x.lstrip().replace(os.sep, "/") for x in compilefile.splitlines()]))
    subprocess.run(
        [sys.executable, pyxfile_setup_complete_path, "build_ext", "--inplace"],
        cwd=dirname,
        shell=True,
        env=os.environ.copy(),
    )
    from . import {module_name}

    '''
    outputpath = os.path.join(os.getcwd(), foldername)
    os.makedirs(outputpath, exist_ok=True)
    initfile = os.path.join(outputpath, "__init__.py")
    with open(initfile, mode="w", encoding="utf-8") as f:
        f.write(filewrite)
    return initfile
