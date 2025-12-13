import sys
from src.constitution import Constitution, SimpleRetriever, DEFAULT_PRINCIPLES
from src.judge import ConstitutionalJudge
from src.metrics import calculate_compliance_score
from src.red_team import RedTeamer
from src.data_loader import load_interactions_as_tuples

def main():
    print("=== Constitutional AI Compliance System ===")
    
    # 1. Setup
    constitution = Constitution(DEFAULT_PRINCIPLES)
    retriever = SimpleRetriever(constitution)
    judge = ConstitutionalJudge(retriever)
    
    # 2. Load interactions from external dataset
    interactions = load_interactions_as_tuples()
    
    print(f"\nRunning evaluation on {len(interactions)} interactions...")
    traces = []
    for prompt, response in interactions:
        trace = judge.evaluate(prompt, response)
        traces.append(trace)
        print(f"[-] Prompt: {prompt[:30]}... | Verdict: {trace.verdict.label} (Score: {trace.verdict.score})")
        
    # 3. Calculate Score
    score = calculate_compliance_score(traces)
    print(f"\nOverall Constitutional Compliance Score (CCS): {score:.2f} / 1.00")
    
    # 4. Red Teaming Demo
    print("\n=== Automated Red Teaming ===")
    red_teamer = RedTeamer()
    attacks = red_teamer.generate_attacks()
    print(f"Generated {len(attacks)} adversarial prompts.")
    print(f"Example: {attacks[0]}")
    
    # In a real loop, we would feed these to the model and evaluate.
    print("Red Teaming complete.")

if __name__ == "__main__":
    main()
