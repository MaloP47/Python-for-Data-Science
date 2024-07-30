from load_image import ft_load


def main():
    try:
        print(ft_load("landscape.jpg"))
    except as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
