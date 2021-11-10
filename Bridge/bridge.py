import time


def wait_for_job():
    time.sleep(1.5)


def _print(content):
    print(content)
    wait_for_job()


class MacbookImageDownloader:
    def get_local_image_storage(self):
        _print('macbook의 사진 저장 공간을 가져옵니다.') 
        return 10

    def check_capacity(self, capacity, filesize):
        _print(f'남은 저장 공간 용량은 {capacity}MB 입니다.')
        if filesize > capacity:
            _print('저장 공간이 부족합니다.')
            return False
        _print('사진을 저장 공간에 저장합니다.')
        return True

    def save_image(self, filesize):
        capacity = self.get_local_image_storage()
        _print(f'{filesize} 크기의 사진을 받았습니다.') 
        if not self.check_capacity(capacity, filesize):
            return False
        return True


class IphoneImageDownloader:
    def get_local_image_storage(self):
        _print('iphone의 사진 저장 공간을 가져옵니다.')
        return 3 

    def check_capacity(self, capacity, filesize):
        _print(f'남은 저장 공간 용량은 {capacity}MB 입니다.')
        if filesize > capacity:
            _print('저장 공간이 부족합니다.')
            return False
        _print('사진을 저장 공간에 저장합니다.')
        return True
	
    def save_image(self, filesize):
        capacity = self.get_local_image_storage()
        _print(f'{filesize} 크기의 사진을 받았습니다.') 
        if not self.check_capacity(capacity, filesize):
            return False
        return True


class IpadImageDownloader:
    def get_local_image_storage(self):
        _print('ipad의 사진 저장 공간을 가져옵니다.')
        return 5

    def check_capacity(self, capacity, filesize):
        _print(f'남은 저장 공간 용량은 {capacity}MB 입니다.')
        if filesize > capacity:
            _print('저장 공간이 부족합니다.')
            return False
        _print('사진을 저장 공간에 저장합니다.')
        return True
	
    def save_image(self, filesize):
        capacity = self.get_local_image_storage()
        _print(f'{filesize} 크기의 사진을 받았습니다.') 
        if not self.check_capacity(capacity, filesize):
            return False
        return True


class ImageDownloader:
    def __init__(self, device):
        self.device = device

    def save_image(self, filesize):
        result = self.device.save_image(filesize)
        if not result:
            _print('사진 저장에 실패했습니다.')
        else:
            _print('사진이 저장되었습니다.')


def main():
    device = None
    filesize = input('파일의 크기를 입력해주세요 : ')
    device_type = input('디바이스의 종류를 입력해주세요 (맥북:1, 아이폰:2, 아이패드:3) : ')
    
    if int(device_type) == 1:
        device = MacbookImageDownloader()
    elif int(device_type) == 2:
        device = IphoneImageDownloader()
    elif int(device_type) == 3:
        device = IpadImageDownloader()
    else:
        print('올바른 선택지가 아닙니다.')
        main()

    image_downloader = ImageDownloader(device)
    image_downloader.save_image(int(filesize))


main()
