
import subprocess


class Tool:
    @classmethod
    def check_ping(cls, ip_address: str) -> bool:
        try:
            result = subprocess.run(['ping', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if 'bytes=' in result.stdout or 'bytes=' in result.stderr:
                return True
            else:
                return False
        except Exception as err:
            return False
