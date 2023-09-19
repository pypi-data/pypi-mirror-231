# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 7, 0):
    raise RuntimeError("Python 3.7 or later required")

from . import _ITKCommonPython


from . import _CudaCommonPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkCudaDataManagerPython
else:
    import _itkCudaDataManagerPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkCudaDataManagerPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkCudaDataManagerPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import collections.abc
import itk.ITKCommonBasePython
import itk.itkMatrixPython
import itk.itkCovariantVectorPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkFixedArrayPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython

def itkCudaDataManager_New():
    return itkCudaDataManager.New()

class itkCudaDataManager(itk.ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkCudaDataManager class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCudaDataManagerPython.itkCudaDataManager___New_orig__)
    Clone = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_Clone)
    SetBufferSize = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_SetBufferSize)
    GetBufferSize = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_GetBufferSize)
    SetBufferFlag = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_SetBufferFlag)
    SetCPUBufferPointer = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_SetCPUBufferPointer)
    SetCPUDirtyFlag = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_SetCPUDirtyFlag)
    SetGPUDirtyFlag = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_SetGPUDirtyFlag)
    SetCPUBufferDirty = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_SetCPUBufferDirty)
    SetGPUBufferDirty = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_SetGPUBufferDirty)
    IsCPUBufferDirty = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_IsCPUBufferDirty)
    IsGPUBufferDirty = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_IsGPUBufferDirty)
    UpdateCPUBuffer = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_UpdateCPUBuffer)
    UpdateGPUBuffer = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_UpdateGPUBuffer)
    Allocate = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_Allocate)
    Free = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_Free)
    Update = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_Update)
    Graft = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_Graft)
    Initialize = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_Initialize)
    GetGPUBufferPointer = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_GetGPUBufferPointer)
    GetCPUBufferPointer = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_GetCPUBufferPointer)
    GetGPUBufferSize = _swig_new_instance_method(_itkCudaDataManagerPython.itkCudaDataManager_GetGPUBufferSize)
    __swig_destroy__ = _itkCudaDataManagerPython.delete_itkCudaDataManager
    cast = _swig_new_static_method(_itkCudaDataManagerPython.itkCudaDataManager_cast)

    def New(*args, **kargs):
        """New() -> itkCudaDataManager

        Create a new object of the class itkCudaDataManager and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCudaDataManager.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCudaDataManager.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCudaDataManager.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCudaDataManager in _itkCudaDataManagerPython:
_itkCudaDataManagerPython.itkCudaDataManager_swigregister(itkCudaDataManager)
itkCudaDataManager___New_orig__ = _itkCudaDataManagerPython.itkCudaDataManager___New_orig__
itkCudaDataManager_cast = _itkCudaDataManagerPython.itkCudaDataManager_cast



