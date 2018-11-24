import subprocess


class CameraCapture:
    def __init__(self, logger):
        self.logger = logger

    def capture_image(self):
        p = subprocess.Popen(['./data_acquisition/raspistill.sh'], stdout=subprocess.PIPE)
        com = p.communicate()[0].decode()
        self.logger.debug('Camera Still Captured')
        return
    

if __name__ == '__main__':
    camera = CameraCapture()
    print(camera.capture_image())
    
