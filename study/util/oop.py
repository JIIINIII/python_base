class Person:

    # initializer(magic function- __로 시작해서 __로 끝나는 함수, 생성자)
    # 객체 생성시 자동으로 호출되는 함수
    # 명시적으로 호출이 불가
    def __init__(self,name,subject,email):
        self.name = name
        self.subject = subject
        self.email = email

    def perInfo(self):
        return '이름 {}, 과목 {}, 메일 {}'.format(self.name,self.subject,self.email)