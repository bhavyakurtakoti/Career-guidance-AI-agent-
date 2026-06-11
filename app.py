print("=== Career Guidance AI Agent ===")

name = input("Enter your name: ")
interest = input("Enter your interest (coding/electronics/biology/business): ")

print("\nHello", name)

if interest.lower() == "coding":
    print("Recommended Careers:")
    print("- Software Engineer")
    print("- AI Engineer")
    print("- Data Scientist")

elif interest.lower() == "electronics":
    print("Recommended Careers:")
    print("- Electronics Engineer")
    print("- Embedded Systems Engineer")

elif interest.lower() == "biology":
    print("Recommended Careers:")
    print("- Doctor")
    print("- Biotechnologist")
    print("- Research Scientist")

elif interest.lower() == "business":
    print("Recommended Careers:")
    print("- Entrepreneur")
    print("- Business Analyst")
    print("- Marketing Manager")

else:
    print("Please enter a valid interest.")
