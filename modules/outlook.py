import pandas as pd
import win32com.client as win32

def csv_to_html_table(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Convert the DataFrame to an HTML table
    html_table = df.to_html(index=False)
    
    return html_table

def open_email_with_table(html_table, subject, body_text, to_email):
    # Create an instance of the Outlook application
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)  # 0: Mail item
    
    # Construct the HTML body of the email
    html_body = f"""
    <html>
    <body>
        <p>{body_text}</p>
        {html_table}
    </body>
    </html>
    """
    
    # Set up the email parameters
    mail.Subject = subject
    mail.HtmlBody = html_body
    mail.To = to_email
    
    # Display the email to review and edit before sending
    mail.Display()
    print(f"Email draft opened with subject '{subject}'")

def main():
    csv_file = 'csv.csv'  # Path to your CSV file
    subject = 'Subject of the Email'
    body_text = 'This is the paragraph with some information.'
    to_email = 'recipient@example.com'
    
    html_table = csv_to_html_table(csv_file)
    open_email_with_table(html_table, subject, body_text, to_email)

if __name__ == '__main__':
    main()
