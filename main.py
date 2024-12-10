import subprocess
import os

def load_proxies(filename="proxy.txt"):
    try:
        with open(filename, "r") as file:
            proxies = file.readlines()
        return [proxy.strip() for proxy in proxies if proxy.strip()]
    except FileNotFoundError:
        print("Error: proxy.txt not found!")
        return []

def set_proxy_environment(proxy):
    os.environ["http_proxy"] = proxy
    os.environ["https_proxy"] = proxy

def run_forestgrass():
    print("⚠️YOU ARE ABOUT TO RUN THE SCRIPT ON YOUR OWN RISK⚠️")
    subprocess.run(["python", "forestgrass.txt"])

def main():
    proxies = load_proxies()
    if not proxies:
        print("No proxies available. Running without proxy.")
        run_forestgrass()
        return

    print("Do you want to connect using a proxy?")
    choice = input("Type 'yes' to use a proxy or 'no' to run directly: ").strip().lower()

    if choice == "yes":
        print("Available proxies:")
        for i, proxy in enumerate(proxies):
            print(f"{i + 1}. {proxy}")
        
        try:
            selection = int(input("Select a proxy by number: ")) - 1
            if 0 <= selection < len(proxies):
                selected_proxy = proxies[selection]
                print(f"Connecting to proxy: {selected_proxy}")
                set_proxy_environment(selected_proxy)
                run_forestgrass()
            else:
                print("Invalid selection. Running without proxy.")
                run_forestgrass()
        except ValueError:
            print("Invalid input. Running without proxy.")
            run_forestgrass()
    else:
        run_forestgrass()

if __name__ == "__main__":
    main()