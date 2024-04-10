from netmiko import ConnectHandler


class DeviceTools:
    @classmethod
    def create_device_dictionary_from_queryset_with_hostname(cls, request_data) -> dict:
        return {
            "hostname": request_data.hostname,
            "device_type": request_data.device_type,
            "ip": request_data.ip_address,
            "username": 'admin',
            "password": "cisco",
            "secret": "cisco"
        }

    @classmethod
    def create_device_dictionary_from_queryset(cls, request_data) -> dict:
        return {
            "device_type": request_data.device_type,
            "host": request_data.ip_address,
            "username": 'admin',
            "password": "cisco",
            "secret": "cisco"
        }

    @classmethod
    def create_device_dictionary_from_request(cls, request_data: dict) -> dict:
        return {
            "device_type": request_data.get('device_type'),
            "host": request_data.get('ip_address'),
            "username": 'admin',
            "password": "cisco",
            "secret": "cisco"
        }

    @classmethod
    def device_connection(cls, device_data: dict):
        return ConnectHandler(**device_data)

    @classmethod
    def test_device_connection(cls, device_data: dict):
        try:
            if ConnectHandler(**device_data):
                return {
                    "device_connection": "Established",
                    "connection": True,
                }
        except Exception as err:
            return {
                "device_connection": "Non-established",
                "connection": False
            }

    @classmethod
    def send_command_access_mode(cls, device_data, command: str) -> dict:
        try:
            connection = ConnectHandler(**device_data)
            command_result = connection.send_command(command)
            connection.disconnect()

            if command_result:
                return {
                    "status": "successful",
                    "command_sended": command,
                    "prompt_result": command_result,
                    "action": True
                }
            else:
                return {
                    "status": "un-successful",
                    "command_sended": command,
                    "prompt_result": command_result,
                    "action": False
                }

        except Exception as error:
            return {
                "status": "error",
                "command_sended": command,
                "prompt_result": "error",
                "action": False
            }

    @classmethod
    def send_command_privilege_mode(cls, device_data, command) -> dict:
        try:
            connection = ConnectHandler(**device_data)
            enable_mode = connection.enable()
            command_result = enable_mode.send_command(command)
            connection.disconnect()
            if command_result:
                return {
                    "status": "successful",
                    "command_sended": command,
                    "prompt_result": command_result,
                    "action": True
                }
            else:
                return {
                    "status": "un-successful",
                    "command_sended": command,
                    "prompt_result": command_result,
                    "action": False
                }

        except Exception as error:
            return {
                "status": "error",
                "command_sended": command,
                "prompt_result": "error",
                "action": False
            }

    @classmethod
    def send_command_config_mode(cls, device, command) -> dict:
        try:
            device_connection = ConnectHandler(**device)
            command_result = device_connection.send_config_set([command])
            device_connection.disconnect()

            if command_result:
                return {
                    "status": "successful",
                    "command_sended": command,
                    "prompt_result": command_result,
                    "action": True
                }
            else:
                return {
                    "status": "un-successful",
                    "command_sended": command,
                    "prompt_result": command_result,
                    "action": False
                }

        except Exception as error:
            return {
                "status": "error",
                "command_sended": command,
                "prompt_result": "error",
                "action": False
            }

    @classmethod
    def send_command_from_file(cls, device, config_archive) -> dict:
        try:
            device_connection = ConnectHandler(**device)
            command_result = device_connection.send_config_from_file(config_archive)
            device_connection.disconnect()
            if command_result:
                return {
                    "status": "successful",
                    "command_sended": config_archive,
                    "prompt_result": command_result,
                    "action": True
                }
            else:
                return {
                    "status": "un-successful",
                    "command_sended": config_archive,
                    "prompt_result": command_result,
                    "action": False
                }

        except Exception as error:
            return {
                "status": "error",
                "command_sended": config_archive,
                "prompt_result": "error",
                "action": False
            }
