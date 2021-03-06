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
import parser
import taxonomy

from jsondiff import diff

taxonomy = taxonomy.Taxonomy()
parser = parser.Parser(taxonomy)

class TestParser(unittest.TestCase):
    # Note: this module is tested differently than others.  Sample JSON and XML
    # files are imported and then exported and later compared using the string
    # methods.  Thereafter files are loaded and created but the files contents
    # themselves are not examined (it is assumed that this would be picked up
    # in the comparisons of the strings).
    
    def test_json(self):
        
        entrypoint = parser.from_JSON_string(TEST_JSON)
        out = parser.to_JSON_string(entrypoint)
        d = diff(TEST_JSON, out)

        # TODO: Right now the JSON input and output has too many discrepancies to run the Equality
        # check.  Leave commented out for the time being and keep as a future testing goal. 
        # self.assertEqual(d, "{}")

    def test_xml(self):
        entrypoint = parser.from_JSON_string(TEST_JSON)
        out = parser.to_JSON_string(entrypoint)

        # TODO: Add an XML diff tool and run tests on it.

    def test_files(self):
        # TODO:
        # Test validate XML
        # Test validate JSON
        # Test convert XML to JSON
        # Test convert JSON to XML
        pass


TEST_JSON = """
{
  "documentType": "http://www.xbrl.org/WGWD/YYYY-MM-DD/xbrl-json",
  "prefixes": {
    "xbrl": "http://www.xbrl.org/WGWD/YYYY-MM-DD/oim",
    "solar": "http://xbrl.us/Solar/v1.1/2018-02-09/solar",
    "us-gaap": "http://fasb.org/us-gaap/2017-01-31",
    "iso4217": "http://www.xbrl.org/2003/iso4217",
    "SI": "http://www.xbrl.org/2009/utr"
  },
  "dtsReferences": [
    {
      "type": "schema",
      "href": "https://raw.githubusercontent.com/xbrlus/solar/v1.2/core/solar_all_2018-03-31_r01.xsd"
    }
  ],
  "facts": [
    {
      "id": "16f60d57-2536-4ec3-8414-02b95d067e02",
      "value": true,
      "aspects": {
        "xbrl:concept": "solar:MonthlyOperatingReportAvailabilityOfDocument",
        "xbrl:entity": "JUPITER",
        "xbrl:periodStart": "2017-11-01T00:00:00",
        "xbrl:periodEnd": "2017-11-30T00:00:00"
      }
    },
    {
      "id": "8333ad4e-24b4-42c1-83b3-fca9ef7fce55",
      "value": true,
      "aspects": {
        "xbrl:concept": "solar:MonthlyOperatingReportAvailabilityOfFinalDocument",
        "xbrl:entity": "JUPITER",
        "xbrl:periodStart": "2017-11-01T00:00:00",
        "xbrl:periodEnd": "2017-11-30T00:00:00"
      }
    }
  ]
}
"""