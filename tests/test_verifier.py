"""Unit tests for speculative-draft-verifier-pool."""
import unittest
from speculative_draft_verifier_pool.verifier import SpeculativeDraftVerifierPool


class TestSpeculativeDraftVerifierPool(unittest.TestCase):
    def test_full_acceptance(self):
        pool = SpeculativeDraftVerifierPool()
        stream = ["a", "b", "c"]
        res = pool.verify_draft(stream, lambda p: stream[len(p)])
        self.assertEqual(res.accepted_tokens, stream)
        self.assertIsNone(res.correction_token)
        self.assertEqual(res.acceptance_rate, 1.0)

    def test_partial_divergence(self):
        pool = SpeculativeDraftVerifierPool()
        draft = ["a", "b", "WRONG"]
        truth = ["a", "b", "CORRECT"]
        res = pool.verify_draft(draft, lambda p: truth[len(p)])
        self.assertEqual(res.accepted_tokens, ["a", "b"])
        self.assertEqual(res.correction_token, "CORRECT")
        self.assertAlmostEqual(res.acceptance_rate, 2/3)
