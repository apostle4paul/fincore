from datetime import date


class Member:
    def __init__(
            self,
            member_id: str,
            full_name: str,
            phone:str,
            email: str,
            date_joined:str | None=None,
            status:str= "ACTIVE",
    ):
        self.member_id = member_id
        self.full_name= full_name
        self.phone=phone
        self.email=email
        self.date_joined= date_joined | date.today().isoformat()
        self.status= status

# converts the object received to dictionary (key value pair)
    def to_dict(self)-> dict:
        return{
        "member_id": self.member_id,
        "full_name": self.full_name,
        "phone": self.phone,
        "email": self.email,
        "date_joined": self.date_joined,
        "status": self.status,
        }
#  converts the dictionary to object and it is a class method
    def from_dict(cls, data:dict):
        return cls(
            member_id=data["member_id"],
            full_name=data["full_name"],
            phone=data["phone"],
            email=data["email"],
            date_joined=data.get("date_joined"),
            status=data.get("status", "ACTIVE"),
        )
    # shows the member object as a text
    def __str__(self)-> str:
        return(
            f"Member ID:{self.member_id}\n"
            f"Name:{self.full_name}\n"
            f"phone:{self.phone}\n"
            f"Email{self.email}\n"
            f"Date_joined:{self.date_joined}\n"
            f"Status:{self.status}"
        )