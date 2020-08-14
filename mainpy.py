import analyze
from getpdf import main as download_pdfs
from analyze import main as create_janru_csv


def main():
    download_pdfs()
    create_janru_csv()


if __name__ == '__main__':
    main()
