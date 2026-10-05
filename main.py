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
    ]

    for q in demo_questions:
        print(f"Q: {q}")
        answer = ask(agent, q)
        print(f"A: {answer}\n")


if __name__ == "__main__":
    main()