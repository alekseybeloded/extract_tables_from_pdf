from app.app import extract_pdf, find_target_tables
import sys


def main() -> None:
    all_tables = extract_pdf(sys.argv[1])
    result = find_target_tables(all_tables)
    result


if __name__ == '__main__':
    main()
