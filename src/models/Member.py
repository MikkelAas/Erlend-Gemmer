class Member:
    def __init__(self, data: dict) -> None:
        self.name = data.get("name")
        self.tag = data.get("tag")
