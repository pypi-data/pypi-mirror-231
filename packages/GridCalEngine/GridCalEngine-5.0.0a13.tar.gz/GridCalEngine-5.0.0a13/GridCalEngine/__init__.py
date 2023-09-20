# GridCal
# Copyright (C) 2015 - 2023 Santiago Peñate Vera
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

# from GridCalEngine.Replacements import *
from GridCalEngine.basic_structures import *
from GridCalEngine.grid_analysis import *
from GridCalEngine.Simulations import *
from GridCalEngine.IO import *
from GridCalEngine.Core import *
from GridCalEngine.Core.DataStructures.numerical_circuit import NumericalCircuit, compile_numerical_circuit_at

# from ortools.linear_solver import pywraplp
# from ortools.init import pywrapinit
#
#
# # pywrapinit.CppBridge.InitLogging('SuggestedFix.py')
# cpp_flags = pywrapinit.CppFlags()
# cpp_flags.logtostderr = True
# cpp_flags.log_prefix = False
# pywrapinit.CppBridge.SetFlags(cpp_flags)
