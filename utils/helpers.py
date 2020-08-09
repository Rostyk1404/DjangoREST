"""This is a helper module for DjangoREST project."""

def change_date_format(date):
    """Change date format
    from: YYYY/MM/DD
    to: YYYY-MM-DD."""
    return (lambda line: '-'.join(line.split('/')))(date)