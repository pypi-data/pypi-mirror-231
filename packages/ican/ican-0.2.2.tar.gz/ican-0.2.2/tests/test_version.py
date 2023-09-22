# -*- coding: utf-8 -*-

import unittest
from ican.version import Version


class TestVersion(unittest.TestCase):
    def test_parse(self):
        v = Version.parse('1.3.3-beta.2+build.300')
        self.assertEqual(v.semantic, '1.3.3-beta.2+build.300')

    def test_semantic(self):
        ver = Version(1, 2, 3, 'beta', 1, 99)
        self.assertEqual(ver.semantic, '1.2.3-beta.1+build.99')

    def test_public(self):
        ver = Version(1, 2, 3, 'beta', 1, 99)
        self.assertEqual(ver.public, '1.2.3')

    def test_pep440(self):
        ver = Version(1, 2, 3, 'beta', 1, 99)
        self.assertEqual(ver.pep440, '1.2.3b1.99')

    def test_bump_build(self):
        ver = Version(1, 2, 3, 'beta', 1, 99)
        ver.bump('build')
        self.assertEqual(ver.semantic, '1.2.3-beta.1+build.100')

    def test_bump_initial_prerelease(self):
        ver = Version(1, 2, 3, build=99)
        ver.bump('prerelease')
        self.assertEqual(ver.semantic, '1.2.3-beta.1+build.100')

    def test_bump_prerelease(self):
        ver = Version(1, 2, 3, 'beta', 1, 99)
        ver.bump('prerelease')
        self.assertEqual(ver.semantic, '1.2.3-beta.2+build.100')

    def test_bump_prerelease_by_token(self):
        ver = Version(1, 2, 3, 'alpha', 1, 99)
        ver.bump('beta')
        self.assertEqual(ver.semantic, '1.2.3-beta.1+build.100')

    def test_bump_patch(self):
        ver = Version(1, 2, 3, 'beta', 1, 99)
        ver.bump('patch')
        self.assertEqual(ver.semantic, '1.2.4+build.100')

    def test_bump_minor(self):
        ver = Version(1, 2, 3, 'beta', 1, 99)
        ver.bump('minor')
        self.assertEqual(ver.semantic, '1.3.0+build.100')

    def test_bump_major(self):
        ver = Version(1, 2, 3, 'beta', 1, 99)
        ver.bump('major')
        self.assertEqual(ver.semantic, '2.0.0+build.100')

    def test_tag(self):
        ver = Version(1, 2, 3, 'beta', 1, 99)
        self.assertEqual(ver.tag, 'v1.2.3')

    def test_bumped_false(self):
        ver = Version(1, 2, 3, 'beta', 1, 99)
        self.assertFalse(ver.bumped)

    def test_bumped_true(self):
        ver = Version(1, 2, 3, 'beta', 1, 99)
        ver.bump('build')
        self.assertTrue(ver.bumped)

    def test_string_input(self):
        ver = Version("1", "2", "3", "beta", "1", "99")
        self.assertEqual(ver.semantic, '1.2.3-beta.1+build.99')


if __name__ == '__main__':
    unittest.main()
