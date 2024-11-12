import speedtest

def check_speed():
    # Create a Speedtest object
    test = speedtest.Speedtest()

    # Get the best server based on ping
    print("Finding the best server...")
    test.get_best_server()

    # Perform download and upload speed tests
    print("Testing download speed...")
    download_speed = test.download() / 1_000_000  # Convert to Mbps
    print("Testing upload speed...")
    upload_speed = test.upload() / 1_000_000      # Convert to Mbps

    # Get the ping
    ping = test.results.ping

    # Print the results
    print(f"\nDownload speed: {download_speed:.2f} Mbps")
    print(f"Upload speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")

if __name__ == "__main__":
    check_speed()
