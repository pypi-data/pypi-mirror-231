import unittest
import os
import pandas as pd
from src.pyphetools.creation import HpoParser, CaseEncoder, MetaData
HP_JSON_FILENAME = os.path.join(os.path.dirname(__file__), 'data', 'hp.json')
# The API requires us to pass a column name but the column name will not be used in the tests
TEST_COLUMN = "test"


class TestCaseParse(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        hpparser = HpoParser(hpo_json_file=HP_JSON_FILENAME)
        cls._hpo_cr = hpparser.get_hpo_concept_recognizer()
        metadata = MetaData(created_by="ORCID:0000-0002-0736-9199")
        metadata.default_versions_with_hpo(version="2022-05-05")
        cls._parser = CaseEncoder(hpo_cr=cls._hpo_cr, individual_id="A", pmid="PMID:123", metadata=metadata.to_ga4gh())

    def test_chief_complaint(self):
        """
        Expect to get
        HP:0000365 	Hearing impairment 	True 	True
        HP:0001742 	Nasal congestion 	True 	True
        HP:0025267 	Snoring
        """
        vignette = "A 17-mo-old boy presented with progressive nasal obstruction, snoring and hearing loss symptoms when referred to the hospital."
        results = self._parser.add_vignette(vignette=vignette)
        self.assertEqual(3, len(results))
        self.assertTrue(isinstance(results, pd.DataFrame))
        tid = results.loc[(results['id'] == 'HP:0000365')]['id'].values[0]
        self.assertEqual("HP:0000365", tid)

    def test_excluded(self):
        """
        Currently, our text mining does not attempt to detect negation, but users can enter a set of term labels that are excluded
        In this case, He had no nasal obstruction should lead to excluded/Nasal congestion
        """
        vignette = "He had no nasal obstruction and he stated that his smell sensation was intact."
        excluded = set()
        excluded.add("Nasal congestion")
        results = self._parser.add_vignette(vignette=vignette, excluded_terms=excluded)
        self.assertEqual(1, len(results))
        tid = results.loc[(results['id'] == 'HP:0001742')]['id'].values[0]
        self.assertEqual("HP:0001742", tid)
        label = results.loc[(results['id'] == 'HP:0001742')]['label'].values[0]
        self.assertEqual("Nasal congestion", label)
        observed = results.loc[(results['id'] == 'HP:0001742')]['observed'].values[0]
        self.assertFalse(observed)
        measured = results.loc[(results['id'] == 'HP:0001742')]['measured'].values[0]
        self.assertTrue(measured)

    def test_excluded2(self):
        """
        The goal if this test is to enzure that 'Seizure' is annotated as 'excluded'
        """
        vignette = "The patient is not on seizure medication at this time."
        excluded = set()
        excluded.add("Seizure")
        metadata = MetaData(created_by="ORCID:0000-0002-0736-9199")
        metadata.default_versions_with_hpo(version="2022-05-05")
        encoder = CaseEncoder(hpo_cr=self._hpo_cr, individual_id="id", metadata=metadata.to_ga4gh(), pmid="PMID:1")
        df = encoder.add_vignette(vignette=vignette, excluded_terms=excluded)
        self.assertEqual(1, len(df))
        
        self.assertEqual("HP:0001250", df.iloc[0]['id'])
        self.assertEqual("Seizure",df.iloc[0]['label'])
        self.assertFalse(df.iloc[0]['observed'])
        self.assertTrue(df.iloc[0]['measured'])

    def test_phenopacket_id(self):
        """
        Test that we construct the phenopacket ID to include the PMID and the individual id
        """
        ppkt = self._parser.get_phenopacket()
        expected_ppkt_id = "PMID_123_A"
        self.assertEqual(expected_ppkt_id, ppkt.id)

