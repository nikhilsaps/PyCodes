import win32com.client as win32

def create_outlook_email():
    # Initialize Outlook
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)  # 0: olMailItem

    # Set email subject and recipient (optional)
    mail.Subject = 'Generated Email with Compact Tables Aligned in Rows'
    mail.To = 'recipient@example.com'

    # Generate the email body
    # Add a paragraph of information
    email_body = "<p>This is the introductory paragraph with some information.</p>"

    # Create the table structure
    for row in range(3):  # 3 rows
        email_body += "<div style='display: flex; justify-content: space-between; margin-bottom: 20px;'>"
        for col in range(5):  # 5 tables per row
            table_header = f"<h3 style='text-align: center;'>Table {row + 1}-{col + 1} Header</h3>"
            email_body += "<div style='width: 19%;'>"  # Each table takes 19% width of the row to fit 5 tables
            email_body += table_header
            email_body += "<table border='1' style='border-collapse:collapse; width: 100%; table-layout: fixed;'>"
            # Add table rows and columns
            for i in range(22):  # 22 rows
                email_body += "<tr>"
                if i == 0:
                    # Header Row
                    email_body += ("<th style='width: 25%;'>MP</th>"
                                   "<th style='width: 25%;'>In Queue</th>"
                                   "<th style='width: 25%;'>Age</th>"
                                   "<th style='width: 25%;'>Status</th>")
                else:
                    # Data Rows
                    email_body += (f"<td style='width: 25%;'>MP{col+1}-{i}</td>"
                                   f"<td style='width: 25%;'>Queue{col+1}-{i}</td>"
                                   f"<td style='width: 25%;'>{i*2} days</td>"
                                   f"<td style='width: 25%;'>Status{col+1}-{i}</td>")
                email_body += "</tr>"
            email_body += "</table>"
            email_body += "</div>"
        email_body += "</div>"

    # Set the body format as HTML
    mail.HTMLBody = email_body

    # Display the email (do not send it automatically)
    mail.Display()

if __name__ == "__main__":
    create_outlook_email()
