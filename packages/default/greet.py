def main(args):
    name = args.get('name', "World2")
    name = name if name else "World"
    message = "Hello, " + name + "!";
    print(message)
    return {
        "body": {"message": message}
    }
