# Copyright 2018 Wells Fargo

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import taxonomy_misc

tax_numeric_types = taxonomy_misc.TaxonomyNumericTypes()
tax_generic_roles = taxonomy_misc.TaxonomyGenericRoles()
tax_ref_parts = taxonomy_misc.TaxonomyRefParts()

class TestTaxonomyMisc(unittest.TestCase):

    def test_taxonomy_numeric_types(self):
        self.assertEqual(len(tax_numeric_types.numeric_types()), 13)

    def test_taxonomy_ref_parts(self):
        self.assertEqual(len(tax_ref_parts.ref_parts()), 6)

    def test_taxonomy_generic_roles(self):
        self.assertEqual(len(tax_generic_roles.generic_roles()), 5)

    def test_validate_numeric_types(self):
        self.assertTrue(tax_numeric_types.validate_numeric_type("insolationItemType"))
        self.assertTrue(tax_numeric_types.validate_numeric_type("speedItemType"))
        self.assertTrue(tax_numeric_types.validate_numeric_type("luminousIntensityItemType"))
        self.assertFalse(tax_numeric_types.validate_numeric_type("inslationItemType"))
        self.assertFalse(tax_numeric_types.validate_numeric_type("speedItemTye"))
        self.assertFalse(tax_numeric_types.validate_numeric_type("luminousIntensityIteType"))

    def test_validate_ref_part(self):
        self.assertTrue(tax_ref_parts.validate_ref_part("Publisher"))
        self.assertTrue(tax_ref_parts.validate_ref_part("Sample"))
        self.assertTrue(tax_ref_parts.validate_ref_part("Confidentiality"))
        self.assertFalse(tax_ref_parts.validate_ref_part("Publishe"))
        self.assertFalse(tax_ref_parts.validate_ref_part("Sampl"))
        self.assertFalse(tax_ref_parts.validate_ref_part("Confidentialit"))

    def test_validate_generic_role(self):
        self.assertTrue(tax_generic_roles.validate_generic_role("Generic UML aggregation arc"))
        self.assertTrue(tax_generic_roles.validate_generic_role("Generic UML inheritance arc"))
        self.assertTrue(tax_generic_roles.validate_generic_role("Generic UML property arc"))
        self.assertFalse(tax_generic_roles.validate_generic_role("Genric UML aggregation arc"))
        self.assertFalse(tax_generic_roles.validate_generic_role("Genric UML inheritance arc"))
        self.assertFalse(tax_generic_roles.validate_generic_role("Genric UML property arc"))
