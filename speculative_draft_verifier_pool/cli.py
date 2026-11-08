"""CLI for speculative-draft-verifier-pool."""
import sys
import argparse
from .verifier import SpeculativeDraftVerifierPool


def main():
    parser = argparse.ArgumentParser(description="Speculative Draft Verifier Pool CLI")
    parser.add_argument("--demo", action="store_true", help="Run speculative draft verification demo")
    args = parser.parse_args()

    if args.demo:
        pool = SpeculativeDraftVerifierPool()
        ground_truth = ["import", " ", "sys", "\n", "def"]
        draft = ["import", " ", "sys", "\n", "class"]  # diverges on 5th token

        def oracle(prefix):
            return ground_truth[len(prefix)]

        res = pool.verify_draft(draft, oracle)
        print(f"[+] Speculative Verification Result:")
        print(f"    Accepted Tokens: {res.accepted_tokens}")
        print(f"    Correction Token: '{res.correction_token}'")
        print(f"    Acceptance Rate: {res.acceptance_rate * 100:.1f}%")
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
