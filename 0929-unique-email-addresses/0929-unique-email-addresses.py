class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()

        for email in emails:
            local, domain = email.split("@")

            local = local.split("+")

            local = local[0].replace(".", "")

            res.add(local + "@" + domain)

        return len(res)