def main(args):
    name = args.get('name', ".")
    name = name if name else "."
    message = "python file test Upload file for Ronen and Tomer" + name + "!";
    print(message)
    return {
        "body": {"message": message}
    }
