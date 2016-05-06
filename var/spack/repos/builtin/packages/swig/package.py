##############################################################################
# Copyright (c) 2014, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Written by Matthew LeGendre, legendre1@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License (as published by
# the Free Software Foundation) version 2.1 dated February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################

from spack import *

class Swig(Package):
    """SWIG is an interface compiler that connects programs written in
       C and C++ with scripting languages such as Perl, Python, Ruby,
       and Tcl. It works by taking the declarations found in C/C++
       header files and using them to generate the wrapper code that
       scripting languages need to access the underlying C/C++
       code. In addition, SWIG provides a variety of customization
       features that let you tailor the wrapping process to suit your
       application."""

    homepage = "http://www.swig.org"
    url      = "http://prdownloads.sourceforge.net/swig/swig-3.0.8.tar.gz"

    version('3.0.8', 'c96a1d5ecb13d38604d7e92148c73c97')
    version('3.0.7', '7fff46c84b8c630ede5b0f0827e3d90a')
    version('3.0.2', '62f9b0d010cef36a13a010dc530d0d41')
    version('2.0.12', 'c3fb0b2d710cc82ed0154b91e43085a4')
    version('2.0.2', 'eaf619a4169886923e5f828349504a29')
    version('1.3.40', '2df766c9e03e02811b1ab4bba1c7b9cc')

    depends_on('pcre')

    def install(self, spec, prefix):
        configure('--prefix=%s' % prefix)
        make()
        make('install')
