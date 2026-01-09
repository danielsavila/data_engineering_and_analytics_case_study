from etl_files.extract import extract
from etl_files.transform import transform
from etl_files.load import load


def main():
    df = extract()
    df = transform(df)
    load(df)

if __name__ == "__main__":
    main()