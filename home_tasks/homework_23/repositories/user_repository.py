from home_tasks.homework_23.session import session
from home_tasks.homework_23.models.users import Users


class UsersRepository:
    def __init__(self):
        self.__session = session

    def select_all(self):
        all_users = self.__session.query(Users).all()
        for user in all_users:
            print(user)

    def add_new_user(self, id: str, name: str, age: int, email: str):
        self.bddata = Users(id=id, name=name, age=age, email=email)
        self.__session.add(self.bddata)
        self.__session.commit()

    def delete_by_email(self, del_email: str):
        self.__session.query(Users).filter(Users.email == del_email).delete()
        self.__session.commit()

    def modify_by_id(self, user_id: str, name: str, age: int, email: str):
        self.__session.query(Users).filter(Users.id == user_id).update(
            {
                'name': name,
                'age': age,
                'email': email
            }
        )
        self.__session.commit()


if __name__ == '__main__':
    users_repository = UsersRepository()
    users_repository.add_new_user("pppppppp", "Minica", 19, "monica@gmail.com")
    users_repository.modify_by_id('pppppppp', 'Minica', 20, 'monica_sex@gmail.com')
    users_repository.select_all()
    # users_repository.delete_by_email('monica_sex@gmail.com')
