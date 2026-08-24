from app.exceptions import FinCoreError
from app.services.member_service import MemberService

service = MemberService()


def show(member):
    print("\n" + "-" * 40)
    print(member)
    print("-" * 40)


def member_menu():

    while True:

        print("""
=== MEMBER MANAGEMENT ===
1. Register
2. View
3. Search
4. Update
5. Deactivate
6. List All
7. Back
""")

        choice = input("Choose: ")

        try:
            if choice == "1":
                register()

            elif choice == "2":
                view()

            elif choice == "3":
                search()

            elif choice == "4":
                update()

            elif choice == "5":
                deactivate()

            elif choice == "6":
                list_all()

            elif choice == "7":
                break

            else:
                print("Invalid choice.")

        except FinCoreError as e:
            print("Error:", e)


def register():

    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    member = service.register_member(name, phone, email)

    print("\nMember registered.")
    show(member)


def view():

    member_id = input("Member ID: ").upper()

    member = service.get_member(member_id)

    show(member)


def search():

    term = input("Search: ")

    members = service.search_member(term)

    if not members:
        print("No members found.")
        return

    for member in members:
        show(member)


def update():

    member_id = input("Member ID: ").upper()

    member = service.get_member(member_id)

    print("\nCurrent member:")
    show(member)

    name = input("New name: ")
    phone = input("New phone: ")
    email = input("New email: ")

    member = service.update_member(
        member_id,
        name,
        phone,
        email
    )

    print("\nMember updated.")
    show(member)


def deactivate():

    member_id = input("Member ID: ").upper()

    member = service.get_member(member_id)

    show(member)

    confirm = input("Deactivate? (y/n): ").lower()

    if confirm == "y":
        member = service.deactivate_member(member_id)
        print("\nMember deactivated.")
        show(member)
    else:
        print("Cancelled.")


def list_all():

    members = service.list_members()

    if not members:
        print("No members found.")
        return

    for member in members:
        show(member)