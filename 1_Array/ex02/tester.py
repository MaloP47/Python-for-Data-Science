from load_image import ft_load


def main():
    try:
        # ft_load("./images/test.txt")
        # ft_load("./images/landscape.jpg")
        # ft_load("./images/test.jpg")
        print(ft_load("./images/landscape.jpg"))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
