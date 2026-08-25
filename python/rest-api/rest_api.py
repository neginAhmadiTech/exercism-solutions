import json


class RestAPI:
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):

        if not payload:
            return json.dumps(self.database)

        result = {"users": []}
        if url == "/users":
            payload = json.loads(payload)

            for name in payload["users"]:
                for user in self.database["users"]:

                    if user["name"] == name:
                        user["balance"] = sum(user["owed_by"].values()) - sum(
                            user["owes"].values()
                        )
                        result["users"].append(user)

            result["users"] = sorted(result["users"], key=lambda user: user["name"])
            result = json.dumps(result)

            return result

    def post(self, url, payload=None):

        payload = json.loads(payload)

        if url == "/add":

            for user in self.database["users"]:
                if user["name"] == payload["user"]:
                    return

            self.database["users"].append(
                {"name": payload["user"], "owes": {}, "owed_by": {}, "balance": 0}
            )
            return json.dumps(self.database["users"][-1])

        elif url == "/iou":
            lender = {}
            borrower = {}
            result = {"users": []}

            for user in self.database["users"]:
                if user["name"] == payload["lender"]:
                    lender = user
                elif user["name"] == payload["borrower"]:
                    borrower = user

            # update balance
            lender["balance"] += payload["amount"]
            borrower["balance"] -= payload["amount"]

            if lender["owes"].get(payload["borrower"], None):
                difference = lender["owes"][payload["borrower"]] - payload["amount"]

                if difference > 0:
                    lender["owes"].update({payload["borrower"]: difference})
                    borrower["owed_by"].update({payload["lender"]: difference})

                elif difference == 0:
                    lender["owes"].pop(payload["borrower"])
                    borrower["owed_by"].pop(payload["lender"])
                else:
                    lender["owes"].pop(payload["borrower"])
                    lender["owed_by"].setdefault(payload["borrower"], abs(difference))
                    borrower["owed_by"].pop(payload["lender"])
                    borrower["owes"].setdefault(payload["lender"], abs(difference))
            else:

                # update lender props
                lender["owed_by"].setdefault(payload["borrower"], payload["amount"])

                # update borrower props
                borrower["owes"].setdefault(payload["lender"], payload["amount"])

            result["users"] = [lender, borrower]
            result["users"] = sorted(result["users"], key=lambda user: user["name"])

            return json.dumps(result)
