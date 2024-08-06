import imageio
import imageio.plugins.ffmpeg

def list_cameras():
    for index in range(10):  # Limit the number of indices to check
        try:
            reader = imageio.get_reader(f'<video{index}>')
            reader.get_next_data()
            print(f"Index {index}: Camera found")
        except Exception as e:
            print(f"Index {index}: Camera not found, error: {e}")

if __name__ == "__main__":
    list_cameras()

