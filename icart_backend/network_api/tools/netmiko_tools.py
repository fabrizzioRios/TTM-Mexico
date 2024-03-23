from netmiko import ConnectHandler


class DeviceTools:
    @classmethod
    def create_device_dictionary_from_queryset(cls, request_data) -> dict:
        return {
            "device_type": request_data.device_type,
            "host": request_data.ip_address,
            "username": request_data.username,
            "password": "test_network",
            "secret": "test_network"
        }
    @classmethod
    def create_device_dictionary_from_request(cls, request_data: dict) -> dict:
        return {
            "device_type": request_data.get('device_type'),
            "host": request_data.get('ip_address'),
            "username": request_data.get('username'),
            "password": "test_network",
            "secret": "test_network"
        }

    @classmethod
    def device_connection(cls, device_data: dict):
        try:
            return ConnectHandler(**device_data)
        except Exception as error:
            return {
                "device_connection": "Error",
                "connection": False
            }

    @classmethod
    def send_command_access_mode(cls, device_network_connection, command: str) -> dict:
        try:
            command_result = device_network_connection.send_command(command)
            device_network_connection.disconnect()

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
    def send_command_privilege_mode(cls, device_network_connection, command: str) -> dict:
        try:
            enable_mode = device_network_connection.enable()
            command_result = enable_mode.send_command(command)
            enable_mode.exit_enable_mode()
            device_network_connection.disconnect()

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
    def send_command_config_mode(cls, device_network_connection, command: list) -> dict:
        try:
            command_result = device_network_connection.send_config_set(command)
            device_network_connection.disconnect()

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
    def send_command_from_file(cls, device_network_connection, file) -> dict:
        try:
            command_result = device_network_connection.send_config_from_file(file)
            device_network_connection.disconnect()
            if command_result:
                return {
                    "status": "successful",
                    "command_sended": file,
                    "prompt_result": command_result,
                    "action": True
                }
            else:
                return {
                    "status": "un-successful",
                    "command_sended": file,
                    "prompt_result": command_result,
                    "action": False
                }

        except Exception as error:
            return {
                "status": "error",
                "command_sended": file,
                "prompt_result": "error",
                "action": False
            }