def transform(text):
    return text.strip()
    
if __name__ == "__main__":
    test = "  Teamwork makes  Python better!  "
    result = transform(test)

    print("INPUT :", repr(test))
    print("OUTPUT:", repr(result))