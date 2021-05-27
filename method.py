class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("이름:", self.name, "나이:", self.age)

    def call(self):
        print(self.name, ".를 호출합니다.")


person = Human("성규", 27)
person.info()
person.call()
