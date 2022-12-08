import WpVideo


def print_hi():
    videos = WpVideo.WpVideo('G:\Video\契约之吻', './test.txt', 14, '契约之吻')
    videos.write_dom()


if __name__ == '__main__':
    print_hi()
