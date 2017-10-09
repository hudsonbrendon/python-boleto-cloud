def write_pdf(ticket):
    with open('boleto.pdf', 'wb') as file:
        file.write(ticket.content)
