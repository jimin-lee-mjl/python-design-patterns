from abc import ABCMeta, abstractmethod
from base import _print, Singleton


class Approval:
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        self.drafter = kwargs.get('employee')
        self.display_date = kwargs.get('display_date')
        self.start_datetime = kwargs.get('start_datetime')
        self.end_datetime = kwargs.get('end_datetime')
        self.approvers = kwargs.get('approvers')

    def __call__(self):
        _print(f'{self.drafter.name}님의 {self.display_date} 날짜 연차 결재가 올라갔습니다.')


class Attendance:
    def __init__(self, *args, **kwargs):
        self.drafter = kwargs.get('drafter')
        self.display_date = kwargs.get('display_date')
        self.start_datetime = kwargs.get('start_datetime')
        self.end_datetime = kwargs.get('end_datetime')
        self.status = kwargs.get('status')
        self.category = kwargs.get('category')


class Employee:
    def __init__(self, name):
        self.name = name

    def update_leave(self):
        _print('가용 연차가 업데이트 되었습니다.')

    def send_email(self):
        _print(f'{self.name}님께 이메일을 보냈습니다.')

    def send_push_notification(self):
        _print(f'{self.name}님께 푸시 알림을 보냈습니다.')


class OffEventListener(metaclass=ABCMeta):
    @abstractmethod
    def update(self, data):
        pass


class OffEventManager(metaclass=Singleton):
    _subscribers = []

    def subscribe(self, listener):
        self._subscribers.append(listener)

    def unsubscribe(self, listener):
        self._subscribers.remove(listener)

    def bulk_subscribe(self, listeners):
        for listener in listeners:
            self.subscribe(listener)

    def notify(self, data):
        for listener in self._subscribers:
            listener.update(data)


class EmployeeListener(OffEventListener):
    def update(self, data):
        employee = data.drafter
        employee.update_leave()


class AttendanceListener(OffEventListener):
    def update(self, data):
        context = {
            'employee': data.drafter,
            'display_date': data.display_date,
            'start_datetime': data.start_datetime,
            'end_datetime': data.end_datetime,
            'status': 'WAITING_APPROVAL',
            'category': 'LEAVE',
        }
        attendance = Attendance(**context)
        _print(f'{attendance.status} 상태인 {attendance.display_date} 날짜의 근태 기록이 생성되었습니다.')


class ApproverListener(OffEventListener):
    def update(self, data):
        _print('결재자에게 알림 전송을 시작합니다.')
        approvers = data.approvers
        for approver in approvers:
            approver.send_email()
            approver.send_push_notification()


def create_off_approval(data):
    _print('...연차 결재 생성을 시작합니다...')
    data['name'] = "연차"
    approval = Approval(**data)
    approval()
    event_manager = OffEventManager()
    event_manager.notify(approval)
    _print('...연차 결재 생성 및 그에 따른 추가 작업이 완료되었습니다..!')


def main():
    jm = Employee('이지민')
    gu = Employee('이기욱')
    hl = Employee('김혜린')

    event_manager = OffEventManager()
    employee_listener = EmployeeListener()
    attendance_listener = AttendanceListener()
    approver_listener = ApproverListener()
    event_manager.bulk_subscribe([attendance_listener, employee_listener, approver_listener])

    approval_context = {
        'employee': jm,
        'display_date': '2021-10-31',
        'start_datetime': '10:00',
        'end_datetime': '18:00',
        'approvers': [gu, hl],
    }
    create_off_approval(approval_context)


main()
