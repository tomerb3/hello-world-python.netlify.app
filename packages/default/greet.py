def main(args):
    name = args.get('name', "World2")
    name = name if name else "World"
    message = "Upload file for Ronen and Tomer" + name + "!";
    print(message)
    return {
        "body": {"message": message}
    }
