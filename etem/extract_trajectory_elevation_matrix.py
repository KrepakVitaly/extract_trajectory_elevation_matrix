#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Example Google style docstrings.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
import numpy as np
import scipy
from osgeo import gdal  # https://pythongisandstuff.wordpress.com/2016/04/13/installing-gdal-ogr-for-python-on-windows/
import sys

class TrajectoryElevationMatrixExtractor():
    """Интерфейс алгоритма извлечения матриц высот для заданной траектории

    В данном алгоритме решена реальная задача.
    Соисполнители предоставили траекторную модель СВН (средства воздушного нападения) с огибанием рельефа Земли.
    Соответственно для её корректной работы её необходимо снабдить данными о высотах местности,
    над которой модель СВН пролетает.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    def __init__(self, trajectory, mwidth, dump_path="../srtm_dumps"):
        """Example of docstring on the __init__ method.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            trajectory (:obj:`list` of :obj:`tuple` of :obj:'float'): Набор контрольных точек траектории –
                список с широтами и долготами контрольных точек. List[Tuple[float, float]], широты и долготы в градусах.

            mwidth: (float): Ширина интересующей полосы рельефа в метрах

            dump_path (str): Путь к каталогу с картами рельефа для всей Земли
                Карты рельефа представляют собой каталог со сжатыми GeoTIFF файлами - тайлами.
                Скачать карты можно тут: http://srtm.csi.cgiar.org/srtmdata/
                В данном источнике нет данных около полюсов.
        """
        pass
        print("Hello, I'm TrajectoryElevationMatrixExtractor")

    def extract(self):
        """Извлечения матриц высот для заданной траектории

        Требования к алгоритму:
            Алгоритм должен работать для всего земного шара.
            Если данных в источнике не хватает, необходимо сгенерировать пользовательское исключение
            ReliefDataNotAvailableException.
            Траектории могут пролегать в нескольких соседних тайлах.
            По сути тут два отдельных алгоритма: нарезка на прямоугольники и генерация данных для этих прямоугольников.
            Нужно пользоваться специализированными библиотеками для работы с картами вроде GDAL.
            При необходимости можно добавить файл с метаинформацией в каталоге тайлов. В этом случае надо рассказать
            как генерировать эту метаинформацию.

        Технические требования к реализации:
            Соответствие требования PEP8
            Использование NumPy там где это оправдано
            Модульное тестирование с использованием pytest
            Документация публичных методов (желательно Google стиль)
            Реализация в виде модуля с возможностью дистрибуции средствами requirements.txt и setup.py
            Опционально: использование модуля typing.
        `PEP 484`_ type annotations are supported. If attribute, parameter, and
        return types are annotated according to `PEP 484`_, they do not need to be
        included in the docstring:

        Args:

        Returns:
            List[np.ndarray]: Список прямоугольников с рельефом (двумерных массивов)

        .. _PEP 484:
            https://www.python.org/dev/peps/pep-0484/

        """
        print("TrajectoryElevationMatrixExtractor EXTRACT!!!")


    def extract(self):
        """нарезка на прямоугольники

        Технические требования к реализации:
            Соответствие требования PEP8
            Использование NumPy там где это оправдано
            Модульное тестирование с использованием pytest
            Документация публичных методов (желательно Google стиль)
            Реализация в виде модуля с возможностью дистрибуции средствами requirements.txt и setup.py
            Опционально: использование модуля typing.
        `PEP 484`_ type annotations are supported. If attribute, parameter, and
        return types are annotated according to `PEP 484`_, they do not need to be
        included in the docstring:

        Args:

        Returns:
            List[np.ndarray]: Список прямоугольников с рельефом (двумерных массивов)

        .. _PEP 484:
            https://www.python.org/dev/peps/pep-0484/

        """
        print("TrajectoryElevationMatrixExtractor EXTRACT!!!")


class ReliefDataNotAvailableException(Exception):
    """Exceptions are documented in the same way as classes.

    The __init__ method may be documented in either the class level
    docstring, or as a docstring on the __init__ method itself.

    Either form is acceptable, but the two should not be mixed. Choose one
    convention to document the __init__ method and be consistent with it.

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        msg (str): Human readable string describing the exception.
        code (:obj:`int`, optional): Error code.

    Attributes:
        msg (str): Human readable string describing the exception.
        code (int): Exception error code.

    """

    def __init__(self, msg, code):
        self.msg = msg
        self.code = code


if __name__ == '__main__':

    print("Hello")
    # this allows GDAL to throw Python Exceptions
    src_ds = gdal.Open("../../srtm_dumps/srtm_31_05.tif")
    data = src_ds.ReadAsArray()
    # src_ds.show()

    vmin = 0 # minimum value in your data (will be black in the output)
    vmax = 1 # minimum value in your data (will be white in the output)
    ds = gdal.Translate('fused.png', '../../srtm_dumps/srtm_31_05.tif', format='PNG', outputType=gdal.GDT_Byte, scaleParams=[[vmin,vmax]])
    ds = None