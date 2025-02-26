import unittest
from src.secret_santa import SecretSanta

class TestSecretSanta(unittest.TestCase):
    def setUp(self):
        self.santa = SecretSanta("test_employees.csv", "test_previous_santa.csv", "test_output.csv")
        self.santa.employees = [
            {"name": "Hamish Murray", "email": "hamish.murray@acme.com"},
            {"name": "Layla Graham", "email": "layla.graham@acme.com"},
            {"name": "Matthew King", "email": "matthew.king@acme.com"}
        ]
        self.santa.previous_assignments = {
            "hamish.murray@acme.com": "mark.lawrence@acme.com",
            "layla.graham@acme.com": "matthew.king.jr@acme.com",
            "benjamin.collins@acme.com": "charlie.ross.jr@acme.com"
        }

    def test_assignments(self):
        assignments = self.santa.assign_secret_santa()
        assigned_emails = {a[1]: a[3] for a in assignments}
        self.assertEqual(len(set(assigned_emails.values())), len(self.santa.employees))  # No duplicate assignments
        for emp in self.santa.employees:
            self.assertNotEqual(emp["email"], assigned_emails[emp["email"]])  # No self-assignments

if __name__ == '__main__':
    unittest.main()