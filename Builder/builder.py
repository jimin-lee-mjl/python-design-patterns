from abc import ABCMeta, abstractmethod
import time 


def wait_for_job():
    time.sleep(1.5)
    print('끝났습니다.')


class Attendance:
    user = 'Real user'


class TestAttendance:
    user = 'Test user'


class ApprovalBuilder(metaclass=ABCMeta):
    @abstractmethod
    def create_approval_form(self):
        pass

    @abstractmethod
    def create_attendance_form(self):
        pass

    @abstractmethod
    def notify_approvers(self):
        pass

    def update_leave(self):
        pass 


class OffAprrovalBuilder(ApprovalBuilder):
    def __init__(self):
        self.name = '연차 결재'
        self.attendance = None

    def create_approval_form(self):
        print(f'{self.name} 양식을 만들고 있습니다.')
        wait_for_job()

    def create_attendance_form(self):
        print(f'{self.name}를 위한 새로운 근태 양식을 만들고 있습니다.')
        self.attendance = Attendance()
        wait_for_job()

    def notify_approvers(self):
        print('결재자에게 알림과 이메일을 보내고 있습니다.')
        wait_for_job()

    def update_leave(self):
        print(f'남은 연차 개수를 업데이트하고 있습니다.')
        wait_for_job()


class OvertimeApprovalBuilder(ApprovalBuilder):
    def __init__(self):
        self.name = '야근연장 결재'
        self.attendance = None

    def create_approval_form(self):
        print(f'{self.name} 양식을 만들고 있습니다.')
        wait_for_job()

    def create_attendance_form(self):
        print(f'{self.name}를 위한 새로운 근태 양식을 만들고 있습니다.')
        self.attendance = Attendance()
        wait_for_job()

    def notify_approvers(self):
        print('결재자에게 알림과 이메일을 보내고 있습니다.')
        wait_for_job()


class TestApprovalBuilder(ApprovalBuilder):
    def __init__(self):
        self.name = '테스트용 결재'
        self.attendance = None

    def create_approval_form(self):
        print(f'{self.name} 양식을 만들고 있습니다.')
        wait_for_job()

    def create_attendance_form(self):
        print(f'{self.name}를 위한 테스트용 근태 양식을 만들고 있습니다.')
        self.attendance = TestAttendance()
        wait_for_job()

    def notify_approvers(self):
        print('결재자에게 알림과 이메일을 보내고 있습니다.')
        wait_for_job()


class Director:
    def __init__(self):
        self.builder = None
        self.step = None

    def ask_for_approval_type(self):
        type = input('어떤 결재를 올리시겠습니까? a.연차 b.야근연장 c.테스트 : ')
        if type == 'a':
            self.builder = OffAprrovalBuilder()
            self.step = 4
        elif type == 'b':
            self.builder = OvertimeApprovalBuilder()
            self.step = 3
        elif type == 'c':
            self.builder = TestApprovalBuilder()
            self.step = 3
        else:
            raise KeyError('a, b, c 중에서 선택해주세요.')

    def send_approval(self):
        print('결재 생성을 시작합니다.')

        steps = [
            self.builder.create_approval_form,
            self.builder.create_attendance_form,
            self.builder.notify_approvers,
            self.builder.update_leave,
        ]
        for i in range(self.step):
            steps[i]()

        print('결재가 올라갔습니다.')


# client code
def main():
    director = Director()
    director.ask_for_approval_type()
    director.send_approval()


main()
