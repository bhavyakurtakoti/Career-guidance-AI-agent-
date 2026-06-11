print("=== Career Guidance AI Agent ===")

name = input("Enter your name: ")
interest = input("Enter your interest (coding/electronics/biology/business): ").strip().lower()

print("\nHello", name)

if interest == "coding":
    print("Recommended Careers:")
    print("- Software Engineer")
    print("- AI Engineer")
    print("- Data Scientist")

elif interest == "electronics":
    print("Recommended Careers:")
    print("- Electronics Engineer")
    print("- Embedded Systems Engineer")

elif interest == "biology":
    print("Recommended Careers:")
    print("- Doctor")
    print("- Biotechnologist")
    print("- Research Scientist")

elif interest == "business":
    print("Recommended Careers:")
    print("- Entrepreneur")
    print("- Business Analyst")
    print("- Marketing Manager")

else:
    print("Please enter a valid interest.")
