from services.rag_service import answer_question


while True:

    question = input("Ask Scholar.AI a question: ")

    if question.lower() == "exit":
        print("Scholar.AI: Goodbye!")
        break

    answer = answer_question(question)

    print("\nScholar.AI:")
    print(answer)
    print()