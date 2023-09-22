import json
from argparse import ArgumentParser

from simpleaudiocontroller import AudioController

audio_controller = AudioController()


def list_devices(device_type):
    print(device_type)
    devices = (
        audio_controller.get_headphones()
        if device_type == "headphones"
        else audio_controller.get_microphones()
    )
    for device in devices:
        print(f"Name: {device.name} | In use: {device.is_current_device}")


def save_config(destination_path: str):
    current_microphone = audio_controller.get_current_microphone()
    current_headphone = audio_controller.get_current_headphone()
    current_config = {
        "current_headphone": current_headphone.name if current_headphone else None,
        "current_microphone": current_microphone.name if current_microphone else None,
    }

    try:
        with open(destination_path, "w") as f:
            json.dump(current_config, f, indent=3)
    except Exception as e:
        print(f"Error saving config: {e}")


def load_config(config_path: str):
    try:
        with open(config_path, "r") as f:
            config = json.load(f)

        if config["current_headphone"]:
            headphone = audio_controller.get_device_by_name(config["current_headphone"])
            if headphone:
                audio_controller.set_default_device(headphone)
        if config["current_microphone"]:
            microphone = audio_controller.get_device_by_name(
                config["current_microphone"]
            )
            if microphone:
                audio_controller.set_default_device(microphone)

        print("Config loaded successfully")
    except Exception as e:
        print(f"Error loading config: {e}")


def set_device(device_name: str):
    device = audio_controller.get_device_by_name(device_name)
    if device:
        audio_controller.set_default_device(device)
        print(f"Device set to {device_name}")
    else:
        print("Device not found")


def main():
    option_func = {
        "list-headphones": list_devices,
        "list-microphones": list_devices,
        "load": load_config,
        "save": save_config,
        "set": set_device,
    }

    parser = ArgumentParser(
        description="Simple interface for controlling audio devices"
    )
    parser.add_argument(
        "action", choices=option_func.keys(), help="Action to be executed"
    )
    parser.add_argument("data", nargs="?", help="Argument for the action")

    args = parser.parse_args()

    if args.action in option_func:
        if args.action in ["list-headphones", "list-microphones"]:
            option_func[args.action](args.action.split("-")[1])
        else:
            option_func[args.action](args.data)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
