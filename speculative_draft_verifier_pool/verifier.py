"""Core Speculative Draft Verifier Pool implementation."""
from typing import List, Dict, Tuple, Optional, Any, Callable


class DraftVerificationResult:
    def __init__(self, accepted_tokens: List[str], correction_token: Optional[str], total_drafted: int):
        self.accepted_tokens = accepted_tokens
        self.correction_token = correction_token
        self.total_drafted = total_drafted

    @property
    def acceptance_rate(self) -> float:
        if self.total_drafted == 0:
            return 0.0
        return len(self.accepted_tokens) / float(self.total_drafted)


class SpeculativeDraftVerifierPool:
    def __init__(self):
        self.stats = {"total_drafted": 0, "total_accepted": 0}

    def verify_draft(
        self,
        draft_tokens: List[str],
        oracle_evaluator: Callable[[List[str]], str]
    ) -> DraftVerificationResult:
        """Verifies proposed draft tokens against an oracle target evaluator."""
        accepted: List[str] = []
        correction: Optional[str] = None
        self.stats["total_drafted"] += len(draft_tokens)

        for i, token in enumerate(draft_tokens):
            expected = oracle_evaluator(accepted)
            if token == expected:
                accepted.append(token)
                self.stats["total_accepted"] += 1
            else:
                correction = expected
                break

        return DraftVerificationResult(accepted, correction, len(draft_tokens))
