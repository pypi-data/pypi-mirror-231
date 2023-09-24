#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SPEX - SPectra EXtractor.

Extract spectra from spectral data cubes.

Copyright (C) 2022  Maurizio D'Addona <mauritiusdadd@gmail.com>
"""
from __future__ import absolute_import, division, print_function

import os
import sys
import unittest
import warnings

from astropy.io import fits
from astropy.table import Table, join

from specex.cube import cutout_main
from specex.stack import cube_stack
from specex.sources import detect_from_cube
from specex.zeropoints import main as zpinfo
from specex.specex import specex
from specex.plot import plot_spectra

from test import make_synt_cube, get_hst_test_images, TEST_DATA_PATH
from test import make_synt_specs


try:
    from specex.rrspecex import rrspecex
except ImportError:
    HAS_RR = False
else:
    HAS_RR = True


Z_FTOL = 0.01


NICMOS_REGFILE_DATA = """
# Region file format: DS9 version 4.1
fk5
box(182.6350214,39.4064356,5.000",3.000",262.21022)
circle(182.6356792,39.4058053,2.500")
ellipse(182.6349624,39.4062180,2.500",1.500",217.21022)
"""


class MyTests(unittest.TestCase):

    test_hst_imgs = get_hst_test_images()
    reg_file, cat_file, cube_file = make_synt_cube.main(overwrite=False)
    spec_files = make_synt_specs.main()

    def test_zeropoint_info(self):
        print(">>> Testing zeropoint_info...\n")
        if not self.test_hst_imgs:
            print(
                "Failed to download HST test images, skipping this test...",
                file=sys.stderr
            )
            return True
        zpinfo(self.test_hst_imgs)

    def test_stack_cube(self):
        print(">>> Testing cube_stack...\n")
        print(self.cube_file)
        cube_stack_options = [
            self.cube_file
        ]
        cube_stack(cube_stack_options)

    def test_grayscale_cutout(self):
        print(">>> Testing grayscale cutout...\n")
        if not self.test_hst_imgs:
            print(
                "Failed to download HST test images, skipping this test...",
                file=sys.stderr
            )
            return True
        for img in self.test_hst_imgs:
            if img.endswith('NICMOSn4hk12010_mos.fits'):
                regfile = os.path.join(
                    TEST_DATA_PATH, 'NICMOSn4hk12010_mos.reg'
                )

                with open(regfile, 'w') as f:
                    f.write(NICMOS_REGFILE_DATA)

                cutout_options = [
                    '--verbose',
                    '--regionfile', regfile,
                    img
                ]
                cutout_main(cutout_options)
                break

    def test_cube_cutout(self):
        print(">>> Testing cube cutout...\n")
        regfile = os.path.join(
            TEST_DATA_PATH, 'cutout_test_cube.reg'
        )

        with open(regfile, 'w') as f:
            f.write(NICMOS_REGFILE_DATA)

        cutout_options = [
            '--verbose',
            '--regionfile', regfile,
            self.cube_file
        ]
        cutout_main(cutout_options)

    def test_extract_sources(self):
        print(">>> Testing sources detection from datacube...\n")
        detect_from_cube([self.cube_file])

    def test_specex_catalog_success(self):
        print(">>> Testing specex catalog...\n")
        specex_options = [
            '--catalog', self.cat_file,
            '--mode', 'circular_aperture',
            '--aperture-size', '0.8arcsec',
            '--weighting', 'whitelight',
            '--no-nans', self.cube_file
        ]
        specex(options=specex_options)

    def test_specex_regionfile_success(self):
        print(">>> Testing specex regionfile...")
        specex_options = [
            '--regionfile', self.reg_file,
            '--mode', 'kron_ellipse',
            '--no-nans', self.cube_file
        ]
        specex(options=specex_options)

    def test_plot_success(self):
        print(">>> Testing specex-plot...")

        plot_options = [
            '--restframe',
            '--outdir', 'test_plot_out',
            *self.spec_files
        ]

        plot_spectra(options=plot_options)

"""
# unittest seems to have some issues with redrock implementation...
class TestRRSpex(unittest.TestCase):

    @unittest.skipIf(not HAS_RR, "redrock not installed")
    def test_rrspecex_success(self):
        global HAS_RR
        
        if not HAS_RR:
            return

        test_files = make_synt_specs.main()

        true_z_table = Table(
            names=['SPECID', 'TRUE_Z'],
            dtype=['U10', 'float32']
        )

        for file in test_files:
            header = fits.getheader(file, ext=0)
            true_z_table.add_row([header['ID'], header['OBJ_Z']])

        options = ['--quite', ] + test_files
        targets, zbest, scandata = rrspecex(options=options)

        zbest = join(true_z_table, zbest, keys=['SPECID'])
        print(zbest)

        for i, obj in enumerate(zbest):
            delta_z = abs(obj['TRUE_Z'] - obj['Z'])/(1 + obj['TRUE_Z'])
            if delta_z >= Z_FTOL:
                warnings.warn(
                    f"OBJ {i}: computed redshift outside f01 limit!",
                )
"""

if __name__ == '__main__':
    tests = MyTests()
    tests.test_zeropoint_info()

    tests.test_stack_cube()

    tests.test_grayscale_cutout()
    tests.test_cube_cutout()

    tests.test_extract_sources()

    tests.test_specex_catalog_success()
    tests.test_specex_regionfile_success()

    tests.test_plot_success()

    # if HAS_RR:
    #     test_06 = TestRRSpex()
    #     test_06.test_rrspecex_success()
