from app.models.member import Member
from app.repositories.base_repository import BaseRepository


class MemberRepository(BaseRepository):

    def __init__(self, file_path="data/members.json"):
        super().__init__(file_path)

#  to get all the members
    def get_all(self):
        data = self._read_data()

        members = []

        for item in data:
            member = Member.from_dict(item)
            members.append(member)

        return members

#  to filter member by id

    def get_by_id(self, member_id):
        members = self.get_all()

        for member in members:
            if member.member_id == member_id:
                return member

        return None
    
# to filter member by their phone number

    def get_by_phone(self, phone):
        members = self.get_all()

        for member in members:
            if member.phone == phone:
                return member

        return None
#  to add a new member

    def save(self, member):
        data = self._read_data()

        data.append(member.to_dict())

        self._write_data(data)

        return member

#  to update the existing member

    def update(self, member):
        data = self._read_data()

        for i in range(len(data)):
            if data[i]["member_id"] == member.member_id:
                data[i] = member.to_dict()

                self._write_data(data)

                return member

        return None