from app.app import extract_pdf, find_target_tables


def main():
    all_tables = extract_pdf('/home/beloded/different/decoration.pdf')
    find_target_tables(all_tables)

if __name__ == '__main__':
    print(main())