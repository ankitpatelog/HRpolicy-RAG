"""
command line to start the pipeline 
"""

from hr_assistant.pipeline import ask, build_hr_assistant

def main():
    print("Building the HR policy assistant...")
    agent = build_hr_assistant()
    print("HR Assistant is ready!\n")

    demo_questions = [
        "What is the company's leave policy?",
        "How do I apply for paternity leave?",
        "Who should I contact regarding payroll queries?",
        "Is there a remote work policy?",
        "What are the official holidays for this year?"
    ]

    for q in demo_questions:
        print(f"Q: {q}")
        answer = ask(agent, q)
        print(f"A: {answer}\n")


if __name__ == "__main__":
    main()