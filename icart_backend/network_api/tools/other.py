
import subprocess
import textfsm


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
    
    @classmethod
    def filter_output(filter_path: str, stdout_output: str) -> list:

        with open(filter_path) as template:
            fsm = textfsm.TextFSM(template)
            result = fsm.ParseText(stdout_output)

        return result
